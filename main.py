import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow
import sqlite3
import time
from threading import Thread
from mydb import *

class Configurator(QtWidgets.QMainWindow):
    def __init__(self):
        super(Configurator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

        # self.ui.comboBox.currentIndexChanged.connect(self.comboBoxTriger) # video_card
        # self.ui.comboBox_2.currentIndexChanged.connect(self.comboBoxTriger) # motherboard
        # self.ui.comboBox_3.currentIndexChanged.connect(self.comboBoxTriger) # ram
        # self.ui.comboBox_4.currentIndexChanged.connect(self.comboBoxTriger) # hdd
        self.ui.comboBox_5.currentIndexChanged.connect(self.comboBox_5_Triger) # cpu
        # self.ui.comboBox_6.currentIndexChanged.connect(self.comboBoxTriger) # cooling
        # self.ui.comboBox_7.currentIndexChanged.connect(self.comboBoxTriger) # ssd
        # self.ui.comboBox_8.currentIndexChanged.connect(self.comboBoxTriger) # power_supply
        # self.ui.comboBox_9.currentIndexChanged.connect(self.comboBoxTriger) # housing

    def init_UI(self):
        self.setWindowTitle('Конфигуратор')


    def comboBox_5_Triger(self, id):
        code = 'cpu'
        text, price, info = get_full_info(code, self.ui.comboBox_5.currentText())

        print(text, price, info)

app = QtWidgets.QApplication([])
application = Configurator()
application.show()
sys.exit(app.exec())        
