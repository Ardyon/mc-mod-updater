from typing import TypedDict, NotRequired, Awaitable, Optional, Callable

from MCModUpdater.src.core.enums import SearchResult, ModLoader


class ModData(TypedDict):
    origin: str | None
    mc_version: str
    page_url: str
    mod_loader: ModLoader
    search_result: SearchResult
    slug: NotRequired[str]
    mod_id: NotRequired[str]
    mod_title: NotRequired[str]
    file_title: NotRequired[str]
    file_name: NotRequired[str]
    file_version: NotRequired[str]
    file_url: NotRequired[str]
    logo_url: NotRequired[str]
    logo_content: NotRequired[bytes]


class TagData(TypedDict):
    text: str
    background_color: str
    foreground_color: str
    width: int
    height: int


ResponseCallback = Optional[Callable[[ModData], Awaitable[None]]]
