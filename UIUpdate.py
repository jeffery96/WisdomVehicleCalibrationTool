from PySide2.QtCore import Qt, QObject, Signal
from PySide2.QtWidgets import QTableWidgetItem
from zlgcan import ZCAN_Receive_Data
from main import *

class UIUpdate(QObject):

    glb_signal = Signal([ZCAN_Receive_Data])
    TableUpdateSignal = Signal(str, str, str, str, str)

    def __init__(self, mainwindow):
        super().__init__()
        self.mw = mainwindow  # type: MainWindow
        self.TableUpdateSignal.connect(self.TableUpdateFunc)
        self.glb_signal.connect(self.PlainTextShow)

    def TableUpdateFunc(self, time, id, dir, dlc, data):
        time = str(time)
        id = hex(id)
        dir = str(dir)
        dlc = str(dlc)
        data = str(data)
        table_row_cnt = self.mw.ui.MsgShow_tblw.rowCount()
        self.mw.ui.MsgShow_tblw.insertRow(table_row_cnt)
        # 序号
        item = QTableWidgetItem(str(table_row_cnt + 1))
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.mw.ui.MsgShow_tblw.setItem(table_row_cnt, 0, item)
        # 时间
        item = QTableWidgetItem(time)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.mw.ui.MsgShow_tblw.setItem(table_row_cnt, 1, item)
        # ID
        item = QTableWidgetItem(id)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.mw.ui.MsgShow_tblw.setItem(table_row_cnt, 2, item)
        # 方向
        item = QTableWidgetItem(dir)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.mw.ui.MsgShow_tblw.setItem(table_row_cnt, 3, item)
        # 长度
        item = QTableWidgetItem(dlc)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.mw.ui.MsgShow_tblw.setItem(table_row_cnt, 4, item)

        self.mw.ui.MsgShow_tblw.setItem(table_row_cnt, 5, QTableWidgetItem(data))
        self.mw.ui.MsgShow_tblw.scrollToBottom()

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
                    self.mw.ui.plainTextEdit_2.appendPlainText(f'收到报文,id:{hex(nm.id)},data:{nm.data}')
                    self.TableUpdateFunc(nm.time, nm.id, nm.dir, nm.dlc, nm.data)

                case 0x18ffe6a6:
                    self.mw.ui.plainTextEdit_2.appendPlainText(f'收到报文,id:{hex(nm.id)},data:{nm.data}')

                case _:
                    self.mw.ui.plainTextEdit_2.appendPlainText('收到未知报文')
