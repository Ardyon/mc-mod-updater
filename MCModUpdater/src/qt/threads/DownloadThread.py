import asyncio

from PySide6 import QtCore

from MCModUpdater.src.core.custom_types import ModData
from MCModUpdater.src.core.mmu_core import download_mods, get_gather


class DownloadThread(QtCore.QThread):
    sgl_update_progress = QtCore.Signal()
    sgl_done = QtCore.Signal()
    sgl_cancelled = QtCore.Signal()

    def __init__(self, mods_data: list[ModData], download_dir: str):
        super().__init__()

        self.mods_data: list[ModData] = mods_data
        self.download_dir: str = download_dir

    async def download(self):
        async def after_response_callback(mod_data: ModData):
            self.sgl_update_progress.emit()

        await download_mods(
            mods_data=self.mods_data,
            download_path=self.download_dir,
            after_response_callback=after_response_callback,
        )

    def run(self):
        try:
            asyncio.run(self.download())
        except asyncio.exceptions.CancelledError:
            self.sgl_cancelled.emit()
            return

        self.sgl_done.emit()

    def stop(self):
        get_gather().cancel()
        # for t in get_tasks():
        #     t.cancel()
