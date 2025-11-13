# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tab_general.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QLabel, QLineEdit, QPlainTextEdit, QProgressBar,
    QPushButton, QRadioButton, QScrollArea, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_TabGeneral(object):
    def setupUi(self, TabGeneral):
        if not TabGeneral.objectName():
            TabGeneral.setObjectName(u"TabGeneral")
        TabGeneral.resize(1050, 701)
        self.settings = QFrame(TabGeneral)
        self.settings.setObjectName(u"settings")
        self.settings.setGeometry(QRect(10, 10, 511, 681))
        self.settings.setStyleSheet(u"#settings {\n"
"	background-color: #2a2a2a;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"/* Label */\n"
"QLabel {\n"
"	color: #DCE4EE\n"
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
""
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
"/* RadioButton */\n"
"QRadioButton {\n"
"  color: #DCE4EE;\n"
"}\n"
"\n"
"\n"
"/* PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	padding: 3px;\n"
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
"	border-rad"
                        "ius: 0px;\n"
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
"QScrollBar::add-line:horizontal {\n"
"	width: 0px;\n"
"}\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical,\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical,\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal,\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"	background: none;\n"
""
                        "}\n"
"\n"
"\n"
"/* ProgressBar */\n"
"QProgressBar {\n"
"    border: 2px solid #dce4ee;\n"
"	padding: 3px;\n"
"    border-radius: 3px;\n"
"	color: #dce4ee;\n"
"    background-color: #2a2a2a;\n"
"}\n"
"QProgressBar::chunk {\n"
"	background-color: green;\n"
"}")
        self.settings.setFrameShape(QFrame.Shape.StyledPanel)
        self.settings.setFrameShadow(QFrame.Shadow.Raised)
        self.modUrlsTextEdit = QPlainTextEdit(self.settings)
        self.modUrlsTextEdit.setObjectName(u"modUrlsTextEdit")
        self.modUrlsTextEdit.setEnabled(True)
        self.modUrlsTextEdit.setGeometry(QRect(10, 310, 490, 251))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(9)
        self.modUrlsTextEdit.setFont(font)
        self.modUrlsTextEdit.setTabChangesFocus(True)
        self.modUrlsTextEdit.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap)
        self.extraOptionsLabel = QLabel(self.settings)
        self.extraOptionsLabel.setObjectName(u"extraOptionsLabel")
        self.extraOptionsLabel.setGeometry(QRect(10, 150, 111, 31))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.extraOptionsLabel.setFont(font1)
        self.extraOptionsLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.downloadDirInput = QLineEdit(self.settings)
        self.downloadDirInput.setObjectName(u"downloadDirInput")
        self.downloadDirInput.setEnabled(True)
        self.downloadDirInput.setGeometry(QRect(10, 30, 361, 30))
        self.downloadDirInput.setFont(font)
        self.progressBar = QProgressBar(self.settings)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(140, 640, 231, 20))
        self.progressBar.setStyleSheet(u"")
        self.progressBar.setMinimum(0)
        self.progressBar.setValue(50)
        self.progressBar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.downloadDirLabel = QLabel(self.settings)
        self.downloadDirLabel.setObjectName(u"downloadDirLabel")
        self.downloadDirLabel.setGeometry(QRect(10, 10, 141, 20))
        self.downloadDirLabel.setFont(font1)
        self.downloadDirLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.versionInput = QLineEdit(self.settings)
        self.versionInput.setObjectName(u"versionInput")
        self.versionInput.setGeometry(QRect(10, 100, 181, 33))
        self.versionInput.setFont(font)
        self.versionInput.setMaxLength(8)
        self.searchModsButton = QPushButton(self.settings)
        self.searchModsButton.setObjectName(u"searchModsButton")
        self.searchModsButton.setGeometry(QRect(40, 580, 191, 31))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(10)
        font2.setBold(False)
        self.searchModsButton.setFont(font2)
        self.versionLabel = QLabel(self.settings)
        self.versionLabel.setObjectName(u"versionLabel")
        self.versionLabel.setGeometry(QRect(10, 78, 181, 20))
        self.versionLabel.setFont(font1)
        self.versionLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.downloadDirButton = QPushButton(self.settings)
        self.downloadDirButton.setObjectName(u"downloadDirButton")
        self.downloadDirButton.setEnabled(True)
        self.downloadDirButton.setGeometry(QRect(380, 30, 121, 31))
        self.downloadDirButton.setFont(font2)
        self.modUrlsLabel = QLabel(self.settings)
        self.modUrlsLabel.setObjectName(u"modUrlsLabel")
        self.modUrlsLabel.setGeometry(QRect(10, 280, 181, 31))
        self.modUrlsLabel.setFont(font1)
        self.modUrlsLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.modloaderOptions = QComboBox(self.settings)
        self.modloaderOptions.addItem("")
        self.modloaderOptions.addItem("")
        self.modloaderOptions.addItem("")
        self.modloaderOptions.addItem("")
        self.modloaderOptions.addItem("")
        self.modloaderOptions.setObjectName(u"modloaderOptions")
        self.modloaderOptions.setEnabled(True)
        self.modloaderOptions.setGeometry(QRect(230, 100, 181, 34))
        self.modloaderOptions.setFont(font)
        self.downloadModsButton = QPushButton(self.settings)
        self.downloadModsButton.setObjectName(u"downloadModsButton")
        self.downloadModsButton.setGeometry(QRect(280, 580, 191, 31))
        self.downloadModsButton.setFont(font2)
        self.modloaderLabel = QLabel(self.settings)
        self.modloaderLabel.setObjectName(u"modloaderLabel")
        self.modloaderLabel.setGeometry(QRect(230, 78, 181, 20))
        self.modloaderLabel.setFont(font1)
        self.modloaderLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.extraOptions_useBackupApi = QCheckBox(self.settings)
        self.extraOptions_useBackupApi.setObjectName(u"extraOptions_useBackupApi")
        self.extraOptions_useBackupApi.setEnabled(False)
        self.extraOptions_useBackupApi.setGeometry(QRect(170, 180, 151, 21))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(9)
        font3.setStrikeOut(True)
        self.extraOptions_useBackupApi.setFont(font3)
        self.extraOptions_useBackupApi.setChecked(False)
        self.extraOptions_backup = QFrame(self.settings)
        self.extraOptions_backup.setObjectName(u"extraOptions_backup")
        self.extraOptions_backup.setGeometry(QRect(10, 179, 151, 81))
        self.extraOptions_backup.setFrameShape(QFrame.Shape.StyledPanel)
        self.extraOptions_backup.setFrameShadow(QFrame.Shadow.Raised)
        self.oldModsNothing = QRadioButton(self.extraOptions_backup)
        self.oldModsNothing.setObjectName(u"oldModsNothing")
        self.oldModsNothing.setGeometry(QRect(10, 50, 131, 21))
        self.oldModsNothing.setFont(font)
        self.oldModsNothing.setChecked(False)
        self.oldModsBackup = QRadioButton(self.extraOptions_backup)
        self.oldModsBackup.setObjectName(u"oldModsBackup")
        self.oldModsBackup.setGeometry(QRect(10, 10, 131, 21))
        self.oldModsBackup.setFont(font)
        self.oldModsBackup.setChecked(True)
        self.oldModsDelete = QRadioButton(self.extraOptions_backup)
        self.oldModsDelete.setObjectName(u"oldModsDelete")
        self.oldModsDelete.setGeometry(QRect(10, 30, 131, 21))
        self.oldModsDelete.setFont(font)
        self.oldModsDelete.setChecked(False)
        self.mods = QFrame(TabGeneral)
        self.mods.setObjectName(u"mods")
        self.mods.setGeometry(QRect(530, 10, 511, 681))
        self.mods.setStyleSheet(u"#mods {\n"
"	background-color: #2a2a2a;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"/* Label */\n"
"QFrame QLabel {\n"
"	color: #DCE4EE;\n"
"}\n"
"\n"
"\n"
"/* Frame */\n"
"QFrame,\n"
"#foundModsContainer {\n"
"	background-color: #2a2a2a;\n"
"}\n"
"\n"
"\n"
"/* modWidget */\n"
"#foundModsContainer > QWidget {\n"
"	background-color: rgba(255, 255, 255, 0.1);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"/* modWidget Label */\n"
"#foundModsContainer > QWidget QLabel {\n"
"	background-color: rgba(255, 255, 255, 0.0);\n"
"}\n"
"\n"
"\n"
"/* modWidget PushButton */\n"
"#foundModsContainer > QWidget QPushButton {\n"
"	background-color: #9e2c24;\n"
"	border-radius: 5px;\n"
"}\n"
"#foundModsContainer > QWidget QPushButton:pressed {\n"
"	background-color: #6b1d18;\n"
"}\n"
"\n"
"\n"
"/* ScrollArea */\n"
"QScrollArea {\n"
"	background-color: #2a2a2a;\n"
"	border-radius: 15px;\n"
"}\n"
"/* VERTICAL SCROLLBAR */\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: #2a2a2a;\n"
"    width: 10px;\n"
" }\n"
"/*"
                        "  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {	\n"
"	background: #DCE4EE;\n"
"	border-radius: 5px;\n"
"}\n"
"QScrollBar::handle:vertical:pressed {	\n"
"	background-color: #acb3bb;\n"
"}\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical, \n"
"QScrollBar::add-line:vertical {\n"
"	height: 0px;\n"
"}\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical,\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}\n"
"/* HORIZONTAL SCROLLBAR */\n"
"QScrollBar:horizontal {\n"
"	border: none;\n"
"    background: #3f3f3f;\n"
"    height: 10px;\n"
"	border-radius: 0px;\n"
"}\n"
"/*  HANDLE BAR HORIZONTAL */\n"
"QScrollBar::handle:horizontal {\n"
"	background: #DCE4EE;\n"
"	border-radius: 5px;\n"
"}\n"
"QScrollBar::handle:horizontal:pressed {	\n"
"	background-color: #acb3bb;\n"
"}\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:horizontal, \n"
"QScrollBar::add-line:horizontal {\n"
"	width: 0px;\n"
"}\n"
"/* RESET ARRO"
                        "W */\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal,\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"	background: none;\n"
"}")
        self.mods.setFrameShape(QFrame.Shape.StyledPanel)
        self.mods.setFrameShadow(QFrame.Shadow.Raised)
        self.scrollArea = QScrollArea(self.mods)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(10, 36, 491, 631))
        self.scrollArea.setWidgetResizable(True)
        self.foundModsContainer = QWidget()
        self.foundModsContainer.setObjectName(u"foundModsContainer")
        self.foundModsContainer.setGeometry(QRect(0, 0, 491, 631))
        self.verticalLayout = QVBoxLayout(self.foundModsContainer)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.modWidgetExample = QWidget(self.foundModsContainer)
        self.modWidgetExample.setObjectName(u"modWidgetExample")
        self.modWidgetExample.setMinimumSize(QSize(0, 80))
        self.modWidgetExample.setMaximumSize(QSize(470, 80))
        self.modIcon = QLabel(self.modWidgetExample)
        self.modIcon.setObjectName(u"modIcon")
        self.modIcon.setGeometry(QRect(10, 10, 61, 61))
        self.modIcon.setPixmap(QPixmap(u":/icons/no-icon.png"))
        self.modIcon.setScaledContents(True)
        self.modIcon.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.modName = QLabel(self.modWidgetExample)
        self.modName.setObjectName(u"modName")
        self.modName.setGeometry(QRect(80, 0, 291, 31))
        self.modName.setFont(font1)
        self.modDetails = QLabel(self.modWidgetExample)
        self.modDetails.setObjectName(u"modDetails")
        self.modDetails.setGeometry(QRect(80, 50, 321, 20))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(9)
        font4.setBold(False)
        self.modDetails.setFont(font4)
        self.modDetails.setTextFormat(Qt.TextFormat.PlainText)
        self.modDetails.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.actionButton = QPushButton(self.modWidgetExample)
        self.actionButton.setObjectName(u"actionButton")
        self.actionButton.setGeometry(QRect(410, 20, 41, 41))
        icon = QIcon()
        icon.addFile(u":/icons/trash.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionButton.setIcon(icon)
        self.actionButton.setIconSize(QSize(32, 32))
        self.modIcon.raise_()
        self.actionButton.raise_()
        self.modDetails.raise_()
        self.modName.raise_()

        self.verticalLayout.addWidget(self.modWidgetExample, 0, Qt.AlignmentFlag.AlignTop)

        self.scrollArea.setWidget(self.foundModsContainer)
        self.foundModsLabel = QLabel(self.mods)
        self.foundModsLabel.setObjectName(u"foundModsLabel")
        self.foundModsLabel.setGeometry(QRect(10, 10, 231, 21))
        self.foundModsLabel.setFont(font1)
        self.foundModsLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.retranslateUi(TabGeneral)

        self.modloaderOptions.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(TabGeneral)
    # setupUi

    def retranslateUi(self, TabGeneral):
        TabGeneral.setWindowTitle(QCoreApplication.translate("TabGeneral", u"Form", None))
        self.modUrlsTextEdit.setPlainText("")
        self.extraOptionsLabel.setText(QCoreApplication.translate("TabGeneral", u"Extra options:", None))
        self.downloadDirInput.setText("")
        self.downloadDirInput.setPlaceholderText(QCoreApplication.translate("TabGeneral", u"Minecraft mods folder here", None))
        self.progressBar.setFormat(QCoreApplication.translate("TabGeneral", u"%p%", None))
        self.downloadDirLabel.setText(QCoreApplication.translate("TabGeneral", u"Your Mods Folder:", None))
        self.versionInput.setText("")
        self.versionInput.setPlaceholderText(QCoreApplication.translate("TabGeneral", u"Minecraft version here", None))
        self.searchModsButton.setText(QCoreApplication.translate("TabGeneral", u"Search Mods", None))
        self.versionLabel.setText(QCoreApplication.translate("TabGeneral", u"Minecraft Version:", None))
        self.downloadDirButton.setText(QCoreApplication.translate("TabGeneral", u"Change", None))
        self.modUrlsLabel.setText(QCoreApplication.translate("TabGeneral", u"Mods URLs to look for:", None))
        self.modloaderOptions.setItemText(0, QCoreApplication.translate("TabGeneral", u"Forge", None))
        self.modloaderOptions.setItemText(1, QCoreApplication.translate("TabGeneral", u"NeoForge", None))
        self.modloaderOptions.setItemText(2, QCoreApplication.translate("TabGeneral", u"Fabric", None))
        self.modloaderOptions.setItemText(3, QCoreApplication.translate("TabGeneral", u"Quilt", None))
        self.modloaderOptions.setItemText(4, QCoreApplication.translate("TabGeneral", u"Quilt with Fabric fallback", None))

        self.modloaderOptions.setCurrentText(QCoreApplication.translate("TabGeneral", u"Quilt with Fabric fallback", None))
        self.downloadModsButton.setText(QCoreApplication.translate("TabGeneral", u"Download Mods", None))
        self.modloaderLabel.setText(QCoreApplication.translate("TabGeneral", u"Modloader:", None))
#if QT_CONFIG(tooltip)
        self.extraOptions_useBackupApi.setToolTip(QCoreApplication.translate("TabGeneral", u"(Not implemented yet) When an API fails to find a mod, use another API to check again", None))
#endif // QT_CONFIG(tooltip)
        self.extraOptions_useBackupApi.setText(QCoreApplication.translate("TabGeneral", u"Use backup API", None))
#if QT_CONFIG(tooltip)
        self.oldModsNothing.setToolTip(QCoreApplication.translate("TabGeneral", u"New and old mods will be in the same folder", None))
#endif // QT_CONFIG(tooltip)
        self.oldModsNothing.setText(QCoreApplication.translate("TabGeneral", u"Do nothing", None))
#if QT_CONFIG(tooltip)
        self.oldModsBackup.setToolTip(QCoreApplication.translate("TabGeneral", u"Move old mods to a backup folder", None))
#endif // QT_CONFIG(tooltip)
        self.oldModsBackup.setText(QCoreApplication.translate("TabGeneral", u"Backup old mods", None))
#if QT_CONFIG(tooltip)
        self.oldModsDelete.setToolTip(QCoreApplication.translate("TabGeneral", u"Delete old mods", None))
#endif // QT_CONFIG(tooltip)
        self.oldModsDelete.setText(QCoreApplication.translate("TabGeneral", u"Delete old mods", None))
        self.modName.setText(QCoreApplication.translate("TabGeneral", u"Mod name", None))
        self.modDetails.setText(QCoreApplication.translate("TabGeneral", u"File: this-is-a-test.jar\n"
"Source: Something", None))
        self.actionButton.setText("")
        self.foundModsLabel.setText(QCoreApplication.translate("TabGeneral", u"Mods Found Online:", None))
    # retranslateUi

