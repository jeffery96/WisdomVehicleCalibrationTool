# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI_BASEqPQGdW.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from CustomWidgets.CustomGaugePanel import GaugePanel
from CustomWidgets.CustomProgressBar import ProgressBar
from CustomWidgets.CustomIndicatorLight import IndicatorLight

import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 720)
        MainWindow.setMinimumSize(QSize(1000, 720))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(66, 73, 90, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(55, 61, 75, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(22, 24, 30, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(29, 32, 40, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        brush6 = QBrush(QColor(210, 210, 210, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        brush8 = QBrush(QColor(85, 170, 255, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Active, QPalette.Link, brush8)
        brush9 = QBrush(QColor(255, 0, 127, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush10 = QBrush(QColor(44, 49, 60, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        brush11 = QBrush(QColor(210, 210, 210, 128))
        brush11.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
        brush12 = QBrush(QColor(210, 210, 210, 128))
        brush12.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        brush13 = QBrush(QColor(51, 153, 255, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush13)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        brush14 = QBrush(QColor(210, 210, 210, 128))
        brush14.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush14)
#endif
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QMainWindow {background: transparent; }\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(27, 29, 35, 160);\n"
"	border: 1px solid rgb(40, 40, 40);\n"
"	border-radius: 2px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background: transparent;\n"
"color: rgb(210, 210, 210);")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"/* LINE EDIT */\n"
"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* SCROLL BARS */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(85, 170, 255);\n"
"    min-width: 25px;\n"
"	border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
""
                        "	border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
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
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(85, 170, 255);\n"
"    min-height: 25px;\n"
"	border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63"
                        ", 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
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
"/* CHECKBOX */\n"
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
"	background-image: url(:/16x16/icons/16x16/cil-check-alt.png);\n"
"}\n"
"\n"
"/* RADIO BUTTON */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius"
                        ": 10px;\n"
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
"/* COMBOBOX */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb("
                        "85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* SLIDERS */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 9px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:verti"
                        "cal {\n"
"    background-color: rgb(85, 170, 255);\n"
"	border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 65))
        self.frame_top.setMaximumSize(QSize(16777215, 65))
        self.frame_top.setStyleSheet(u"background-color: transparent;")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.frame_top)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 16777215))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle_menu = QPushButton(self.frame_toggle)
        self.btn_toggle_menu.setObjectName(u"btn_toggle_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle_menu.sizePolicy().hasHeightForWidth())
        self.btn_toggle_menu.setSizePolicy(sizePolicy)
        self.btn_toggle_menu.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(27, 29, 35);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_toggle_menu)


        self.horizontalLayout_3.addWidget(self.frame_toggle)

        self.frame_top_right = QFrame(self.frame_top)
        self.frame_top_right.setObjectName(u"frame_top_right")
        self.frame_top_right.setStyleSheet(u"background: transparent;")
        self.frame_top_right.setFrameShape(QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_top_right)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top_btns = QFrame(self.frame_top_right)
        self.frame_top_btns.setObjectName(u"frame_top_btns")
        self.frame_top_btns.setMaximumSize(QSize(16777215, 42))
        self.frame_top_btns.setStyleSheet(u"background-color: rgba(27, 29, 35, 200)")
        self.frame_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_label_top_btns = QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setObjectName(u"frame_label_top_btns")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_label_top_btns.sizePolicy().hasHeightForWidth())
        self.frame_label_top_btns.setSizePolicy(sizePolicy1)
        self.frame_label_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 10, 0)
        self.frame_icon_top_bar = QFrame(self.frame_label_top_btns)
        self.frame_icon_top_bar.setObjectName(u"frame_icon_top_bar")
        self.frame_icon_top_bar.setMaximumSize(QSize(30, 30))
        self.frame_icon_top_bar.setStyleSheet(u"background: transparent;\n"
"background-image: url(:/16x16/icons/16x16/cil-terminal.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"")
        self.frame_icon_top_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_icon_top_bar.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_icon_top_bar)

        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_title_bar_top.setFont(font1)
        self.label_title_bar_top.setStyleSheet(u"background: transparent;\n"
"")

        self.horizontalLayout_10.addWidget(self.label_title_bar_top)


        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)

        self.frame_btns_right = QFrame(self.frame_top_btns)
        self.frame_btns_right.setObjectName(u"frame_btns_right")
        sizePolicy1.setHeightForWidth(self.frame_btns_right.sizePolicy().hasHeightForWidth())
        self.frame_btns_right.setSizePolicy(sizePolicy1)
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_btns_right)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy2)
        self.btn_minimize.setMinimumSize(QSize(40, 0))
        self.btn_minimize.setMaximumSize(QSize(40, 16777215))
        self.btn_minimize.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/16x16/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.btn_minimize)

        self.btn_maximize_restore = QPushButton(self.frame_btns_right)
        self.btn_maximize_restore.setObjectName(u"btn_maximize_restore")
        sizePolicy2.setHeightForWidth(self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
        self.btn_maximize_restore.setSizePolicy(sizePolicy2)
        self.btn_maximize_restore.setMinimumSize(QSize(40, 0))
        self.btn_maximize_restore.setMaximumSize(QSize(40, 16777215))
        self.btn_maximize_restore.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/16x16/icons/16x16/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize_restore.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.btn_maximize_restore)

        self.btn_close = QPushButton(self.frame_btns_right)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy2.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy2)
        self.btn_close.setMinimumSize(QSize(40, 0))
        self.btn_close.setMaximumSize(QSize(40, 16777215))
        self.btn_close.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.btn_close)


        self.horizontalLayout_4.addWidget(self.frame_btns_right, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_top_btns)

        self.frame_top_info = QFrame(self.frame_top_right)
        self.frame_top_info.setObjectName(u"frame_top_info")
        self.frame_top_info.setMaximumSize(QSize(16777215, 65))
        self.frame_top_info.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_top_info.setFrameShape(QFrame.NoFrame)
        self.frame_top_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_top_info)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.label_top_info_1 = QLabel(self.frame_top_info)
        self.label_top_info_1.setObjectName(u"label_top_info_1")
        self.label_top_info_1.setMaximumSize(QSize(16777215, 15))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        self.label_top_info_1.setFont(font2)
        self.label_top_info_1.setStyleSheet(u"color: rgb(98, 103, 111); ")

        self.horizontalLayout_8.addWidget(self.label_top_info_1)

        self.label_top_info_2 = QLabel(self.frame_top_info)
        self.label_top_info_2.setObjectName(u"label_top_info_2")
        self.label_top_info_2.setMinimumSize(QSize(0, 0))
        self.label_top_info_2.setMaximumSize(QSize(250, 20))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setBold(True)
        font3.setWeight(75)
        self.label_top_info_2.setFont(font3)
        self.label_top_info_2.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_top_info_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_top_info_2)


        self.verticalLayout_2.addWidget(self.frame_top_info)


        self.horizontalLayout_3.addWidget(self.frame_top_right)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setObjectName(u"frame_center")
        sizePolicy.setHeightForWidth(self.frame_center.sizePolicy().hasHeightForWidth())
        self.frame_center.setSizePolicy(sizePolicy)
        self.frame_center.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.frame_center.setFrameShape(QFrame.NoFrame)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.frame_center)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy3)
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setLayoutDirection(Qt.LeftToRight)
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_menus = QFrame(self.frame_left_menu)
        self.frame_menus.setObjectName(u"frame_menus")
        self.frame_menus.setFrameShape(QFrame.NoFrame)
        self.frame_menus.setFrameShadow(QFrame.Raised)
        self.layout_menus = QVBoxLayout(self.frame_menus)
        self.layout_menus.setSpacing(0)
        self.layout_menus.setObjectName(u"layout_menus")
        self.layout_menus.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.frame_menus, 0, Qt.AlignTop)

        self.frame_extra_menus = QFrame(self.frame_left_menu)
        self.frame_extra_menus.setObjectName(u"frame_extra_menus")
        sizePolicy3.setHeightForWidth(self.frame_extra_menus.sizePolicy().hasHeightForWidth())
        self.frame_extra_menus.setSizePolicy(sizePolicy3)
        self.frame_extra_menus.setFrameShape(QFrame.NoFrame)
        self.frame_extra_menus.setFrameShadow(QFrame.Raised)
        self.layout_menu_bottom = QVBoxLayout(self.frame_extra_menus)
        self.layout_menu_bottom.setSpacing(10)
        self.layout_menu_bottom.setObjectName(u"layout_menu_bottom")
        self.layout_menu_bottom.setContentsMargins(0, 0, 0, 25)
        self.label_user_icon = QLabel(self.frame_extra_menus)
        self.label_user_icon.setObjectName(u"label_user_icon")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_user_icon.sizePolicy().hasHeightForWidth())
        self.label_user_icon.setSizePolicy(sizePolicy4)
        self.label_user_icon.setMinimumSize(QSize(60, 60))
        self.label_user_icon.setMaximumSize(QSize(60, 60))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(12)
        self.label_user_icon.setFont(font4)
        self.label_user_icon.setStyleSheet(u"QLabel {\n"
"	border-radius: 30px;\n"
"	background-color: rgb(44, 49, 60);\n"
"	border: 5px solid rgb(39, 44, 54);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}")
        self.label_user_icon.setAlignment(Qt.AlignCenter)

        self.layout_menu_bottom.addWidget(self.label_user_icon, 0, Qt.AlignHCenter)


        self.verticalLayout_5.addWidget(self.frame_extra_menus, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_content_right = QFrame(self.frame_center)
        self.frame_content_right.setObjectName(u"frame_content_right")
        self.frame_content_right.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.frame_content_right.setFrameShape(QFrame.NoFrame)
        self.frame_content_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_content_right)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_content = QFrame(self.frame_content_right)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_content)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"/*QWidget{*/\n"
