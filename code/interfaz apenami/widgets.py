import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QStackedWidget, QVBoxLayout, QPushButton, QDialog
from PyQt5.uic import loadUi
#Pantalla principal
class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi("screen1.ui",self)#carga la primera pantalla
        self.pushButton.clicked.connect(self.go_screen2)#aca usamos el boton para ir a la segunda pantalla
    def go_screen2(self):#funcion que llama el boton
        s_2=screen2()#se inicializa aca la segunda pantalla
        widget.addWidget(s_2)#se suma el widget
        widget.setCurrentIndex(widget.currentIndex()+1)#aca lo que hacemos es aumentar en uno ya que va a una pantalla despues
#esta es la clase de la segunda pantalla
class screen2(QDialog):
    def __init__(self):
        super(screen2,self).__init__()
        loadUi("screen2.ui",self)#carga la segunda pantalla

#main
app=QApplication(sys.argv)
widget=QStackedWidget()
mainwin=MainWindow()
widget.addWidget(mainwin)
widget.setFixedHeight(300)
widget.setFixedWidth(400)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Saliendo")