# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tab_settings.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QStackedWidget,
    QWidget)

class Ui_settingsWidget(object):
    def setupUi(self, settingsWidget):
        if not settingsWidget.objectName():
            settingsWidget.setObjectName(u"settingsWidget")
        settingsWidget.resize(1050, 701)
        self.settings = QFrame(settingsWidget)
        self.settings.setObjectName(u"settings")
        self.settings.setGeometry(QRect(10, 10, 1031, 681))
        self.settings.setStyleSheet(u"#settings {\n"
"	background-color: #2a2a2a;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"#leftArrow,\n"
"#rightArrow {\n"
"  border-radius: 2px;\n"
"  color: #DCE4EE;\n"
"  background: none;\n"
"}\n"
"\n"
"#leftArrow:pressed,\n"
"#rightArrow:pressed {\n"
"  color: #959aa1;\n"
"  background: rgba(0, 0, 0, 0.5);\n"
"}\n"
"\n"
"\n"
"QGroupBox {\n"
"	border: 2px solid #DCE4EE;\n"
"    border-radius: 5px;\n"
"	margin-top: 0.5em;\n"
"}\n"
"QGroupBox::title {\n"
"	top: -10px;\n"
"	left: 10px;\n"
"	padding: 0 2px ;\n"
"	color: #DCE4EE;\n"
"}\n"
"\n"
"\n"
"/* Label */\n"
"QLabel {\n"
"	color: #DCE4EE;\n"
"}\n"
"\n"
"\n"
"/* PushButton */\n"
"QPushButton {\n"
"	color: #DCE4EE;\n"
"	background-color: #2f5ea1;\n"
"	border-radius: 8px;\n"
"}\n"
"QPushButton:pressed {\n"
"	color: #DCE4EE;\n"
"	background-color: #20406d;\n"
"}\n"
"QPushButton:disabled {\n"
"	color: #959aa1;\n"
"	background-color: #183154;\n"
"}\n"
"#stopButton {\n"
"	background-color: #9e2c24;\n"
"}\n"
"#stopButton:pressed {\n"
"	background-color: #6b1d18;\n"
""
                        "}\n"
"\n"
"\n"
"/* LineEdit */\n"
"QLineEdit {\n"
"	color: #DCE4EE;\n"
"	background-color: rgba(255, 255, 255, 0.1);\n"
"	border-radius: 3px;\n"
"	border: 1px solid #DCE4EE;\n"
"}\n"
"QLineEdit:disabled {\n"
"	color: #959aa1;\n"
"	background-color: rgba(255, 255, 255, 0.05);\n"
"	border: 1px solid #959aa1;\n"
"}\n"
"\n"
"\n"
"/* ComboBox */\n"
"QComboBox {\n"
"	border-radius: 0px;\n"
"	color: #DCE4EE;\n"
"	background-color: rgba(255, 255, 255, 0.1);\n"
"}\n"
"QComboBox:disabled {\n"
"	color: #959aa1;\n"
"	background-color: rgba(255, 255, 255, 0.05);\n"
"}\n"
"QComboBox QListView {\n"
"	padding: 5px;\n"
"	color: #DCE4EE;\n"
"	background-color: rgba(255, 255, 255, 0.1);\n"
"	border-radius: 0px;\n"
"	outline: 0px;\n"
"}\n"
"QComboBox QListView:disabled {\n"
"	color: #959aa1;\n"
"	background-color: rgba(255, 255, 255, 0.05);\n"
"}\n"
"\n"
"\n"
"/* CheckBox */\n"
"QCheckBox {\n"
"	color: #DCE4EE;\n"
"}\n"
"QCheckBox:disabled {\n"
"	color: #959aa1;\n"
"}\n"
"\n"
"\n"
"/* PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	pa"
                        "dding: 3px;\n"
"	border: 1px solid #DCE4EE;\n"
"	border-radius: 10px;\n"
"	color: #DCE4EE;\n"
"	background-color: rgba(255, 255, 255, 0.1);\n"
"}\n"
"QPlainTextEdit:disabled {\n"
"	border: 1px solid #959aa1;\n"
"	color: #959aa1;\n"
"	background-color: rgba(255, 255, 255, 0.05);\n"
"}\n"
"/* SCROLLBAR */\n"
"QScrollBar {\n"
"	border: none;\n"
"    background: #3f3f3f;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar:vertical {\n"
"    width: 10px;\n"
" }\n"
"QScrollBar:horizontal {\n"
"    height: 10px;\n"
"}\n"
"QScrollBar:disabled {\n"
"    background: rgba(255, 255, 255, 0.0);\n"
" }\n"
"/* HANDLE BAR */\n"
"QScrollBar::handle {\n"
"	background: #DCE4EE;\n"
"	border-radius: 5px;\n"
"}\n"
"QScrollBar::handle:pressed {	\n"
"	background-color: #acb3bb;\n"
"}\n"
"QScrollBar::handle:disabled {\n"
"	background: #959aa1;\n"
"}\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical, \n"
"QScrollBar::add-line:vertical {\n"
"	height: 0px;\n"
"}\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:horizontal, \n"
""
                        "QScrollBar::add-line:horizontal {\n"
"	width: 0px;\n"
"}\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical,\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical,\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal,\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"	background: none;\n"
"}")
        self.settings.setFrameShape(QFrame.StyledPanel)
        self.settings.setFrameShadow(QFrame.Raised)
        self.miscSettings = QGroupBox(self.settings)
        self.miscSettings.setObjectName(u"miscSettings")
        self.miscSettings.setGeometry(QRect(10, 410, 271, 261))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        self.miscSettings.setFont(font)
        self.modListImportButton = QPushButton(self.miscSettings)
        self.modListImportButton.setObjectName(u"modListImportButton")
        self.modListImportButton.setEnabled(True)
        self.modListImportButton.setGeometry(QRect(140, 30, 121, 31))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        font1.setBold(False)
        self.modListImportButton.setFont(font1)
        self.modListExportButton = QPushButton(self.miscSettings)
        self.modListExportButton.setObjectName(u"modListExportButton")
        self.modListExportButton.setEnabled(True)
        self.modListExportButton.setGeometry(QRect(10, 30, 121, 31))
        self.modListExportButton.setFont(font1)
        self.apiSettings = QStackedWidget(self.settings)
        self.apiSettings.setObjectName(u"apiSettings")
        self.apiSettings.setGeometry(QRect(10, 10, 951, 61))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.apiKeyApplyButton = QPushButton(self.page)
        self.apiKeyApplyButton.setObjectName(u"apiKeyApplyButton")
        self.apiKeyApplyButton.setEnabled(True)
        self.apiKeyApplyButton.setGeometry(QRect(790, 20, 71, 31))
        self.apiKeyApplyButton.setFont(font1)
        self.apiKeyLabel = QLabel(self.page)
        self.apiKeyLabel.setObjectName(u"apiKeyLabel")
        self.apiKeyLabel.setGeometry(QRect(0, -1, 151, 21))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.apiKeyLabel.setFont(font2)
        self.apiKeyLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.apiKeyInput = QLineEdit(self.page)
        self.apiKeyInput.setObjectName(u"apiKeyInput")
        self.apiKeyInput.setEnabled(True)
        self.apiKeyInput.setGeometry(QRect(0, 20, 781, 30))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(9)
        self.apiKeyInput.setFont(font3)
        self.apiKeyInput.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.apiKeyInput.setEchoMode(QLineEdit.Password)
        self.apiKeyHelpButton = QPushButton(self.page)
        self.apiKeyHelpButton.setObjectName(u"apiKeyHelpButton")
        self.apiKeyHelpButton.setEnabled(True)
        self.apiKeyHelpButton.setGeometry(QRect(870, 20, 71, 31))
        self.apiKeyHelpButton.setFont(font1)
        self.apiSettings.addWidget(self.page)
        self.apiSettingsArrows = QFrame(self.settings)
        self.apiSettingsArrows.setObjectName(u"apiSettingsArrows")
        self.apiSettingsArrows.setGeometry(QRect(970, 10, 51, 21))
        self.apiSettingsArrows.setFrameShape(QFrame.StyledPanel)
        self.apiSettingsArrows.setFrameShadow(QFrame.Raised)
        self.rightArrow = QPushButton(self.apiSettingsArrows)
        self.rightArrow.setObjectName(u"rightArrow")
        self.rightArrow.setGeometry(QRect(30, 0, 21, 21))
        font4 = QFont()
        font4.setPointSize(22)
        font4.setBold(False)
        font4.setItalic(False)
        self.rightArrow.setFont(font4)
        self.leftArrow = QPushButton(self.apiSettingsArrows)
        self.leftArrow.setObjectName(u"leftArrow")
        self.leftArrow.setGeometry(QRect(0, 0, 21, 21))
        font5 = QFont()
        font5.setPointSize(22)
        self.leftArrow.setFont(font5)

        self.retranslateUi(settingsWidget)

        self.apiSettings.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(settingsWidget)
    # setupUi

    def retranslateUi(self, settingsWidget):
        settingsWidget.setWindowTitle(QCoreApplication.translate("settingsWidget", u"Form", None))
        self.miscSettings.setTitle(QCoreApplication.translate("settingsWidget", u"Misc settings", None))
        self.modListImportButton.setText(QCoreApplication.translate("settingsWidget", u"Import mod list", None))
        self.modListExportButton.setText(QCoreApplication.translate("settingsWidget", u"Export mod list", None))
        self.apiKeyApplyButton.setText(QCoreApplication.translate("settingsWidget", u"Save", None))
        self.apiKeyLabel.setText(QCoreApplication.translate("settingsWidget", u"CurseForge API Key", None))
        self.apiKeyInput.setText("")
        self.apiKeyInput.setPlaceholderText(QCoreApplication.translate("settingsWidget", u"Put your CurseForge API key here", None))
        self.apiKeyHelpButton.setText(QCoreApplication.translate("settingsWidget", u"Help", None))
#if QT_CONFIG(tooltip)
        self.rightArrow.setToolTip(QCoreApplication.translate("settingsWidget", u"Next API", None))
#endif // QT_CONFIG(tooltip)
        self.rightArrow.setText(QCoreApplication.translate("settingsWidget", u"\u25b6", None))
#if QT_CONFIG(tooltip)
        self.leftArrow.setToolTip(QCoreApplication.translate("settingsWidget", u"Previous API", None))
#endif // QT_CONFIG(tooltip)
        self.leftArrow.setText(QCoreApplication.translate("settingsWidget", u"\u25c0", None))
    # retranslateUi

