from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from math import *
import sys


class ProgressBar(QWidget):

    def __init__(self, parent=None):
        super(ProgressBar, self).__init__(parent=parent)
        # self.resize(500, 500)
        # self.setFixedWidth(500)
        # self.setMinimumWidth(300)
        # self.setMinimumHeight(300)

        # self._pbForeColor = 'white'
        # self._pbBackColor = 'rgb(52,59,72)'
        # self._lbColor = 'black'

        self._initValue = 36

        self.pb = QProgressBar(self)
        self.pb.setSizePolicy(
            QSizePolicy(
                QSizePolicy.Expanding,
                QSizePolicy.Expanding))
        self.pb.setTextVisible(False)
        self.setStyleSheet(
            'QProgressBar{background-color: rgb(52,59,72); border: 0px solid rgb(52,59,72); border-radius: 6px;}'
            'QProgressBar::chunk{background-color: #05B8CC; border-radius: 6px;}')
        self.lb = QLabel(self)
        self.lb.setStyleSheet(
            'font-family: "Segoe UI";font-size: 18px; font-weight: bold; color: rgb(210,210,210); margin-right: 0px;'
        )
        self.hBox = QHBoxLayout(self)
        self.hBox.addWidget(self.pb)
        self.hBox.addWidget(self.lb)
        self.hBox.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.setAttribute(Qt.WA_StyledBackground)
        self.hBox.setContentsMargins(0, 0, 0, 0)
        self.pb.valueChanged.connect(self.__setText)

        self.pb.setValue(self._initValue)

    def setMaximum(self, max):
        self.pb.setMaximum(max)

    def setMaximum(self, min):
        self.pb.setMinimum(min)

    def setValue(self, value):
        self.pb.setValue(value)

    def __setText(self):
        self.lb.setText(str(self.pb.value()) + '℃')

