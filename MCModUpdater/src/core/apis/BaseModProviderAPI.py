import re
from abc import ABC, abstractmethod

from MCModUpdater.src.core.constants import APP_VERSION, GITHUB_REPO_NAME
from MCModUpdater.src.core.custom_types import ModData, TagData, ResponseCallback
from MCModUpdater.src.core.enums import ModLoader, ApiKeyRequirement


class BaseModProviderAPI(ABC):
    def __init__(self) -> None:
        self.headers: dict = {
            "User-Agent": f"{GITHUB_REPO_NAME}_{APP_VERSION}",
            "Accept": "application/json",
        }

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def mod_url_regex(self) -> str:
        pass

    @property
    @abstractmethod
    def api_key_requirement(self) -> ApiKeyRequirement:
        pass

    @abstractmethod
    def get_api_key(self) -> str:
        pass

    @abstractmethod
    def set_api_key(self, api_key: str) -> None:
        pass

    @property
    @abstractmethod
    def api_key_warning_text(self) -> str:
        pass

    def set_headers(self, headers: dict) -> dict:
        self.headers.update(headers)
        return self.headers

    def match_mod_url(self, url) -> str | None:
        """
        Checks if the given url matches the regex for this mod provider.

        Args:
            url: The url to check.

        Returns:
            None if the url doesn't match, or the trimmed version of the url if it does match.

        Raises:
            NotImplementedError: If URL regex is not set.
        """

        if self.mod_url_regex is None:
            raise NotImplementedError("URL regex is not set")

        possible_match = re.search(self.mod_url_regex, url)
        if not possible_match:
            return None
        return possible_match.group()

    @property
    def env_name(self) -> str:
        """
        Name that is saved in the ENV file if the API has a key
        """

        return f"{self.name.upper()}_KEY"

    @staticmethod
    @abstractmethod
    def get_tag_data() -> TagData:
        pass

    @abstractmethod
    async def get_mod_data(
        self,
        mod_data: ModData,
        essential_data_only: bool = True,
        before_response_call: ResponseCallback = None,
        after_response_call: ResponseCallback = None,
    ) -> ModData:
        pass

    @abstractmethod
    def _convert_mod_loader(self, mod_loader: ModLoader):
        pass
