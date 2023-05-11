import sys
from PyQt5 import QtWidgets, uic

app = QtWidgets.QApplication([])

Menu_Principal = uic.loadUi("Pantalla_Principal.ui")
Ventana2 = uic.loadUi("Pantalla2.ui")

def gui_menu():
    name = Menu_Principal.lineEdit.text()

def gui_ventana2():
    Ventana2.show()

Menu_Principal.pushButton_1.clicked.connect(gui_ventana2)
Menu_Principal.pushButton_4.clicked.connect(QtWidgets.QApplication.quit)  # Conectamos el botón de salida a la función quit() de QApplication
Menu_Principal.show()

sys.exit(app.exec())
