import os.path

from PySide6.QtWidgets import QTabWidget, QWidget
from PySide6.QtUiTools import QUiLoader

from MCModUpdater.src.qt.gui.tabs.tab_general import TabGeneral
from MCModUpdater.src.qt.gui.tabs.tab_settings import TabSettings
from MCModUpdater.src.qt.gui.tabs.tabs_ui import Ui_TabWidget

_loader = QUiLoader()


class Tabs(QTabWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        # self.window = _loader.load(os.path.join(DESIGNER_DIR_PATH, "tabs", "tabs.ui"))
        self.ui = Ui_TabWidget()
        self.ui.setupUi(self)

        # Define widgets
        self.tab_general_ui = self.findChild(QWidget, "general")
        self.tab_search_ui = self.findChild(QWidget, "search")
        self.tab_settings_ui = self.findChild(QWidget, "settings")

        # Define content
        self.tab_general = TabGeneral(parent=self.tab_general_ui)
        self.tab_settings = TabSettings(
            mod_list_input=self.tab_general.mod_urls_input, parent=self.tab_settings_ui
        )

        self.show()

    def save_settings(self):
        self.tab_general.save_settings()
        # self.tab_search.save_settings()
        # self.tab_settings.save_settings()
