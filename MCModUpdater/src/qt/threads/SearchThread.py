import asyncio

from PySide6 import QtCore
from PySide6.QtCore import QThread
from httpx import Response, AsyncClient

from MCModUpdater.src.core.custom_types import ModData
from MCModUpdater.src.core.enums import ModLoader, SearchResult
from MCModUpdater.src.core.mmu_core import (
    search_mods,
    get_all_apis,
    get_client,
    get_gather,
)


class SearchThread(QThread):
    sgl_update_progress = QtCore.Signal()
    sgl_done = QtCore.Signal()
    sgl_cancelled = QtCore.Signal()
    sgl_append_found_mod = QtCore.Signal(dict)
    sgl_append_failed_mod = QtCore.Signal(dict)

    def __init__(self, urls: list[str], mc_version: str, mod_loader: ModLoader):
        super().__init__()
        self.urls = urls
        self.mc_version = mc_version
        self.mod_loader = mod_loader

    async def search(self):
        async def after_response_callback(mod_data: ModData):
            if mod_data["search_result"] is not SearchResult.SUCCESS:
                self.sgl_update_progress.emit()
                self.sgl_append_failed_mod.emit(mod_data)
                return

            client: AsyncClient = get_client()
            headers = [
                api.headers for api in get_all_apis() if api.name == mod_data["origin"]
            ][0]
            mod_logo_response: Response = await client.get(
                mod_data["logo_url"], headers=headers, timeout=30
            )

            # TODO: Check if this is necessary and if this needs to be moved to the API
            if mod_logo_response.status_code == 302:
                mod_logo_response = await client.get(
                    mod_logo_response.headers["Location"], headers=headers
                )

            mod_data["logo_content"] = mod_logo_response.content
            self.sgl_append_found_mod.emit(mod_data)
            self.sgl_update_progress.emit()

        await search_mods(
            apis=get_all_apis(),
            urls=self.urls,
            mc_version=self.mc_version,
            mod_loader=self.mod_loader,
            essential_data_only=False,
            after_response_callback=after_response_callback,
        )

    def run(self):
        try:
            asyncio.run(self.search())
        except asyncio.exceptions.CancelledError:
            self.sgl_cancelled.emit()
            return

        self.sgl_done.emit()

    def stop(self):
        get_gather().cancel()
