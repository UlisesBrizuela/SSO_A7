'''
Acttividad 7 - Seminario de solucion de problemas de sistemas operativos
Brizuela Arias Ulises Israel
'''
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QFrame, QTextBrowser
from PyQt5.QtGui import QPixmap, QIcon, QFont
from PyQt5.QtCore import QThread, pyqtSignal, QRect

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
#       VENTANA PRINCIPAL
        self.setWindowTitle('ACT7 - PRODUCTOR - CONSUMIDOR 1')
        self.setWindowIcon(QIcon(str('Appicon.ico')))
        self.setFixedSize(980,544)
#       LABELS INDICATIVOS DE POSISION DE CAJON DE ESTACIONAMIENTO
        self.label_1 = QLabel(self)
        self.label_1.setGeometry(QRect(9, 6, 121, 20))
        self.label_1.setText("CAJON 1")
        self.label_2 = QLabel(self)
        self.label_2.setGeometry(QRect(149, 6, 121, 20))
        self.label_2.setText("CAJON 2")
        self.label_3 = QLabel(self)
        self.label_3.setGeometry(QRect(289, 6, 121, 20))
        self.label_3.setText("CAJON 3")
        self.label_4 = QLabel(self)
        self.label_4.setGeometry(QRect(429, 6, 121, 20))
        self.label_4.setText("CAJON 4")
        self.label_5 = QLabel(self)
        self.label_5.setGeometry(QRect(9, 186, 121, 20))
        self.label_5.setText("CAJON 5")
        self.label_6 = QLabel(self)
        self.label_6.setGeometry(QRect(149, 186, 121, 20))
        self.label_6.setText("CAJON 6")
        self.label_7 = QLabel(self)
        self.label_7.setGeometry(QRect(289, 186, 121, 20))
        self.label_7.setText("CAJON 7")
        self.label_8 = QLabel(self)
        self.label_8.setGeometry(QRect(429, 186, 121, 20))
        self.label_8.setText("CAJON 8")
        self.label_9 = QLabel(self)
        self.label_9.setGeometry(QRect(10, 366, 121, 20))
        self.label_9.setText("CAJON 9")
        self.label_10 = QLabel(self)
        self.label_10.setGeometry(QRect(150, 366, 121, 20))
        self.label_10.setText("CAJON 10")
        self.label_11 = QLabel(self)
        self.label_11.setGeometry(QRect(290, 366, 121, 20))
        self.label_11.setText("CAJON 11")
        self.label_12 = QLabel(self)
        self.label_12.setGeometry(QRect(430, 366, 121, 20))
        self.label_12.setText("CAJON 12")
        labels = [self.label_1, self.label_2, self.label_3, self.label_4, self.label_5, self.label_6, self.label_7, self.label_8, self.label_9, self.label_10, self.label_11, self.label_12]
        for label in labels:
            font = QFont()
            font.setPointSize(10)
            font.setBold(True)
            label.setFont(font)
#       LABELS DE CAJONES DE ESTACIONAMIENTO
        self.cajon_1 = QLabel(self)
        self.cajon_1.setGeometry(QRect(5, 26, 130, 150))
        self.cajon_2 = QLabel(self)
        self.cajon_2.setGeometry(QRect(145, 26, 130, 150))
        self.cajon_3 = QLabel(self)
        self.cajon_3.setGeometry(QRect(285, 26, 130, 150))
        self.cajon_4 = QLabel(self)
        self.cajon_4.setGeometry(QRect(425, 26, 130, 150))
        self.cajon_5 = QLabel(self)
        self.cajon_5.setGeometry(QRect(5, 206, 130, 150))
        self.cajon_6 = QLabel(self)
        self.cajon_6.setGeometry(QRect(145, 206, 130, 150))
        self.cajon_7 = QLabel(self)
        self.cajon_7.setGeometry(QRect(285, 206, 130, 150))
        self.cajon_8 = QLabel(self)
        self.cajon_8.setGeometry(QRect(425, 206, 130, 150))
        self.cajon_9 = QLabel(self)
        self.cajon_9.setGeometry(QRect(5, 386, 130, 150))
        self.cajon_10 = QLabel(self)
        self.cajon_10.setGeometry(QRect(145, 386, 130, 150))
        self.cajon_11 = QLabel(self)
        self.cajon_11.setGeometry(QRect(285, 386, 130, 150))
        self.cajon_12 = QLabel(self)
        self.cajon_12.setGeometry(QRect(425, 386, 130, 150))
        cajones =[self.cajon_1, self.cajon_2, self.cajon_3, self.cajon_4, self.cajon_5, self.cajon_6, self.cajon_7, self.cajon_8, self.cajon_9, self.cajon_10, self.cajon_11, self.cajon_12]
        for cajon in cajones:
            cajon.setFrameShape(QFrame.WinPanel)
            cajon.setFrameShadow(QFrame.Sunken)
            cajon.setPixmap(QPixmap('libre.png').scaled(100, 100))
#       CAJON DE LOG DEL SISTEMA
#'''
        self.label_log = QLabel(self)
        self.label_log.setGeometry(QRect(570, 10, 401, 20))
        self.label_log.setText('SYSTEM LOG')
        self.text_log = QTextBrowser(self)
        self.text_log.setGeometry(QRect(570, 30, 401, 511))

#'''



    
if __name__ == '__main__':
    app =  QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())