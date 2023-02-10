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

        self.can_dev = CAN_Device(mainwindow=self)

        # PRINT ==> SYSTEM
        print('System: ' + platform.system())
        print('Version: ' + platform.release())

        #######################################################################
        # START - WINDOW ATTRIBUTES
        #######################################################################

        # REMOVE ==> STANDARD TITLE BAR
        UIFunctions.removeTitleBar(True)
        ## ==> END ##

        # SET ==> WINDOW TITLE
        self.setWindowTitle('Main Window - Python Base')
        UIFunctions.labelTitle(self, 'Main Window - Python Base')
        UIFunctions.labelDescription(self, 'Set text')
        ## ==> END ##

        # WINDOW SIZE ==> DEFAULT SIZE
        startSize = QSize(1000, 720)
        self.resize(startSize)
        self.setMinimumSize(startSize)
        # UIFunctions.enableMaximumSize(self, 500, 720)
        ## ==> END ##

        # ==> CREATE MENUS
        #######################################################################

        # ==> TOGGLE MENU SIZE
        self.ui.btn_toggle_menu.clicked.connect(
            lambda: UIFunctions.toggleMenu(self, 220, True))
        ## ==> END ##

        # ==> ADD CUSTOM MENUS
        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.addNewMenu(
            self,
            "主页",
            "btn_home",
            "url(:/16x16/icons/16x16/cil-home.png)",
            True)
        UIFunctions.addNewMenu(
            self,
            "设备",
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
            "Add User",
            "btn_new_user",
            "url(:/16x16/icons/16x16/cil-user-follow.png)",
            True)
        UIFunctions.addNewMenu(
            self,
            "test",
            "btn_test",
            "url(:/16x16/icons/16x16/cil-user-follow.png)",
            True)
        UIFunctions.addNewMenu(
            self,
            "Custom Widgets",
            "btn_widgets",
            "url(:/16x16/icons/16x16/cil-equalizer.png)",
            False)
        ## ==> END ##

        # START MENU => SELECTION
        UIFunctions.selectStandardMenu(self, "btn_home")
        ## ==> END ##

        # ==> START PAGE
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
        ## ==> END ##

        # USER ICON ==> SHOW HIDE
        UIFunctions.userIcon(self, "WM", "", True)
        ## ==> END ##

        # ==> MOVE WINDOW / MAXIMIZE / RESTORE
        #######################################################################

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
        ## ==> END ##

        # ==> LOAD DEFINITIONS
        #######################################################################
        UIFunctions.uiDefinitions(self)
        ## ==> END ##

        #######################################################################
        # END - WINDOW ATTRIBUTES
        ############################## ---/--/--- #############################

        #######################################################################
        #                                                                      #
        ## START -------------- WIDGETS FUNCTIONS/PARAMETERS ---------------- ##
        #                                                                      #
        ## ==> USER CODES BELLOW                                              ##
        #######################################################################
        self.ui.OpenDevice_Btn.clicked.connect(self.can_dev.BtnOpenDev_Click)
        self.ui.CanTransClick_Btn.clicked.connect(
            self.can_dev.BtnCanTrans_Click)

        # ==> QTableWidget RARAMETERS
        #######################################################################
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.Stretch)
        self.ui.MsgShow_tblw.horizontalHeader().resizeSection(0, 60)
        self.ui.MsgShow_tblw.horizontalHeader().resizeSection(1, 120)
        self.ui.MsgShow_tblw.horizontalHeader().resizeSection(2, 120)
        self.ui.MsgShow_tblw.horizontalHeader().resizeSection(3, 60)
        self.ui.MsgShow_tblw.horizontalHeader().resizeSection(4, 60)

        self.ui.MsgShow_tblw.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.MsgShow_tblw.customContextMenuRequested.connect(
            self.TableWidgetContext)
        ## ==> END ##
        self.ui.widget.setValue(0)
        self.ui.widget.setMinMaxValue(0, 3000)
        self.ui.widget.setScaleMainNum(10)
        self.ui.widget.setScaleSubNum(5)
        self.ui.widget.setTitle('x100rpm')
        # # self.ui.widget.setStyleSheet("background-color: rgb(255,255,255);")
        self.ui.horizontalSlider_2.setRange(0, 3000)
        self.ui.horizontalSlider_2.valueChanged.connect(
            lambda: self.ui.widget.setValue(
                self.ui.horizontalSlider_2.value()))

        #######################################################################
        #                                                                      #
        ## END --------------- WIDGETS FUNCTIONS/PARAMETERS ----------------- ##
        #                                                                      #
        ############################## ---/--/--- #############################

        # SHOW ==> MAIN WINDOW
        #######################################################################
        self.show()
        ## ==> END ##

    def TableWidgetContext(self):
        menu = QMenu()
        clearAllAct = menu.addAction("清空全部")

        def tblwClearAllRow():
            row_num = self.ui.MsgShow_tblw.rowCount()
            for i in range(0, row_num)[::-1]:
                self.ui.MsgShow_tblw.removeRow(i)

        clearAllAct.triggered.connect(tblwClearAllRow)
        menu.exec_(QCursor.pos())
        pass

    ########################################################################
    # MENUS ==> DYNAMIC MENUS FUNCTIONS
    ########################################################################

    def Button(self):
        # GET BT CLICKED
        btnWidget = self.sender()

        # PAGE HOME
        if btnWidget.objectName() == "btn_home":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            UIFunctions.resetStyle(self, "btn_home")
            UIFunctions.labelPage(self, "Home")
            btnWidget.setStyleSheet(
                UIFunctions.selectMenu(
                    btnWidget.styleSheet()))

        # PAGE DEVICE
        if btnWidget.objectName() == "btn_device":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_device)
            UIFunctions.resetStyle(self, "btn_device")
            UIFunctions.labelPage(self, "设备")
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

        # PAGE WIDGETS
        if btnWidget.objectName() == "btn_widgets":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_widgets)
            UIFunctions.resetStyle(self, "btn_widgets")
            UIFunctions.labelPage(self, "Custom Widgets")
            btnWidget.setStyleSheet(
                UIFunctions.selectMenu(
                    btnWidget.styleSheet()))

        # PAGE TEST
        if btnWidget.objectName() == "btn_test":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_test)
            UIFunctions.resetStyle(self, "btn_test")
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
    app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    mw = MainWindow()
    sys.exit(app.exec_())
