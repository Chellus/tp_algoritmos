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

 