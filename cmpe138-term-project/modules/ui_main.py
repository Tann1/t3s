# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainIiEYse.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QCommandLinkButton, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QMainWindow, QPlainTextEdit, QPushButton,
    QRadioButton, QScrollArea, QScrollBar, QSizePolicy,
    QSlider, QStackedWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget)
from . resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1106, 720)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(18"
                        "9, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb("
                        "189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border"
                        "-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-sty"
                        "le: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb"
                        "(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-co"
                        "lor: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-c"
                        "olor: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
""
                        "QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     su"
                        "bcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	back"
                        "ground-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subco"
                        "ntrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    h"
                        "eight: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLi"
                        "nkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setAutoFillBackground(False)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")
        self.toggleButton.setFlat(True)

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)

        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font)
        self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font)
        self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_adjustments)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font)
        self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon1)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon2)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        self.widgets.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.widgets)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.row_1 = QFrame(self.widgets)
        self.row_1.setObjectName(u"row_1")
        self.row_1.setFrameShape(QFrame.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.row_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.row_1)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setFont(font)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_18.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_17.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit = QLineEdit(self.frame_content_wid_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.frame_content_wid_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 30))
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon3)

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        self.labelVersion_3.setObjectName(u"labelVersion_3")
        self.labelVersion_3.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_3.setLineWidth(1)
        self.labelVersion_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_3, 1, 0, 1, 2)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_17.addWidget(self.frame_content_wid_1)


        self.verticalLayout_16.addWidget(self.frame_div_content_1)


        self.verticalLayout.addWidget(self.row_1)

        self.row_2 = QFrame(self.widgets)
        self.row_2.setObjectName(u"row_2")
        self.row_2.setMinimumSize(QSize(0, 150))
        self.row_2.setFrameShape(QFrame.StyledPanel)
        self.row_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.row_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox = QCheckBox(self.row_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)

        self.radioButton = QRadioButton(self.row_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.radioButton, 0, 1, 1, 1)

        self.verticalSlider = QSlider(self.row_2)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setStyleSheet(u"")
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalSlider, 0, 2, 3, 1)

        self.verticalScrollBar = QScrollBar(self.row_2)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.verticalScrollBar.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalScrollBar, 0, 4, 3, 1)

        self.scrollArea = QScrollArea(self.row_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u" QScrollBar:vertical {\n"
"    background: rgb(52, 59, 72);\n"
" }\n"
" QScrollBar:horizontal {\n"
"    background: rgb(52, 59, 72);\n"
" }")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 274, 218))
        self.scrollAreaWidgetContents.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.horizontalLayout_11 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.plainTextEdit = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(200, 200))
        self.plainTextEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_11.addWidget(self.plainTextEdit)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 5, 3, 1)

        self.comboBox = QComboBox(self.row_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.comboBox.setIconSize(QSize(16, 16))
        self.comboBox.setFrame(True)

        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 2)

        self.horizontalScrollBar = QScrollBar(self.row_2)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        sizePolicy.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar.setSizePolicy(sizePolicy)
        self.horizontalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalScrollBar, 1, 3, 1, 1)

        self.commandLinkButton = QCommandLinkButton(self.row_2)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.commandLinkButton.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton.setIcon(icon4)

        self.gridLayout_2.addWidget(self.commandLinkButton, 1, 6, 1, 1)

        self.horizontalSlider = QSlider(self.row_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setStyleSheet(u"")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider, 2, 0, 1, 2)


        self.verticalLayout_19.addLayout(self.gridLayout_2)


        self.verticalLayout.addWidget(self.row_2)

        self.row_3 = QFrame(self.widgets)
        self.row_3.setObjectName(u"row_3")
        self.row_3.setMinimumSize(QSize(0, 150))
        self.row_3.setFrameShape(QFrame.StyledPanel)
        self.row_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.row_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.row_3)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 16):
            self.tableWidget.setRowCount(16)
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font4);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem23)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy3)
        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.tableWidget.setPalette(palette)
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_12.addWidget(self.tableWidget)


        self.verticalLayout.addWidget(self.row_3)

        self.stackedWidget.addWidget(self.widgets)
        self.managerUI = QWidget()
        self.managerUI.setObjectName(u"managerUI")
        self.bottom_Frame_2 = QFrame(self.managerUI)
        self.bottom_Frame_2.setObjectName(u"bottom_Frame_2")
        self.bottom_Frame_2.setGeometry(QRect(10, 60, 831, 301))
        self.bottom_Frame_2.setFrameShape(QFrame.StyledPanel)
        self.bottom_Frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_2 = QWidget(self.bottom_Frame_2)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(0, 10, 811, 211))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.Button_UpdateMenu = QPushButton(self.gridLayoutWidget_2)
        self.Button_UpdateMenu.setObjectName(u"Button_UpdateMenu")
        self.Button_UpdateMenu.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.Button_UpdateMenu.sizePolicy().hasHeightForWidth())
        self.Button_UpdateMenu.setSizePolicy(sizePolicy4)
        self.Button_UpdateMenu.setMinimumSize(QSize(150, 30))
        self.Button_UpdateMenu.setFont(font)
        self.Button_UpdateMenu.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_UpdateMenu.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.Button_UpdateMenu.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-browser.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Button_UpdateMenu.setIcon(icon5)
        self.Button_UpdateMenu.setIconSize(QSize(16, 16))

        self.gridLayout_4.addWidget(self.Button_UpdateMenu, 0, 1, 1, 1)

        self.Button_ManageSubscriptions = QPushButton(self.gridLayoutWidget_2)
        self.Button_ManageSubscriptions.setObjectName(u"Button_ManageSubscriptions")
        self.Button_ManageSubscriptions.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.Button_ManageSubscriptions.sizePolicy().hasHeightForWidth())
        self.Button_ManageSubscriptions.setSizePolicy(sizePolicy4)
        self.Button_ManageSubscriptions.setMinimumSize(QSize(150, 30))
        self.Button_ManageSubscriptions.setFont(font)
        self.Button_ManageSubscriptions.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_ManageSubscriptions.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.Button_ManageSubscriptions.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon6 = QIcon()
        icon6.addFile(u":/icons/images/icons/cil-star.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Button_ManageSubscriptions.setIcon(icon6)

        self.gridLayout_4.addWidget(self.Button_ManageSubscriptions, 0, 0, 1, 1)

        self.Button_ManageEmployees = QPushButton(self.gridLayoutWidget_2)
        self.Button_ManageEmployees.setObjectName(u"Button_ManageEmployees")
        self.Button_ManageEmployees.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.Button_ManageEmployees.sizePolicy().hasHeightForWidth())
        self.Button_ManageEmployees.setSizePolicy(sizePolicy4)
        self.Button_ManageEmployees.setMinimumSize(QSize(150, 30))
        self.Button_ManageEmployees.setFont(font)
        self.Button_ManageEmployees.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_ManageEmployees.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.Button_ManageEmployees.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon7 = QIcon()
        icon7.addFile(u":/icons/images/icons/cil-people.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Button_ManageEmployees.setIcon(icon7)

        self.gridLayout_4.addWidget(self.Button_ManageEmployees, 0, 2, 1, 1)

        self.Button_Addrecipe = QPushButton(self.gridLayoutWidget_2)
        self.Button_Addrecipe.setObjectName(u"Button_Addrecipe")
        self.Button_Addrecipe.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.Button_Addrecipe.sizePolicy().hasHeightForWidth())
        self.Button_Addrecipe.setSizePolicy(sizePolicy4)
        self.Button_Addrecipe.setMinimumSize(QSize(150, 30))
        self.Button_Addrecipe.setFont(font)
        self.Button_Addrecipe.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_Addrecipe.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.Button_Addrecipe.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon8 = QIcon()
        icon8.addFile(u":/icons/images/icons/cil-pin.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Button_Addrecipe.setIcon(icon8)
        self.Button_Addrecipe.setIconSize(QSize(16, 16))

        self.gridLayout_4.addWidget(self.Button_Addrecipe, 1, 1, 1, 1)

        self.stackedWidget.addWidget(self.managerUI)
        self.ManageSubs = QWidget()
        self.ManageSubs.setObjectName(u"ManageSubs")
        self.subscribers_ = QTableWidget(self.ManageSubs)
        if (self.subscribers_.columnCount() < 5):
            self.subscribers_.setColumnCount(5)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.subscribers_.setHorizontalHeaderItem(0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.subscribers_.setHorizontalHeaderItem(1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.subscribers_.setHorizontalHeaderItem(2, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.subscribers_.setHorizontalHeaderItem(3, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.subscribers_.setHorizontalHeaderItem(4, __qtablewidgetitem28)
        if (self.subscribers_.rowCount() < 4):
            self.subscribers_.setRowCount(4)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem29.setFont(font4);
        self.subscribers_.setVerticalHeaderItem(0, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setTextAlignment(Qt.AlignCenter);
        self.subscribers_.setVerticalHeaderItem(1, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setTextAlignment(Qt.AlignCenter);
        self.subscribers_.setVerticalHeaderItem(2, __qtablewidgetitem31)
        font5 = QFont()
        font5.setFamilies([u"Ofelia Display"])
        font5.setPointSize(10)
        font5.setBold(True)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem32.setFont(font5);
        __qtablewidgetitem32.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.subscribers_.setItem(0, 0, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem33.setFont(font5);
        self.subscribers_.setItem(0, 1, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem34.setFont(font5);
        self.subscribers_.setItem(0, 2, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem35.setFont(font5);
        self.subscribers_.setItem(0, 3, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem36.setFont(font5);
        self.subscribers_.setItem(0, 4, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.subscribers_.setItem(2, 0, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.subscribers_.setItem(2, 1, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.subscribers_.setItem(2, 2, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.subscribers_.setItem(3, 0, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.subscribers_.setItem(3, 1, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.subscribers_.setItem(3, 2, __qtablewidgetitem42)
        self.subscribers_.setObjectName(u"subscribers_")
        self.subscribers_.setGeometry(QRect(30, 40, 671, 181))
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.subscribers_.sizePolicy().hasHeightForWidth())
        self.subscribers_.setSizePolicy(sizePolicy5)
        self.subscribers_.setSizeIncrement(QSize(0, 0))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush5 = QBrush(QColor(0, 0, 0, 255))
        brush5.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush6 = QBrush(QColor(0, 0, 0, 255))
        brush6.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.subscribers_.setPalette(palette1)
        self.subscribers_.setFont(font)
        self.subscribers_.setAutoFillBackground(False)
        self.subscribers_.setFrameShape(QFrame.NoFrame)
        self.subscribers_.setLineWidth(2)
        self.subscribers_.setMidLineWidth(0)
        self.subscribers_.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.subscribers_.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.subscribers_.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.subscribers_.setAutoScroll(True)
        self.subscribers_.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.subscribers_.setAlternatingRowColors(False)
        self.subscribers_.setSelectionMode(QAbstractItemView.SingleSelection)
        self.subscribers_.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.subscribers_.setShowGrid(True)
        self.subscribers_.setGridStyle(Qt.SolidLine)
        self.subscribers_.setSortingEnabled(False)
        self.subscribers_.setCornerButtonEnabled(True)
        self.subscribers_.setRowCount(4)
        self.subscribers_.horizontalHeader().setVisible(False)
        self.subscribers_.horizontalHeader().setCascadingSectionResizes(False)
        self.subscribers_.horizontalHeader().setMinimumSectionSize(30)
        self.subscribers_.horizontalHeader().setDefaultSectionSize(130)
        self.subscribers_.horizontalHeader().setHighlightSections(False)
        self.subscribers_.horizontalHeader().setStretchLastSection(False)
        self.subscribers_.verticalHeader().setVisible(False)
        self.subscribers_.verticalHeader().setCascadingSectionResizes(False)
        self.subscribers_.verticalHeader().setMinimumSectionSize(25)
        self.subscribers_.verticalHeader().setDefaultSectionSize(25)
        self.subscribers_.verticalHeader().setHighlightSections(False)
        self.subscribers_.verticalHeader().setStretchLastSection(False)
        self.stackedWidget.addWidget(self.ManageSubs)
        self.UpdateMenuUI = QWidget()
        self.UpdateMenuUI.setObjectName(u"UpdateMenuUI")
        self.menu_ = QTableWidget(self.UpdateMenuUI)
        if (self.menu_.columnCount() < 6):
            self.menu_.setColumnCount(6)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.menu_.setHorizontalHeaderItem(0, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.menu_.setHorizontalHeaderItem(1, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.menu_.setHorizontalHeaderItem(2, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.menu_.setHorizontalHeaderItem(3, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.menu_.setHorizontalHeaderItem(4, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.menu_.setHorizontalHeaderItem(5, __qtablewidgetitem48)
        if (self.menu_.rowCount() < 4):
            self.menu_.setRowCount(4)
        __qtablewidgetitem49 = QTableWidgetItem()
        __qtablewidgetitem49.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem49.setFont(font4);
        self.menu_.setVerticalHeaderItem(0, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        __qtablewidgetitem50.setTextAlignment(Qt.AlignCenter);
        self.menu_.setVerticalHeaderItem(1, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        __qtablewidgetitem51.setTextAlignment(Qt.AlignCenter);
        self.menu_.setVerticalHeaderItem(2, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        __qtablewidgetitem52.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem52.setFont(font5);
        __qtablewidgetitem52.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.menu_.setItem(0, 0, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        __qtablewidgetitem53.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem53.setFont(font5);
        self.menu_.setItem(0, 1, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        __qtablewidgetitem54.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem54.setFont(font5);
        self.menu_.setItem(0, 2, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        __qtablewidgetitem55.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem55.setFont(font5);
        self.menu_.setItem(0, 3, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        __qtablewidgetitem56.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem56.setFont(font5);
        self.menu_.setItem(0, 4, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        __qtablewidgetitem57.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem57.setFont(font5);
        self.menu_.setItem(0, 5, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.menu_.setItem(2, 0, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.menu_.setItem(2, 1, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.menu_.setItem(2, 2, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.menu_.setItem(3, 0, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.menu_.setItem(3, 1, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.menu_.setItem(3, 2, __qtablewidgetitem63)
        self.menu_.setObjectName(u"menu_")
        self.menu_.setGeometry(QRect(30, 20, 861, 241))
        sizePolicy5.setHeightForWidth(self.menu_.sizePolicy().hasHeightForWidth())
        self.menu_.setSizePolicy(sizePolicy5)
        self.menu_.setSizeIncrement(QSize(0, 0))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush8 = QBrush(QColor(0, 0, 0, 255))
        brush8.setStyle(Qt.NoBrush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush9 = QBrush(QColor(0, 0, 0, 255))
        brush9.setStyle(Qt.NoBrush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush10 = QBrush(QColor(0, 0, 0, 255))
        brush10.setStyle(Qt.NoBrush)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.menu_.setPalette(palette2)
        self.menu_.setFont(font)
        self.menu_.setAutoFillBackground(False)
        self.menu_.setFrameShape(QFrame.NoFrame)
        self.menu_.setLineWidth(2)
        self.menu_.setMidLineWidth(0)
        self.menu_.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.menu_.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.menu_.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.menu_.setAutoScroll(True)
        self.menu_.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.menu_.setAlternatingRowColors(False)
        self.menu_.setSelectionMode(QAbstractItemView.SingleSelection)
        self.menu_.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.menu_.setShowGrid(True)
        self.menu_.setGridStyle(Qt.SolidLine)
        self.menu_.setSortingEnabled(False)
        self.menu_.setCornerButtonEnabled(True)
        self.menu_.setRowCount(4)
        self.menu_.horizontalHeader().setVisible(False)
        self.menu_.horizontalHeader().setCascadingSectionResizes(False)
        self.menu_.horizontalHeader().setMinimumSectionSize(30)
        self.menu_.horizontalHeader().setDefaultSectionSize(130)
        self.menu_.horizontalHeader().setHighlightSections(False)
        self.menu_.horizontalHeader().setStretchLastSection(False)
        self.menu_.verticalHeader().setVisible(False)
        self.menu_.verticalHeader().setCascadingSectionResizes(False)
        self.menu_.verticalHeader().setMinimumSectionSize(25)
        self.menu_.verticalHeader().setDefaultSectionSize(25)
        self.menu_.verticalHeader().setHighlightSections(False)
        self.menu_.verticalHeader().setStretchLastSection(False)
        self.Button_Confirm_Changes = QPushButton(self.UpdateMenuUI)
        self.Button_Confirm_Changes.setObjectName(u"Button_Confirm_Changes")
        self.Button_Confirm_Changes.setGeometry(QRect(300, 290, 261, 51))
        self.Button_Confirm_Changes.setMinimumSize(QSize(150, 30))
        self.Button_Confirm_Changes.setFont(font)
        self.Button_Confirm_Changes.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_Confirm_Changes.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon9 = QIcon()
        icon9.addFile(u":/icons/images/icons/cil-check-alt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Button_Confirm_Changes.setIcon(icon9)
        self.stackedWidget.addWidget(self.UpdateMenuUI)
        self.shoppingcart_page = QWidget()
        self.shoppingcart_page.setObjectName(u"shoppingcart_page")
        self.verticalLayout_20 = QVBoxLayout(self.shoppingcart_page)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame = QFrame(self.shoppingcart_page)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.Label_Shoppingcart = QLabel(self.frame)
        self.Label_Shoppingcart.setObjectName(u"Label_Shoppingcart")
        self.Label_Shoppingcart.setGeometry(QRect(0, 0, 811, 51))
        self.Label_Shoppingcart.setStyleSheet(u"font: 500 12pt \"Ofelia Display\";")
        self.Label_Shoppingcart.setAlignment(Qt.AlignCenter)
        self.ShoppingCart_button_2 = QPushButton(self.frame)
        self.ShoppingCart_button_2.setObjectName(u"ShoppingCart_button_2")
        self.ShoppingCart_button_2.setEnabled(True)
        self.ShoppingCart_button_2.setGeometry(QRect(550, 480, 266, 79))
        sizePolicy4.setHeightForWidth(self.ShoppingCart_button_2.sizePolicy().hasHeightForWidth())
        self.ShoppingCart_button_2.setSizePolicy(sizePolicy4)
        self.ShoppingCart_button_2.setMinimumSize(QSize(150, 30))
        self.ShoppingCart_button_2.setFont(font)
        self.ShoppingCart_button_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.ShoppingCart_button_2.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.ShoppingCart_button_2.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon10 = QIcon()
        icon10.addFile(u":/icons/images/icons/cil-cart.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ShoppingCart_button_2.setIcon(icon10)
        self.ShoppingCart_button_3 = QPushButton(self.frame)
        self.ShoppingCart_button_3.setObjectName(u"ShoppingCart_button_3")
        self.ShoppingCart_button_3.setEnabled(True)
        self.ShoppingCart_button_3.setGeometry(QRect(-10, 480, 266, 79))
        sizePolicy4.setHeightForWidth(self.ShoppingCart_button_3.sizePolicy().hasHeightForWidth())
        self.ShoppingCart_button_3.setSizePolicy(sizePolicy4)
        self.ShoppingCart_button_3.setMinimumSize(QSize(150, 30))
        self.ShoppingCart_button_3.setFont(font)
        self.ShoppingCart_button_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.ShoppingCart_button_3.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.ShoppingCart_button_3.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon11 = QIcon()
        icon11.addFile(u":/icons/images/icons/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ShoppingCart_button_3.setIcon(icon11)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-20, -10, 831, 461))
        self.label.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.shopping_cart_ = QTableWidget(self.frame)
        if (self.shopping_cart_.columnCount() < 4):
            self.shopping_cart_.setColumnCount(4)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.shopping_cart_.setHorizontalHeaderItem(0, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.shopping_cart_.setHorizontalHeaderItem(1, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.shopping_cart_.setHorizontalHeaderItem(2, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        self.shopping_cart_.setHorizontalHeaderItem(3, __qtablewidgetitem67)
        if (self.shopping_cart_.rowCount() < 2):
            self.shopping_cart_.setRowCount(2)
        __qtablewidgetitem68 = QTableWidgetItem()
        __qtablewidgetitem68.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem68.setFont(font4);
        self.shopping_cart_.setVerticalHeaderItem(0, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        __qtablewidgetitem69.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem69.setFont(font5);
        __qtablewidgetitem69.setFlags(Qt.NoItemFlags);
        self.shopping_cart_.setItem(0, 0, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        __qtablewidgetitem70.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem70.setFont(font5);
        self.shopping_cart_.setItem(0, 1, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        __qtablewidgetitem71.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem71.setFont(font5);
        self.shopping_cart_.setItem(0, 2, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        __qtablewidgetitem72.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem72.setFont(font5);
        self.shopping_cart_.setItem(0, 3, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        self.shopping_cart_.setItem(1, 0, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        self.shopping_cart_.setItem(1, 1, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        self.shopping_cart_.setItem(1, 2, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        self.shopping_cart_.setItem(1, 3, __qtablewidgetitem76)
        self.shopping_cart_.setObjectName(u"shopping_cart_")
        self.shopping_cart_.setGeometry(QRect(130, 60, 541, 261))
        sizePolicy5.setHeightForWidth(self.shopping_cart_.sizePolicy().hasHeightForWidth())
        self.shopping_cart_.setSizePolicy(sizePolicy5)
        self.shopping_cart_.setSizeIncrement(QSize(0, 0))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush11 = QBrush(QColor(0, 0, 0, 255))
        brush11.setStyle(Qt.NoBrush)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush11)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush12 = QBrush(QColor(0, 0, 0, 255))
        brush12.setStyle(Qt.NoBrush)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush13 = QBrush(QColor(0, 0, 0, 255))
        brush13.setStyle(Qt.NoBrush)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush13)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.shopping_cart_.setPalette(palette3)
        self.shopping_cart_.setFont(font)
        self.shopping_cart_.setAutoFillBackground(False)
        self.shopping_cart_.setFrameShape(QFrame.NoFrame)
        self.shopping_cart_.setLineWidth(2)
        self.shopping_cart_.setMidLineWidth(0)
        self.shopping_cart_.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.shopping_cart_.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.shopping_cart_.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.shopping_cart_.setAutoScroll(True)
        self.shopping_cart_.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.shopping_cart_.setAlternatingRowColors(False)
        self.shopping_cart_.setSelectionMode(QAbstractItemView.NoSelection)
        self.shopping_cart_.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.shopping_cart_.setShowGrid(True)
        self.shopping_cart_.setGridStyle(Qt.SolidLine)
        self.shopping_cart_.setSortingEnabled(False)
        self.shopping_cart_.setCornerButtonEnabled(True)
        self.shopping_cart_.setRowCount(2)
        self.shopping_cart_.horizontalHeader().setVisible(False)
        self.shopping_cart_.horizontalHeader().setCascadingSectionResizes(False)
        self.shopping_cart_.horizontalHeader().setMinimumSectionSize(30)
        self.shopping_cart_.horizontalHeader().setDefaultSectionSize(130)
        self.shopping_cart_.horizontalHeader().setHighlightSections(False)
        self.shopping_cart_.horizontalHeader().setStretchLastSection(False)
        self.shopping_cart_.verticalHeader().setVisible(False)
        self.shopping_cart_.verticalHeader().setCascadingSectionResizes(False)
        self.shopping_cart_.verticalHeader().setMinimumSectionSize(25)
        self.shopping_cart_.verticalHeader().setDefaultSectionSize(25)
        self.shopping_cart_.verticalHeader().setHighlightSections(False)
        self.shopping_cart_.verticalHeader().setStretchLastSection(False)
        self.Label_Shoppingcart_2 = QLabel(self.frame)
        self.Label_Shoppingcart_2.setObjectName(u"Label_Shoppingcart_2")
        self.Label_Shoppingcart_2.setGeometry(QRect(540, 400, 61, 51))
        self.Label_Shoppingcart_2.setStyleSheet(u"font: 500 12pt \"Ofelia Display\";")
        self.Label_Shoppingcart_2.setAlignment(Qt.AlignCenter)
        self.Total_Label = QLabel(self.frame)
        self.Total_Label.setObjectName(u"Total_Label")
        self.Total_Label.setGeometry(QRect(680, 400, 61, 51))
        self.Total_Label.setStyleSheet(u"font: 500 12pt \"Ofelia Display\";")
        self.Total_Label.setAlignment(Qt.AlignCenter)
        self.Label_Shoppingcart_3 = QLabel(self.frame)
        self.Label_Shoppingcart_3.setObjectName(u"Label_Shoppingcart_3")
        self.Label_Shoppingcart_3.setGeometry(QRect(540, 360, 81, 51))
        self.Label_Shoppingcart_3.setStyleSheet(u"font: 500 12pt \"Ofelia Display\";")
        self.Label_Shoppingcart_3.setAlignment(Qt.AlignCenter)
        self.Discount_Label = QLabel(self.frame)
        self.Discount_Label.setObjectName(u"Discount_Label")
        self.Discount_Label.setGeometry(QRect(680, 360, 61, 51))
        self.Discount_Label.setStyleSheet(u"font: 500 12pt \"Ofelia Display\";")
        self.Discount_Label.setAlignment(Qt.AlignCenter)
        self.Label_Shoppingcart_4 = QLabel(self.frame)
        self.Label_Shoppingcart_4.setObjectName(u"Label_Shoppingcart_4")
        self.Label_Shoppingcart_4.setGeometry(QRect(540, 320, 111, 51))
        self.Label_Shoppingcart_4.setStyleSheet(u"font: 500 12pt \"Ofelia Display\";")
        self.Label_Shoppingcart_4.setAlignment(Qt.AlignCenter)
        self.Deliver_Label = QLabel(self.frame)
        self.Deliver_Label.setObjectName(u"Deliver_Label")
        self.Deliver_Label.setGeometry(QRect(680, 320, 61, 51))
        self.Deliver_Label.setStyleSheet(u"font: 500 12pt \"Ofelia Display\";")
        self.Deliver_Label.setAlignment(Qt.AlignCenter)
        self.label.raise_()
        self.Label_Shoppingcart.raise_()
        self.ShoppingCart_button_2.raise_()
        self.ShoppingCart_button_3.raise_()
        self.shopping_cart_.raise_()
        self.Label_Shoppingcart_2.raise_()
        self.Total_Label.raise_()
        self.Label_Shoppingcart_3.raise_()
        self.Discount_Label.raise_()
        self.Label_Shoppingcart_4.raise_()
        self.Deliver_Label.raise_()

        self.verticalLayout_20.addWidget(self.frame)

        self.stackedWidget.addWidget(self.shoppingcart_page)
        self.AddRecipeUI = QWidget()
        self.AddRecipeUI.setObjectName(u"AddRecipeUI")
        self.layoutWidget = QWidget(self.AddRecipeUI)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 60, 801, 271))
        self.addMenu_grid = QGridLayout(self.layoutWidget)
        self.addMenu_grid.setObjectName(u"addMenu_grid")
        self.addMenu_grid.setSizeConstraint(QLayout.SetNoConstraint)
        self.addMenu_grid.setContentsMargins(0, 0, 0, 0)
        self.Button_Upload = QPushButton(self.layoutWidget)
        self.Button_Upload.setObjectName(u"Button_Upload")
        self.Button_Upload.setMinimumSize(QSize(150, 30))
        self.Button_Upload.setFont(font)
        self.Button_Upload.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_Upload.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.Button_Upload.setIcon(icon3)

        self.addMenu_grid.addWidget(self.Button_Upload, 0, 1, 1, 1)

        self.Textbox_Recipename = QLineEdit(self.layoutWidget)
        self.Textbox_Recipename.setObjectName(u"Textbox_Recipename")
        self.Textbox_Recipename.setMinimumSize(QSize(0, 30))
        font6 = QFont()
        font6.setFamilies([u"Ofelia Display"])
        font6.setPointSize(10)
        font6.setBold(False)
        font6.setItalic(False)
        self.Textbox_Recipename.setFont(font6)
        self.Textbox_Recipename.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"font: 10pt \"Ofelia Display\";")

        self.addMenu_grid.addWidget(self.Textbox_Recipename, 1, 0, 1, 1)

        self.Textbox_Ethnictype = QLineEdit(self.layoutWidget)
        self.Textbox_Ethnictype.setObjectName(u"Textbox_Ethnictype")
        self.Textbox_Ethnictype.setMinimumSize(QSize(0, 30))
        self.Textbox_Ethnictype.setFont(font6)
        self.Textbox_Ethnictype.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"font: 10pt \"Ofelia Display\";")

        self.addMenu_grid.addWidget(self.Textbox_Ethnictype, 4, 0, 1, 1)

        self.Textbox_RecipeDescription = QLineEdit(self.layoutWidget)
        self.Textbox_RecipeDescription.setObjectName(u"Textbox_RecipeDescription")
        self.Textbox_RecipeDescription.setMinimumSize(QSize(0, 30))
        self.Textbox_RecipeDescription.setFont(font6)
        self.Textbox_RecipeDescription.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"font: 10pt \"Ofelia Display\";")

        self.addMenu_grid.addWidget(self.Textbox_RecipeDescription, 2, 0, 1, 1)

        self.Textbox_Upload = QLineEdit(self.layoutWidget)
        self.Textbox_Upload.setObjectName(u"Textbox_Upload")
        self.Textbox_Upload.setMinimumSize(QSize(0, 30))
        self.Textbox_Upload.setFont(font6)
        self.Textbox_Upload.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"font: 10pt \"Ofelia Display\";")

        self.addMenu_grid.addWidget(self.Textbox_Upload, 0, 0, 1, 1)

        self.Textbox_Nutrition = QLineEdit(self.layoutWidget)
        self.Textbox_Nutrition.setObjectName(u"Textbox_Nutrition")
        self.Textbox_Nutrition.setMinimumSize(QSize(0, 30))
        self.Textbox_Nutrition.setFont(font6)
        self.Textbox_Nutrition.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"font: 10pt \"Ofelia Display\";")

        self.addMenu_grid.addWidget(self.Textbox_Nutrition, 3, 0, 1, 1)

        self.Textbox_Setprice = QLineEdit(self.layoutWidget)
        self.Textbox_Setprice.setObjectName(u"Textbox_Setprice")
        self.Textbox_Setprice.setMinimumSize(QSize(0, 30))
        self.Textbox_Setprice.setFont(font6)
        self.Textbox_Setprice.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"font: 10pt \"Ofelia Display\";")

        self.addMenu_grid.addWidget(self.Textbox_Setprice, 5, 0, 1, 1)

        self.Label_addnewrecipe = QLabel(self.AddRecipeUI)
        self.Label_addnewrecipe.setObjectName(u"Label_addnewrecipe")
        self.Label_addnewrecipe.setGeometry(QRect(20, 30, 131, 16))
        self.Label_addnewrecipe.setStyleSheet(u"font: 700 11pt \"Ofelia Display\";")
        self.Label_deleterecipe = QLabel(self.AddRecipeUI)
        self.Label_deleterecipe.setObjectName(u"Label_deleterecipe")
        self.Label_deleterecipe.setGeometry(QRect(20, 370, 131, 16))
        self.Label_deleterecipe.setStyleSheet(u"font: 700 11pt \"Ofelia Display\";")
        self.DELETE_Textbox_Recipename = QLineEdit(self.AddRecipeUI)
        self.DELETE_Textbox_Recipename.setObjectName(u"DELETE_Textbox_Recipename")
        self.DELETE_Textbox_Recipename.setGeometry(QRect(20, 400, 251, 30))
        self.DELETE_Textbox_Recipename.setMinimumSize(QSize(0, 30))
        self.DELETE_Textbox_Recipename.setFont(font6)
        self.DELETE_Textbox_Recipename.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"font: 10pt \"Ofelia Display\";")
        self.DELETE_Textbox_RecipeID = QLineEdit(self.AddRecipeUI)
        self.DELETE_Textbox_RecipeID.setObjectName(u"DELETE_Textbox_RecipeID")
        self.DELETE_Textbox_RecipeID.setGeometry(QRect(370, 400, 251, 30))
        self.DELETE_Textbox_RecipeID.setMinimumSize(QSize(0, 30))
        self.DELETE_Textbox_RecipeID.setFont(font6)
        self.DELETE_Textbox_RecipeID.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"font: 10pt \"Ofelia Display\";")
        self.Label_OR = QLabel(self.AddRecipeUI)
        self.Label_OR.setObjectName(u"Label_OR")
        self.Label_OR.setGeometry(QRect(310, 400, 31, 31))
        self.Label_OR.setStyleSheet(u"font: 700 11pt \"Ofelia Display\";")
        self.Button_Delete = QPushButton(self.AddRecipeUI)
        self.Button_Delete.setObjectName(u"Button_Delete")
        self.Button_Delete.setGeometry(QRect(670, 400, 150, 30))
        self.Button_Delete.setMinimumSize(QSize(150, 30))
        self.Button_Delete.setFont(font)
        self.Button_Delete.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_Delete.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon12 = QIcon()
        icon12.addFile(u":/icons/images/icons/cil-ban.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Button_Delete.setIcon(icon12)
        self.Button_Confirm = QPushButton(self.AddRecipeUI)
        self.Button_Confirm.setObjectName(u"Button_Confirm")
        self.Button_Confirm.setGeometry(QRect(300, 340, 211, 30))
        self.Button_Confirm.setMinimumSize(QSize(150, 30))
        self.Button_Confirm.setFont(font)
        self.Button_Confirm.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_Confirm.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.Button_Confirm.setIcon(icon9)
        self.stackedWidget.addWidget(self.AddRecipeUI)
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.bottom_Frame = QFrame(self.home_page)
        self.bottom_Frame.setObjectName(u"bottom_Frame")
        self.bottom_Frame.setGeometry(QRect(10, 450, 831, 101))
        self.bottom_Frame.setFrameShape(QFrame.StyledPanel)
        self.bottom_Frame.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget = QWidget(self.bottom_Frame)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 10, 811, 81))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.ShoppingCart_button = QPushButton(self.gridLayoutWidget)
        self.ShoppingCart_button.setObjectName(u"ShoppingCart_button")
        self.ShoppingCart_button.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.ShoppingCart_button.sizePolicy().hasHeightForWidth())
        self.ShoppingCart_button.setSizePolicy(sizePolicy4)
        self.ShoppingCart_button.setMinimumSize(QSize(150, 30))
        self.ShoppingCart_button.setFont(font)
        self.ShoppingCart_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.ShoppingCart_button.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.ShoppingCart_button.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.ShoppingCart_button.setIcon(icon10)

        self.gridLayout_3.addWidget(self.ShoppingCart_button, 0, 2, 1, 1)

        self.Subscribe_Button = QPushButton(self.gridLayoutWidget)
        self.Subscribe_Button.setObjectName(u"Subscribe_Button")
        self.Subscribe_Button.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.Subscribe_Button.sizePolicy().hasHeightForWidth())
        self.Subscribe_Button.setSizePolicy(sizePolicy4)
        self.Subscribe_Button.setMinimumSize(QSize(150, 30))
        self.Subscribe_Button.setFont(font)
        self.Subscribe_Button.setCursor(QCursor(Qt.PointingHandCursor))
        self.Subscribe_Button.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.Subscribe_Button.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.Subscribe_Button.setIcon(icon6)

        self.gridLayout_3.addWidget(self.Subscribe_Button, 0, 0, 1, 1)

        self.Menu_Button = QPushButton(self.gridLayoutWidget)
        self.Menu_Button.setObjectName(u"Menu_Button")
        self.Menu_Button.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.Menu_Button.sizePolicy().hasHeightForWidth())
        self.Menu_Button.setSizePolicy(sizePolicy4)
        self.Menu_Button.setMinimumSize(QSize(150, 30))
        self.Menu_Button.setFont(font)
        self.Menu_Button.setCursor(QCursor(Qt.PointingHandCursor))
        self.Menu_Button.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.Menu_Button.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.Menu_Button.setIcon(icon5)
        self.Menu_Button.setIconSize(QSize(16, 16))

        self.gridLayout_3.addWidget(self.Menu_Button, 0, 1, 1, 1)

        self.pic_frame = QFrame(self.home_page)
        self.pic_frame.setObjectName(u"pic_frame")
        self.pic_frame.setGeometry(QRect(389, 39, 541, 301))
        self.pic_frame.setFrameShape(QFrame.StyledPanel)
        self.pic_frame.setFrameShadow(QFrame.Raised)
        self.pic_input = QLabel(self.pic_frame)
        self.pic_input.setObjectName(u"pic_input")
        self.pic_input.setGeometry(QRect(40, 0, 391, 291))
        self.pic_input.setPixmap(QPixmap(u":/ui_images/ui_images/chamorro_chicken.jpg"))
        self.pic_input.setScaledContents(True)
        self.frame_2 = QFrame(self.home_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 40, 431, 291))
        self.frame_2.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.Description_Label = QLabel(self.frame_2)
        self.Description_Label.setObjectName(u"Description_Label")
        self.Description_Label.setEnabled(True)
        self.Description_Label.setGeometry(QRect(0, 60, 421, 81))
        self.Description_Label.setFont(font6)
        self.Description_Label.setStyleSheet(u"font: 700 12pt \"Ofelia Display\";\n"
"font: 10pt \"Ofelia Display\";")
        self.Description_Label.setAlignment(Qt.AlignCenter)
        self.Description_Label.setWordWrap(True)
        self.Nutrition_Label = QLabel(self.frame_2)
        self.Nutrition_Label.setObjectName(u"Nutrition_Label")
        self.Nutrition_Label.setEnabled(True)
        self.Nutrition_Label.setGeometry(QRect(0, 150, 421, 81))
        self.Nutrition_Label.setFont(font6)
        self.Nutrition_Label.setStyleSheet(u"font: 700 12pt \"Ofelia Display\";\n"
"font: 10pt \"Ofelia Display\";")
        self.Nutrition_Label.setAlignment(Qt.AlignCenter)
        self.Nutrition_Label.setWordWrap(True)
        self.Featured_Label = QLabel(self.frame_2)
        self.Featured_Label.setObjectName(u"Featured_Label")
        self.Featured_Label.setEnabled(True)
        self.Featured_Label.setGeometry(QRect(2, 0, 421, 55))
        font7 = QFont()
        font7.setFamilies([u"Ofelia Display"])
        font7.setPointSize(12)
        font7.setBold(True)
        font7.setItalic(False)
        self.Featured_Label.setFont(font7)
        self.Featured_Label.setStyleSheet(u"font: 700 12pt \"Ofelia Display\";")
        self.Featured_Label.setAlignment(Qt.AlignCenter)
        self.Featured_Label.setWordWrap(False)
        self.Button_Addtocart = QPushButton(self.frame_2)
        self.Button_Addtocart.setObjectName(u"Button_Addtocart")
        self.Button_Addtocart.setEnabled(True)
        self.Button_Addtocart.setGeometry(QRect(140, 240, 151, 41))
        sizePolicy4.setHeightForWidth(self.Button_Addtocart.sizePolicy().hasHeightForWidth())
        self.Button_Addtocart.setSizePolicy(sizePolicy4)
        self.Button_Addtocart.setMinimumSize(QSize(150, 30))
        self.Button_Addtocart.setFont(font)
        self.Button_Addtocart.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_Addtocart.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.Button_Addtocart.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon13 = QIcon()
        icon13.addFile(u":/icons/images/icons/cil-paper-plane.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Button_Addtocart.setIcon(icon13)
        self.Price_Label = QLabel(self.frame_2)
        self.Price_Label.setObjectName(u"Price_Label")
        self.Price_Label.setEnabled(True)
        self.Price_Label.setGeometry(QRect(0, 230, 141, 55))
        self.Price_Label.setFont(font7)
        self.Price_Label.setStyleSheet(u"font: 700 12pt \"Ofelia Display\";")
        self.Price_Label.setAlignment(Qt.AlignCenter)
        self.Price_Label.setWordWrap(False)
        self.Textbox_Amount = QLineEdit(self.frame_2)
        self.Textbox_Amount.setObjectName(u"Textbox_Amount")
        self.Textbox_Amount.setGeometry(QRect(290, 240, 131, 41))
        self.Textbox_Amount.setMinimumSize(QSize(0, 30))
        self.Textbox_Amount.setFont(font6)
        self.Textbox_Amount.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"font: 10pt \"Ofelia Display\";")
        self.Textbox_Amount.setAlignment(Qt.AlignCenter)
        self.Textbox_Amount.setClearButtonEnabled(True)
        self.button_goright = QPushButton(self.home_page)
        self.button_goright.setObjectName(u"button_goright")
        self.button_goright.setEnabled(True)
        self.button_goright.setGeometry(QRect(670, 330, 150, 41))
        sizePolicy4.setHeightForWidth(self.button_goright.sizePolicy().hasHeightForWidth())
        self.button_goright.setSizePolicy(sizePolicy4)
        self.button_goright.setMinimumSize(QSize(150, 30))
        self.button_goright.setFont(font)
        self.button_goright.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_goright.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.button_goright.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon14 = QIcon()
        icon14.addFile(u":/icons/images/icons/cil-chevron-circle-right-alt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_goright.setIcon(icon14)
        self.button_goleft = QPushButton(self.home_page)
        self.button_goleft.setObjectName(u"button_goleft")
        self.button_goleft.setEnabled(True)
        self.button_goleft.setGeometry(QRect(0, 330, 150, 41))
        sizePolicy4.setHeightForWidth(self.button_goleft.sizePolicy().hasHeightForWidth())
        self.button_goleft.setSizePolicy(sizePolicy4)
        self.button_goleft.setMinimumSize(QSize(150, 30))
        self.button_goleft.setFont(font)
        self.button_goleft.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_goleft.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.button_goleft.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon15 = QIcon()
        icon15.addFile(u":/icons/images/icons/cil-chevron-circle-left-alt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_goleft.setIcon(icon15)
        self.stackedWidget.addWidget(self.home_page)
        self.frame_2.raise_()
        self.bottom_Frame.raise_()
        self.pic_frame.raise_()
        self.button_goright.raise_()
        self.button_goleft.raise_()
        self.Thankyou_page = QWidget()
        self.Thankyou_page.setObjectName(u"Thankyou_page")
        self.gridLayoutWidget_3 = QWidget(self.Thankyou_page)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(0, 80, 1001, 371))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Thank_you_4 = QLabel(self.gridLayoutWidget_3)
        self.Thank_you_4.setObjectName(u"Thank_you_4")
        self.Thank_you_4.setStyleSheet(u"font: 700 11pt \"Ofelia Display\";")
        self.Thank_you_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.Thank_you_4, 3, 0, 1, 1)

        self.Thank_you = QLabel(self.gridLayoutWidget_3)
        self.Thank_you.setObjectName(u"Thank_you")
        self.Thank_you.setStyleSheet(u"font: 700 11pt \"Ofelia Display\";")
        self.Thank_you.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.Thank_you, 4, 0, 1, 1)

        self.Thank_you_6 = QLabel(self.gridLayoutWidget_3)
        self.Thank_you_6.setObjectName(u"Thank_you_6")
        self.Thank_you_6.setStyleSheet(u"font: 700 11pt \"Ofelia Display\";")
        self.Thank_you_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.Thank_you_6, 2, 0, 1, 1)

        self.Thank_you_5 = QLabel(self.gridLayoutWidget_3)
        self.Thank_you_5.setObjectName(u"Thank_you_5")
        self.Thank_you_5.setStyleSheet(u"font: 700 11pt \"Ofelia Display\";")
        self.Thank_you_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.Thank_you_5, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.Thankyou_page)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(4)
        self.Button_UpdateMenu.setDefault(False)
        self.Button_ManageSubscriptions.setDefault(False)
        self.Button_ManageEmployees.setDefault(False)
        self.Button_Addrecipe.setDefault(False)
        self.ShoppingCart_button_2.setDefault(False)
        self.ShoppingCart_button_3.setDefault(False)
        self.ShoppingCart_button.setDefault(False)
        self.Subscribe_Button.setDefault(False)
        self.Menu_Button.setDefault(False)
        self.Button_Addtocart.setDefault(False)
        self.button_goright.setDefault(False)
        self.button_goleft.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"MVP", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Modern GUI / Flat Style", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"Adjustments", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">PyDracula</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">An interface created using Python and PySide (support for PyQt), and with colors based on the Dracula theme created by Zen"
                        "o Rocha.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">MIT License</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#bd93f9;\">Created by: Wanderson M. Pimenta</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert UI</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-uic main.ui &gt; ui_main.py</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-in"
                        "dent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert QRC</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-rcc resources.qrc -o resources_rc.py</span></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"Welcome", None))
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"FILE BOX", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.labelVersion_3.setText(QCoreApplication.translate("MainWindow", u"Label description", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Test 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))

        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"Link Button", None))
        self.commandLinkButton.setDescription(QCoreApplication.translate("MainWindow", u"Link description", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem20 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Test", None));
        ___qtablewidgetitem21 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Text", None));
        ___qtablewidgetitem22 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Cell", None));
        ___qtablewidgetitem23 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Line", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

#if QT_CONFIG(tooltip)
        self.Button_UpdateMenu.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.Button_UpdateMenu.setText(QCoreApplication.translate("MainWindow", u"Update Menu", None))
#if QT_CONFIG(tooltip)
        self.Button_ManageSubscriptions.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.Button_ManageSubscriptions.setText(QCoreApplication.translate("MainWindow", u"Manage Subscriptions", None))
#if QT_CONFIG(tooltip)
        self.Button_ManageEmployees.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.Button_ManageEmployees.setText(QCoreApplication.translate("MainWindow", u"Manage Employees", None))
#if QT_CONFIG(tooltip)
        self.Button_Addrecipe.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.Button_Addrecipe.setText(QCoreApplication.translate("MainWindow", u"Add/Delete a Recipe", None))
        ___qtablewidgetitem24 = self.subscribers_.horizontalHeaderItem(0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem25 = self.subscribers_.horizontalHeaderItem(1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem26 = self.subscribers_.horizontalHeaderItem(2)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem27 = self.subscribers_.horizontalHeaderItem(3)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem28 = self.subscribers_.horizontalHeaderItem(4)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem29 = self.subscribers_.verticalHeaderItem(0)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem30 = self.subscribers_.verticalHeaderItem(1)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem31 = self.subscribers_.verticalHeaderItem(2)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled1 = self.subscribers_.isSortingEnabled()
        self.subscribers_.setSortingEnabled(False)
        ___qtablewidgetitem32 = self.subscribers_.item(0, 0)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Customer ID", None));
        ___qtablewidgetitem33 = self.subscribers_.item(0, 1)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"First Name", None));
        ___qtablewidgetitem34 = self.subscribers_.item(0, 2)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Last Name", None));
        ___qtablewidgetitem35 = self.subscribers_.item(0, 3)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Loyalty Points", None));
        ___qtablewidgetitem36 = self.subscribers_.item(0, 4)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Subscribed On", None));
        ___qtablewidgetitem37 = self.subscribers_.item(2, 0)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"test", None));
        ___qtablewidgetitem38 = self.subscribers_.item(2, 1)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"test", None));
        ___qtablewidgetitem39 = self.subscribers_.item(2, 2)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"s", None));
        ___qtablewidgetitem40 = self.subscribers_.item(3, 0)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"test", None));
        ___qtablewidgetitem41 = self.subscribers_.item(3, 1)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"test", None));
        ___qtablewidgetitem42 = self.subscribers_.item(3, 2)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"test", None));
        self.subscribers_.setSortingEnabled(__sortingEnabled1)

        ___qtablewidgetitem43 = self.menu_.horizontalHeaderItem(0)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem44 = self.menu_.horizontalHeaderItem(1)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem45 = self.menu_.horizontalHeaderItem(2)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem46 = self.menu_.horizontalHeaderItem(3)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem47 = self.menu_.horizontalHeaderItem(4)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem48 = self.menu_.horizontalHeaderItem(5)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem49 = self.menu_.verticalHeaderItem(0)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem50 = self.menu_.verticalHeaderItem(1)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem51 = self.menu_.verticalHeaderItem(2)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled2 = self.menu_.isSortingEnabled()
        self.menu_.setSortingEnabled(False)
        ___qtablewidgetitem52 = self.menu_.item(0, 0)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"Recipe ID", None));
        ___qtablewidgetitem53 = self.menu_.item(0, 1)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"Recipe Name", None));
        ___qtablewidgetitem54 = self.menu_.item(0, 2)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"Description", None));
        ___qtablewidgetitem55 = self.menu_.item(0, 3)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"Nutrition", None));
        ___qtablewidgetitem56 = self.menu_.item(0, 4)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"Ethnic Type", None));
        ___qtablewidgetitem57 = self.menu_.item(0, 5)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"Price", None));
        ___qtablewidgetitem58 = self.menu_.item(2, 0)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"test", None));
        ___qtablewidgetitem59 = self.menu_.item(2, 1)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"test", None));
        ___qtablewidgetitem60 = self.menu_.item(2, 2)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"s", None));
        ___qtablewidgetitem61 = self.menu_.item(3, 0)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"test", None));
        ___qtablewidgetitem62 = self.menu_.item(3, 1)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"test", None));
        ___qtablewidgetitem63 = self.menu_.item(3, 2)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"test", None));
        self.menu_.setSortingEnabled(__sortingEnabled2)

        self.Button_Confirm_Changes.setText(QCoreApplication.translate("MainWindow", u"Confirm Changes", None))
        self.Label_Shoppingcart.setText(QCoreApplication.translate("MainWindow", u"Shopping Cart", None))
