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

import globalVal
from main import *
from zlgcan import *
import json
import threading
from PySide2.QtCore import Signal, QObject, QThread, QTimer, QFileInfo, QFile
import datetime
from ui_control import UiControl
from HexFileParse import *
import time  # 测试用

import inspect  # 线程用
import ctypes   # 线程用

MAX_DISPLAY = 1000
MAX_RCV_NUM = 10

USBCANFD_TYPE = (41, 42, 43)
USBCAN_XE_U_TYPE = (20, 21, 31)
USBCAN_I_II_TYPE = (3, 4)


class CAN(ZCAN):
    def __init__(self, mainwindow, ui_control):
        super().__init__()
        self.mw = mainwindow  # type: MainWindow
        self._dev_info = None

        with open("./dev_info.json", "r") as fd:
            self._dev_info = json.load(fd)
        if self._dev_info is None:
            print("device info no exist!")
            return

        self.DeviceInit()

        self.uc = ui_control


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
            # TODO: CAN4EU未正确关闭可能导致下次链接不上，需要重新插拔USB，因此需要在主界面关闭时候调用设备关闭函数
            # 如果设备已打开则关闭设备
            # 先终止下载线程
            if self.mw.vcu_download._isDownloading:
                self.mw.vcu_download.StartDownload_Click()

            for can_channel in self._can_handle_dict.keys():
                self._zcan.ResetCAN(can_channel)
                print(f'通道{can_channel}关闭')
                # self.btnCANCtrl.invoke()

            # Close Device，关闭设备
            self._zcan.CloseDevice(self._dev_handle)

            # self.strvDevCtrl.set("打开")
            self.mw.ui.btn_opendevice.setText('打开设备')
            self.mw.ui.cbb_devicetype.setEnabled(True)
            self.mw.ui.cbb_deviceindex.setEnabled(True)
            self.mw.ui.cbb_baudrate.setEnabled(True)
            self.mw.ui.cbb_canchannel.setEnabled(True)
            # self.cmbDevType["state"] = "readonly"
            # self.cmbDevIdx["state"] = "readonly"

            self._read_thread.join(0.1)
            self._isOpen = False
        else:

            self._cur_dev_info = self._dev_info[self.mw.ui.cbb_devicetype.currentText()]

            # Open Device
            self._dev_handle = self._zcan.OpenDevice(
                self._cur_dev_info["dev_type"], self.mw.ui.cbb_deviceindex.currentIndex(), 0)
            if self._dev_handle == INVALID_DEVICE_HANDLE:
                # Open failed
                # messagebox.showerror(title="打开设备", message="打开设备失败！")
                # QMessageBox.information(parent=self.mw, title='aaa', text="打开设备失败！", button0=QMessageBox.Ok)
                QMessageBox.information(
                    self.mw,
                    '打开设备失败',
                    '1、请检查CAN卡索引或CAN通道是否正确\n2、检查是否其他软件占用CAN卡\n3、请检查CAN卡是否接上',
                    QMessageBox.Ok)

                self._dev_handle = INVALID_DEVICE_HANDLE
                return

            # Initial channel
            chn_cfg = ZCAN_CHANNEL_INIT_CONFIG()
            chn_cfg.can_type = ZCAN_TYPE_CAN

            if self.mw.ui.cbb_devicetype.currentText() == 'USBCAN-I' or self.mw.ui.cbb_devicetype.currentText() == 'USBCAN-II':
                # 0表示正常模式，能收能发
                chn_cfg.config.can.mode = 0
                brt = self._cur_dev_info["chn_info"]["baudrate"][self.mw.ui.cbb_baudrate.currentText(
                )]
                chn_cfg.config.can.timing0 = brt["timing0"]
                chn_cfg.config.can.timing1 = brt["timing1"]
                chn_cfg.config.can.acc_code = 0
                chn_cfg.config.can.acc_mask = 0xFFFFFFFF
            elif self.mw.ui.cbb_devicetype.currentText() == 'USBCAN-2E-U' or self.mw.ui.cbb_devicetype.currentText() == 'USBCAN-4E-U':
                # 0表示正常模式，能收能发
                chn_cfg.config.can.mode = 0
                ip = self._zcan.GetIProperty(self._dev_handle)
                ret = self._zcan.SetValue(ip, str(0) + "/baud_rate", self._cur_dev_info["chn_info"]["baudrate"][
                    self.mw.ui.cbb_baudrate.currentText(
                    )])  # 250Kbps
                ret = self._zcan.SetValue(ip, str(1) + "/baud_rate", self._cur_dev_info["chn_info"]["baudrate"][
                    self.mw.ui.cbb_baudrate.currentText()])  # 250Kbps
                self._zcan.ReleaseIProperty(ip)
                # chn_cfg.config.can.acc_code = 0
                # chn_cfg.config.can.acc_mask = 0xFFFFFFFF

            can_index = self.mw.ui.cbb_canchannel.currentIndex()
            if can_index == 0 or can_index == 1:
                self._can_handle = self._zcan.InitCAN(
                    self._dev_handle, can_index, chn_cfg)
                self._can_handle_dict[can_index] = self._can_handle
                print('通道0或1初始化成功')
            else:
                self._can_handle = self._zcan.InitCAN(
                    self._dev_handle, 0, chn_cfg)
                self._can_handle_dict[0] = self._can_handle
                self._can_handle = self._zcan.InitCAN(
                    self._dev_handle, 1, chn_cfg)
                self._can_handle_dict[1] = self._can_handle
                print('通道0和1初始化成功')

            for can_handle in self._can_handle_dict.values():
                if self._can_handle == INVALID_CHANNEL_HANDLE:
                    # messagebox.showerror(title="打开通道", message="初始化通道失败!")
                    QMessageBox.information(self.mw, f'CAN{can_handle}通道初始化失败',
                                            f'CAN{can_handle}通道初始化失败，请重试！',
                                            QMessageBox.Ok)
                    return

                ret = self._zcan.StartCAN(can_handle)
                if ret != ZCAN_STATUS_OK:
                    # messagebox.showerror(title="打开通道", message="打开通道失败!")
                    QMessageBox.information(self.mw, f'CAN{can_handle}通道打开失败',
                                            f'CAN{can_handle}通道打开失败，请重试！',
                                            QMessageBox.Ok)
                    return

            # self.strvDevCtrl.set("关闭")
            self.mw.ui.btn_opendevice.setText('关闭设备')
            self.mw.ui.cbb_devicetype.setEnabled(False)
            self.mw.ui.cbb_deviceindex.setEnabled(False)
            self.mw.ui.cbb_baudrate.setEnabled(False)
            self.mw.ui.cbb_canchannel.setEnabled(False)

            # 报文接收线程
            self._read_thread = threading.Thread(
                None, target=self.msgRecvThreadFunc)
            self._read_thread.start()

            self._isOpen = True

    def btnMsgSend_Click(self):
        # TODO: 优化使用QTimer周期发送精度不高的问题，改用自定线程定时器来解决
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
                # 使用QTimer精度差，只能基本满足周期发送要求
                self._send_timer = QTimer()
                # self._send_timer.setTimerType(Qt.PreciseTimer)
                self._send_timer.timeout.connect(lambda: self.msgPeriodSendFunc(msg))
                sendInterval = int(self.mw.ui.le_sendinterval.text())
                if not self._send_timer.isActive():
                    self._send_timer.start(sendInterval)

        else:
            QMessageBox.information(self.mw, f'设备未打开',
                                    f'设备未打开,请先打开设备',
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

                self.uc.msg_signal.emit(can_msgs)
                self.mw.vcu_download._download_thread.fb_msg_signal.emit(can_msgs)


                # print('收到报文内容:')
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


class TimerThread(QThread):
    def __init__(self, timeout):
        super().__init__()
        self.timer = QTimer()
        self.timer.moveToThread(self)  # 在主线程创建本线程对象，则timer属于主线程，需要移动到子线程才能使用，同时需要调用线程的exec()
        self.timer.timeout.connect(self.timeoutSet)
        self.timeout_flag = False
        self.timeout = timeout

    def run(self) -> None:
        self.timer.start(self.timeout)
        self.exec_()

    def exit(self):
        self.timeout_flag = False
        super().exit()

    def timeoutSet(self):
        self.timeout_flag = True


class DownloadThread(QThread, QObject):
    fb_msg_signal = Signal([ZCAN_Receive_Data])

    def __init__(self, mw, ui_control):
        super().__init__()
        self.mw = mw
        self.uc = ui_control
        self.hex_file = None
        self.timer_thread = None
        self.timer_thread = TimerThread(3000)
        self.timeout = False
        self._isDownloading = False
        self.fb_msg_signal.connect(self.vcuFeedbackMsg)

        self.vcu_feedback_flag = False

    def vcuFeedbackMsg(self, msgs):
        # TODO：增加DBC解析信号功能
        # msgs = list(map(self.msgConvert, msgs))
        for m in msgs:
            if m.frame.can_id == 0x18000002:
                self.vcu_feedback_flag = True

    def run(self) -> None:
        self.downloadThreadFunc()

    def downloadThreadFunc(self):

        # 第一步先请求boot标志位
        msg = ZCAN_Transmit_Data()
        msg.transmit_type = 2  # 0-正常发送，1-单次发送，2-自发自收，3-单次自发自收
        msg.frame.can_id = 0x18000001
        msg.frame.rtr = 0
        msg.frame.eff = 1
        msg.frame.can_dlc = 8
        msg.frame.data[0] = 0x0f
        # self.mw.can.Transmit(self.mw.can._can_handle_dict[0], msg, 1)
        # 第二步等待下位机返回NAK
        # 第三步开始传输
        # if self.hex_file.hex_records_32Bytes_len % 128 == 0:
        #     pack_num = self.hex_file.hex_records_32Bytes_len / 128    # type: MyHex
        # else:
        #     pack_num = self.hex_file.hex_records_32Bytes_len / 128 + 1
        # xmodem_pdu = [self.Xmodem.SOH]
        total = self.hex_file.hex_records_32Bytes_len
        cnt = 0

        for segment, data in self.hex_file.hex_records_32Bytes.items():
            segment = segment[2:]  # 去除0x字符
            # 发送地址
            msg.frame.data[0] = int(segment[6:8], 16)
            msg.frame.data[1] = int(segment[4:6], 16)
            msg.frame.data[2] = int(segment[2:4], 16)
            msg.frame.data[3] = int(segment[0:2], 16)
            msg.frame.data[4] = 0xDD
            msg.frame.data[5] = 0xCC
            msg.frame.data[6] = 0xBB
            msg.frame.data[7] = 0xAA
            self.mw.can.Transmit(self.mw.can._can_handle_dict[0], msg, 1)

            crc_code = (0x100 - (reduce(lambda x, y: x + y, msg.frame.data[0:4]) % 256)) % 256
            self.uc.DownloadTextBrowserSig.emit('发送起始地址...\n')
            self.uc.DownloadTextBrowserSig.emit(f' - CRC校验码: {f"0x{{:02X}}".format(crc_code)}\n')

            # 等待反馈CRC校验码
            # self.timer_thread.start()
            # while True:
            #     if self.timer_thread.timeout_flag:
            #         self.uc.DownloadTextBrowserSig.emit('在规定时间内CRC校验失败...')
            #         self.uc.DownloadStartBtnSig.emit()
            #         self.timer_thread.exit()
            #         return
            #     else:
            #         if globalVal.Boot_Msg[0] == crc_code:  # type: UiControl.NewFrame
            #             self.timer_thread.exit()
            #             break
            #         pass

            for index, i in enumerate(data):
                self.uc.DownloadTextBrowserSig.emit(
                    f' 正在下载: {f"0x{{:02X}}".format(int(segment, 16) + 32 * index)} - {f"0x{{:02X}}".format(int(segment, 16) + 32 * (index + 1))}')

                for j in range(5):
                    # msg.frame.data[0] = int(i[j * 8:(j + 1) * 8][0], 16)
                    # msg.frame.data[1] = int(i[j * 8:(j + 1) * 8][1], 16)
                    # msg.frame.data[2] = int(i[j * 8:(j + 1) * 8][2], 16)
                    # msg.frame.data[3] = int(i[j * 8:(j + 1) * 8][3], 16)
                    # msg.frame.data[4] = int(i[j * 8:(j + 1) * 8][4], 16)
                    # msg.frame.data[5] = int(i[j * 8:(j + 1) * 8][5], 16)
                    # msg.frame.data[6] = int(i[j * 8:(j + 1) * 8][6], 16)
                    # msg.frame.data[7] = int(i[j * 8:(j + 1) * 8][7], 16)
                    if j != 4:
                        msg.frame.data[0] = j + 1  # 子包序号
                        msg.frame.data[1] = int(i[j * 7:(j + 1) * 7][0], 16)
                        msg.frame.data[2] = int(i[j * 7:(j + 1) * 7][1], 16)
                        msg.frame.data[3] = int(i[j * 7:(j + 1) * 7][2], 16)
                        msg.frame.data[4] = int(i[j * 7:(j + 1) * 7][3], 16)
                        msg.frame.data[5] = int(i[j * 7:(j + 1) * 7][4], 16)
                        msg.frame.data[6] = int(i[j * 7:(j + 1) * 7][5], 16)
                        msg.frame.data[7] = int(i[j * 7:(j + 1) * 7][6], 16)
                    else:
                        msg.frame.data[0] = j + 1  # 子包序号
                        msg.frame.data[1] = int(i[j * 7:(j + 1) * 7][0], 16)
                        msg.frame.data[2] = int(i[j * 7:(j + 1) * 7][1], 16)
                        msg.frame.data[3] = int(i[j * 7:(j + 1) * 7][2], 16)
                        msg.frame.data[4] = int(i[j * 7:(j + 1) * 7][3], 16)
                        msg.frame.data[5] = 0xAA
                        msg.frame.data[6] = 0xAA
                        msg.frame.data[7] = 0xAA

                    self.mw.can.Transmit(self.mw.can._can_handle_dict[0], msg, 1)

                    self.msleep(10)  # 间隔发送

                while not self.vcu_feedback_flag:
                    print('等待VCU反馈写入完成')
                self.vcu_feedback_flag = False

                cnt += 32
                self.uc.DownloadProgressBarSetSig.emit(cnt / total * 100)
                crc_code = (0x100 - (reduce(lambda x, y: x + y, [int(u, 16) for u in i]) % 256)) % 256
                self.uc.DownloadTextBrowserSig.emit(f'\n - CRC校验码: {f"0x{{:02X}}".format(crc_code)}\n')
                pass

        # msg.frame.data[0] = 0x03
        # msg.frame.data[1] = 0x02
        # msg.frame.data[2] = 0x01
        # msg.frame.data[3] = 0x00
        # msg.frame.data[4] = 0x07
        # msg.frame.data[5] = 0x06
        # msg.frame.data[6] = 0x05
        # msg.frame.data[7] = 0x04
        # self.mw.can.Transmit(self.mw.can._can_handle_dict[0], msg, 1)
        pass
        # self.uc.DownloadStartBtnSig.emit()
        self.mw.vcu_download._isDownloading = False
        self.vcu_feedback_flag = False
        self.uc.DownloadStartBtnSig.emit()

        msg.frame.data[0] = 0xCC
        msg.frame.data[1] = 0xCC
        msg.frame.data[2] = 0xCC
        msg.frame.data[3] = 0xCC
        msg.frame.data[4] = 0xCC
        msg.frame.data[5] = 0xCC
        msg.frame.data[6] = 0xCC
        msg.frame.data[7] = 0xCC

        self.mw.can.Transmit(self.mw.can._can_handle_dict[0], msg, 1)
        self.uc.DownloadTextBrowserSig.emit(f'烧写完成,总耗时为: \n')
        # while True:
        #     time.sleep(0.5)
        # pass


class VcuDownload(object):
    class Xmodem:
        # Xmodem协议控制字符
        SOH = 0x01
        EOT = 0x24
        ACK = 0x06
        NAK = 0x15
        ETB = 0x17
        CAN = 0x18
        C = 0x43

    def __init__(self, mainwindow, ui_control):
        super().__init__()
        self.mw = mainwindow  # type: MainWindow
        self.uc = ui_control
        self._isDownloading = False
        self.hex_file = None  # type: MyHex
        self._download_thread = DownloadThread(self.mw, self.uc)
        self.mw.ui.SelectHexFile_btn.clicked.connect(self.SelectHexFile_Click)
        self.mw.ui.StartDownload_btn.clicked.connect(self.StartDownload_Click)

    def SelectHexFile_Click(self):
        filepath, _ = QFileDialog.getOpenFileName(parent=self.mw, caption='选择Hex文件', filter='Hex Files(*.hex)')
        self.mw.ui.SelectHexFile_le.setText(filepath)
        fileinfo = QFileInfo(filepath)
        filesize = fileinfo.size()
        filelastmodified = fileinfo.lastModified().toString()
        self.mw.ui.HexFileInfo_lb.setText(f'Hex文件大小: {filesize}Bytes, 修改日期: {filelastmodified}')
        self.hex_file = MyHex(filepath)
        print(self.hex_file)
        self.uc.DownloadTextBrowserSig.emit(self.hex_file)
        self._download_thread.hex_file = self.hex_file
        # self.mw.ui.DownloadProgress_pb.setValue(100)

    def StartDownload_Click(self):
        if not self.mw.can._isOpen:
            QMessageBox.information(self.mw, 'CAN设备未开启', '请开启CAN设备后重试！', QMessageBox.Ok)
            return

        file_exist = QFile.exists(self.mw.ui.SelectHexFile_le.text())
        if not file_exist:
            QMessageBox.information(self.mw, 'Hex文件不存在', '所选Hex文件不存在，请检查文件路径是否正确！',
                                    QMessageBox.Ok)
            return
        # self.downloadThreadFunc()
        if not self._isDownloading:
            self.uc.DownloadStartBtnSig.emit()
            self._download_thread.start()
            self._isDownloading = True
        else:
            self.uc.DownloadStartBtnSig.emit()
            self._download_thread.terminate()
            self._isDownloading = False
    pass
