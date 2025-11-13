import os.path
import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtUiTools import QUiLoader

from MCModUpdater.src.core.Settings import Settings
from MCModUpdater.src.core.constants import (
    APP_VERSION,
    RESOURCES_DIR_PATH,
    APP_NAME, LOGO_DIR_PATH,
)
from MCModUpdater.src.core.enums import ApiKeyRequirement
from MCModUpdater.src.core.mmu_core import get_all_apis, _logger
from MCModUpdater.src.qt.gui.main_ui import Ui_MainWindow
from MCModUpdater.src.qt.gui.popups.api_warning import ApiWarningPopup
from MCModUpdater.src.qt.gui.tabs.tabs import Tabs

_loader = QUiLoader()

class GUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.window = _loader.load(os.path.join(DESIGNER_DIR_PATH, "main.ui"), self)

        self.settings = Settings()

        # Set properties
        self.setWindowTitle(f"{APP_NAME} {APP_VERSION}")
        print(os.path.join(RESOURCES_DIR_PATH, "mc_mod_updater_icon.ico"))
        self.setWindowIcon(
            QIcon(os.path.join(LOGO_DIR_PATH, "mc_mod_updater_icon.ico"))
        )

        # Define widgets
        self.tabs = Tabs(parent=self.centralWidget())

        self.show()

        self.check_api_keys()

    def save_settings(self):
        self.tabs.save_settings()
        self.settings.save()

    def check_api_keys(self):
        if self.settings.ignore_api_warning:
            return

        for api in get_all_apis():
            if api.api_key_requirement is not ApiKeyRequirement.REQUIRED:
                continue

            if api.get_api_key() is not None:
                continue

            self.api_popup = ApiWarningPopup(api)
            self.api_popup.exec()
            api_key, button_text = self.api_popup.get_response()

            if button_text == "Save":
                _logger.info("User clicked the save button")
                if not api_key:
                    _logger.warning("No API key provided")
                    continue

                api.set_api_key(api_key)
                _logger.info(f"API key for '{api.name}' set")
            elif button_text == "Ignore":
                _logger.info("User clicked the ignore button")
                self.settings.ignore_api_warning = True
            elif button_text == "Close":
                _logger.info("User clicked the close button")

    def closeEvent(self, *args, **kwargs):
        self.save_settings()
        super(QMainWindow, self).closeEvent(*args, **kwargs)


# TODO: Make popup when errors occur
if __name__ == "__main__":
    # Initialize the app
    app = QApplication(sys.argv)
    UIWindow = GUI()
    sys.exit(app.exec())
