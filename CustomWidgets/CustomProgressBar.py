from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from math import *
import sys


class ProgressBar(QWidget):
    # TODO: 完善进度条功能

    unitChanged = Signal()

    def __init__(self, parent=None):
        super(ProgressBar, self).__init__(parent=parent)
        # self.resize(500, 500)
        # self.setFixedWidth(500)
        # self.setMinimumWidth(300)
        # self.setMinimumHeight(300)

        # self._pbForeColor = 'white'
        # self._pbBackColor = 'rgb(52,59,72)'
        # self._lbColor = 'black'

        self._initValue = 0
        self._unit = ''

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
        self.lb.setMinimumSize(50, 0)
        self.lb.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        self.lb.setStyleSheet(
            'font-family: "Segoe UI";font-size: 16px; font-weight: bold; color: rgb(210,210,210); margin-right: 0px;'
        )
        self.hBox = QHBoxLayout(self)
        self.hBox.addWidget(self.pb)
        self.hBox.addWidget(self.lb)
        self.hBox.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.setAttribute(Qt.WA_StyledBackground)
        self.hBox.setContentsMargins(0, 0, 0, 0)

        self.unitChanged.connect(self.__setText)
        self.pb.valueChanged.connect(self.__setText)

        self.pb.setValue(self._initValue)

    def setMinMaxValue(self, min, max):
        self.pb.setMinimum(min)
        self.pb.setMaximum(max)

    def setUnit(self, unit):
        self._unit = unit
        self.unitChanged.emit()

    def setValue(self, value):
        self.pb.setValue(value)

    def __setText(self):
        self.lb.setText(str(self.pb.value()) + self._unit)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    pb = ProgressBar()
    pb.show()
    sys.exit(app.exec_())
