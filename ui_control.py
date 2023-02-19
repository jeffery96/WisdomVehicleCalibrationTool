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
        self.graphInit()

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
        # 报文显示表格Table Widget初始化
        self.mw.ui.tableWidget.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.Stretch)
        self.mw.ui.tablew_msgdisplay.horizontalHeader().resizeSection(0, 60)
        self.mw.ui.tablew_msgdisplay.horizontalHeader().resizeSection(1, 120)
        self.mw.ui.tablew_msgdisplay.horizontalHeader().resizeSection(2, 60)
        self.mw.ui.tablew_msgdisplay.horizontalHeader().resizeSection(3, 100)
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

    def graphInit(self):
        import pyqtgraph as pg
        import numpy as np
        pg.setConfigOptions(antialias=True, background=QColor(39, 44, 54))
        self.pg_layout = pg.GraphicsLayoutWidget()
        self.mw.ui.verticalLayout_graph.addWidget(self.pg_layout)
        pg.setConfigOptions(antialias=True)  # Enable antialiasing for prettier plots
        # data = np.random.normal(size=100)
        self.p1 = self.pg_layout.addPlot(title="Basic array plotting")
        self.data = [[], []]
        self.p1_curve = self.p1.plot(pen=(0, 255, 0), symbol='o')
        self.pg_layout.nextRow()
        self.p2 = self.pg_layout.addPlot(title="Multiple curves")
        self.p2.plot(np.random.normal(size=100), pen=(255, 0, 0), name="Red curve")
        self.p2.plot(np.random.normal(size=110) + 5, pen=(0, 255, 0), name="Green curve")
        self.p2.plot(np.random.normal(size=120) + 10, pen=(0, 0, 255), name="Blue curve")
        self.pg_layout.nextRow()
        p3 = self.pg_layout.addPlot(title="Drawing with points")
        p3.plot(np.random.normal(size=100), pen=(200, 200, 200), symbolBrush=(255, 0, 0), symbolPen='w')

        vLine = pg.InfiniteLine(angle=90, movable=False)
        # hLine = pg.InfiniteLine(angle=0, movable=False)
        self.p1.addItem(vLine, ignoreBounds=True)
        # p1.addItem(hLine, ignoreBounds=True)
        vb = self.p1.vb

        def mouseMoved(evt):
            pos = evt
            if self.p1.sceneBoundingRect().contains(pos):
                mousePoint = vb.mapSceneToView(pos)
                # TODO: 获取离鼠标x坐标最近的那个data X轴数值
                index = min(self.data[0], key=lambda x: abs(x - mousePoint))
                # index = int(mousePoint.x())
                if 0 < index < len(self.data[1]):
                    print((mousePoint.x(), self.data[1][index]))

                vLine.setPos(mousePoint.x())
                # hLine.setPos(mousePoint.y())

        # proxy = pg.SignalProxy(p1.scene().sigMouseMoved, rateLimit=60, slot=mouseMoved)
        self.p1.scene().sigMouseMoved.connect(mouseMoved)
        pass

    def msgUiDisplay(self, msgs):
        # TODO：增加DBC解析信号功能
        msgs = list(map(self.msgConvert, msgs))

        for m in msgs:
            match m.id:
                case 0x18FFE6A5:
                    self.data[0].append(m.time / 1e6)
                    self.data[1].append(m.getSignal(0, 2))
                    self.p1_curve.setData(self.data[0], self.data[1])
                    pass

                case 0x18FFE6A6:
                    pass

                case 0x18FF3D27:
                    Motor1_Speed = m.getSignal(0, 16) - 15000
                    self.mw.ui.gp_motorspeed.setValue(Motor1_Speed)

                case 0x1884EFF3:
                    SOC = m.getSignal(0, 8) * 0.4
                    self.mw.ui.pb_soc.setValue(SOC)

                case _:
                    pass

            self.mw.ui.pte_info.appendPlainText(f'收到报文\nID:{hex(m.id)}\n数据域:{m.data}\n')
            self.msgTablewDisplay(m.time, 1, m.id, m.dir, m.data)

    def msgTablewDisplay(self, time, chn, id, dir, data):
        time = time / 1e6
        time = '%.3f' % time  # 用该方法可以保留小数末尾0，round方法无法保存小鼠末尾0
        chn = str(chn)
        id = hex(id)
        dir = str(dir)
        data = ''.join(['%02X' % d + ' ' for d in data])[:-1]
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
        # 通道
        item = QTableWidgetItem(chn)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.mw.ui.tablew_msgdisplay.setItem(table_row_cnt, 2, item)
        # ID
        item = QTableWidgetItem(id)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.mw.ui.tablew_msgdisplay.setItem(table_row_cnt, 3, item)
        # 方向
        item = QTableWidgetItem(dir)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.mw.ui.tablew_msgdisplay.setItem(table_row_cnt, 4, item)

        self.mw.ui.tablew_msgdisplay.setItem(
            table_row_cnt, 5, QTableWidgetItem(data))
        self.mw.ui.tablew_msgdisplay.scrollToBottom()

    @staticmethod
    def msgConvert(msg: ZCAN_Receive_Data):
        class NewFrame:
            id = None
            time = None
            dir = None
            dlc = None
            data = None
            Bytes = None

            def getSignal(self, startbit, len):
                # 根据开始位和信号长度获取信号
                # TODO: 使用了字符串操作，可利用纯数值计算减小计算开销
                data_in_64bits = 0
                for i, B in enumerate(self.Bytes):
                    data_in_64bits = data_in_64bits + (B << i * 8)

                res = int(bin(data_in_64bits)[::-1][startbit:len][::-1], 2)
                return res

        nf = NewFrame()
        nf.id = msg.frame.can_id
        nf.time = msg.timestamp
        nf.dir = 'Rx'
        nf.dlc = msg.frame.can_dlc
        nf.data = list(msg.frame.data)
        nf.Bytes = nf.data

        return nf

    # 右键菜单动作
    def tblwClearAllRow(self):
        row_num = self.mw.ui.tablew_msgdisplay.rowCount()
        for i in range(0, row_num)[::-1]:
            self.mw.ui.tablew_msgdisplay.removeRow(i)

    def tblwSaveAllRow(self):
        # 右键保存报文为asc格式
        header = 'data ' + time.ctime() + '\nbase hex timestamps absolute' + '\ninternal events logged' + \
            '\n// version 7.2.0' + '\nBegin Triggerblock ' + time.ctime() + '\n0.000000 Start of measurement\n'
        row_num = self.mw.ui.tablew_msgdisplay.rowCount()
        col_num = self.mw.ui.tablew_msgdisplay.columnCount()
        items = [self.mw.ui.tablew_msgdisplay.item(row, col) for row in range(row_num) for col in range(col_num)]
        items = list(zip(*[iter(items)] * col_num))
        file_url, _ = QFileDialog.getSaveFileName(None, 'Save File', './', 'Asc (*.asc)')
        if file_url != '':
            with open(file_url, 'w') as f:
                f.write(header)
                for r in items:
                    f.write(
                        f'{r[1].text()}      {r[2].text()}          {r[3].text()[2:]}x'
                        f'     {r[4].text()}     d 8 {r[5].text()}')
                    f.write('\n')

                f.write('End TriggerBlock')

    def pteClearAll(self):
        self.mw.ui.pte_info.clear()
