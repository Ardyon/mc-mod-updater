# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tabs.ui'
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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QTabWidget, QWidget)

class Ui_TabWidget(object):
    def setupUi(self, TabWidget):
        if not TabWidget.objectName():
            TabWidget.setObjectName(u"TabWidget")
        TabWidget.resize(1050, 725)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TabWidget.sizePolicy().hasHeightForWidth())
        TabWidget.setSizePolicy(sizePolicy)
        TabWidget.setMinimumSize(QSize(1050, 725))
        TabWidget.setMaximumSize(QSize(1050, 725))
        TabWidget.setStyleSheet(u"QMenuBar {\n"
"	background-color: #2a2a2a;\n"
"	color: #dce4ee;\n"
"}\n"
"\n"
"QTabWidget #general,\n"
"QTabWidget #search,\n"
"QTabWidget #settings {\n"
"	background: #1a1a1a;\n"
"}\n"
"QTabBar {\n"
"	qproperty-drawBase: 0;\n"
"	border-bottom: 1px solid #dce4ee;\n"
"}\n"
"QTabBar::tab {\n"
"	min-width: 75px;\n"
"    padding: 2px;\n"
"	margin-top: 2px;\n"
"    background: #3f3f3f;\n"
"	color: #dce4ee;\n"
"    border: 1px solid #dce4ee;\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background: #1a1a1a;\n"
"}\n"
"QTabBar::tab:selected {\n"
"    border-bottom-color: #1a1a1a;\n"
"}\n"
"QTabBar::tab:!selected {\n"
"	margin-top: 4px;\n"
"}\n"
"QTabBar::tab:first {\n"
"    margin-left: 5px;\n"
"}\n"
"QTabBar::tab:!first {\n"
"    margin-left: -1px;\n"
"}")
        TabWidget.setDocumentMode(True)
        self.general = QWidget()
        self.general.setObjectName(u"general")
        TabWidget.addTab(self.general, "")
        self.search = QWidget()
        self.search.setObjectName(u"search")
        TabWidget.addTab(self.search, "")
        self.settings = QWidget()
        self.settings.setObjectName(u"settings")
        TabWidget.addTab(self.settings, "")

        self.retranslateUi(TabWidget)

        TabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(TabWidget)
    # setupUi

    def retranslateUi(self, TabWidget):
        TabWidget.setWindowTitle(QCoreApplication.translate("TabWidget", u"TabWidget", None))
        TabWidget.setTabText(TabWidget.indexOf(self.general), QCoreApplication.translate("TabWidget", u"General", None))
        TabWidget.setTabText(TabWidget.indexOf(self.search), QCoreApplication.translate("TabWidget", u"Search", None))
        TabWidget.setTabText(TabWidget.indexOf(self.settings), QCoreApplication.translate("TabWidget", u"Settings", None))
    # retranslateUi

