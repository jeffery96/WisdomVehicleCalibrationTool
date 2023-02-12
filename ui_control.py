from PySide2.QtCore import Qt, QObject, Signal
from PySide2.QtWidgets import QTableWidgetItem
from zlgcan import ZCAN_Receive_Data
from main import *


class UiControl(QObject):

    glb_signal = Signal([ZCAN_Receive_Data])
    TableUpdateSignal = Signal(str, str, str, str, str)

    def __init__(self, mainwindow):
        super().__init__()
        self.mw = mainwindow  # type: MainWindow
        self.TableUpdateSignal.connect(self.TableUpdateFunc)
        self.glb_signal.connect(self.PlainTextShow)

        self.uiInit()

    def uiInit(self):
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
        self.mw.ui.gp_motortorque.setValueSubTitle('Nm')
        # VCU Torque仪表盘初始化
        self.mw.ui.gp_vcutorque.setMinMaxValue(-3000, 3000)
        self.mw.ui.gp_vcutorque.setScaleMainNum(10)
        self.mw.ui.gp_vcutorque.setScaleSubNum(5)
        self.mw.ui.gp_vcutorque.setMinRadio(100)
        self.mw.ui.gp_vcutorque.setTitle('x100Nm')
        self.mw.ui.gp_vcutorque.setValueSubTitle('Nm')
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

    def TableUpdateFunc(self, time, id, dir, dlc, data):
        time = time / 1e6
        time = str(time) + 's'
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

        self.mw.ui.tablew_msgdisplay.setItem(table_row_cnt, 5, QTableWidgetItem(data))
        self.mw.ui.tablew_msgdisplay.scrollToBottom()

    @staticmethod
    def FrameConvert(msg: ZCAN_Receive_Data):
        class NewFrame:
            id = None
            time = None
            dir = None
            dlc = None
            data = None

        nf = NewFrame()
        nf.id = msg.frame.can_id
        nf.time = msg.timestamp
        nf.dir = 'rx'
        nf.dlc = msg.frame.can_dlc
        nf.data = list(msg.frame.data)

        return nf

    def PlainTextShow(self, msgs):

        new_msgs = list(map(self.FrameConvert, msgs))
        for nm in new_msgs:
            match nm.id:
                case 0x18ffe6a5:
                    self.mw.ui.pte_info.appendPlainText(f'收到报文,id:{hex(nm.id)},data:{nm.data}')
                    self.TableUpdateFunc(nm.time, nm.id, nm.dir, nm.dlc, nm.data)
                    
                case 0x18ffe6a6:
                    self.mw.ui.pte_info.appendPlainText(f'收到报文,id:{hex(nm.id)},data:{nm.data}')

                case _:
                    self.mw.ui.pte_info.appendPlainText('收到未知报文')
