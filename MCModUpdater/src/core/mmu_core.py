import asyncio
import importlib.util
import os
import pathlib
import shutil
import time
from asyncio import Future
from functools import lru_cache
from typing import Coroutine

from httpx import AsyncClient, Response

from MCModUpdater.src.core.apis.BaseModProviderAPI import BaseModProviderAPI
from MCModUpdater.src.core.constants import CORE_DIR_PATH
from MCModUpdater.src.core.custom_types import ModData, ResponseCallback
from MCModUpdater.src.core.enums import SearchResult, ModLoader, BackupOption
from MCModUpdater.src.utils.logger import get_logger


@lru_cache(maxsize=128, typed=False)
def get_all_apis() -> list[BaseModProviderAPI]:
    def load_apis(api_dir_path: str):
        apis: list[BaseModProviderAPI] = []
        api_dir_path = os.path.abspath(os.path.normpath(api_dir_path))

        for filename in os.listdir(api_dir_path):
            if not filename.endswith(".py"):
                continue

            if os.path.isdir(filename):
                continue

            plugin_path = os.path.join(api_dir_path, filename)
            spec = importlib.util.spec_from_file_location(filename[:-3], plugin_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            for attribute_name in dir(module):
                attribute = getattr(module, attribute_name)

                if not isinstance(attribute, type):
                    continue

                if not issubclass(attribute, BaseModProviderAPI):
                    continue

                if attribute is BaseModProviderAPI:
                    continue

                apis.append(attribute())

        return apis

    builtin_apis: list[BaseModProviderAPI] = load_apis(
        os.path.join(CORE_DIR_PATH, "apis")
    )
    # TODO: Add plugin support
    # custom_apis: list[BaseModProviderAPI] = load_apis(PLUGINS_PATH)
    custom_apis: list[BaseModProviderAPI] = []

    return builtin_apis + custom_apis


async def search_mods(
    urls: list[str],
    apis: list[BaseModProviderAPI],
    mc_version: str,
    mod_loader: ModLoader,
    essential_data_only: bool = True,
    before_response_callback: ResponseCallback = None,
    after_response_callback: ResponseCallback = None,
) -> list[ModData]:
    """
    Searches for the specified mods.

    Args:
        urls: The page urls of the mods
        apis: The mod provider APIs
        mc_version: Minecraft version
        mod_loader: Mod loader
        essential_data_only: Whether to fetch just essential data, or extra data like logo and file name
        before_response_callback: Optional callback function that will be called before API is called
        after_response_callback: Optional callback function that will be called after API response is received

    Returns:
        list of ModData objects

    Raises:
        asyncio.CancelledError: When gather is cancelled
    """

    global _client, _gather

    tasks: list[Coroutine] = []
    results: list[ModData] = []
    _client = AsyncClient()

    async def before_response(mod_data: ModData):
        _logger.info(f"Searching '{mod_data['page_url']}' using {mod_data['origin']}")
        if before_response_callback is not None:
            await before_response_callback(mod_data)

    async def after_response(mod_data: ModData):
        results.append(mod_data)
        match mod_data["search_result"]:
            case SearchResult.SUCCESS:
                _logger.info(
                    f"Found file for '{mod_data['slug']}' using {mod_data['origin']}"
                )
            case SearchResult.MOD_NOT_FOUND:
                _logger.info(
                    f"Couldn't find mod '{mod_data['slug']}' using {mod_data['origin']}"
                )
            case SearchResult.FILE_NOT_FOUND:
                _logger.info(
                    f"Couldn't find correct file for '{mod_data['slug']}' using {mod_data['origin']}"
                )
            case SearchResult.API_KEY_INCORRECT:
                _logger.error(
                    f"Cannot search for '{url}' because API key "
                    + f"for {mod_data['origin']} is incorrect or not set"
                )
            case SearchResult.URL_NOT_SUPPORTED:
                _logger.error(f"URL '{mod_data['page_url']}' is not supported")

        if after_response_callback is not None:
            await after_response_callback(mod_data)

    _logger.info("Searching for mods...")
    for url in urls:
        mod_data: ModData = _make_base_mod_data(url, mc_version, mod_loader, None)
        corrected_url, api = _get_supported_provider(apis, url)

        if not corrected_url and not api:
            await before_response(mod_data)
            mod_data["search_result"] = SearchResult.URL_NOT_SUPPORTED
            await after_response(mod_data)
            continue

        mod_data["page_url"] = corrected_url
        tasks.append(
            api.get_mod_data(
                mod_data=mod_data,
                essential_data_only=essential_data_only,
                before_response_call=before_response,
                after_response_call=after_response,
            )
        )

    try:
        _gather = asyncio.gather(*tasks)
        await _gather
    except asyncio.CancelledError:
        _logger.info("Searching for mods cancelled")
        raise asyncio.CancelledError()
    finally:
        await _client.aclose()

    _logger.info("Done searching")

    return results


async def download_mods(
    mods_data: list[ModData],
    download_path: str,
    before_resonse_callback: ResponseCallback = None,
    after_response_callback: ResponseCallback = None,
) -> None:
    global _client, _gather

    if not os.path.exists(download_path):
        pathlib.Path(download_path).mkdir(parents=True, exist_ok=True)

    tasks = []
    _client = AsyncClient()
    _logger.info("Downloading mods")

    # TODO: Maybe make this an API method if download requires API key
    async def download_mod(mod_data: ModData, download_path: str) -> None:
        _logger.info(f"Downloading '{mod_data['file_name']}'")
        if before_resonse_callback is not None:
            await before_resonse_callback(mod_data)

        response: Response = await _client.get(mod_data["file_url"])
        with open(os.path.join(download_path, mod_data["file_name"]), "wb") as outfile:
            outfile.write(response.content)

        _logger.info(f"Done downloading '{mod_data['file_name']}'")

        if after_response_callback is not None:
            await after_response_callback(mod_data)

    for mod_data in mods_data:
        tasks.append(download_mod(mod_data, download_path))

    try:
        _gather = asyncio.gather(*tasks)
        await _gather
    except asyncio.CancelledError:
        _logger.info("Downloading mods cancelled")
        raise asyncio.CancelledError()
    finally:
        await _client.aclose()

    # TODO: Maybe show popup saying it's done.
    # Example (5/5 mods downloaded)

    _logger.info("Done downloading mods")


def backup_old_files(path: str, backup_option: BackupOption) -> None:
    if backup_option is BackupOption.NO_BACKUP:
        _logger.info("Not backing up old mods")
        return

    if not os.path.exists(path):
        pathlib.Path(path).mkdir(parents=True, exist_ok=True)

    mod_files = [
        f for f in os.listdir(path) if f.endswith(".jar") and not os.path.isdir(f)
    ]
    if backup_option is BackupOption.BACKUP_IN_DIRECTORY:
        if not any(mod_files):
            _logger.info("No old mods to backup")
            return

        _logger.info("Moving old mods to backup directory...")
        backup_dir_name = "Backup " + time.strftime(
            "%Y-%m-%d %H.%M.%S", time.localtime()
        )
        backup_path = os.path.join(path, backup_dir_name)
        if not os.path.exists(backup_path):
            pathlib.Path(backup_path).mkdir(parents=True, exist_ok=True)

        for file in mod_files:
            _logger.info(f"Moving '{file}' to '{backup_dir_name}'")
            src_path = os.path.join(path, file)
            dst_path = os.path.join(path, backup_dir_name, file)
            shutil.move(src_path, dst_path)
        _logger.info("Done backing up old mods")
    elif backup_option is BackupOption.DELETE_OLD_FILES:
        if not any(mod_files):
            _logger.info("No old mods to remove")
            return

        _logger.info("Removing old mods...")
        for file in mod_files:
            os.remove(os.path.join(path, file))

        _logger.info("Done removing old mods")


def _make_base_mod_data(
    page_url: str, mc_version: str, mod_loader: ModLoader, origin: str | None
) -> ModData:
    """
    Make the base mod data.

    Args:
        page_url: The page url of the mod
        mc_version: Minecraft version
        mod_loader: Mod loader
        origin: The origin of the mod

    Returns:
        The base for the mod data
    """

    mod_data: ModData = {
        "search_result": SearchResult.INITIALISED,
        "page_url": page_url,
        "mc_version": mc_version,
        "mod_loader": mod_loader,
        "origin": origin,
    }
    return mod_data


def _get_supported_provider(
    apis: list[BaseModProviderAPI], url: str
) -> tuple[str, BaseModProviderAPI] | tuple[None, None]:
    """
    Tries to find the supported API for the specified url.

    Args:
        apis: List of APIs
        url: The page url of the mod

    Returns:
        (trimmed_url, supported_provider_api) if provider is supported, otherwise returns (None, None)
    """

    trimmed_urls: list[str | None] = [api.match_mod_url(url) for api in apis]
    for i, trimmed_url in enumerate(trimmed_urls):
        if trimmed_url is not None:
            return trimmed_url, apis[i]
    return None, None


def get_client() -> AsyncClient:
    global _client
    return _client


def get_gather():
    global _gather
    return _gather


_logger = get_logger()
_client: AsyncClient | None = None
_gather: Future[list] | None = None
