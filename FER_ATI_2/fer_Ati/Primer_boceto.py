import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QStackedWidget, QVBoxLayout, QPushButton, QLabel, QFrame, QHBoxLayout, QVBoxLayout, QSpacerItem
from PyQt5.QtWidgets import QApplication, QWidget, QSizePolicy
from PyQt5.QtGui import QCursor, QIcon, QFont
from PyQt5.uic import loadUi
from PyQt5.QtCore import QCoreApplication, Qt, QSize
from PyQt5.QtCore import QMetaObject
from PyQt5 import QtWidgets, uic
app = QtWidgets.QApplication([])

Menu_Principal = uic.loadUi("menu.ui")
Ventana2 = uic.loadUi("main_window.ui")

def gui_menu():
    name = Menu_Principal.lineEdit.text()

def gui_ventana2():
    Ventana2.show()

Menu_Principal.pushButton.clicked.connect(gui_ventana2())
Menu_Principal.show()
sys.exit(app.exec())
