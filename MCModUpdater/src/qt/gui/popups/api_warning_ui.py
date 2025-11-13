# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'api_warning.ui'
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
    QLabel, QLineEdit, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(650, 280)
        Dialog.setMinimumSize(QSize(650, 280))
        Dialog.setMaximumSize(QSize(650, 280))
        icon = QIcon()
        icon.addFile(u"../icon/mc_mod_updater_icon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        self.explanationLabel = QLabel(Dialog)
        self.explanationLabel.setObjectName(u"explanationLabel")
        self.explanationLabel.setGeometry(QRect(10, 10, 630, 191))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        self.explanationLabel.setFont(font)
        self.explanationLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.explanationLabel.setWordWrap(True)
        self.explanationLabel.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse)
        self.apiLabel = QLabel(Dialog)
        self.apiLabel.setObjectName(u"apiLabel")
        self.apiLabel.setGeometry(QRect(10, 210, 51, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setUnderline(False)
        self.apiLabel.setFont(font1)
        self.apiLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.apiLabel.setWordWrap(False)
        self.apiInput = QLineEdit(Dialog)
        self.apiInput.setObjectName(u"apiInput")
        self.apiInput.setGeometry(QRect(82, 210, 551, 22))
        self.apiInput.setEchoMode(QLineEdit.Password)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 240, 631, 28))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close|QDialogButtonBox.Ignore|QDialogButtonBox.Save)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"API Key Warning", None))
        self.explanationLabel.setText(QCoreApplication.translate("Dialog", u"This is some test data to see what it would look like.<br/>\n"
"CurseForge links require an API key to get data from the website.<br/>\n"
"Modrinth links don't need an API key.<br/>\n"
"Skipping this step means that you won't be able to use CurseForge links.<br/>\n"
"<br/>\n"
"To get an API key, visit this link: <a href=\"https://console.curseforge.com/\">https://console.curseforge.com/</span></a><br/>\n"
"1. Login or create an account<br/>\n"
"2. Once you're logged in, go to the tab 'API keys' and copy the key<br/>", None))
        self.apiLabel.setText(QCoreApplication.translate("Dialog", u"API Key:", None))
    # retranslateUi

