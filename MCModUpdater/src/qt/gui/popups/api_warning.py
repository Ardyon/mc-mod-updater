import os.path
import sys

from PySide6.QtWidgets import QDialog, QApplication, QDialogButtonBox, QLineEdit, QLabel
from PySide6.QtUiTools import QUiLoader

from MCModUpdater.src.core.apis.BaseModProviderAPI import BaseModProviderAPI
from MCModUpdater.src.core.apis.CurseForgeAPI import CurseForgeAPI
from MCModUpdater.src.qt.gui.popups.api_warning_ui import Ui_Dialog

_loader = QUiLoader()

class ApiWarningPopup(QDialog):
    def __init__(self, api: BaseModProviderAPI):
        super().__init__()

        # _loader.load(os.path.join(DESIGNER_DIR_PATH, "popups", "api_warning.ui"), self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Define widgets
        self._explanation_label: QLabel = self.findChild(QLabel, "explanationLabel")
        self._api_input: QLineEdit = self.findChild(QLineEdit, "apiInput")
        self._button_box: QDialogButtonBox = self.findChild(
            QDialogButtonBox, "buttonBox"
        )

        self._api_input.setFocus()
        self._button_box.button(QDialogButtonBox.StandardButton.Save).clicked.connect(
            self._save
        )
        self._button_box.button(QDialogButtonBox.StandardButton.Ignore).clicked.connect(
            self._ignore
        )
        self._button_box.button(QDialogButtonBox.StandardButton.Close).clicked.connect(
            self._close
        )
        self._pressed_button_text = ""

        self._explanation_label.setOpenExternalLinks(True)
        self._explanation_label.setText(api.api_key_warning_text)

        self.setWindowTitle(f"API Key Warning - {api.name}")

    def _save(self):
        self._pressed_button_text = "Save"

    def _ignore(self):
        self._pressed_button_text = "Ignore"

    def _close(self):
        self._pressed_button_text = "Close"

    def get_response(self):
        return self._api_input.text(), self._pressed_button_text


if __name__ == "__main__":
    # Initialize the app
    app = QApplication(sys.argv)
    UIWindow = ApiWarningPopup(CurseForgeAPI())
    UIWindow.show()
    app.exec()
