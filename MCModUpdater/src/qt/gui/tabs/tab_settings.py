import os

from PySide6.QtWidgets import (
    QWidget,
    QPlainTextEdit,
    QPushButton,
    QFileDialog,
    QMessageBox,
    QStackedWidget,
    QLabel,
)
from PySide6.QtUiTools import QUiLoader

from MCModUpdater.src.core.Settings import Settings
from MCModUpdater.src.core.constants import CONFIG_DIR_PATH
from MCModUpdater.src.core.mmu_core import get_all_apis, _logger
from MCModUpdater.src.qt.gui.tabs.tab_settings_ui import Ui_settingsWidget

_loader = QUiLoader()

class TabSettings(QWidget):
    def __init__(self, mod_list_input: QPlainTextEdit, parent=None):
        super().__init__(parent=parent)

        self.mod_list_input = mod_list_input

        # Load UI file
        # self.window = _loader.load(os.path.join(DESIGNER_DIR_PATH, "tabs", "tab_settings.ui"), self)
        self.ui = Ui_settingsWidget()
        self.ui.setupUi(self)

        self.settings = Settings()
        self.load_all_api_settings()

        # Define widgets
        self.mod_list_export_button: QPushButton = self.findChild(
            QPushButton, "modListExportButton"
        )
        self.mod_list_import_button: QPushButton = self.findChild(
            QPushButton, "modListImportButton"
        )

        # Make widgets functional
        self.mod_list_export_button.clicked.connect(self.export_mod_list)
        self.mod_list_import_button.clicked.connect(self.import_mod_list)

        self.load_settings()

    def export_mod_list(self):
        file_names = QFileDialog.getSaveFileName(
            parent=self,
            caption="Save mod list as file",
            dir=f"{CONFIG_DIR_PATH}/mod-list.txt",
            filter="Text files (*.txt)",
        )

        file_location = file_names[0]
        if file_location:
            with open(file_location, "w") as f:
                f.write(self.mod_list_input.toPlainText())
            _logger.info(f"Exported mod list to file '{file_location}'")
        else:
            _logger.info("User cancelled exporting mod list")

    def import_mod_list(self):
        file_names = QFileDialog.getOpenFileName(
            parent=self,
            caption="Open mod list file",
            dir=f"{CONFIG_DIR_PATH}/mod-list.txt",
            filter="Text files (*.txt)",
        )

        file_location = file_names[0]
        if file_location:
            with open(file_location, "r") as f:
                file_content = f.read()
                self.mod_list_input.setPlainText(file_content)

            _logger.info(f"Imported mod list from file '{file_location}'")
            dialog = QMessageBox(
                parent=self,
                text=f"Importing '{os.path.basename(file_location)}' was successful.",
            )
            dialog.setWindowTitle("Import successful")
            dialog.exec()
        else:
            _logger.info("User cancelled importing mod list")

    def load_all_api_settings(self):
        stacked_widget: QStackedWidget = self.findChild(QStackedWidget, "apiSettings")
        left_arrow: QPushButton = self.findChild(QPushButton, "leftArrow")
        right_arrow: QPushButton = self.findChild(QPushButton, "rightArrow")

        left_arrow.clicked.connect(
            lambda: stacked_widget.setCurrentIndex(stacked_widget.currentIndex() - 1)
        )
        right_arrow.clicked.connect(
            lambda: stacked_widget.setCurrentIndex(stacked_widget.currentIndex() + 1)
        )

        for api in get_all_apis():
            widget: QWidget = QWidget()
            label: QLabel = QLabel(parent=widget, text=api.name)
            label.setGeometry(0, 0, 151, 21)
            stacked_widget.addWidget(widget)

    def load_settings(self):
        pass

    def save_settings(self):
        raise NotImplementedError()
