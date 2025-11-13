# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mod_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_modWidget(object):
    def setupUi(self, modWidget):
        if not modWidget.objectName():
            modWidget.setObjectName(u"modWidget")
        modWidget.resize(470, 80)
        modWidget.setMinimumSize(QSize(0, 80))
        modWidget.setMaximumSize(QSize(470, 80))
        modWidget.setStyleSheet(u"/* modWidget */\n"
"#modWidget {\n"
"  background-color: rgba(255, 255, 255, 0.1);\n"
"  border-radius: 10px;\n"
"}\n"
"\n"
"/* modWidget Label */\n"
"#modWidget QLabel {\n"
"  color: #DCE4EE;\n"
"  background-color: rgba(255, 255, 255, 0.0);\n"
"}\n"
"\n"
"/* modWidget PushButton */\n"
"#modWidget QPushButton {\n"
"  background-color: #9e2c24;\n"
"  border-radius: 5px;\n"
"}\n"
"#modWidget QPushButton:pressed {\n"
"  background-color: #6b1d18;\n"
"}")
        self.modName = QLabel(modWidget)
        self.modName.setObjectName(u"modName")
        self.modName.setGeometry(QRect(80, 0, 291, 31))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        font.setBold(True)
        self.modName.setFont(font)
        self.actionButton = QPushButton(modWidget)
        self.actionButton.setObjectName(u"actionButton")
        self.actionButton.setGeometry(QRect(410, 20, 41, 41))
        icon = QIcon()
        icon.addFile(u"../../../../resources/trash.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionButton.setIcon(icon)
        self.actionButton.setIconSize(QSize(32, 32))
        self.modIcon = QLabel(modWidget)
        self.modIcon.setObjectName(u"modIcon")
        self.modIcon.setGeometry(QRect(10, 10, 61, 61))
        self.modIcon.setPixmap(QPixmap(u"../../../../resources/icons/no-icon.png"))
        self.modIcon.setScaledContents(True)
        self.modIcon.setAlignment(Qt.AlignCenter)
        self.modDetails = QLabel(modWidget)
        self.modDetails.setObjectName(u"modDetails")
        self.modDetails.setGeometry(QRect(80, 50, 321, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(9)
        font1.setBold(False)
        self.modDetails.setFont(font1)
        self.modDetails.setTextFormat(Qt.PlainText)
        self.modDetails.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.retranslateUi(modWidget)

        QMetaObject.connectSlotsByName(modWidget)
    # setupUi

    def retranslateUi(self, modWidget):
        modWidget.setWindowTitle(QCoreApplication.translate("modWidget", u"Form", None))
#if QT_CONFIG(tooltip)
        self.modName.setToolTip(QCoreApplication.translate("modWidget", u"Mod name", None))
#endif // QT_CONFIG(tooltip)
        self.modName.setText(QCoreApplication.translate("modWidget", u"Mod name", None))
        self.actionButton.setText("")
#if QT_CONFIG(tooltip)
        self.modDetails.setToolTip(QCoreApplication.translate("modWidget", u"File: this-is-a-test.jar", None))
#endif // QT_CONFIG(tooltip)
        self.modDetails.setText(QCoreApplication.translate("modWidget", u"File: this-is-a-test.jar", None))
    # retranslateUi

