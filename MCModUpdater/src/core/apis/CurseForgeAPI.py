from enum import Enum

from httpx import Response

from MCModUpdater.src.core.apis.BaseModProviderAPI import BaseModProviderAPI
from MCModUpdater.src.core.custom_types import ModData, TagData, ResponseCallback
from MCModUpdater.src.core.enums import ModLoader, SearchResult, ApiKeyRequirement
from MCModUpdater.src.core.mmu_core import get_client

CF_BASE_MOD_URL: str = "https://www.curseforge.com/minecraft/mc-mods"
CF_API_BASE: str = "https://api.curseforge.com"
CF_API_VERSION: str = "v1"
CF_API_URL: str = f"{CF_API_BASE}/{CF_API_VERSION}"
CF_GAME_ID: int = 432  # Minecraft
CF_CATEGORY_ID: int = 6  # Mods


class CurseForgeModLoader(Enum):
    FORGE = "1"
    NEO_FORGE = "6"
    FABRIC = "4"
    QUILT = "5"
    QUILT_FABRIC_FALLBACK = ["5", "4"]


class CurseForgeAPI(BaseModProviderAPI):
    def __init__(self):
        super().__init__()

    @property
    def name(self) -> str:
        return "CurseForgeAPI"

    @property
    def mod_url_regex(self) -> str:
        return r"^(https:\/\/www\.curseforge\.com\/minecraft\/mc-mods\/[A-z\-0-9]+)"

    @property
    def api_key_requirement(self) -> ApiKeyRequirement:
        return ApiKeyRequirement.REQUIRED

    def get_api_key(self) -> str | None:
        return self.headers.get("x-api-key", None)

    def set_api_key(self, api_key: str) -> None:
        self.headers["x-api-key"] = api_key

    @property
    def api_key_warning_text(self) -> str:
        return (
            "CurseForge links require an API key to get data from the website.<br/>"
            "Modrinth links don't need an API key.<br/>"
            "<strong>Skipping this step means that you won't be able to use CurseForge links.</strong><br/>"
            "You can always add the API key later, in the Settings tab<br/>"
            "<br/>"
            'To get an API key, visit this link: <a href="https://console.curseforge.com/">https://console.curseforge.com/</a><br/>'
            "1. Login or create an account<br/>"
            "2. Once you're logged in, go to the tab 'API keys' and copy the key<br/>"
        )

    @staticmethod
    def get_tag_data() -> TagData:
        tag_data: TagData = {
            "text": "CurseForge",
            "background_color": "#451D0E",
            "foreground_color": "#F16436",
            "width": 70,
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

        mod_data = await self._get_general_data(mod_data, essential_data_only)

        if (
            not essential_data_only
            and mod_data["search_result"] is SearchResult.SUCCESS
        ):
            mod_data = await self._get_file_data(mod_data, essential_data_only)

        if after_response_call is not None:
            await after_response_call(mod_data)

        return mod_data

    async def _get_file_data(
        self,
        mod_data: ModData,
        essential_data_only: bool,
        page_size: int = 50,
        is_fallback: bool = False,
    ) -> ModData:
        mod_id: str = mod_data["mod_id"]
        # TODO: Make this work with the fallback loaders
        mod_loader: ModLoader = mod_data["mod_loader"]
        mc_version: str = mod_data["mc_version"]
        url: str = f"{CF_API_URL}/mods/{mod_id}/files"
        params = {
            "gameVersion": mc_version,
            "modLoaderType": self._convert_mod_loader(mod_loader).value,
            "pageSize": page_size,
        }

        if mod_loader is CurseForgeModLoader.QUILT_FABRIC_FALLBACK:
            params["modLoaderType"] = mod_loader.value[0 if not is_fallback else 1]

        response: Response = await get_client().get(
            url=url, params=params, headers=self.headers
        )

        if response.status_code == 403:
            mod_data["search_result"] = SearchResult.API_KEY_INCORRECT
            return mod_data

        if response.status_code != 200:
            mod_data["search_result"] = SearchResult.MOD_NOT_FOUND
            return mod_data

        data = response.json()["data"]

        if not data:
            # TODO: Make this work dynamically with other fallbacks
            if (
                mod_loader is CurseForgeModLoader.QUILT_FABRIC_FALLBACK
                and not is_fallback
            ):
                mod_data = await self._get_file_data(
                    mod_data, essential_data_only, is_fallback=True
                )
            else:
                mod_data["search_result"] = SearchResult.FILE_NOT_FOUND
                return mod_data

        file = data[0]
        mod_data["search_result"] = SearchResult.SUCCESS
        mod_data["file_url"] = file["downloadUrl"]
        if not essential_data_only:
            mod_data["file_title"] = file["displayName"]
            mod_data["file_name"] = file["fileName"]

        return mod_data

    async def _get_general_data(
        self, mod_data: ModData, essential_data_only: bool
    ) -> ModData:
        slug: str = mod_data["slug"]
        url: str = f"{CF_API_URL}/mods/search"
        params = {
            "gameId": CF_GAME_ID,
            "classId": CF_CATEGORY_ID,
            "slug": slug,
        }

        response: Response = await get_client().get(
            url=url, params=params, headers=self.headers
        )

        if response.status_code == 403:
            mod_data["search_result"] = SearchResult.API_KEY_INCORRECT
            return mod_data

        if response.status_code != 200:
            mod_data["search_result"] = SearchResult.MOD_NOT_FOUND
            return mod_data

        data = response.json()["data"]

        if not data:
            mod_data["search_result"] = SearchResult.MOD_NOT_FOUND
            return mod_data

        mod = data[0]
        mod_data["search_result"] = SearchResult.SUCCESS
        mod_data["mod_id"] = mod["id"]
        if not essential_data_only:
            mod_data["mod_title"] = mod["name"]
            mod_data["logo_url"] = mod["logo"]["url"]

        return mod_data

    def _convert_mod_loader(self, mod_loader: ModLoader) -> CurseForgeModLoader:
        match mod_loader:
            case ModLoader.FORGE:
                return CurseForgeModLoader.FORGE
            case ModLoader.NEOFORGE:
                return CurseForgeModLoader.NEO_FORGE
            case ModLoader.FABRIC:
                return CurseForgeModLoader.FABRIC
            case ModLoader.QUILT:
                return CurseForgeModLoader.QUILT
            case ModLoader.QUILT_FABRIC_FALLBACK:
                return CurseForgeModLoader.QUILT_FABRIC_FALLBACK
            case _:
                raise ValueError(f"Invalid modloader {mod_loader}")