"/*    background-color: white;*/\n"
"/*}*/\n"
"background: transparent;\n"
"\n"
"")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_10 = QVBoxLayout(self.page_home)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_6 = QLabel(self.page_home)
        self.label_6.setObjectName(u"label_6")
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(40)
        self.label_6.setFont(font5)
        self.label_6.setStyleSheet(u"")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_6)

        self.label = QLabel(self.page_home)
        self.label.setObjectName(u"label")
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(20)
        self.label.setFont(font6)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label)

        self.label_7 = QLabel(self.page_home)
        self.label_7.setObjectName(u"label_7")
        font7 = QFont()
        font7.setFamily(u"Segoe UI")
        font7.setPointSize(15)
        self.label_7.setFont(font7)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_7)

        self.stackedWidget.addWidget(self.page_home)
        self.page_device = QWidget()
        self.page_device.setObjectName(u"page_device")
        self.page_device.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(39, 44, 54);\n"
"	border-radius: 6px;\n"
"	/*font-family:\"Segoe UI\";*/\n"
"}\n"
"QFrame QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QFrame QComboBox:disabled{\n"
"	background-color: rgb(57, 65, 80);\n"
"}\n"
"QFrame QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"QFrame QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QFrame QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QFrame QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"QLineEdit {\n"
"	backg"
                        "round-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.horizontalLayout_18 = QHBoxLayout(self.page_device)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(10)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.frame_4 = QFrame(self.page_device)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy5)
        self.frame_4.setMinimumSize(QSize(231, 211))
        self.frame_4.setMaximumSize(QSize(320, 16777215))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setContentsMargins(-1, -1, -1, 10)
        self.lable_devicetype = QLabel(self.frame_4)
        self.lable_devicetype.setObjectName(u"lable_devicetype")
        self.lable_devicetype.setFont(font2)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lable_devicetype)

        self.cbb_devicetype = QComboBox(self.frame_4)
        self.cbb_devicetype.addItem("")
        self.cbb_devicetype.addItem("")
        self.cbb_devicetype.setObjectName(u"cbb_devicetype")
        sizePolicy5.setHeightForWidth(self.cbb_devicetype.sizePolicy().hasHeightForWidth())
        self.cbb_devicetype.setSizePolicy(sizePolicy5)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.cbb_devicetype)

        self.label_deviceindex = QLabel(self.frame_4)
        self.label_deviceindex.setObjectName(u"label_deviceindex")
        self.label_deviceindex.setFont(font2)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_deviceindex)

        self.cbb_deviceindex = QComboBox(self.frame_4)
        self.cbb_deviceindex.addItem("")
        self.cbb_deviceindex.addItem("")
        self.cbb_deviceindex.addItem("")
        self.cbb_deviceindex.addItem("")
        self.cbb_deviceindex.setObjectName(u"cbb_deviceindex")
        sizePolicy5.setHeightForWidth(self.cbb_deviceindex.sizePolicy().hasHeightForWidth())
        self.cbb_deviceindex.setSizePolicy(sizePolicy5)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.cbb_deviceindex)

        self.label_baudrate = QLabel(self.frame_4)
        self.label_baudrate.setObjectName(u"label_baudrate")
        self.label_baudrate.setFont(font2)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_baudrate)

        self.cbb_baudrate = QComboBox(self.frame_4)
        self.cbb_baudrate.addItem("")
        self.cbb_baudrate.addItem("")
        self.cbb_baudrate.setObjectName(u"cbb_baudrate")
        sizePolicy5.setHeightForWidth(self.cbb_baudrate.sizePolicy().hasHeightForWidth())
        self.cbb_baudrate.setSizePolicy(sizePolicy5)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.cbb_baudrate)

        self.label_canchannel = QLabel(self.frame_4)
        self.label_canchannel.setObjectName(u"label_canchannel")
        self.label_canchannel.setFont(font2)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_canchannel)

        self.cbb_canchannel = QComboBox(self.frame_4)
        self.cbb_canchannel.addItem("")
        self.cbb_canchannel.addItem("")
        self.cbb_canchannel.addItem("")
        self.cbb_canchannel.setObjectName(u"cbb_canchannel")
        sizePolicy5.setHeightForWidth(self.cbb_canchannel.sizePolicy().hasHeightForWidth())
        self.cbb_canchannel.setSizePolicy(sizePolicy5)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.cbb_canchannel)


        self.verticalLayout_12.addLayout(self.formLayout)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.btn_opendevice = QPushButton(self.frame_4)
        self.btn_opendevice.setObjectName(u"btn_opendevice")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.btn_opendevice.sizePolicy().hasHeightForWidth())
        self.btn_opendevice.setSizePolicy(sizePolicy6)
        self.btn_opendevice.setMinimumSize(QSize(93, 28))
        self.btn_opendevice.setMaximumSize(QSize(93, 28))

        self.horizontalLayout_13.addWidget(self.btn_opendevice)


        self.verticalLayout_12.addLayout(self.horizontalLayout_13)


        self.horizontalLayout_17.addLayout(self.verticalLayout_12)


        self.verticalLayout_13.addWidget(self.frame_4)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.pte_info = QPlainTextEdit(self.page_device)
        self.pte_info.setObjectName(u"pte_info")
        self.pte_info.setMaximumSize(QSize(320, 16777215))
        self.pte_info.setStyleSheet(u"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"}\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.pte_info.setReadOnly(True)

        self.horizontalLayout_16.addWidget(self.pte_info)


        self.verticalLayout_13.addLayout(self.horizontalLayout_16)


        self.horizontalLayout_18.addLayout(self.verticalLayout_13)

        self.verticalLayout_36 = QVBoxLayout()
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.tablew_msgdisplay = QTableWidget(self.page_device)
        if (self.tablew_msgdisplay.columnCount() < 6):
            self.tablew_msgdisplay.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tablew_msgdisplay.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tablew_msgdisplay.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tablew_msgdisplay.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tablew_msgdisplay.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tablew_msgdisplay.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tablew_msgdisplay.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tablew_msgdisplay.setObjectName(u"tablew_msgdisplay")
        sizePolicy3.setHeightForWidth(self.tablew_msgdisplay.sizePolicy().hasHeightForWidth())
        self.tablew_msgdisplay.setSizePolicy(sizePolicy3)
        self.tablew_msgdisplay.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tablew_msgdisplay.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}")
        self.tablew_msgdisplay.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tablew_msgdisplay.setAutoScroll(True)
        self.tablew_msgdisplay.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tablew_msgdisplay.setAlternatingRowColors(False)
        self.tablew_msgdisplay.horizontalHeader().setVisible(True)
        self.tablew_msgdisplay.horizontalHeader().setCascadingSectionResizes(False)
        self.tablew_msgdisplay.horizontalHeader().setMinimumSectionSize(60)
        self.tablew_msgdisplay.horizontalHeader().setDefaultSectionSize(100)
        self.tablew_msgdisplay.horizontalHeader().setStretchLastSection(True)
        self.tablew_msgdisplay.verticalHeader().setVisible(False)
        self.tablew_msgdisplay.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_36.addWidget(self.tablew_msgdisplay)

        self.frame_5 = QFrame(self.page_device)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_66 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setSpacing(20)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setHorizontalSpacing(10)
        self.formLayout_2.setVerticalSpacing(20)
        self.label_sendtype = QLabel(self.frame_5)
        self.label_sendtype.setObjectName(u"label_sendtype")
        self.label_sendtype.setFont(font2)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_sendtype)

        self.cbb_sendtype = QComboBox(self.frame_5)
        self.cbb_sendtype.addItem("")
        self.cbb_sendtype.addItem("")
        self.cbb_sendtype.addItem("")
        self.cbb_sendtype.setObjectName(u"cbb_sendtype")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.cbb_sendtype.sizePolicy().hasHeightForWidth())
        self.cbb_sendtype.setSizePolicy(sizePolicy7)
        self.cbb_sendtype.setMinimumSize(QSize(120, 28))
        self.cbb_sendtype.setMaximumSize(QSize(120, 26))

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.cbb_sendtype)

        self.label_id = QLabel(self.frame_5)
        self.label_id.setObjectName(u"label_id")
        self.label_id.setFont(font2)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_id)

        self.le_id = QLineEdit(self.frame_5)
        self.le_id.setObjectName(u"le_id")
        sizePolicy7.setHeightForWidth(self.le_id.sizePolicy().hasHeightForWidth())
        self.le_id.setSizePolicy(sizePolicy7)
        self.le_id.setMinimumSize(QSize(120, 28))
        self.le_id.setMaximumSize(QSize(120, 26))

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.le_id)

        self.label_sendnum = QLabel(self.frame_5)
        self.label_sendnum.setObjectName(u"label_sendnum")
        self.label_sendnum.setFont(font2)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_sendnum)

        self.le_sendnum = QLineEdit(self.frame_5)
        self.le_sendnum.setObjectName(u"le_sendnum")
        self.le_sendnum.setMinimumSize(QSize(120, 28))
        self.le_sendnum.setMaximumSize(QSize(120, 26))

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.le_sendnum)


        self.horizontalLayout_19.addLayout(self.formLayout_2)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setHorizontalSpacing(10)
        self.formLayout_3.setVerticalSpacing(20)
        self.label_sendinterval = QLabel(self.frame_5)
        self.label_sendinterval.setObjectName(u"label_sendinterval")
        self.label_sendinterval.setFont(font2)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_sendinterval)

        self.le_sendinterval = QLineEdit(self.frame_5)
        self.le_sendinterval.setObjectName(u"le_sendinterval")
        self.le_sendinterval.setMinimumSize(QSize(0, 28))
        self.le_sendinterval.setMaximumSize(QSize(150, 26))

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.le_sendinterval)

        self.label_data = QLabel(self.frame_5)
        self.label_data.setObjectName(u"label_data")
        self.label_data.setFont(font2)

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_data)

        self.le_data = QLineEdit(self.frame_5)
        self.le_data.setObjectName(u"le_data")
        self.le_data.setMinimumSize(QSize(210, 28))
        self.le_data.setMaximumSize(QSize(180, 26))

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.le_data)


        self.horizontalLayout_19.addLayout(self.formLayout_3)


        self.horizontalLayout_66.addLayout(self.horizontalLayout_19)

        self.horizontalSpacer_16 = QSpacerItem(63, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_66.addItem(self.horizontalSpacer_16)

        self.verticalLayout_37 = QVBoxLayout()
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_37.addItem(self.verticalSpacer_13)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.btn_sendmsg = QPushButton(self.frame_5)
        self.btn_sendmsg.setObjectName(u"btn_sendmsg")
        sizePolicy6.setHeightForWidth(self.btn_sendmsg.sizePolicy().hasHeightForWidth())
        self.btn_sendmsg.setSizePolicy(sizePolicy6)
        self.btn_sendmsg.setMinimumSize(QSize(93, 28))
        self.btn_sendmsg.setMaximumSize(QSize(93, 28))

        self.horizontalLayout_15.addWidget(self.btn_sendmsg)


        self.verticalLayout_37.addLayout(self.horizontalLayout_15)


        self.horizontalLayout_66.addLayout(self.verticalLayout_37)

        self.horizontalLayout_66.setStretch(1, 1)
        self.horizontalLayout_66.setStretch(2, 1)

        self.verticalLayout_36.addWidget(self.frame_5)

        self.verticalLayout_36.setStretch(0, 3)
        self.verticalLayout_36.setStretch(1, 1)

        self.horizontalLayout_18.addLayout(self.verticalLayout_36)

        self.stackedWidget.addWidget(self.page_device)
        self.page_panel = QWidget()
        self.page_panel.setObjectName(u"page_panel")
        self.page_panel.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(39, 44, 54);\n"
"	border-radius: 6px;\n"
"	/*font-family:\"Segoe UI\";*/\n"
"}\n"
"QFrame QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QFrame QComboBox:disabled{\n"
"	background-color: rgb(57, 65, 80);\n"
"}\n"
"QFrame QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"QFrame QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QFrame QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QFrame QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"")
        self.verticalLayout_14 = QVBoxLayout(self.page_panel)
        self.verticalLayout_14.setSpacing(10)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(10, 10, 10, 10)
        self.frame_gaugepanel = QFrame(self.page_panel)
        self.frame_gaugepanel.setObjectName(u"frame_gaugepanel")
        self.frame_gaugepanel.setMinimumSize(QSize(880, 230))
        self.frame_gaugepanel.setFrameShape(QFrame.NoFrame)
        self.frame_gaugepanel.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_gaugepanel)
        self.horizontalLayout_24.setSpacing(10)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 10, 0, 10)
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_7)

        self.gp_motorspeed = GaugePanel(self.frame_gaugepanel)
        self.gp_motorspeed.setObjectName(u"gp_motorspeed")
        sizePolicy3.setHeightForWidth(self.gp_motorspeed.sizePolicy().hasHeightForWidth())
        self.gp_motorspeed.setSizePolicy(sizePolicy3)
        self.gp_motorspeed.setMinimumSize(QSize(210, 210))
        self.verticalLayout_17 = QVBoxLayout(self.gp_motorspeed)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(self.gp_motorspeed)
        self.label_2.setObjectName(u"label_2")
        font8 = QFont()
        font8.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font8.setPointSize(10)
        font8.setBold(True)
        font8.setWeight(75)
        self.label_2.setFont(font8)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_2)


        self.verticalLayout_16.addLayout(self.horizontalLayout_20)


        self.verticalLayout_17.addLayout(self.verticalLayout_16)


        self.horizontalLayout_24.addWidget(self.gp_motorspeed)

        self.gp_velocity = GaugePanel(self.frame_gaugepanel)
        self.gp_velocity.setObjectName(u"gp_velocity")
        sizePolicy3.setHeightForWidth(self.gp_velocity.sizePolicy().hasHeightForWidth())
        self.gp_velocity.setSizePolicy(sizePolicy3)
        self.gp_velocity.setMinimumSize(QSize(210, 210))
        self.verticalLayout_18 = QVBoxLayout(self.gp_velocity)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_2)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_3)

        self.label_3 = QLabel(self.gp_velocity)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font8)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.label_3)

        self.horizontalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_4)


        self.verticalLayout_19.addLayout(self.horizontalLayout_21)


        self.verticalLayout_18.addLayout(self.verticalLayout_19)


        self.horizontalLayout_24.addWidget(self.gp_velocity)

        self.gp_motortorque = GaugePanel(self.frame_gaugepanel)
        self.gp_motortorque.setObjectName(u"gp_motortorque")
        sizePolicy3.setHeightForWidth(self.gp_motortorque.sizePolicy().hasHeightForWidth())
        self.gp_motortorque.setSizePolicy(sizePolicy3)
        self.gp_motortorque.setMinimumSize(QSize(210, 210))
        self.verticalLayout_20 = QVBoxLayout(self.gp_motortorque)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_3)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_5)

        self.label_4 = QLabel(self.gp_motortorque)
        self.label_4.setObjectName(u"label_4")
        sizePolicy3.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy3)
        self.label_4.setFont(font8)
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.label_4)

        self.horizontalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_6)


        self.verticalLayout_21.addLayout(self.horizontalLayout_22)


        self.verticalLayout_20.addLayout(self.verticalLayout_21)


        self.horizontalLayout_24.addWidget(self.gp_motortorque)

        self.gp_vcutorque = GaugePanel(self.frame_gaugepanel)
        self.gp_vcutorque.setObjectName(u"gp_vcutorque")
        sizePolicy3.setHeightForWidth(self.gp_vcutorque.sizePolicy().hasHeightForWidth())
        self.gp_vcutorque.setSizePolicy(sizePolicy3)
        self.gp_vcutorque.setMinimumSize(QSize(210, 210))
        self.verticalLayout_30 = QVBoxLayout(self.gp_vcutorque)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_31.addItem(self.verticalSpacer_4)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalSpacer_9 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_9)

        self.label_14 = QLabel(self.gp_vcutorque)
        self.label_14.setObjectName(u"label_14")
        sizePolicy3.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy3)
        self.label_14.setFont(font8)
        self.label_14.setScaledContents(True)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.label_14)

        self.horizontalSpacer_10 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_10)


        self.verticalLayout_31.addLayout(self.horizontalLayout_23)


        self.verticalLayout_30.addLayout(self.verticalLayout_31)


        self.horizontalLayout_24.addWidget(self.gp_vcutorque)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_8)


        self.verticalLayout_14.addWidget(self.frame_gaugepanel)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(10)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.frame_6 = QFrame(self.page_panel)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 340))
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.frame_6.setLineWidth(1)
        self.verticalLayout_32 = QVBoxLayout(self.frame_6)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(10, 0, 10, 0)
        self.verticalSpacer_5 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_32.addItem(self.verticalSpacer_5)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setSpacing(5)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 0))
        self.label_5.setMaximumSize(QSize(16777215, 14))
        self.label_5.setFont(font1)

        self.verticalLayout_22.addWidget(self.label_5)

        self.pb_soc = ProgressBar(self.frame_6)
        self.pb_soc.setObjectName(u"pb_soc")
        sizePolicy1.setHeightForWidth(self.pb_soc.sizePolicy().hasHeightForWidth())
        self.pb_soc.setSizePolicy(sizePolicy1)
        self.pb_soc.setMinimumSize(QSize(0, 20))
        self.pb_soc.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_22.addWidget(self.pb_soc)


        self.verticalLayout_32.addLayout(self.verticalLayout_22)

        self.verticalSpacer_6 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_32.addItem(self.verticalSpacer_6)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setSpacing(5)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_8 = QLabel(self.frame_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 0))
        self.label_8.setMaximumSize(QSize(16777215, 14))
        self.label_8.setFont(font1)

        self.verticalLayout_23.addWidget(self.label_8)

        self.pb_mcu1temp = ProgressBar(self.frame_6)
        self.pb_mcu1temp.setObjectName(u"pb_mcu1temp")
        sizePolicy1.setHeightForWidth(self.pb_mcu1temp.sizePolicy().hasHeightForWidth())
        self.pb_mcu1temp.setSizePolicy(sizePolicy1)
        self.pb_mcu1temp.setMinimumSize(QSize(0, 20))
        self.pb_mcu1temp.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_23.addWidget(self.pb_mcu1temp)


        self.verticalLayout_32.addLayout(self.verticalLayout_23)

        self.verticalSpacer_7 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_32.addItem(self.verticalSpacer_7)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setSpacing(5)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_9 = QLabel(self.frame_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 0))
        self.label_9.setMaximumSize(QSize(16777215, 14))
        self.label_9.setFont(font1)

        self.verticalLayout_24.addWidget(self.label_9)

        self.pb_motor1temp = ProgressBar(self.frame_6)
        self.pb_motor1temp.setObjectName(u"pb_motor1temp")
        sizePolicy1.setHeightForWidth(self.pb_motor1temp.sizePolicy().hasHeightForWidth())
        self.pb_motor1temp.setSizePolicy(sizePolicy1)
        self.pb_motor1temp.setMinimumSize(QSize(0, 20))
        self.pb_motor1temp.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_24.addWidget(self.pb_motor1temp)


        self.verticalLayout_32.addLayout(self.verticalLayout_24)

        self.verticalSpacer_8 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_32.addItem(self.verticalSpacer_8)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setSpacing(5)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_10 = QLabel(self.frame_6)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 0))
        self.label_10.setMaximumSize(QSize(16777215, 14))
        self.label_10.setFont(font1)

        self.verticalLayout_25.addWidget(self.label_10)

        self.pb_mcu2temp = ProgressBar(self.frame_6)
        self.pb_mcu2temp.setObjectName(u"pb_mcu2temp")
        sizePolicy1.setHeightForWidth(self.pb_mcu2temp.sizePolicy().hasHeightForWidth())
        self.pb_mcu2temp.setSizePolicy(sizePolicy1)
        self.pb_mcu2temp.setMinimumSize(QSize(0, 20))
        self.pb_mcu2temp.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_25.addWidget(self.pb_mcu2temp)


        self.verticalLayout_32.addLayout(self.verticalLayout_25)

        self.verticalSpacer_9 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_32.addItem(self.verticalSpacer_9)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setSpacing(5)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_11 = QLabel(self.frame_6)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(0, 0))
        self.label_11.setMaximumSize(QSize(16777215, 14))
        self.label_11.setFont(font1)

        self.verticalLayout_26.addWidget(self.label_11)

        self.pb_motor2temp = ProgressBar(self.frame_6)
        self.pb_motor2temp.setObjectName(u"pb_motor2temp")
        sizePolicy1.setHeightForWidth(self.pb_motor2temp.sizePolicy().hasHeightForWidth())
        self.pb_motor2temp.setSizePolicy(sizePolicy1)
        self.pb_motor2temp.setMinimumSize(QSize(0, 20))
        self.pb_motor2temp.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_26.addWidget(self.pb_motor2temp)


        self.verticalLayout_32.addLayout(self.verticalLayout_26)

        self.verticalSpacer_10 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_32.addItem(self.verticalSpacer_10)

        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setSpacing(5)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_13 = QLabel(self.frame_6)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(0, 0))
        self.label_13.setMaximumSize(QSize(16777215, 14))
        self.label_13.setFont(font1)

        self.verticalLayout_28.addWidget(self.label_13)

        self.pb_airpressure1 = ProgressBar(self.frame_6)
        self.pb_airpressure1.setObjectName(u"pb_airpressure1")
        sizePolicy1.setHeightForWidth(self.pb_airpressure1.sizePolicy().hasHeightForWidth())
        self.pb_airpressure1.setSizePolicy(sizePolicy1)
        self.pb_airpressure1.setMinimumSize(QSize(0, 20))
        self.pb_airpressure1.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_28.addWidget(self.pb_airpressure1)


        self.verticalLayout_32.addLayout(self.verticalLayout_28)

        self.verticalSpacer_11 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_32.addItem(self.verticalSpacer_11)

        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setSpacing(5)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_15 = QLabel(self.frame_6)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(0, 0))
        self.label_15.setMaximumSize(QSize(16777215, 14))
        self.label_15.setFont(font1)

        self.verticalLayout_29.addWidget(self.label_15)

        self.pb_airpressure2 = ProgressBar(self.frame_6)
        self.pb_airpressure2.setObjectName(u"pb_airpressure2")
        sizePolicy1.setHeightForWidth(self.pb_airpressure2.sizePolicy().hasHeightForWidth())
        self.pb_airpressure2.setSizePolicy(sizePolicy1)
        self.pb_airpressure2.setMinimumSize(QSize(0, 20))
        self.pb_airpressure2.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_29.addWidget(self.pb_airpressure2)


        self.verticalLayout_32.addLayout(self.verticalLayout_29)

        self.verticalSpacer_12 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_32.addItem(self.verticalSpacer_12)


        self.horizontalLayout_14.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.page_panel)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 340))
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_45.setSpacing(0)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 10, 0, 10)
        self.horizontalSpacer_14 = QSpacerItem(31, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer_14)

        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setSpacing(10)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setSpacing(10)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_26 = QLabel(self.frame_7)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMaximumSize(QSize(16777215, 20))
        self.label_26.setFont(font1)

        self.horizontalLayout_25.addWidget(self.label_26)

        self.il_vculife = IndicatorLight(self.frame_7)
        self.il_vculife.setObjectName(u"il_vculife")
        sizePolicy3.setHeightForWidth(self.il_vculife.sizePolicy().hasHeightForWidth())
        self.il_vculife.setSizePolicy(sizePolicy3)
        self.il_vculife.setMinimumSize(QSize(25, 25))
        self.il_vculife.setMaximumSize(QSize(25, 25))
        self.il_vculife.setStyleSheet(u"background-color:white")

        self.horizontalLayout_25.addWidget(self.il_vculife)


        self.verticalLayout_27.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setSpacing(10)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_25 = QLabel(self.frame_7)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMaximumSize(QSize(16777215, 20))
        self.label_25.setFont(font1)

        self.horizontalLayout_26.addWidget(self.label_25)

        self.il_mculife = IndicatorLight(self.frame_7)
        self.il_mculife.setObjectName(u"il_mculife")
        sizePolicy3.setHeightForWidth(self.il_mculife.sizePolicy().hasHeightForWidth())
        self.il_mculife.setSizePolicy(sizePolicy3)
        self.il_mculife.setMinimumSize(QSize(25, 25))
        self.il_mculife.setMaximumSize(QSize(25, 25))
        self.il_mculife.setStyleSheet(u"background-color:white")

        self.horizontalLayout_26.addWidget(self.il_mculife)


        self.verticalLayout_27.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setSpacing(10)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_28 = QLabel(self.frame_7)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMaximumSize(QSize(16777215, 20))
        self.label_28.setFont(font1)

        self.horizontalLayout_27.addWidget(self.label_28)

        self.il_bmslife = IndicatorLight(self.frame_7)
        self.il_bmslife.setObjectName(u"il_bmslife")
        sizePolicy3.setHeightForWidth(self.il_bmslife.sizePolicy().hasHeightForWidth())
        self.il_bmslife.setSizePolicy(sizePolicy3)
        self.il_bmslife.setMinimumSize(QSize(25, 25))
        self.il_bmslife.setMaximumSize(QSize(25, 25))
        self.il_bmslife.setStyleSheet(u"background-color:white")

        self.horizontalLayout_27.addWidget(self.il_bmslife)


        self.verticalLayout_27.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setSpacing(10)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_27 = QLabel(self.frame_7)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMaximumSize(QSize(16777215, 20))
        self.label_27.setFont(font1)

        self.horizontalLayout_28.addWidget(self.label_27)

        self.il_dcdclife = IndicatorLight(self.frame_7)
        self.il_dcdclife.setObjectName(u"il_dcdclife")
        sizePolicy3.setHeightForWidth(self.il_dcdclife.sizePolicy().hasHeightForWidth())
        self.il_dcdclife.setSizePolicy(sizePolicy3)
        self.il_dcdclife.setMinimumSize(QSize(25, 25))
        self.il_dcdclife.setMaximumSize(QSize(25, 25))
        self.il_dcdclife.setStyleSheet(u"background-color:white")

        self.horizontalLayout_28.addWidget(self.il_dcdclife)


        self.verticalLayout_27.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setSpacing(10)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_32 = QLabel(self.frame_7)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMaximumSize(QSize(16777215, 20))
        self.label_32.setFont(font1)

        self.horizontalLayout_29.addWidget(self.label_32)

        self.il_lvoplife = IndicatorLight(self.frame_7)
        self.il_lvoplife.setObjectName(u"il_lvoplife")
        sizePolicy3.setHeightForWidth(self.il_lvoplife.sizePolicy().hasHeightForWidth())
        self.il_lvoplife.setSizePolicy(sizePolicy3)
        self.il_lvoplife.setMinimumSize(QSize(25, 25))
        self.il_lvoplife.setMaximumSize(QSize(25, 25))
        self.il_lvoplife.setStyleSheet(u"background-color:white")

        self.horizontalLayout_29.addWidget(self.il_lvoplife)


        self.verticalLayout_27.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setSpacing(10)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_30 = QLabel(self.frame_7)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMaximumSize(QSize(16777215, 20))
        self.label_30.setFont(font1)

        self.horizontalLayout_30.addWidget(self.label_30)

        self.il_hvoplife = IndicatorLight(self.frame_7)
        self.il_hvoplife.setObjectName(u"il_hvoplife")
        sizePolicy3.setHeightForWidth(self.il_hvoplife.sizePolicy().hasHeightForWidth())
        self.il_hvoplife.setSizePolicy(sizePolicy3)
        self.il_hvoplife.setMinimumSize(QSize(25, 25))
        self.il_hvoplife.setMaximumSize(QSize(25, 25))
        self.il_hvoplife.setStyleSheet(u"background-color:white")

        self.horizontalLayout_30.addWidget(self.il_hvoplife)


        self.verticalLayout_27.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setSpacing(10)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_29 = QLabel(self.frame_7)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMaximumSize(QSize(16777215, 20))
        self.label_29.setFont(font1)

        self.horizontalLayout_31.addWidget(self.label_29)

        self.il_hvaplife = IndicatorLight(self.frame_7)
        self.il_hvaplife.setObjectName(u"il_hvaplife")
        sizePolicy3.setHeightForWidth(self.il_hvaplife.sizePolicy().hasHeightForWidth())
        self.il_hvaplife.setSizePolicy(sizePolicy3)
        self.il_hvaplife.setMinimumSize(QSize(25, 25))
        self.il_hvaplife.setMaximumSize(QSize(25, 25))
        self.il_hvaplife.setStyleSheet(u"background-color:white")

        self.horizontalLayout_31.addWidget(self.il_hvaplife)


        self.verticalLayout_27.addLayout(self.horizontalLayout_31)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setSpacing(10)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_31 = QLabel(self.frame_7)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMaximumSize(QSize(16777215, 20))
        self.label_31.setFont(font1)

        self.horizontalLayout_32.addWidget(self.label_31)

        self.il_abslife = IndicatorLight(self.frame_7)
        self.il_abslife.setObjectName(u"il_abslife")
        sizePolicy3.setHeightForWidth(self.il_abslife.sizePolicy().hasHeightForWidth())
        self.il_abslife.setSizePolicy(sizePolicy3)
        self.il_abslife.setMinimumSize(QSize(25, 25))
        self.il_abslife.setMaximumSize(QSize(25, 25))
        self.il_abslife.setStyleSheet(u"background-color:white")

        self.horizontalLayout_32.addWidget(self.il_abslife)


        self.verticalLayout_27.addLayout(self.horizontalLayout_32)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setSpacing(10)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_33 = QLabel(self.frame_7)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMaximumSize(QSize(16777215, 20))
        self.label_33.setFont(font1)

        self.horizontalLayout_33.addWidget(self.label_33)

        self.il_epblife = IndicatorLight(self.frame_7)
        self.il_epblife.setObjectName(u"il_epblife")
        sizePolicy3.setHeightForWidth(self.il_epblife.sizePolicy().hasHeightForWidth())
        self.il_epblife.setSizePolicy(sizePolicy3)
        self.il_epblife.setMinimumSize(QSize(25, 25))
        self.il_epblife.setMaximumSize(QSize(25, 25))
        self.il_epblife.setStyleSheet(u"background-color:white")

        self.horizontalLayout_33.addWidget(self.il_epblife)


        self.verticalLayout_27.addLayout(self.horizontalLayout_33)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setSpacing(10)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_34 = QLabel(self.frame_7)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMaximumSize(QSize(16777215, 20))
        self.label_34.setFont(font1)

        self.horizontalLayout_34.addWidget(self.label_34)

        self.il_saslife = IndicatorLight(self.frame_7)
        self.il_saslife.setObjectName(u"il_saslife")
        sizePolicy3.setHeightForWidth(self.il_saslife.sizePolicy().hasHeightForWidth())
        self.il_saslife.setSizePolicy(sizePolicy3)
        self.il_saslife.setMinimumSize(QSize(25, 25))
        self.il_saslife.setMaximumSize(QSize(25, 25))
        self.il_saslife.setStyleSheet(u"background-color:white")

        self.horizontalLayout_34.addWidget(self.il_saslife)


        self.verticalLayout_27.addLayout(self.horizontalLayout_34)


        self.horizontalLayout_45.addLayout(self.verticalLayout_27)

        self.horizontalSpacer_15 = QSpacerItem(30, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer_15)

        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setSpacing(10)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setSpacing(10)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_35 = QLabel(self.frame_7)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMaximumSize(QSize(16777215, 20))
        self.label_35.setFont(font1)

        self.horizontalLayout_35.addWidget(self.label_35)

        self.widget_26 = IndicatorLight(self.frame_7)
        self.widget_26.setObjectName(u"widget_26")
        sizePolicy3.setHeightForWidth(self.widget_26.sizePolicy().hasHeightForWidth())
        self.widget_26.setSizePolicy(sizePolicy3)
        self.widget_26.setMinimumSize(QSize(25, 25))
        self.widget_26.setMaximumSize(QSize(25, 25))
        self.widget_26.setStyleSheet(u"background-color:white")

        self.horizontalLayout_35.addWidget(self.widget_26)


        self.verticalLayout_33.addLayout(self.horizontalLayout_35)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setSpacing(10)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_36 = QLabel(self.frame_7)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMaximumSize(QSize(16777215, 20))
        self.label_36.setFont(font1)

        self.horizontalLayout_36.addWidget(self.label_36)

        self.widget_27 = IndicatorLight(self.frame_7)
        self.widget_27.setObjectName(u"widget_27")
        sizePolicy3.setHeightForWidth(self.widget_27.sizePolicy().hasHeightForWidth())
        self.widget_27.setSizePolicy(sizePolicy3)
        self.widget_27.setMinimumSize(QSize(25, 25))
        self.widget_27.setMaximumSize(QSize(25, 25))
        self.widget_27.setStyleSheet(u"background-color:white")

        self.horizontalLayout_36.addWidget(self.widget_27)


        self.verticalLayout_33.addLayout(self.horizontalLayout_36)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setSpacing(10)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label_37 = QLabel(self.frame_7)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMaximumSize(QSize(16777215, 20))
        self.label_37.setFont(font1)

        self.horizontalLayout_37.addWidget(self.label_37)

        self.widget_28 = IndicatorLight(self.frame_7)
        self.widget_28.setObjectName(u"widget_28")
        sizePolicy3.setHeightForWidth(self.widget_28.sizePolicy().hasHeightForWidth())
        self.widget_28.setSizePolicy(sizePolicy3)
        self.widget_28.setMinimumSize(QSize(25, 25))
        self.widget_28.setMaximumSize(QSize(25, 25))
        self.widget_28.setStyleSheet(u"background-color:white")

        self.horizontalLayout_37.addWidget(self.widget_28)


        self.verticalLayout_33.addLayout(self.horizontalLayout_37)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setSpacing(10)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.label_38 = QLabel(self.frame_7)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMaximumSize(QSize(16777215, 20))
        self.label_38.setFont(font1)

        self.horizontalLayout_38.addWidget(self.label_38)

        self.widget_29 = IndicatorLight(self.frame_7)
        self.widget_29.setObjectName(u"widget_29")
        sizePolicy3.setHeightForWidth(self.widget_29.sizePolicy().hasHeightForWidth())
        self.widget_29.setSizePolicy(sizePolicy3)
        self.widget_29.setMinimumSize(QSize(25, 25))
        self.widget_29.setMaximumSize(QSize(25, 25))
        self.widget_29.setStyleSheet(u"background-color:white")

        self.horizontalLayout_38.addWidget(self.widget_29)


        self.verticalLayout_33.addLayout(self.horizontalLayout_38)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setSpacing(10)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.label_39 = QLabel(self.frame_7)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMaximumSize(QSize(16777215, 20))
        self.label_39.setFont(font1)

        self.horizontalLayout_39.addWidget(self.label_39)

        self.widget_30 = IndicatorLight(self.frame_7)
        self.widget_30.setObjectName(u"widget_30")
        sizePolicy3.setHeightForWidth(self.widget_30.sizePolicy().hasHeightForWidth())
        self.widget_30.setSizePolicy(sizePolicy3)
        self.widget_30.setMinimumSize(QSize(25, 25))
        self.widget_30.setMaximumSize(QSize(25, 25))
        self.widget_30.setStyleSheet(u"background-color:white")

        self.horizontalLayout_39.addWidget(self.widget_30)


        self.verticalLayout_33.addLayout(self.horizontalLayout_39)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setSpacing(10)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.label_40 = QLabel(self.frame_7)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMaximumSize(QSize(16777215, 20))
        self.label_40.setFont(font1)

        self.horizontalLayout_40.addWidget(self.label_40)

        self.widget_31 = IndicatorLight(self.frame_7)
        self.widget_31.setObjectName(u"widget_31")
        sizePolicy3.setHeightForWidth(self.widget_31.sizePolicy().hasHeightForWidth())
        self.widget_31.setSizePolicy(sizePolicy3)
        self.widget_31.setMinimumSize(QSize(25, 25))
        self.widget_31.setMaximumSize(QSize(25, 25))
        self.widget_31.setStyleSheet(u"background-color:white")

        self.horizontalLayout_40.addWidget(self.widget_31)


        self.verticalLayout_33.addLayout(self.horizontalLayout_40)

        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setSpacing(10)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.label_41 = QLabel(self.frame_7)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMaximumSize(QSize(16777215, 20))
        self.label_41.setFont(font1)

        self.horizontalLayout_41.addWidget(self.label_41)

        self.widget_32 = IndicatorLight(self.frame_7)
        self.widget_32.setObjectName(u"widget_32")
        sizePolicy3.setHeightForWidth(self.widget_32.sizePolicy().hasHeightForWidth())
        self.widget_32.setSizePolicy(sizePolicy3)
        self.widget_32.setMinimumSize(QSize(25, 25))
        self.widget_32.setMaximumSize(QSize(25, 25))
        self.widget_32.setStyleSheet(u"background-color:white")

        self.horizontalLayout_41.addWidget(self.widget_32)


        self.verticalLayout_33.addLayout(self.horizontalLayout_41)

        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setSpacing(10)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.label_42 = QLabel(self.frame_7)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMaximumSize(QSize(16777215, 20))
        self.label_42.setFont(font1)

        self.horizontalLayout_42.addWidget(self.label_42)

        self.widget_33 = IndicatorLight(self.frame_7)
        self.widget_33.setObjectName(u"widget_33")
        sizePolicy3.setHeightForWidth(self.widget_33.sizePolicy().hasHeightForWidth())
        self.widget_33.setSizePolicy(sizePolicy3)
        self.widget_33.setMinimumSize(QSize(25, 25))
        self.widget_33.setMaximumSize(QSize(25, 25))
        self.widget_33.setStyleSheet(u"background-color:white")

        self.horizontalLayout_42.addWidget(self.widget_33)


        self.verticalLayout_33.addLayout(self.horizontalLayout_42)

        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setSpacing(10)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.label_43 = QLabel(self.frame_7)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMaximumSize(QSize(16777215, 20))
        self.label_43.setFont(font1)

        self.horizontalLayout_43.addWidget(self.label_43)

        self.widget_34 = IndicatorLight(self.frame_7)
        self.widget_34.setObjectName(u"widget_34")
        sizePolicy3.setHeightForWidth(self.widget_34.sizePolicy().hasHeightForWidth())
        self.widget_34.setSizePolicy(sizePolicy3)
        self.widget_34.setMinimumSize(QSize(25, 25))
        self.widget_34.setMaximumSize(QSize(25, 25))
        self.widget_34.setStyleSheet(u"background-color:white")

        self.horizontalLayout_43.addWidget(self.widget_34)


        self.verticalLayout_33.addLayout(self.horizontalLayout_43)

        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setSpacing(10)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.label_44 = QLabel(self.frame_7)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMaximumSize(QSize(16777215, 20))
        self.label_44.setFont(font1)

        self.horizontalLayout_44.addWidget(self.label_44)

        self.widget_35 = IndicatorLight(self.frame_7)
        self.widget_35.setObjectName(u"widget_35")
        sizePolicy3.setHeightForWidth(self.widget_35.sizePolicy().hasHeightForWidth())
        self.widget_35.setSizePolicy(sizePolicy3)
        self.widget_35.setMinimumSize(QSize(25, 25))
        self.widget_35.setMaximumSize(QSize(25, 25))
        self.widget_35.setStyleSheet(u"background-color:white")

        self.horizontalLayout_44.addWidget(self.widget_35)


        self.verticalLayout_33.addLayout(self.horizontalLayout_44)


        self.horizontalLayout_45.addLayout(self.verticalLayout_33)

        self.horizontalSpacer_13 = QSpacerItem(31, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer_13)

        self.verticalLayout_34 = QVBoxLayout()
        self.verticalLayout_34.setSpacing(10)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setSpacing(10)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.label_45 = QLabel(self.frame_7)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMaximumSize(QSize(16777215, 20))
        self.label_45.setFont(font1)

        self.horizontalLayout_46.addWidget(self.label_45)

        self.widget_36 = IndicatorLight(self.frame_7)
        self.widget_36.setObjectName(u"widget_36")
        sizePolicy3.setHeightForWidth(self.widget_36.sizePolicy().hasHeightForWidth())
        self.widget_36.setSizePolicy(sizePolicy3)
        self.widget_36.setMinimumSize(QSize(25, 25))
        self.widget_36.setMaximumSize(QSize(25, 25))
        self.widget_36.setStyleSheet(u"background-color:white")

        self.horizontalLayout_46.addWidget(self.widget_36)


        self.verticalLayout_34.addLayout(self.horizontalLayout_46)

        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setSpacing(10)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.label_46 = QLabel(self.frame_7)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMaximumSize(QSize(16777215, 20))
        self.label_46.setFont(font1)

        self.horizontalLayout_47.addWidget(self.label_46)

        self.widget_37 = IndicatorLight(self.frame_7)
        self.widget_37.setObjectName(u"widget_37")
        sizePolicy3.setHeightForWidth(self.widget_37.sizePolicy().hasHeightForWidth())
        self.widget_37.setSizePolicy(sizePolicy3)
        self.widget_37.setMinimumSize(QSize(25, 25))
        self.widget_37.setMaximumSize(QSize(25, 25))
        self.widget_37.setStyleSheet(u"background-color:white")

        self.horizontalLayout_47.addWidget(self.widget_37)


        self.verticalLayout_34.addLayout(self.horizontalLayout_47)

        self.horizontalLayout_48 = QHBoxLayout()
        self.horizontalLayout_48.setSpacing(10)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.label_47 = QLabel(self.frame_7)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setMaximumSize(QSize(16777215, 20))
        self.label_47.setFont(font1)

        self.horizontalLayout_48.addWidget(self.label_47)

        self.widget_38 = IndicatorLight(self.frame_7)
        self.widget_38.setObjectName(u"widget_38")
        sizePolicy3.setHeightForWidth(self.widget_38.sizePolicy().hasHeightForWidth())
        self.widget_38.setSizePolicy(sizePolicy3)
        self.widget_38.setMinimumSize(QSize(25, 25))
        self.widget_38.setMaximumSize(QSize(25, 25))
        self.widget_38.setStyleSheet(u"background-color:white")

        self.horizontalLayout_48.addWidget(self.widget_38)


        self.verticalLayout_34.addLayout(self.horizontalLayout_48)

        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setSpacing(10)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.label_48 = QLabel(self.frame_7)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMaximumSize(QSize(16777215, 20))
        self.label_48.setFont(font1)

        self.horizontalLayout_49.addWidget(self.label_48)

        self.widget_39 = IndicatorLight(self.frame_7)
        self.widget_39.setObjectName(u"widget_39")
        sizePolicy3.setHeightForWidth(self.widget_39.sizePolicy().hasHeightForWidth())
        self.widget_39.setSizePolicy(sizePolicy3)
        self.widget_39.setMinimumSize(QSize(25, 25))
        self.widget_39.setMaximumSize(QSize(25, 25))
        self.widget_39.setStyleSheet(u"background-color:white")

        self.horizontalLayout_49.addWidget(self.widget_39)


        self.verticalLayout_34.addLayout(self.horizontalLayout_49)

        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setSpacing(10)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.label_49 = QLabel(self.frame_7)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setMaximumSize(QSize(16777215, 20))
        self.label_49.setFont(font1)

        self.horizontalLayout_50.addWidget(self.label_49)

        self.widget_40 = IndicatorLight(self.frame_7)
        self.widget_40.setObjectName(u"widget_40")
        sizePolicy3.setHeightForWidth(self.widget_40.sizePolicy().hasHeightForWidth())
        self.widget_40.setSizePolicy(sizePolicy3)
        self.widget_40.setMinimumSize(QSize(25, 25))
        self.widget_40.setMaximumSize(QSize(25, 25))
        self.widget_40.setStyleSheet(u"background-color:white")

        self.horizontalLayout_50.addWidget(self.widget_40)


        self.verticalLayout_34.addLayout(self.horizontalLayout_50)

        self.horizontalLayout_51 = QHBoxLayout()
        self.horizontalLayout_51.setSpacing(10)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.label_50 = QLabel(self.frame_7)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setMaximumSize(QSize(16777215, 20))
        self.label_50.setFont(font1)

        self.horizontalLayout_51.addWidget(self.label_50)

        self.widget_41 = IndicatorLight(self.frame_7)
        self.widget_41.setObjectName(u"widget_41")
        sizePolicy3.setHeightForWidth(self.widget_41.sizePolicy().hasHeightForWidth())
        self.widget_41.setSizePolicy(sizePolicy3)
        self.widget_41.setMinimumSize(QSize(25, 25))
        self.widget_41.setMaximumSize(QSize(25, 25))
        self.widget_41.setStyleSheet(u"background-color:white")

        self.horizontalLayout_51.addWidget(self.widget_41)


        self.verticalLayout_34.addLayout(self.horizontalLayout_51)

        self.horizontalLayout_52 = QHBoxLayout()
        self.horizontalLayout_52.setSpacing(10)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.label_51 = QLabel(self.frame_7)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setMaximumSize(QSize(16777215, 20))
        self.label_51.setFont(font1)

        self.horizontalLayout_52.addWidget(self.label_51)

        self.widget_42 = IndicatorLight(self.frame_7)
        self.widget_42.setObjectName(u"widget_42")
        sizePolicy3.setHeightForWidth(self.widget_42.sizePolicy().hasHeightForWidth())
        self.widget_42.setSizePolicy(sizePolicy3)
        self.widget_42.setMinimumSize(QSize(25, 25))
        self.widget_42.setMaximumSize(QSize(25, 25))
        self.widget_42.setStyleSheet(u"background-color:white")

        self.horizontalLayout_52.addWidget(self.widget_42)


        self.verticalLayout_34.addLayout(self.horizontalLayout_52)

        self.horizontalLayout_53 = QHBoxLayout()
        self.horizontalLayout_53.setSpacing(10)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.label_52 = QLabel(self.frame_7)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setMaximumSize(QSize(16777215, 20))
        self.label_52.setFont(font1)

        self.horizontalLayout_53.addWidget(self.label_52)

        self.widget_43 = IndicatorLight(self.frame_7)
        self.widget_43.setObjectName(u"widget_43")
        sizePolicy3.setHeightForWidth(self.widget_43.sizePolicy().hasHeightForWidth())
        self.widget_43.setSizePolicy(sizePolicy3)
        self.widget_43.setMinimumSize(QSize(25, 25))
        self.widget_43.setMaximumSize(QSize(25, 25))
        self.widget_43.setStyleSheet(u"background-color:white")

        self.horizontalLayout_53.addWidget(self.widget_43)


        self.verticalLayout_34.addLayout(self.horizontalLayout_53)

        self.horizontalLayout_54 = QHBoxLayout()
        self.horizontalLayout_54.setSpacing(10)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.label_53 = QLabel(self.frame_7)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setMaximumSize(QSize(16777215, 20))
        self.label_53.setFont(font1)

        self.horizontalLayout_54.addWidget(self.label_53)

        self.widget_44 = IndicatorLight(self.frame_7)
        self.widget_44.setObjectName(u"widget_44")
        sizePolicy3.setHeightForWidth(self.widget_44.sizePolicy().hasHeightForWidth())
        self.widget_44.setSizePolicy(sizePolicy3)
        self.widget_44.setMinimumSize(QSize(25, 25))
        self.widget_44.setMaximumSize(QSize(25, 25))
        self.widget_44.setStyleSheet(u"background-color:white")

        self.horizontalLayout_54.addWidget(self.widget_44)


        self.verticalLayout_34.addLayout(self.horizontalLayout_54)

        self.horizontalLayout_55 = QHBoxLayout()
        self.horizontalLayout_55.setSpacing(10)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.label_54 = QLabel(self.frame_7)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setMaximumSize(QSize(16777215, 20))
        self.label_54.setFont(font1)

        self.horizontalLayout_55.addWidget(self.label_54)

        self.widget_45 = IndicatorLight(self.frame_7)
        self.widget_45.setObjectName(u"widget_45")
        sizePolicy3.setHeightForWidth(self.widget_45.sizePolicy().hasHeightForWidth())
        self.widget_45.setSizePolicy(sizePolicy3)
        self.widget_45.setMinimumSize(QSize(25, 25))
        self.widget_45.setMaximumSize(QSize(25, 25))
        self.widget_45.setStyleSheet(u"background-color:white")

        self.horizontalLayout_55.addWidget(self.widget_45)


        self.verticalLayout_34.addLayout(self.horizontalLayout_55)


        self.horizontalLayout_45.addLayout(self.verticalLayout_34)

        self.horizontalSpacer_12 = QSpacerItem(30, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer_12)

        self.verticalLayout_35 = QVBoxLayout()
        self.verticalLayout_35.setSpacing(10)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.horizontalLayout_56 = QHBoxLayout()
        self.horizontalLayout_56.setSpacing(10)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.label_55 = QLabel(self.frame_7)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setMaximumSize(QSize(16777215, 20))
        self.label_55.setFont(font1)

        self.horizontalLayout_56.addWidget(self.label_55)

        self.widget_46 = IndicatorLight(self.frame_7)
        self.widget_46.setObjectName(u"widget_46")
        sizePolicy3.setHeightForWidth(self.widget_46.sizePolicy().hasHeightForWidth())
        self.widget_46.setSizePolicy(sizePolicy3)
        self.widget_46.setMinimumSize(QSize(25, 25))
        self.widget_46.setMaximumSize(QSize(25, 25))
        self.widget_46.setStyleSheet(u"background-color:white")

        self.horizontalLayout_56.addWidget(self.widget_46)


        self.verticalLayout_35.addLayout(self.horizontalLayout_56)

        self.horizontalLayout_57 = QHBoxLayout()
        self.horizontalLayout_57.setSpacing(10)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.label_56 = QLabel(self.frame_7)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setMaximumSize(QSize(16777215, 20))
        self.label_56.setFont(font1)

        self.horizontalLayout_57.addWidget(self.label_56)

        self.widget_47 = IndicatorLight(self.frame_7)
        self.widget_47.setObjectName(u"widget_47")
        sizePolicy3.setHeightForWidth(self.widget_47.sizePolicy().hasHeightForWidth())
        self.widget_47.setSizePolicy(sizePolicy3)
        self.widget_47.setMinimumSize(QSize(25, 25))
        self.widget_47.setMaximumSize(QSize(25, 25))
        self.widget_47.setStyleSheet(u"background-color:white")

        self.horizontalLayout_57.addWidget(self.widget_47)


        self.verticalLayout_35.addLayout(self.horizontalLayout_57)

        self.horizontalLayout_58 = QHBoxLayout()
        self.horizontalLayout_58.setSpacing(10)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.label_57 = QLabel(self.frame_7)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setMaximumSize(QSize(16777215, 20))
        self.label_57.setFont(font1)

        self.horizontalLayout_58.addWidget(self.label_57)

        self.widget_48 = IndicatorLight(self.frame_7)
        self.widget_48.setObjectName(u"widget_48")
        sizePolicy3.setHeightForWidth(self.widget_48.sizePolicy().hasHeightForWidth())
        self.widget_48.setSizePolicy(sizePolicy3)
        self.widget_48.setMinimumSize(QSize(25, 25))
        self.widget_48.setMaximumSize(QSize(25, 25))
        self.widget_48.setStyleSheet(u"background-color:white")

        self.horizontalLayout_58.addWidget(self.widget_48)


        self.verticalLayout_35.addLayout(self.horizontalLayout_58)

        self.horizontalLayout_59 = QHBoxLayout()
        self.horizontalLayout_59.setSpacing(10)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.label_58 = QLabel(self.frame_7)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setMaximumSize(QSize(16777215, 20))
        self.label_58.setFont(font1)

        self.horizontalLayout_59.addWidget(self.label_58)

        self.widget_49 = IndicatorLight(self.frame_7)
        self.widget_49.setObjectName(u"widget_49")
        sizePolicy3.setHeightForWidth(self.widget_49.sizePolicy().hasHeightForWidth())
        self.widget_49.setSizePolicy(sizePolicy3)
        self.widget_49.setMinimumSize(QSize(25, 25))
        self.widget_49.setMaximumSize(QSize(25, 25))
        self.widget_49.setStyleSheet(u"background-color:white")

        self.horizontalLayout_59.addWidget(self.widget_49)


        self.verticalLayout_35.addLayout(self.horizontalLayout_59)

        self.horizontalLayout_60 = QHBoxLayout()
        self.horizontalLayout_60.setSpacing(10)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.label_59 = QLabel(self.frame_7)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setMaximumSize(QSize(16777215, 20))
        self.label_59.setFont(font1)

        self.horizontalLayout_60.addWidget(self.label_59)

        self.widget_50 = IndicatorLight(self.frame_7)
        self.widget_50.setObjectName(u"widget_50")
        sizePolicy3.setHeightForWidth(self.widget_50.sizePolicy().hasHeightForWidth())
        self.widget_50.setSizePolicy(sizePolicy3)
        self.widget_50.setMinimumSize(QSize(25, 25))
        self.widget_50.setMaximumSize(QSize(25, 25))
        self.widget_50.setStyleSheet(u"background-color:white")

        self.horizontalLayout_60.addWidget(self.widget_50)


        self.verticalLayout_35.addLayout(self.horizontalLayout_60)

        self.horizontalLayout_61 = QHBoxLayout()
        self.horizontalLayout_61.setSpacing(10)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.label_60 = QLabel(self.frame_7)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setMaximumSize(QSize(16777215, 20))
        self.label_60.setFont(font1)

        self.horizontalLayout_61.addWidget(self.label_60)

        self.widget_51 = IndicatorLight(self.frame_7)
        self.widget_51.setObjectName(u"widget_51")
        sizePolicy3.setHeightForWidth(self.widget_51.sizePolicy().hasHeightForWidth())
        self.widget_51.setSizePolicy(sizePolicy3)
        self.widget_51.setMinimumSize(QSize(25, 25))
        self.widget_51.setMaximumSize(QSize(25, 25))
        self.widget_51.setStyleSheet(u"background-color:white")

        self.horizontalLayout_61.addWidget(self.widget_51)


        self.verticalLayout_35.addLayout(self.horizontalLayout_61)

        self.horizontalLayout_62 = QHBoxLayout()
        self.horizontalLayout_62.setSpacing(10)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.label_61 = QLabel(self.frame_7)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setMaximumSize(QSize(16777215, 20))
        self.label_61.setFont(font1)

        self.horizontalLayout_62.addWidget(self.label_61)

        self.widget_52 = IndicatorLight(self.frame_7)
        self.widget_52.setObjectName(u"widget_52")
        sizePolicy3.setHeightForWidth(self.widget_52.sizePolicy().hasHeightForWidth())
        self.widget_52.setSizePolicy(sizePolicy3)
        self.widget_52.setMinimumSize(QSize(25, 25))
        self.widget_52.setMaximumSize(QSize(25, 25))
        self.widget_52.setStyleSheet(u"background-color:white")

        self.horizontalLayout_62.addWidget(self.widget_52)


        self.verticalLayout_35.addLayout(self.horizontalLayout_62)

        self.horizontalLayout_63 = QHBoxLayout()
        self.horizontalLayout_63.setSpacing(10)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.label_62 = QLabel(self.frame_7)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setMaximumSize(QSize(16777215, 20))
        self.label_62.setFont(font1)

        self.horizontalLayout_63.addWidget(self.label_62)

        self.widget_53 = IndicatorLight(self.frame_7)
        self.widget_53.setObjectName(u"widget_53")
        sizePolicy3.setHeightForWidth(self.widget_53.sizePolicy().hasHeightForWidth())
        self.widget_53.setSizePolicy(sizePolicy3)
        self.widget_53.setMinimumSize(QSize(25, 25))
        self.widget_53.setMaximumSize(QSize(25, 25))
        self.widget_53.setStyleSheet(u"background-color:white")

        self.horizontalLayout_63.addWidget(self.widget_53)


        self.verticalLayout_35.addLayout(self.horizontalLayout_63)

        self.horizontalLayout_64 = QHBoxLayout()
        self.horizontalLayout_64.setSpacing(10)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.label_63 = QLabel(self.frame_7)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setMaximumSize(QSize(16777215, 20))
        self.label_63.setFont(font1)

        self.horizontalLayout_64.addWidget(self.label_63)

        self.widget_54 = IndicatorLight(self.frame_7)
        self.widget_54.setObjectName(u"widget_54")
        sizePolicy3.setHeightForWidth(self.widget_54.sizePolicy().hasHeightForWidth())
        self.widget_54.setSizePolicy(sizePolicy3)
        self.widget_54.setMinimumSize(QSize(25, 25))
        self.widget_54.setMaximumSize(QSize(25, 25))
        self.widget_54.setStyleSheet(u"background-color:white")

        self.horizontalLayout_64.addWidget(self.widget_54)


        self.verticalLayout_35.addLayout(self.horizontalLayout_64)

        self.horizontalLayout_65 = QHBoxLayout()
        self.horizontalLayout_65.setSpacing(10)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.label_64 = QLabel(self.frame_7)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setMaximumSize(QSize(16777215, 20))
        self.label_64.setFont(font1)

        self.horizontalLayout_65.addWidget(self.label_64)

        self.widget_55 = IndicatorLight(self.frame_7)
        self.widget_55.setObjectName(u"widget_55")
        sizePolicy3.setHeightForWidth(self.widget_55.sizePolicy().hasHeightForWidth())
        self.widget_55.setSizePolicy(sizePolicy3)
        self.widget_55.setMinimumSize(QSize(25, 25))
        self.widget_55.setMaximumSize(QSize(25, 25))
        self.widget_55.setStyleSheet(u"background-color:white")

        self.horizontalLayout_65.addWidget(self.widget_55)


        self.verticalLayout_35.addLayout(self.horizontalLayout_65)


        self.horizontalLayout_45.addLayout(self.verticalLayout_35)

        self.horizontalSpacer_11 = QSpacerItem(31, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer_11)


        self.horizontalLayout_14.addWidget(self.frame_7)

        self.horizontalLayout_14.setStretch(0, 9)
        self.horizontalLayout_14.setStretch(1, 20)

        self.verticalLayout_14.addLayout(self.horizontalLayout_14)

        self.verticalLayout_14.setStretch(0, 23)
        self.verticalLayout_14.setStretch(1, 60)
        self.stackedWidget.addWidget(self.page_panel)
        self.page_widgets = QWidget()
        self.page_widgets.setObjectName(u"page_widgets")
        self.verticalLayout_6 = QVBoxLayout(self.page_widgets)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame = QFrame(self.page_widgets)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border-radius: 5px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.frame)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setFont(font1)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_8.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_7.addWidget(self.frame_title_wid_1)

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
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.frame_content_wid_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 30))
        font9 = QFont()
        font9.setFamily(u"Segoe UI")
        font9.setPointSize(9)
        self.pushButton.setFont(font9)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/16x16/icons/16x16/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon3)

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        self.labelVersion_3.setObjectName(u"labelVersion_3")
        self.labelVersion_3.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.labelVersion_3.setLineWidth(1)
        self.labelVersion_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_3, 1, 0, 1, 2)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_7.addWidget(self.frame_content_wid_1)


        self.verticalLayout_15.addWidget(self.frame_div_content_1)


        self.verticalLayout_6.addWidget(self.frame)

        self.frame_2 = QFrame(self.page_widgets)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 150))
        self.frame_2.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox = QCheckBox(self.frame_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)

        self.radioButton = QRadioButton(self.frame_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.radioButton, 0, 1, 1, 1)

        self.verticalSlider = QSlider(self.frame_2)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setStyleSheet(u"")
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalSlider, 0, 2, 3, 1)

        self.verticalScrollBar = QScrollBar(self.frame_2)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.verticalScrollBar.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalScrollBar, 0, 4, 3, 1)

        self.scrollArea = QScrollArea(self.frame_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QScrollArea {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 222, 222))
        self.horizontalLayout_11 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.plainTextEdit = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(200, 200))
        self.plainTextEdit.setStyleSheet(u"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"}\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.horizontalLayout_11.addWidget(self.plainTextEdit)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 5, 3, 1)

        self.comboBox = QComboBox(self.frame_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font9)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.comboBox.setIconSize(QSize(16, 16))
        self.comboBox.setFrame(True)

        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 2)

        self.horizontalScrollBar = QScrollBar(self.frame_2)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        sizePolicy5.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar.setSizePolicy(sizePolicy5)
        self.horizontalScrollBar.setStyleSheet(u"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"")
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalScrollBar, 1, 3, 1, 1)

        self.commandLinkButton = QCommandLinkButton(self.frame_2)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setStyleSheet(u"QCommandLinkButton {	\n"
"	color: rgb(85, 170, 255);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(210, 210, 210);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(210, 210, 210);\n"
"	background-color: rgb(52, 58, 71);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/16x16/icons/16x16/cil-link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton.setIcon(icon4)

        self.gridLayout_2.addWidget(self.commandLinkButton, 1, 6, 1, 1)

        self.horizontalSlider = QSlider(self.frame_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setStyleSheet(u"")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider, 2, 0, 1, 2)


        self.verticalLayout_11.addLayout(self.gridLayout_2)


        self.verticalLayout_6.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.page_widgets)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 150))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.frame_3)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        if (self.tableWidget.rowCount() < 2):
            self.tableWidget.setRowCount(2)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem14)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        brush15 = QBrush(QColor(39, 44, 54, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush15)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush15)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush15)
        brush16 = QBrush(QColor(210, 210, 210, 128))
        brush16.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush16)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush15)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush15)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush15)
        brush17 = QBrush(QColor(210, 210, 210, 128))
        brush17.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush17)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush15)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush15)
        brush18 = QBrush(QColor(210, 210, 210, 128))
        brush18.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush18)
