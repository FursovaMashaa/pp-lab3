import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import numb_1
import numb_2
import numb_3
import numb_4
import numb_5

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Lab3")


app = QApplication(sys.argv)

window = MainWindow()
window = QWidget()
window.show()

app.exec()