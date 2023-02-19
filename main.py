##########################################################################
##
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide2
# V: 1.0.0
##
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
##
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
##
##########################################################################

import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (
    QCoreApplication,
    QPropertyAnimation,
    QDate,
    QDateTime,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
    QEvent)
from PySide2.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QIcon,
    QKeySequence,
    QLinearGradient,
    QPalette,
    QPainter,
    QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

# GUI FILE
from app_modules import *


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.can = CAN(mainwindow=self)

        # PRINT ==> SYSTEM
        print('System: ' + platform.system())
        print('Version: ' + platform.release())

        # REMOVE ==> STANDARD TITLE BAR
        UIFunctions.removeTitleBar(True)

        # SET ==> WINDOW TITLE
        self.setWindowTitle('Vehicle Calibration Tool - v0.1')
        UIFunctions.labelTitle(self, 'Vehicle Calibration Tool - v0.1')
        UIFunctions.labelDescription(self, 'Set text')

        # WINDOW SIZE ==> DEFAULT SIZE
        startSize = QSize(1000, 720)
        self.resize(startSize)
        self.setMinimumSize(startSize)
        # UIFunctions.enableMaximumSize(self, 500, 720)

        # ==> TOGGLE MENU SIZE
        self.ui.btn_toggle_menu.clicked.connect(
            lambda: UIFunctions.toggleMenu(self, 220, True))

        # ==> ADD CUSTOM MENUS
        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.addNewMenu(
            self,
            "主    页",
            "btn_home",
            "url(:/16x16/icons/16x16/cil-home.png)",
            True)
        UIFunctions.addNewMenu(
            self,
            "设    备",
            "btn_device",
            "url(:/16x16/icons/16x16/cil-input.png)",
            True)
        UIFunctions.addNewMenu(
            self,
            "仪表盘",
            "btn_panel",
            "url(:/16x16/icons/16x16/cil-speedometer.png)",
            True)
        UIFunctions.addNewMenu(
            self,
            "图    表",
            "btn_graph",
            "url(:/16x16/icons/16x16/cil-chart-line.png)",
            True)
        UIFunctions.addNewMenu(
            self,
            "Custom Widgets",
            "btn_widgets",
            "url(:/16x16/icons/16x16/cil-equalizer.png)",
            False)

        # START MENU => SELECTION
        UIFunctions.selectStandardMenu(self, "btn_home")

        # ==> START PAGE
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)

        # USER ICON ==> SHOW HIDE
        UIFunctions.userIcon(self, "WM", "", True)

        # ==> MOVE WINDOW / MAXIMIZE / RESTORE
        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if UIFunctions.returStatus() == 1:
                UIFunctions.maximize_restore(self)

            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # WIDGET TO MOVE
        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow

        # ==> LOAD DEFINITIONS
        #######################################################################
        UIFunctions.uiDefinitions(self)

        self.ui.btn_opendevice.clicked.connect(self.can.btnOpenDev_Click)
        self.ui.btn_sendmsg.clicked.connect(self.can.btnMsgSend_Click)

        self.show()

    def Button(self):
        # GET BT CLICKED
        btnWidget = self.sender()

        # PAGE HOME
        if btnWidget.objectName() == "btn_home":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            UIFunctions.resetStyle(self, "btn_home")
            UIFunctions.labelPage(self, "主 页")
            btnWidget.setStyleSheet(
                UIFunctions.selectMenu(
                    btnWidget.styleSheet()))

        # PAGE DEVICE
        if btnWidget.objectName() == "btn_device":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_device)
            UIFunctions.resetStyle(self, "btn_device")
            UIFunctions.labelPage(self, "设 备")
            btnWidget.setStyleSheet(
                UIFunctions.selectMenu(
                    btnWidget.styleSheet()))

        # PAGE NEW USER
        if btnWidget.objectName() == "btn_new_user":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            UIFunctions.resetStyle(self, "btn_new_user")
            UIFunctions.labelPage(self, "New User")
            btnWidget.setStyleSheet(
                UIFunctions.selectMenu(
                    btnWidget.styleSheet()))

        # PAGE Panel
        if btnWidget.objectName() == "btn_panel":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_panel)
            UIFunctions.resetStyle(self, "btn_panel")
            UIFunctions.labelPage(self, "仪表盘")
            btnWidget.setStyleSheet(
                UIFunctions.selectMenu(
                    btnWidget.styleSheet()))

        # PAGE GRAPH
        if btnWidget.objectName() == "btn_graph":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_graph)
            UIFunctions.resetStyle(self, "btn_graph")
            UIFunctions.labelPage(self, "图 表")
            btnWidget.setStyleSheet(
                UIFunctions.selectMenu(
                    btnWidget.styleSheet()))

        # PAGE WIDGETS
        if btnWidget.objectName() == "btn_widgets":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_widgets)
            UIFunctions.resetStyle(self, "btn_widgets")
            UIFunctions.labelPage(self, "Custom Widgets")
            btnWidget.setStyleSheet(
                UIFunctions.selectMenu(
                    btnWidget.styleSheet()))



    ## ==> END ##

    ########################################################################
    # START ==> APP EVENTS
    ########################################################################

    # EVENT ==> MOUSE DOUBLE CLICK
    ########################################################################
    def eventFilter(self, watched, event):
        if watched == self.le and event.type() == QtCore.QEvent.MouseButtonDblClick:
            print("pos: ", event.pos())
    ## ==> END ##

    # EVENT ==> MOUSE CLICK
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
        if event.buttons() == Qt.MidButton:
            print('Mouse click: MIDDLE BUTTON')
    ## ==> END ##

    # EVENT ==> KEY PRESSED
    ########################################################################
    def keyPressEvent(self, event):
        print('Key: ' +
              str(event.key()) +
              ' | Text Press: ' +
              str(event.text()))
    ## ==> END ##

    # EVENT ==> RESIZE EVENT
    ########################################################################
    def resizeEvent(self, event):
        self.resizeFunction()
        return super(MainWindow, self).resizeEvent(event)

    def resizeFunction(self):
        print('Height: ' + str(self.height()) +
              ' | Width: ' + str(self.width()))
    ## ==> END ##

    ########################################################################
    # END ==> APP EVENTS
    ############################## ---/--/--- ##############################


if __name__ == "__main__":
    QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)  # 自适应分辨率
    app = QApplication(sys.argv)

    QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    mw = MainWindow()
    sys.exit(app.exec_())