#endif
        self.tableWidget.setPalette(palette1)
        self.tableWidget.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(False)
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
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_12.addWidget(self.tableWidget)


        self.verticalLayout_6.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.page_widgets)

        self.verticalLayout_9.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.frame_content)

        self.frame_grip = QFrame(self.frame_content_right)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(0, 25))
        self.frame_grip.setMaximumSize(QSize(16777215, 25))
        self.frame_grip.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_grip.setFrameShape(QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_grip)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 2, 0)
        self.frame_label_bottom = QFrame(self.frame_grip)
        self.frame_label_bottom.setObjectName(u"frame_label_bottom")
        self.frame_label_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.label_credits = QLabel(self.frame_label_bottom)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setFont(font2)
        self.label_credits.setStyleSheet(u"color: rgb(98, 103, 111);")

        self.horizontalLayout_7.addWidget(self.label_credits)

        self.label_version = QLabel(self.frame_label_bottom)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setMaximumSize(QSize(100, 16777215))
        self.label_version.setFont(font2)
        self.label_version.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_version)


        self.horizontalLayout_6.addWidget(self.frame_label_bottom)

        self.frame_size_grip = QFrame(self.frame_grip)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMaximumSize(QSize(20, 20))
        self.frame_size_grip.setStyleSheet(u"QSizeGrip {\n"
"	background-image: url(:/16x16/icons/16x16/cil-size-grip.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_size_grip)


        self.verticalLayout_4.addWidget(self.frame_grip)


        self.horizontalLayout_2.addWidget(self.frame_content_right)


        self.verticalLayout.addWidget(self.frame_center)


        self.horizontalLayout.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_minimize, self.btn_maximize_restore)
        QWidget.setTabOrder(self.btn_maximize_restore, self.btn_close)
        QWidget.setTabOrder(self.btn_close, self.btn_toggle_menu)
        QWidget.setTabOrder(self.btn_toggle_menu, self.checkBox)
        QWidget.setTabOrder(self.checkBox, self.comboBox)
        QWidget.setTabOrder(self.comboBox, self.radioButton)
        QWidget.setTabOrder(self.radioButton, self.horizontalSlider)
        QWidget.setTabOrder(self.horizontalSlider, self.verticalSlider)
        QWidget.setTabOrder(self.verticalSlider, self.scrollArea)
        QWidget.setTabOrder(self.scrollArea, self.plainTextEdit)
        QWidget.setTabOrder(self.plainTextEdit, self.tableWidget)
        QWidget.setTabOrder(self.tableWidget, self.commandLinkButton)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_toggle_menu.setText("")
        self.label_title_bar_top.setText(QCoreApplication.translate("MainWindow", u"Main Window - Base", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximize_restore.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize_restore.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.label_top_info_1.setText(QCoreApplication.translate("MainWindow", u"C:\\Program Files\\Blender Foundation\\Blender 2.82", None))
        self.label_top_info_2.setText(QCoreApplication.translate("MainWindow", u"| HOME", None))
        self.label_user_icon.setText(QCoreApplication.translate("MainWindow", u"WM", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"WELCOME", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Vehicle Calibration Tool For VCU v0.1", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Wisdom (Fujian) motor co., ltd.", None))
        self.lable_devicetype.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u5907\u7c7b\u578b:", None))
        self.cbb_devicetype.setItemText(0, QCoreApplication.translate("MainWindow", u"USBCAN-I", None))
        self.cbb_devicetype.setItemText(1, QCoreApplication.translate("MainWindow", u"USBCAN-II", None))

        self.label_deviceindex.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u5907\u7d22\u5f15:", None))
        self.cbb_deviceindex.setItemText(0, QCoreApplication.translate("MainWindow", u"0", None))
        self.cbb_deviceindex.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.cbb_deviceindex.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.cbb_deviceindex.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))

        self.label_baudrate.setText(QCoreApplication.translate("MainWindow", u"\u6ce2\u7279\u7387:", None))
        self.cbb_baudrate.setItemText(0, QCoreApplication.translate("MainWindow", u"250K", None))
        self.cbb_baudrate.setItemText(1, QCoreApplication.translate("MainWindow", u"500K", None))

        self.label_canchannel.setText(QCoreApplication.translate("MainWindow", u"CAN\u901a\u9053:", None))
        self.cbb_canchannel.setItemText(0, QCoreApplication.translate("MainWindow", u"0", None))
        self.cbb_canchannel.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.cbb_canchannel.setItemText(2, QCoreApplication.translate("MainWindow", u"0\u548c1", None))

        self.btn_opendevice.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u8bbe\u5907", None))
        ___qtablewidgetitem = self.tablew_msgdisplay.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u5e8f\u53f7", None));
        ___qtablewidgetitem1 = self.tablew_msgdisplay.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u65f6\u95f4", None));
        ___qtablewidgetitem2 = self.tablew_msgdisplay.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u901a\u9053", None));
        ___qtablewidgetitem3 = self.tablew_msgdisplay.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem4 = self.tablew_msgdisplay.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u65b9\u5411", None));
        ___qtablewidgetitem5 = self.tablew_msgdisplay.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e", None));
        self.label_sendtype.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001\u65b9\u5f0f:", None))
        self.cbb_sendtype.setItemText(0, QCoreApplication.translate("MainWindow", u"\u6b63\u5e38\u53d1\u9001", None))
        self.cbb_sendtype.setItemText(1, QCoreApplication.translate("MainWindow", u"\u5355\u6b21\u53d1\u9001", None))
        self.cbb_sendtype.setItemText(2, QCoreApplication.translate("MainWindow", u"\u81ea\u53d1\u81ea\u6536", None))

        self.label_id.setText(QCoreApplication.translate("MainWindow", u"\u62a5\u6587ID:", None))
        self.le_id.setText(QCoreApplication.translate("MainWindow", u"0x18ffe6a5", None))
        self.label_sendnum.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001\u6b21\u6570:", None))
        self.le_sendnum.setInputMask("")
        self.le_sendnum.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_sendinterval.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001\u95f4\u9694:", None))
        self.le_sendinterval.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_data.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u57df:", None))
        self.le_data.setInputMask("")
        self.le_data.setText(QCoreApplication.translate("MainWindow", u"00 01 02 03 04 05 06 07", None))
        self.btn_sendmsg.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Motor Speed", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Velocity", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Motor Torque", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"VCU Torque", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"SOC", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"MCU1 Temperature", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Motor1 Temperature", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"MCU2 Temperature", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Motor2 Temperature", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Air Pressure1", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Air Pressure2", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"VCU_Life", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"MCU_Life", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"BMS_Life", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"DCDC_Life", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"LVOP_Life", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"HVOP_Life", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"HVAP_Life", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"ABS_Life", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"EPB_Life", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"SAS_Life", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"BLENDER INSTALLATION", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Your Password", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Open Blender", None))
        self.labelVersion_3.setText(QCoreApplication.translate("MainWindow", u"Ex: C:Program FilesBlender FoundationBlender 2.82 blender.exe", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Test 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))

        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"CommandLinkButton", None))
        self.commandLinkButton.setDescription(QCoreApplication.translate("MainWindow", u"Open External Link", None))
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u65b9\u5411", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u957f\u5ea6", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem12 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"dfadf", None));
        ___qtablewidgetitem13 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"dafsad", None));
        ___qtablewidgetitem14 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"fdafsa", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"Registered by: Wanderson M. Pimenta", None))
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
    # retranslateUi

