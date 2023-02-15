from PySide2.QtCore import Qt, QObject, Signal
from PySide2.QtWidgets import QTableWidgetItem
from zlgcan import ZCAN_Receive_Data
import time
from main import *


class UiControl(QObject):

    msg_signal = Signal([ZCAN_Receive_Data])
    TableUpdateSignal = Signal(str, str, str, str, str)

    def __init__(self, mainwindow):
        super().__init__()
        self.mw = mainwindow  # type: MainWindow
        self.slotInit()
        self.uiInit()

    def slotInit(self):
        self.TableUpdateSignal.connect(self.msgTablewDisplay)
        self.msg_signal.connect(self.msgUiDisplay)

        # info_pte右键菜单初始化
        def infoPteContext():
            menu = QMenu()
            clearAllAct = menu.addAction("清空全部")
            clearAllAct.triggered.connect(self.pteClearAll)
            menu.exec_(QCursor.pos())

        self.mw.ui.pte_info.setContextMenuPolicy(Qt.CustomContextMenu)
        self.mw.ui.pte_info.customContextMenuRequested.connect(infoPteContext)

        def tablewContext():
            menu = QMenu()
            clearAllAct = menu.addAction("清空全部")
            saveAllAct = menu.addAction('保存报文')
            clearAllAct.triggered.connect(self.tblwClearAllRow)
            saveAllAct.triggered.connect(self.tblwSaveAllRow)
            menu.exec_(QCursor.pos())

        self.mw.ui.tablew_msgdisplay.setContextMenuPolicy(Qt.CustomContextMenu)
        self.mw.ui.tablew_msgdisplay.customContextMenuRequested.connect(
            tablewContext)

    def uiInit(self):
        self.mw.ui.tableWidget.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.Stretch)
        self.mw.ui.tablew_msgdisplay.horizontalHeader().resizeSection(0, 60)
        self.mw.ui.tablew_msgdisplay.horizontalHeader().resizeSection(1, 120)
        self.mw.ui.tablew_msgdisplay.horizontalHeader().resizeSection(2, 120)
        self.mw.ui.tablew_msgdisplay.horizontalHeader().resizeSection(3, 60)
        self.mw.ui.tablew_msgdisplay.horizontalHeader().resizeSection(4, 60)

        # Motor Speed仪表盘初始化
        self.mw.ui.gp_motorspeed.setMinMaxValue(-10000, 10000)
        self.mw.ui.gp_motorspeed.setScaleMainNum(10)
        self.mw.ui.gp_motorspeed.setScaleSubNum(5)
        self.mw.ui.gp_motorspeed.setMinRadio(100)
        self.mw.ui.gp_motorspeed.setTitle('x100rpm')
        self.mw.ui.gp_motorspeed.setValueSubTitle('rpm')
        # Velocity仪表盘初始化
        self.mw.ui.gp_velocity.setMinMaxValue(0, 160)
        self.mw.ui.gp_velocity.setScaleMainNum(10)
        self.mw.ui.gp_velocity.setScaleSubNum(5)
        self.mw.ui.gp_velocity.setMinRadio(10)
        self.mw.ui.gp_velocity.setTitle('x10km/h')
        self.mw.ui.gp_velocity.setValueSubTitle('km/h')
        # Motor Torque仪表盘初始化
        self.mw.ui.gp_motortorque.setMinMaxValue(-3000, 3000)
        self.mw.ui.gp_motortorque.setScaleMainNum(10)
        self.mw.ui.gp_motortorque.setScaleSubNum(5)
        self.mw.ui.gp_motortorque.setMinRadio(100)
        self.mw.ui.gp_motortorque.setTitle('x100Nm')
        self.mw.ui.gp_motortorque.setValueSubTitle('N.m.')
        # VCU Torque仪表盘初始化
        self.mw.ui.gp_vcutorque.setMinMaxValue(-3000, 3000)
        self.mw.ui.gp_vcutorque.setScaleMainNum(10)
        self.mw.ui.gp_vcutorque.setScaleSubNum(5)
        self.mw.ui.gp_vcutorque.setMinRadio(100)
        self.mw.ui.gp_vcutorque.setTitle('x100Nm')
        self.mw.ui.gp_vcutorque.setValueSubTitle('N.m.')
        # SOC进度条初始化
        self.mw.ui.pb_soc.setMinMaxValue(0, 100)
        self.mw.ui.pb_soc.setUnit('%')
        # MCU1 Temperature进度条初始化
        self.mw.ui.pb_mcu1temp.setMinMaxValue(-40, 170)
        self.mw.ui.pb_mcu1temp.setUnit('℃')
        # Motor1 Temperature进度条初始化
        self.mw.ui.pb_motor1temp.setMinMaxValue(-40, 170)
        self.mw.ui.pb_motor1temp.setUnit('℃')
        # MCU2 Temperature进度条初始化
        self.mw.ui.pb_mcu2temp.setMinMaxValue(-40, 170)
        self.mw.ui.pb_mcu2temp.setUnit('℃')
        # Motor2 Temperature进度条初始化
        self.mw.ui.pb_motor2temp.setMinMaxValue(-40, 170)
        self.mw.ui.pb_motor2temp.setUnit('℃')
        # Air Pressure1进度条初始化
        self.mw.ui.pb_airpressure1.setMinMaxValue(0, 1)
        self.mw.ui.pb_airpressure1.setUnit('kPa')
        # Air Pressure2进度条初始化
        self.mw.ui.pb_airpressure2.setMinMaxValue(0, 1)
        self.mw.ui.pb_airpressure2.setUnit('kPa')

    def msgUiDisplay(self, msgs):
        # TODO：增加DBC解析信号功能
        msgs = list(map(self.msgConvert, msgs))

        for m in msgs:
            match m.id:
                case 0x18ffe6a5:
                    pass

                case 0x18ffe6a6:
                    pass

                case 0x18FF3D27:
                    Motor1_Speed = m.getBits(0, 16) - 15000
                    self.mw.ui.gp_motorspeed.setValue(Motor1_Speed)

                case 0x1884EFF3:
                    SOC = m.getBits(0, 8) * 0.4
                    self.mw.ui.pb_soc.setValue(SOC)

                case _:
                    pass

            self.mw.ui.pte_info.appendPlainText(
                f'收到报文\nID:{hex(m.id)}\n数据域:{m.data}\n')
            self.msgTablewDisplay(m.time, m.id, m.dir, m.dlc, m.data)

    def msgTablewDisplay(self, time, id, dir, dlc, data):
        time = time / 1e6
        time = '%.3f' % time  # 用该方法可以保留小数末尾0，round方法无法保存小鼠末尾0
        id = hex(id)
        dir = str(dir)
        dlc = str(dlc)
        data = str(data)
        table_row_cnt = self.mw.ui.tablew_msgdisplay.rowCount()
        self.mw.ui.tablew_msgdisplay.insertRow(table_row_cnt)
        # 序号
        item = QTableWidgetItem(str(table_row_cnt + 1))
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.mw.ui.tablew_msgdisplay.setItem(table_row_cnt, 0, item)
        # 时间
        item = QTableWidgetItem(time)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.mw.ui.tablew_msgdisplay.setItem(table_row_cnt, 1, item)
        # ID
        item = QTableWidgetItem(id)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.mw.ui.tablew_msgdisplay.setItem(table_row_cnt, 2, item)
        # 方向
        item = QTableWidgetItem(dir)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.mw.ui.tablew_msgdisplay.setItem(table_row_cnt, 3, item)
        # 长度
        item = QTableWidgetItem(dlc)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.mw.ui.tablew_msgdisplay.setItem(table_row_cnt, 4, item)

        self.mw.ui.tablew_msgdisplay.setItem(
            table_row_cnt, 5, QTableWidgetItem(data))
        self.mw.ui.tablew_msgdisplay.scrollToBottom()

    def infoPteDisplay(self, msgs):

        new_msgs = list(map(self.frameConvert, msgs))
        for nm in new_msgs:
            match nm.id:
                case 0x18ffe6a5:
                    self.mw.ui.pte_info.appendPlainText(
                        f'收到报文,id:{hex(nm.id)},data:{nm.data}')
                    self.msgTablewDisplay(
                        nm.time, nm.id, nm.dir, nm.dlc, nm.data)
                    pass

                case 0x18ffe6a6:
                    # self.mw.ui.pte_info.appendPlainText(f'收到报文,id:{hex(nm.id)},data:{nm.data}')
                    pass
                case 0x18ff3d27:
                    pass

                case _:
                    # self.mw.ui.pte_info.appendPlainText('收到未知报文')
                    pass

    @staticmethod
    def msgConvert(msg: ZCAN_Receive_Data):
        class NewFrame:
            id = None
            time = None
            dir = None
            dlc = None
            data = None
            Bytes = None

            def getBits(self, startbit, len):
                data_in_64bits = 0
                for i, B in enumerate(self.Bytes):
                    data_in_64bits = data_in_64bits + (B << i * 8)

                res = int(bin(data_in_64bits)[::-1][startbit:len][::-1], 2)
                return res

        nf = NewFrame()
        nf.id = msg.frame.can_id
        nf.time = msg.timestamp
        nf.dir = 'rx'
        nf.dlc = msg.frame.can_dlc
        nf.data = list(msg.frame.data)
        nf.Bytes = nf.data

        return nf

    def getMsgSignal(self, startbit, length):
        pass

    # 右键菜单动作
    def tblwClearAllRow(self):
        row_num = self.mw.ui.tablew_msgdisplay.rowCount()
        for i in range(0, row_num)[::-1]:
            self.mw.ui.tablew_msgdisplay.removeRow(i)

    def tblwSaveAllRow(self):
        pass

        header = 'data ' + time.ctime() + '\nbase hex timestamps absolute' + '\ninternal events logged' + \
            '\n// version 7.2.0' + '\nBegin Triggerblock ' + time.ctime() + '\n0.000000 Start of measurement\n'
        row_num = self.mw.ui.tablew_msgdisplay.rowCount()
        col_num = self.mw.ui.tablew_msgdisplay.columnCount()
        items = [self.mw.ui.tablew_msgdisplay.item(row, col) for row in range(row_num) for col in range(col_num)]
        items = list(zip(*[iter(items)]*col_num))
        file_url, _ = QFileDialog.getSaveFileName(None, 'Save File', './', 'Asc (*.asc)')
        if file_url != '':
            with open(file_url, 'w') as f:
                f.write(header)

                for r in items:
                    for i in r:
                        f.write(i.text() + '    ')
                    f.write('\n')
                pass

    def pteClearAll(self):
        self.mw.ui.pte_info.clear()
