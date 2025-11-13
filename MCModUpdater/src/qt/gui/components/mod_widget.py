import os

from PySide6 import QtGui, QtCore
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QStyleOption, QStyle
from PySide6.QtUiTools import QUiLoader

from MCModUpdater.src.core.constants import ICONS_DIR_PATH
from MCModUpdater.src.core.custom_types import ModData
from MCModUpdater.src.core.mmu_core import get_all_apis
from MCModUpdater.src.qt.gui.components.Tags import Tag
from MCModUpdater.src.qt.gui.components.mod_widget_ui import Ui_modWidget

_loader = QUiLoader()

class ModWidget(QWidget):
    sgl_action_button_clicked: QtCore.Signal = QtCore.Signal(str)

    def __init__(self, mod_data: ModData, parent=None):
        super().__init__(parent=parent)

        # _loader.load(os.path.join(DESIGNER_DIR_PATH, "components", "mod_widget.ui"), self)
        self.ui = Ui_modWidget()
        self.ui.setupUi(self)

        # Define widgets
        self.name_label: QLabel = self.findChild(QLabel, "modName")
        self.icon_label: QLabel = self.findChild(QLabel, "modIcon")
        self.details_label: QLabel = self.findChild(QLabel, "modDetails")
        self.action_button: QPushButton = self.findChild(QPushButton, "actionButton")

        # Mod name
        self.name_label.setText(mod_data["mod_title"])
        self.name_label.setToolTip(mod_data["mod_title"])

        # Mod icon
        mod_icon = QtGui.QPixmap()
        if not mod_data["logo_content"]:
            QtGui.QPixmap(os.path.join(ICONS_DIR_PATH, "no-icon.png"))
        else:
            mod_icon.loadFromData(mod_data["logo_content"])
        self.icon_label.setPixmap(mod_icon)

        # Origin Tag
        for api in get_all_apis():
            if api.name == mod_data["origin"]:
                origin_tag = Tag(tag_data=api.get_tag_data(), parent=self)
                origin_tag.move(80, 28)
                break

        # Filename
        self.details_label.setText(f"File: {mod_data['file_name']}")
        self.details_label.setToolTip(f"File: {mod_data['file_name']}")

        # Action button
        action_icon = QtGui.QIcon(os.path.join(ICONS_DIR_PATH, "trash.png"))
        self.action_button.clicked.connect(self.action_button_clicked)
        self.action_button.setIcon(action_icon)
        self.action_button.setIconSize(QtCore.QSize(32, 32))

    def action_button_clicked(self):
        self.sgl_action_button_clicked.emit(self.name_label.text())
        self.deleteLater()

    # Needed: https://stackoverflow.com/a/32889486, https://stackoverflow.com/a/34300669
    def paintEvent(self, event):
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(
            QStyle.PrimitiveElement.PE_Widget, opt, painter, self
        )
