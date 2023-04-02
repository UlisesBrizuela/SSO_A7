'''
Acttividad 7 - Seminario de solucion de problemas de sistemas operativos
Brizuela Arias Ulises Israel
'''
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QThread, pyqtSignal

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('ACT7 - PRODUCTOR CONSUMIDOR 1')
        self.setWindowIcon(QIcon(str('Appicon.ico')))
        self.setFixedSize(800,800)
    

    
if __name__ == '__main__':
    app =  QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())