from PySide2.QtCore import QTimer
import time


def testfunc():
    print('a')


timer = QTimer()
timer.timeout.connect(testfunc)
timer.setInterval(1000)
timer.start()

print(timer.isActive())
# timer.stop()
# print(timer.isActive())
while True:
    time.sleep(0.5)
    print(timer.isActive())

