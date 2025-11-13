import os.path

import sys

from PySide6 import QtCore
from PySide6.QtWidgets import QDialog, QLabel, QApplication
from PySide6.QtUiTools import QUiLoader

from MCModUpdater.src.core.custom_types import ModData
from MCModUpdater.src.qt.gui.popups.failed_mods_ui import Ui_Dialog

_loader = QUiLoader()

class FailedModsPopup(QDialog):
    def __init__(self):
        super(FailedModsPopup, self).__init__()

        # Load ui file
        # _loader.load(os.path.join(DESIGNER_DIR_PATH, "popups", "failed_mods.ui"), self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Define widgets
        self._mods_label: QLabel = self.findChild(QLabel, "modsLabel")
        self._mods_label.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self._mods_label.setOpenExternalLinks(True)

    def set_mod_urls(self, mods_data: list[ModData]):
        mod_urls = map(
            lambda mod_data: f'<a href="{mod_data["page_url"]}">{mod_data["page_url"]}</a>',
            mods_data,
        )
        self._mods_label.setText("<br>".join(mod_urls))


if __name__ == "__main__":
    # Initialize the app
    app = QApplication(sys.argv)
    UIWindow = FailedModsPopup()
    UIWindow.show()
    app.exec()
