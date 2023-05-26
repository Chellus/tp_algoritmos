import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QStackedWidget
from PyQt5.uic import loadUi
from ui_menu import Ui_CentralWidget

class MainWindow(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self)
        self.ui = Ui_CentralWidget()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.go_nuevo)

    def go_nuevo(self):
        nuevo = Nuevo()
        widget.addWidget(nuevo)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class Nuevo(QWidget):
    def __init__(self):
        super(Nuevo, self).__init__()
        loadUi("main_window.ui", self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QStackedWidget()
    mainwin = MainWindow()
    widget.addWidget(mainwin)
    widget.show()
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