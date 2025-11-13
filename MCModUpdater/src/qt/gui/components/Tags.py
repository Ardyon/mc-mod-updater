from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QLabel

from MCModUpdater.src.core.custom_types import TagData


class Tag(QLabel):
    font: QFont = QFont()
    font.setFamily("Segoe UI")
    font.setPointSize(9)
    font.setBold(True)

    def __init__(self, tag_data: TagData, parent=None):
        super().__init__(parent=parent)

        self.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.setFont(self.font)
        self.setFixedWidth(tag_data["width"])
        self.setFixedHeight(tag_data["height"])
        self.setText(tag_data["text"])
        self.setStyleSheet(
            "QLabel {"
            f"  border: 1px solid {tag_data['foreground_color']};"
            f"  border-radius: 5px;"
            f"  color: {tag_data['foreground_color']};"
            f"  background-color: {tag_data['background_color']};"
            "}"
        )


class UnknownTag(Tag):
    tag_data: TagData = {
        "text": "Unknown",
        "background_color": "#4A4A4A",
        "foreground_color": "#9C9C9C",
        "width": 60,
        "height": 20,
    }

    def __init__(self, parent=None):
        super().__init__(tag_data=self.tag_data, parent=parent)