#if QT_CONFIG(tooltip)
        self.ShoppingCart_button_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.ShoppingCart_button_2.setText(QCoreApplication.translate("MainWindow", u"Checkout", None))
#if QT_CONFIG(tooltip)
        self.ShoppingCart_button_3.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.ShoppingCart_button_3.setText(QCoreApplication.translate("MainWindow", u"Cancel Order", None))
        self.label.setText("")
        ___qtablewidgetitem64 = self.shopping_cart_.horizontalHeaderItem(0)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem65 = self.shopping_cart_.horizontalHeaderItem(1)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem66 = self.shopping_cart_.horizontalHeaderItem(2)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem67 = self.shopping_cart_.horizontalHeaderItem(3)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem68 = self.shopping_cart_.verticalHeaderItem(0)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled3 = self.shopping_cart_.isSortingEnabled()
        self.shopping_cart_.setSortingEnabled(False)
        ___qtablewidgetitem69 = self.shopping_cart_.item(0, 0)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("MainWindow", u"Recipe ID", None));
        ___qtablewidgetitem70 = self.shopping_cart_.item(0, 1)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("MainWindow", u"Recipe Name", None));
        ___qtablewidgetitem71 = self.shopping_cart_.item(0, 2)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("MainWindow", u"Amount", None));
        ___qtablewidgetitem72 = self.shopping_cart_.item(0, 3)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("MainWindow", u"Price", None));
        ___qtablewidgetitem73 = self.shopping_cart_.item(1, 0)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("MainWindow", u"test", None));
        ___qtablewidgetitem74 = self.shopping_cart_.item(1, 1)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("MainWindow", u"test", None));
        ___qtablewidgetitem75 = self.shopping_cart_.item(1, 2)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("MainWindow", u"test", None));
        ___qtablewidgetitem76 = self.shopping_cart_.item(1, 3)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("MainWindow", u"test", None));
        self.shopping_cart_.setSortingEnabled(__sortingEnabled3)

        self.Label_Shoppingcart_2.setText(QCoreApplication.translate("MainWindow", u"Total:", None))
        self.Total_Label.setText(QCoreApplication.translate("MainWindow", u"$0.00", None))
        self.Label_Shoppingcart_3.setText(QCoreApplication.translate("MainWindow", u"Discount:", None))
        self.Discount_Label.setText(QCoreApplication.translate("MainWindow", u"$0.00", None))
        self.Label_Shoppingcart_4.setText(QCoreApplication.translate("MainWindow", u"Delivery Fee:", None))
        self.Deliver_Label.setText(QCoreApplication.translate("MainWindow", u"$0.00", None))
        self.Button_Upload.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.Textbox_Recipename.setText("")
        self.Textbox_Recipename.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Recipe Name", None))
        self.Textbox_Ethnictype.setText("")
        self.Textbox_Ethnictype.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ethnic Type", None))
        self.Textbox_RecipeDescription.setText("")
        self.Textbox_RecipeDescription.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Recipe Description", None))
        self.Textbox_Upload.setText("")
        self.Textbox_Upload.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Upload Picture", None))
        self.Textbox_Nutrition.setText("")
        self.Textbox_Nutrition.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nutrition Info", None))
        self.Textbox_Setprice.setText("")
        self.Textbox_Setprice.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Set Price", None))
        self.Label_addnewrecipe.setText(QCoreApplication.translate("MainWindow", u"Add a new recipe", None))
        self.Label_deleterecipe.setText(QCoreApplication.translate("MainWindow", u"Delete recipe", None))
        self.DELETE_Textbox_Recipename.setText("")
        self.DELETE_Textbox_Recipename.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Recipe Name", None))
        self.DELETE_Textbox_RecipeID.setText("")
        self.DELETE_Textbox_RecipeID.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Recipe ID", None))
        self.Label_OR.setText(QCoreApplication.translate("MainWindow", u"OR", None))
        self.Button_Delete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.Button_Confirm.setText(QCoreApplication.translate("MainWindow", u"Upload", None))
