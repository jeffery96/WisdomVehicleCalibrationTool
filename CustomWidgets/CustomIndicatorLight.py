from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from math import *
import sys


class IndicatorLight(QWidget):
    # TODO： 增加三种状态显示功能，灯灭、红灯故障、绿灯正常
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.setWindowTitle("GaugePanel")
        self.setMinimumWidth(150)
        self.setMinimumHeight(150)

        self._sampleTime = 100
        self._lightMode = 0  # 0：常亮  1：闪烁
        self._isLightOn = False  # 灯状态
        self._twinkleInterval = 500
        self._twinkleCurrentState = True  # 灯闪烁当前状态
        self._sampleCount = 0

        self.timer = QTimer()  # 窗口重绘定时器
        self.timer.timeout.connect(self.update)
        self.timer.start(self._sampleTime)

    def setSampleTime(self, sampleTime):
        # 设置控件UI刷新时间
        self._sampleTime = sampleTime

    def setLightOn(self, isChecked):
        self._isLightOn = isChecked

    def setLightMode(self, lightMode):
        self._lightMode = lightMode

    def setTwinkleInterval(self, interval):
        self._twinkleInterval = interval

    def paintEvent(self, event):
        side = min(self.width(), self.height())

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)    # 抗锯齿
        painter.translate(
            self.width() /
            2,
            self.height() /
            2)  # painter坐标系原点移至widget中央
        # 缩放painterwidget坐标系，使绘制的时钟位于widge中央,即钟表支持缩放
        painter.scale(side / 200, side / 200)   # 将坐标系分为100份
        self.drawIndicatorLight(painter)

    def drawIndicatorLight(self, p):
        p.save()
        radius = 100
        # 绘制边框
        # lg = QLinearGradient(-radius, -radius, radius, radius)
        p.rotate(45)
        lg1 = QLinearGradient(-radius, 0, radius, 0)
        lg1.setColorAt(0, QColor(195, 195, 195))
        lg1.setColorAt(1, QColor(70, 70, 70))

        lg2 = QLinearGradient(-radius * 0.92, 0, radius * 0.92, 0)
        lg2.setColorAt(0, QColor(75, 75, 75))
        lg2.setColorAt(1, QColor(188, 188, 188))

        # 灯亮颜色
        lg3 = QLinearGradient(-radius * 0.84, 0, radius * 0.84, 0)
        lg3.setColorAt(0, QColor(0, 255, 0))
        lg3.setColorAt(1, QColor(0, 195, 0))

        # 灯灭颜色
        lg4 = QLinearGradient(-radius * 0.84, 0, radius * 0.84, 0)
        lg4.setColorAt(0, QColor(0, 100, 0))
        lg4.setColorAt(1, QColor(0, 50, 0))
        p.setPen(Qt.NoPen)

        # 绘制边框
        p.setBrush(lg1)
        p.drawEllipse(QPoint(0, 0), radius, radius)
        p.setBrush(lg2)
        p.drawEllipse(QPoint(0, 0), radius*0.92, radius*0.92)

        # 绘制灯
        if self._isLightOn:
            if self._lightMode == 1:
                if self._sampleTime * self._sampleCount % self._twinkleInterval == 0:
                    self._twinkleCurrentState = not self._twinkleCurrentState

                if self._twinkleCurrentState:
                    p.setBrush(lg3)
                else:
                    p.setBrush(lg4)

                p.drawEllipse(QPoint(0, 0), 100 * 0.84, 100 * 0.84)
                self._sampleCount += 1
                pass
            else:
                p.setBrush(lg3)
                p.drawEllipse(QPoint(0, 0), 100 * 0.84, 100 * 0.84)

        else:
            p.setBrush(lg4)
            p.drawEllipse(QPoint(0, 0), 100 * 0.84, 100 * 0.84)

        p.restore()

