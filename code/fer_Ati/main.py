import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from ui_menu import Ui_CentralWidget

class MainWindow(QWidget):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_CentralWidget()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

 '''
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QStackedWidget, QVBoxLayout, QPushButton, QLabel, QFrame, QHBoxLayout, QVBoxLayout, QSpacerItem
from PyQt5.QtWidgets import QApplication, QWidget, QSizePolicy
from PyQt5.QtGui import QCursor, QIcon, QFont
from PyQt5.uic import loadUi
from PyQt5.QtCore import QCoreApplication, Qt, QSize
from PyQt5.QtCore import QMetaObject
 
 '''