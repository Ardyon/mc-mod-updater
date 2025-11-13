from enum import Enum

from httpx import Response, AsyncClient

from MCModUpdater.src.core.apis.BaseModProviderAPI import BaseModProviderAPI
from MCModUpdater.src.core.custom_types import ModData, TagData, ResponseCallback
from MCModUpdater.src.core.enums import ModLoader, SearchResult, ApiKeyRequirement
from MCModUpdater.src.core.mmu_core import get_client

MR_BASE_MOD_URL: str = "https://modrinth.com/mod"
MR_API_BASE: str = "https://api.modrinth.com"
MR_API_VERSION: str = "v2"
MR_API_URL: str = f"{MR_API_BASE}/{MR_API_VERSION}"


class ModrinthModLoader(Enum):
    FORGE = '["forge"]'
    NEO_FORGE = '["neoforge"]'
    FABRIC = '["fabric"]'
    QUILT = '["quilt"]'
    QUILT_FABRIC_FALLBACK = '["quilt", "fabric"]'


class ModrinthAPI(BaseModProviderAPI):
    def __init__(self):
        super().__init__()

    @property
    def name(self) -> str:
        return "ModrinthAPI"

    @property
    def mod_url_regex(self) -> str:
        return r"^(https:\/\/modrinth\.com\/mod\/[A-z\-0-9]+)"

    @property
    def api_key_requirement(self) -> ApiKeyRequirement:
        return ApiKeyRequirement.OPTIONAL

    def get_api_key(self) -> str:
        raise NotImplementedError()

    def set_api_key(self, api_key: str) -> None:
        raise NotImplementedError()

    @property
    def api_key_warning_text(self) -> str:
        raise NotImplementedError()

    @staticmethod
    def get_tag_data() -> TagData:
        tag_data: TagData = {
            "text": "Modrinth",
            "background_color": "#0F3A1B",
            "foreground_color": "#1BD96A",
            "width": 60,
            "height": 20,
        }
        return tag_data

    async def get_mod_data(
        self,
        mod_data: ModData,
        essential_data_only: bool = True,
        before_response_call: ResponseCallback = None,
        after_response_call: ResponseCallback = None,
    ) -> ModData:
        page_url: str = mod_data["page_url"]
        slug: str = page_url.split("/")[-1]
        mod_data["origin"] = self.name
        mod_data["search_result"] = SearchResult.BUSY
        mod_data["slug"] = slug

        if before_response_call is not None:
            await before_response_call(mod_data)

        mod_data = await self._get_file_data(mod_data, essential_data_only)

        if (
            not essential_data_only
            and mod_data["search_result"] is SearchResult.SUCCESS
        ):
            mod_data = await self._get_general_data(mod_data)

        if after_response_call is not None:
            await after_response_call(mod_data)

        return mod_data

    async def _get_file_data(
        self, mod_data: ModData, essential_data_only: bool
    ) -> ModData:
        slug: str = mod_data["slug"]
        # TODO: Make this work with the fallback loaders
        mod_loader: ModLoader = mod_data["mod_loader"]
        mc_version: str = mod_data["mc_version"]
        url: str = f"{MR_API_URL}/project/{slug}/version"
        params = {
            "game_versions": f'["{mc_version}"]',
            "loaders": self._convert_mod_loader(mod_loader).value,
        }

        response: Response = await get_client().get(
            url=url, headers=self.headers, params=params
        )

        if response.status_code != 200:
            mod_data["search_result"] = SearchResult.MOD_NOT_FOUND
            return mod_data

        versions = response.json()
        if not versions:
            mod_data["search_result"] = SearchResult.FILE_NOT_FOUND
            return mod_data

        version = versions[0]
        mod_data["search_result"] = SearchResult.SUCCESS
        mod_data["file_url"] = version["files"][0]["url"]
        if not essential_data_only:
            mod_data["mod_id"] = version["project_id"]
            mod_data["file_title"] = version["name"]
            mod_data["file_version"] = version["version_number"]
            mod_data["file_name"] = version["files"][0]["filename"]

        return mod_data

    async def _get_general_data(self, mod_data: ModData) -> ModData:
        slug: str = mod_data["slug"]
        url: str = f"{MR_API_URL}/project/{slug}"

        client: AsyncClient = get_client()
        response: Response = await client.get(url=url, headers=self.headers)

        if response.status_code != 200:
            mod_data["search_result"] = SearchResult.MOD_NOT_FOUND
            return mod_data

        mod = response.json()
        if not mod:
            mod_data["search_result"] = SearchResult.MOD_NOT_FOUND
            return mod_data

        mod_data["search_result"] = SearchResult.SUCCESS
        mod_data["mod_title"] = mod["title"]
        mod_data["logo_url"] = mod["icon_url"]

        return mod_data

    def _convert_mod_loader(self, mod_loader: ModLoader) -> ModrinthModLoader:
        match mod_loader:
            case ModLoader.FORGE:
                return ModrinthModLoader.FORGE
            case ModLoader.NEOFORGE:
                return ModrinthModLoader.NEO_FORGE
            case ModLoader.FABRIC:
                return ModrinthModLoader.FABRIC
            case ModLoader.QUILT:
                return ModrinthModLoader.QUILT
            case ModLoader.QUILT_FABRIC_FALLBACK:
                return ModrinthModLoader.QUILT_FABRIC_FALLBACK
            case _:
                raise ValueError(f"Invalid modloader {mod_loader}")
