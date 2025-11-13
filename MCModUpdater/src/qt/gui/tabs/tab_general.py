import os.path

from PySide6 import QtCore
from PySide6.QtWidgets import (
    QWidget,
    QLineEdit,
    QPushButton,
    QComboBox,
    QCheckBox,
    QPlainTextEdit,
    QProgressBar,
    QVBoxLayout,
    QLabel,
    QFileDialog,
    QRadioButton,
)
from PySide6.QtUiTools import QUiLoader

from MCModUpdater.src.core.Settings import Settings
from MCModUpdater.src.core.custom_types import ModData
from MCModUpdater.src.core.enums import ModLoader, BackupOption
from MCModUpdater.src.core.mmu_core import backup_old_files
from MCModUpdater.src.qt.gui.tabs.tab_general_ui import Ui_TabGeneral
from MCModUpdater.src.utils.logger import get_logger
from MCModUpdater.src.utils.utils import (
    get_default_download_directory,
    clean_url_list,
    load_enum,
)
from MCModUpdater.src.qt.gui.components.mod_widget import ModWidget
from MCModUpdater.src.qt.gui.popups.failed_mods import FailedModsPopup
from MCModUpdater.src.qt.threads.DownloadThread import DownloadThread
from MCModUpdater.src.qt.threads.SearchThread import SearchThread


_loader = QUiLoader()

