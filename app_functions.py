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
# ==> GUI FILE
import time

from main import *
from zlgcan import *
import json
import threading
from PySide2.QtCore import Signal, QObject, QThread, QTimer
import datetime
from ui_control import UiControl

MAX_DISPLAY = 1000
MAX_RCV_NUM = 10

USBCANFD_TYPE = (41, 42, 43)
USBCAN_XE_U_TYPE = (20, 21, 31)
USBCAN_I_II_TYPE = (3, 4)


class CAN(ZCAN):
    def __init__(self, mainwindow):
        super().__init__()
        self.mw = mainwindow  # type: MainWindow
        self._dev_info = None

        with open("./dev_info.json", "r") as fd:
            self._dev_info = json.load(fd)
        if self._dev_info is None:
            print("device info no exist!")
            return

        self.DeviceInit()

        self.ms = UiControl(self.mw)

    def DeviceInit(self):
        self._zcan = ZCAN()
        self._dev_handle = INVALID_DEVICE_HANDLE
        self._can_handle = INVALID_CHANNEL_HANDLE
        self._can_handle_dict = {}

        self._isOpen = False
        self._isChnOpen = False

        # current device info
        self._is_canfd = False
        self._res_support = False

        # Transmit and receive count display
        self._tx_cnt = 0
        self._rx_cnt = 0
        self._view_cnt = 0

        # read can/canfd message thread
        self._read_thread = None
        self._terminated = False
        # self._lock = threading.RLock()

        # period send var
        self._is_sending = False
        self._id_increase = False
        self._send_num = 1
        self._send_cnt = 0
        self._is_canfd_msg = False
        self._send_msgs = None
        self._send_timer = None

    def btnOpenDev_Click(self):
        if self._isOpen:
            # ????????????????????????????????????
            for can_channel in self._can_handle_dict.keys():
                self._zcan.ResetCAN(can_channel)
                print(f'??????{can_channel}??????')
                # self.btnCANCtrl.invoke()

            # Close Device???????????????
            self._zcan.CloseDevice(self._dev_handle)

            # self.strvDevCtrl.set("??????")
            self.mw.ui.btn_opendevice.setText('????????????')
            self.mw.ui.cbb_devicetype.setEnabled(True)
            self.mw.ui.cbb_deviceindex.setEnabled(True)
            self.mw.ui.cbb_baudrate.setEnabled(True)
            self.mw.ui.cbb_canchannel.setEnabled(True)
            # self.cmbDevType["state"] = "readonly"
            # self.cmbDevIdx["state"] = "readonly"
            self._isOpen = False
        else:

            self._cur_dev_info = self._dev_info[self.mw.ui.cbb_devicetype.currentText(
            )]

            # Open Device
            self._dev_handle = self._zcan.OpenDevice(
                self._cur_dev_info["dev_type"], self.mw.ui.cbb_deviceindex.currentIndex(), 0)
            if self._dev_handle == INVALID_DEVICE_HANDLE:
                # Open failed
                # messagebox.showerror(title="????????????", message="?????????????????????")
                # QMessageBox.information(parent=self.mw, title='aaa', text="?????????????????????", button0=QMessageBox.Ok)
                QMessageBox.information(
                    self.mw,
                    '??????????????????',
                    '1????????????CAN????????????CAN??????????????????\n2?????????????????????????????????CAN???\n3????????????CAN???????????????',
                    QMessageBox.Ok)
                return

            # Initial channel
            chn_cfg = ZCAN_CHANNEL_INIT_CONFIG()
            chn_cfg.can_type = ZCAN_TYPE_CAN
            # 0?????????????????????????????????
            chn_cfg.config.can.mode = 0

            brt = self._cur_dev_info["chn_info"]["baudrate"][self.mw.ui.cbb_baudrate.currentText(
            )]
            chn_cfg.config.can.timing0 = brt["timing0"]
            chn_cfg.config.can.timing1 = brt["timing1"]
            chn_cfg.config.can.acc_code = 0
            chn_cfg.config.can.acc_mask = 0xFFFFFFFF

            can_index = self.mw.ui.cbb_canchannel.currentIndex()
            if can_index == 0 or can_index == 1:
                self._can_handle = self._zcan.InitCAN(
                    self._dev_handle, can_index, chn_cfg)
                self._can_handle_dict[can_index] = self._can_handle
                print('??????0???1???????????????')
            else:
                self._can_handle = self._zcan.InitCAN(
                    self._dev_handle, 0, chn_cfg)
                self._can_handle_dict[0] = self._can_handle
                self._can_handle = self._zcan.InitCAN(
                    self._dev_handle, 1, chn_cfg)
                self._can_handle_dict[1] = self._can_handle
                print('??????0???1???????????????')

            for can_handle in self._can_handle_dict.values():
                if self._can_handle == INVALID_CHANNEL_HANDLE:
                    # messagebox.showerror(title="????????????", message="?????????????????????!")
                    QMessageBox.information(self.mw, f'CAN{can_handle}?????????????????????',
                                            f'CAN{can_handle}????????????????????????????????????',
                                            QMessageBox.Ok)
                    return

                ret = self._zcan.StartCAN(can_handle)
                if ret != ZCAN_STATUS_OK:
                    # messagebox.showerror(title="????????????", message="??????????????????!")
                    QMessageBox.information(self.mw, f'CAN{can_handle}??????????????????',
                                            f'CAN{can_handle}?????????????????????????????????',
                                            QMessageBox.Ok)
                    return

            # self.strvDevCtrl.set("??????")
            self.mw.ui.btn_opendevice.setText('????????????')
            self.mw.ui.cbb_devicetype.setEnabled(False)
            self.mw.ui.cbb_deviceindex.setEnabled(False)
            self.mw.ui.cbb_baudrate.setEnabled(False)
            self.mw.ui.cbb_canchannel.setEnabled(False)

            # ??????????????????
            self._read_thread = threading.Thread(
                None, target=self.msgRecvThreadFunc)
            self._read_thread.start()

            self._isOpen = True

    def btnMsgSend_Click(self):
        # TODO: ????????????QTimer????????????????????????????????????????????????????????????????????????
        if self._isOpen:
            msg = ZCAN_Transmit_Data()
            msg.transmit_type = self.mw.ui.cbb_sendtype.currentIndex()
            msg.frame.can_id = int(self.mw.ui.le_id.text(), 16)
            msg.frame.rtr = 0
            msg.frame.eff = 1
            msg.frame.can_dlc = 8

            data = self.mw.ui.le_data.text().split(' ')
            for i in range(8):
                if i < len(data):
                    try:
                        msg.frame.data[i] = int(data[i], 16)
                    except:
                        msg.frame.data[i] = 0
                else:
                    msg.frame.data[i] = 0

            self._send_num = int(self.mw.ui.le_sendnum.text())
            if self._send_num == 1:
                ret = self._zcan.Transmit(self._can_handle_dict[0], msg, 1)
            else:
                # ??????QTimer????????????????????????????????????????????????
                self._send_timer = QTimer()
                # self._send_timer.setTimerType(Qt.PreciseTimer)
                self._send_timer.timeout.connect(lambda: self.msgPeriodSendFunc(msg))
                sendInterval = int(self.mw.ui.le_sendinterval.text())
                if not self._send_timer.isActive():
                    self._send_timer.start(sendInterval)

        else:
            QMessageBox.information(self.mw, f'???????????????',
                                    f'???????????????,??????????????????',
                                    QMessageBox.Ok)

    def msgPeriodSendFunc(self, msg):
        ret = self._zcan.Transmit(self._can_handle_dict[0], msg, 1)
        if ret == 1:
            self._send_cnt += 1
        if self._send_cnt >= self._send_num:
            self._send_timer.stop()
            self._send_cnt = 0

    def msgRecvThreadFunc(self):
        while True:
            if self._isOpen:
                can_num = self._zcan.GetReceiveNum(
                    self._can_handle, ZCAN_TYPE_CAN)
                if not can_num:
                    time.sleep(0.005)  # wait 5ms
                    continue

                read_cnt = MAX_RCV_NUM if can_num >= MAX_RCV_NUM else can_num
                can_msgs, act_num = self._zcan.Receive(
                    self._can_handle, read_cnt, MAX_RCV_NUM)  # type: list

                self.ms.msg_signal.emit(can_msgs)
                # print('??????????????????:')
                # data = can_msgs[0].frame.data
                # print(list(map(hex, data)))

                # self.MsgDisplay(can_msgs[0])

    # def MsgDisplay(self, msg):
    #     frame = msg.frame
    #     time = str(msg.timestamp)
    #     # id_col = 0
    #     # dir_col = 1
    #     # len_col = 2
    #     # data_col = 3
    #     id = hex(frame.can_id)
    #     dir = 'rx'
    #     dlc = str(frame.can_dlc)
    #     data = ""
    #     for i in frame.data:
    #         data = data + str(i) + ' '
    #
    #     self.ms.TableUpdateSignal.emit(time, id, dir, dlc, data)