#if QT_CONFIG(tooltip)
        self.ShoppingCart_button.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.ShoppingCart_button.setText(QCoreApplication.translate("MainWindow", u"Shopping Cart", None))
#if QT_CONFIG(tooltip)
        self.Subscribe_Button.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.Subscribe_Button.setText(QCoreApplication.translate("MainWindow", u"Subscribe", None))
#if QT_CONFIG(tooltip)
        self.Menu_Button.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.Menu_Button.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.pic_input.setText("")
        self.Button_Addtocart.setText(QCoreApplication.translate("MainWindow", u"Add to cart", None))
        self.Textbox_Amount.setText("")
        self.Textbox_Amount.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Amount", None))
#if QT_CONFIG(tooltip)
        self.button_goright.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.button_goright.setText("")
#if QT_CONFIG(tooltip)
        self.button_goleft.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.button_goleft.setText("")
        self.Thank_you_4.setText(QCoreApplication.translate("MainWindow", u"Healthier You.", None))
        self.Thank_you.setText(QCoreApplication.translate("MainWindow", u"Thanks for subscribing! ", None))
        self.Thank_you_6.setText(QCoreApplication.translate("MainWindow", u"Discounted Orders.", None))
        self.Thank_you_5.setText(QCoreApplication.translate("MainWindow", u"Free Delivery.", None))
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
    # retranslateUi

