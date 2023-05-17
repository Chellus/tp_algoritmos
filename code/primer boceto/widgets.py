import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QStackedWidget, QVBoxLayout, QPushButton, QDialog
from PyQt5.uic import loadUi
#Pantalla principal

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()#para llamarse a si mismo 
        loadUi("main.ui",self)#carga la primera pantalla, o ventana principal por ah
        self.btn_nuevo.clicked.connect(self.go_nuevo)#aca usamos el boton para ir a la segunda pantalla
        # self.setWindowTitle("ORGANIFILL")tITULO SUPUESTAMENTE
    def go_nuevo(self):#funcion que llama el boton
        s_2=Nuevo()#se inicializa aca la segunda pantalla
        widget.addWidget(s_2)#se suma el widget
        widget.setCurrentIndex(widget.currentIndex()+1)#aca lo que hacemos es aumentar en uno ya que va a una pantalla despues
    
#esta es la clase de la segunda pantalla
class Nuevo(QWidget):
    def __init__(self):#jijija
        super(Nuevo,self).__init__()
        loadUi("pantalla_nuevo.ui",self)#carga la segunda pantalla
        self.btn_volver.clicked.connect(self.go_main)#aca usamos el boton para ir a la segunda pantalla
        self.btn_nueva_forma.clicked.connect(self.crear_forma)#botón que crea nueva forma
    def go_main(self):#funcion que llama el boton
        mainwin=MainWindow()#se inicializa aca la segunda pantalla
        widget.addWidget(mainwin)#se suma el widget
        widget.setCurrentIndex(widget.currentIndex()-1)

    def crear_forma(self):#muestra el formulario
        formulario = Formulario()
        formulario.exec_()

class Formulario(QDialog):
    def __init__(self):
        super(Formulario,self).__init__()
        loadUi("form_dependencia.ui", self)
         
#main
app=QApplication(sys.argv)
widget=QStackedWidget()
mainwin=MainWindow()

widget.addWidget(mainwin)
formulario = loadUi("form_dependencia.ui")
widget.setFixedHeight(700) 
widget.setFixedWidth(800)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Saliendo")