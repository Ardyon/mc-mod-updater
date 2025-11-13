# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'failed_mods.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QScrollArea, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(590, 470)
        Dialog.setMinimumSize(QSize(590, 470))
        Dialog.setMaximumSize(QSize(590, 470))
        icon = QIcon()
        icon.addFile(u"../icon/mc_mod_updater_icon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(u"#scrollAreaWidgetContents QLabel {\n"
"	padding: 3px;\n"
"	background-color: rgba(0, 0, 0, 0.1);\n"
"}\n"
"")
        self.warningLabel = QLabel(Dialog)
        self.warningLabel.setObjectName(u"warningLabel")
        self.warningLabel.setGeometry(QRect(9, 9, 561, 121))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        self.warningLabel.setFont(font)
        self.warningLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.warningLabel.setWordWrap(True)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(12, 430, 571, 28))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)
        self.scrollArea = QScrollArea(Dialog)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(10, 130, 559, 289))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 557, 287))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.modsLabel = QLabel(self.scrollAreaWidgetContents)
        self.modsLabel.setObjectName(u"modsLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modsLabel.sizePolicy().hasHeightForWidth())
        self.modsLabel.setSizePolicy(sizePolicy)
        self.modsLabel.setMinimumSize(QSize(0, 0))
        self.modsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.modsLabel.setWordWrap(True)
        self.modsLabel.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse)

        self.verticalLayout_2.addWidget(self.modsLabel)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Mods not found", None))
        self.warningLabel.setText(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Some mods could not be found.<br />Reason could be:<br />  - Typo in the URLs<br />  - API keys weren't set correctly<br />  - Mistake in the program</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If you want to check for yourself, here are the links:</p></body></html>", None))
        self.modsLabel.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><a href=\"https://modrinth.com/mod/sodium\"><span style=\" text-decoration: underline; color:#0000ff;\">https://modrinth.com/mod/sodium</span></a></p><p><a href=\"https://modrinth.com/mod/sodium-extra\"><span style=\" text-decoration: underline; color:#0000ff;\">https://modrinth.com/mod/sodium-extra</span></a></p></body></html>", None))
    # retranslateUi