class TabGeneral(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        # self.window = _loader.load(os.path.join(DESIGNER_DIR_PATH, "tabs", "tab_general.ui"), self)
        self.ui = Ui_TabGeneral()
        self.ui.setupUi(self)

        self.settings = Settings()
        self.logger = get_logger()
        self.mod_index = 0
        self.found_mods: list[ModData] = []
        self.failed_mods: list[ModData] = []
        self.interactive_widgets: list[QWidget] = []

        # Define widgets
        self.download_dir_input: QLineEdit = self.findChild(
            QLineEdit, "downloadDirInput"
        )
        self.download_dir_button: QPushButton = self.findChild(
            QPushButton, "downloadDirButton"
        )
        self.mc_version_input: QLineEdit = self.findChild(QLineEdit, "versionInput")
        self.mod_loader_input: QComboBox = self.findChild(QComboBox, "modloaderOptions")
        self.backup_inputs: list[QRadioButton] = [
            self.findChild(QRadioButton, "oldModsBackup"),
            self.findChild(QRadioButton, "oldModsDelete"),
            self.findChild(QRadioButton, "oldModsNothing"),
        ]
        self.use_backup_api_input: QCheckBox = self.findChild(
            QCheckBox, "extraOptions_useBackupApi"
        )
        self.mod_urls_input: QPlainTextEdit = self.findChild(
            QPlainTextEdit, "modUrlsTextEdit"
        )
        self.search_mods_button: QPushButton = self.findChild(
            QPushButton, "searchModsButton"
        )
        self.download_mods_button: QPushButton = self.findChild(
            QPushButton, "downloadModsButton"
        )
        self.progress_bar: QProgressBar = self.findChild(QProgressBar, "progressBar")
        self.found_mods_label: QLabel = self.findChild(QLabel, "foundModsLabel")
        self.found_mods_container: QWidget = self.findChild(
            QWidget, "foundModsContainer"
        )
        self.vertical_layout: QVBoxLayout = self.findChild(
            QVBoxLayout, "verticalLayout"
        )

        # Hide widgets/delete delete example widgets
        self.findChild(QWidget, "modWidgetExample").deleteLater()
        self.progress_bar.hide()

        # Setup for getting download directory
        self.download_dir_input.setText(get_default_download_directory())
        self.download_dir_button.clicked.connect(self.get_directory)

        # Setup for searching for mods online
        self.search_mods_button.clicked.connect(self.search_mods)
        self.mod_urls_input.setPlaceholderText(
            "Mod URLs here, example:\n"
            "https://www.curseforge.com/minecraft/mc-mods/fabric-api\n"
            "https://modrinth.com/mod/sodium\n"
            "https://modrinth.com/mod/sodium-extra\n"
            "https://www.curseforge.com/minecraft/mc-mods/controlling"
        )
        self.mod_urls_input.setPlainText("")

        # Setup for download mods
        self.download_mods_button.clicked.connect(self.download_mods)

        # Misc
        self.mc_version_input.setFocus()
        self.vertical_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.use_backup_api_input.setEnabled(False)

        # Add interactive widgets to list
        self.interactive_widgets.append(self.download_dir_input)
        self.interactive_widgets.append(self.download_dir_button)
        self.interactive_widgets.append(self.mc_version_input)
        self.interactive_widgets.append(self.mod_loader_input)
        self.interactive_widgets.extend(self.backup_inputs)
        # self.interactive_widgets.append(self.use_backup_api_input)
        self.interactive_widgets.append(self.mod_urls_input)
        self.interactive_widgets.append(self.search_mods_button)
        self.interactive_widgets.append(self.download_mods_button)

        self.load_settings()

        self.show()

    def get_directory(self):
        previous = self.download_dir_input.text()
        directory = str(
            QFileDialog.getExistingDirectory(
                self.download_dir_input,
                caption="Select the directory where the mods are stored",
                directory=self.download_dir_input.text(),
            )
        )

        if directory == "":
            directory = previous

        self.download_dir_input.setText(directory)
        if directory != previous:
            self.logger.info(f"Changed directory from '{previous}' to '{directory}'")

    def search_mods(self):
        def show_failed_mods():
            self.logger.info("Creating popup showing what mods failed...")
            self.failed_mods_popup = FailedModsPopup()
            self.failed_mods_popup.set_mod_urls(self.failed_mods)
            self.failed_mods_popup.exec()
            self.logger.info("Done showing popup")

        def widget_action_button_clicked(mod_title: str):
            self.found_mods = [
                md for md in self.found_mods if md["mod_title"] != mod_title
            ]

        def widget_destoyed():
            self.found_mods_label.setText(
                f"Mods Found Online ({len(self.found_mods)}): "
            )

        def when_done():
            self.found_mods.sort(key=lambda mod_data: mod_data["mod_title"])
            self.found_mods_label.setText(
                f"Mods Found Online ({len(self.found_mods)}): "
            )
            for mod_data in self.found_mods:
                widget: ModWidget = ModWidget(
                    mod_data, parent=self.found_mods_container
                )
                widget.sgl_action_button_clicked.connect(widget_action_button_clicked)
                widget.destroyed.connect(widget_destoyed)
                self.vertical_layout.addWidget(
                    widget, alignment=QtCore.Qt.AlignmentFlag.AlignTop
                )

            self.progress_bar.hide()
            self.enable_interactive_widgets(True, self.search_mods_button)

            if self.failed_mods:
                show_failed_mods()

        def when_cancelled():
            self.progress_bar.hide()
            self.enable_interactive_widgets(True, self.search_mods_button)
            self.logger.info("Searching stopped by user")

        # Reset arrays and remove old mod results
        self.found_mods = []
        self.failed_mods = []
        for widget in self.found_mods_container.findChildren(QWidget, "modWidget"):
            widget.deleteLater()

        mod_urls = clean_url_list(self.mod_urls_input.toPlainText().split("\n"))
        mc_version = self.mc_version_input.text()
        mod_loader = ModLoader(self.mod_loader_input.currentIndex() + 1)

        self.progress_bar.setValue(0)
        self.progress_bar.setMaximum(len(mod_urls))
        self.progress_bar.show()
        self.enable_interactive_widgets(False, self.search_mods_button)

        # Run SearchThread
        self.thread = SearchThread(
            urls=mod_urls, mc_version=mc_version, mod_loader=mod_loader
        )
        self.thread.sgl_update_progress.connect(
            lambda: self.progress_bar.setValue(self.progress_bar.value() + 1)
        )
        self.thread.sgl_append_found_mod.connect(self.found_mods.append)
        self.thread.sgl_append_failed_mod.connect(self.failed_mods.append)
        self.thread.sgl_cancelled.connect(when_cancelled)
        self.thread.sgl_done.connect(when_done)
        self.thread.start()

    def download_mods(self):
        def when_done():
            self.progress_bar.hide()
            self.enable_interactive_widgets(True, self.download_mods_button)

        def when_cancelled():
            self.progress_bar.hide()
            self.enable_interactive_widgets(True, self.download_mods_button)

        download_dir = self.download_dir_input.text()
        backup_option: BackupOption = self.get_backup_option()

        backup_old_files(download_dir, backup_option)
        self.progress_bar.setValue(0)
        self.progress_bar.setMaximum(len(self.found_mods))
        self.progress_bar.show()
        self.enable_interactive_widgets(False, self.download_mods_button)

        # Run DownloadThread
        self.thread = DownloadThread(self.found_mods, download_dir)
        self.thread.sgl_update_progress.connect(
            lambda: self.progress_bar.setValue(self.progress_bar.value() + 1)
        )
        self.thread.sgl_done.connect(when_done)
        self.thread.sgl_cancelled.connect(when_cancelled)
        self.thread.start()

    def enable_interactive_widgets(self, val: bool, trigger_widget: QPushButton = None):
        for widget in self.interactive_widgets:
            if widget is not trigger_widget:
                widget.setEnabled(val)

        for mod_widget in self.found_mods_container.findChildren(QWidget, "modWidget"):
            mod_widget.setEnabled(val)

        if trigger_widget is None:
            return

        # Set trigger_widget to normal/stop button
        trigger_widget.clicked.disconnect()
        if trigger_widget.text() != "Stop":
            trigger_widget.setText("Stop")
            trigger_widget.setStyleSheet(
                "QPushButton {"
                + "  background-color: #9e2c24;"
                + "}"
                + "QPushButton:pressed {"
                + "  background-color: #6b1d18;"
                + "}"
            )
            trigger_widget.clicked.connect(self.stop_thread_action)
        else:
            if trigger_widget is self.search_mods_button:
                trigger_widget.setText("Search Mods")
                trigger_widget.clicked.connect(self.search_mods)
            elif trigger_widget is self.download_mods_button:
                trigger_widget.setText("Download Mods")
                trigger_widget.clicked.connect(self.download_mods)
            trigger_widget.setStyleSheet("")

    def stop_thread_action(self):
        self.thread.stop()

    def load_settings(self):
        self.logger.info("Loading General Tab settings...")
        self.download_dir_input.setText(self.settings.download_dir)
        self.mc_version_input.setText(self.settings.mc_version)
        self.mod_loader_input.setCurrentIndex(self.settings.mod_loader.value - 1)
        self.mod_urls_input.setPlainText("\n".join(self.settings.urls))
        self.set_backup_option(self.settings.backup_option)
        self.logger.info("General Tab settings loaded")

    def save_settings(self):
        self.logger.info("Saving General Tab settings...")
        self.settings.download_dir = self.download_dir_input.text()
        self.settings.mc_version = self.mc_version_input.text()
        self.settings.mod_loader = load_enum(
            ModLoader, self.mod_loader_input.currentIndex() + 1
        )
        self.settings.urls = self.mod_urls_input.toPlainText().split("\n")
        self.settings.backup_option = self.get_backup_option()
        self.logger.info("General Tab settings saved")

    def get_backup_option(self) -> BackupOption | None:
        """
        Converts the backup options in the UI to the `BackupOption` enum.

        ONLY WORKS IF RADIO BUTTONS AND ENUM ARE IN THE SAME ORDER!

        Returns:
            The correct BackupOption enum, or None if something went wrong
        """

        for i, radio_input in enumerate(self.backup_inputs):
            if radio_input.isChecked():
                return load_enum(BackupOption, i + 1)
        return None

    def set_backup_option(self, backup_option_index: int):
        """
        Converts the `BackupOption` enum to the backup options in the UI.

        ONLY WORKS IF RADIO BUTTONS AND ENUM ARE IN THE SAME ORDER!
        """

        for i, radio_input in enumerate(self.backup_inputs):
            if i + 1 == backup_option_index:
                radio_input.setChecked(True)
            else:
                radio_input.setChecked(False)
