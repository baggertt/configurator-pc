import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow
import description
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

        self.ui.comboBox.currentIndexChanged.connect(self.comboBox_Triger) # video_card
        self.ui.comboBox_2.currentIndexChanged.connect(self.comboBox_2_Triger) # motherboard
        self.ui.comboBox_3.currentIndexChanged.connect(self.comboBox_3_Triger) # ram
        self.ui.comboBox_4.currentIndexChanged.connect(self.comboBox_4_Triger) # hdd
        self.ui.comboBox_5.currentIndexChanged.connect(self.comboBox_5_Triger) # cpu
        self.ui.comboBox_6.currentIndexChanged.connect(self.comboBox_6_Triger) # cooling
        self.ui.comboBox_7.currentIndexChanged.connect(self.comboBox_7_Triger) # ssd
        self.ui.comboBox_8.currentIndexChanged.connect(self.comboBox_8_Triger) # power_supply

        self.video_card_price = 0
        self.motherboard_price = 0
        self.ram_price = 0
        self.hdd_price = 0
        self.cpu_price = 0
        self.cooling_price = 0
        self.ssd_price = 0
        self.power_supply_price = 0

        self.window = QtWidgets.QMainWindow()
        self.ui2 = description.Ui_MainWindow()
        self.ui2.setupUi(self.window)
        self.window.setWindowTitle('Описание')

        self.ui.pushButton.clicked.connect(self.open_description_window)
        self.ui.pushButton_2.clicked.connect(self.open_description_window_2)
        self.ui.pushButton_3.clicked.connect(self.open_description_window_3)
        self.ui.pushButton_4.clicked.connect(self.open_description_window_4)
        self.ui.pushButton_5.clicked.connect(self.open_description_window_5)
        self.ui.pushButton_9.clicked.connect(self.open_description_window_6)
        self.ui.pushButton_6.clicked.connect(self.open_description_window_7)
        self.ui.pushButton_7.clicked.connect(self.open_description_window_8)

        
    def init_UI(self):
        self.setWindowTitle('Конфигуратор')

    def comboBox_Triger(self, id):
        code = 'video_card'
        text, price, info = get_full_info(code, self.ui.comboBox.currentText())

        self.ui.label_10.setText(str(text))
        self.ui.label_11.setText(str(price))
        self.ui.label_12.setText(str(text))

        self.ui2.label.setText(str(info))

        self.video_card_price = price

        self.updatePrice()


    def comboBox_2_Triger(self, id):
        code = 'motherboard'
        text, price, info = get_full_info(code, self.ui.comboBox_2.currentText())

        self.ui.label_16.setText(str(text))
        self.ui.label_14.setText(str(price))
        self.ui.label_15.setText(str(text))

        self.ui2.label.setText(str(info))

        self.motherboard_price = price
        self.updatePrice()

    def comboBox_3_Triger(self, id):
        code = 'ram'
        text, price, info = get_full_info(code, self.ui.comboBox_3.currentText())

        self.ui.label_22.setText(str(text))
        self.ui.label_17.setText(str(price))
        self.ui.label_18.setText(str(text))

        self.ui2.label.setText(str(info))

        self.ram_price = price
        self.updatePrice()

    def comboBox_4_Triger(self, id):
        code = 'hdd'
        text, price, info = get_full_info(code, self.ui.comboBox_4.currentText())

        self.ui.label_28.setText(str(text))
        self.ui.label_20.setText(str(price))
        self.ui.label_21.setText(str(text))

        self.ui2.label.setText(str(info))

        self.hdd_price = price
        self.updatePrice()

    def comboBox_5_Triger(self, id):
        code = 'cpu'
        text, price, info = get_full_info(code, self.ui.comboBox_5.currentText())

        self.ui.label_34.setText(str(text))
        self.ui.label_23.setText(str(price))
        self.ui.label_24.setText(str(text))

        self.ui2.label.setText(str(info))

        self.cpu_price = price
        self.updatePrice()

    def comboBox_6_Triger(self, id):
        code = 'cooling'
        text, price, info = get_full_info(code, self.ui.comboBox_6.currentText())

        self.ui.label_36.setText(str(text))
        self.ui.label_26.setText(str(price))
        self.ui.label_27.setText(str(text))

        self.ui2.label.setText(str(info))

        self.cooling_price = price
        self.updatePrice()

    def comboBox_7_Triger(self, id):
        code = 'ssd'
        text, price, info = get_full_info(code, self.ui.comboBox_7.currentText())

        self.ui.label_40.setText(str(text))
        self.ui.label_29.setText(str(price))
        self.ui.label_30.setText(str(text))

        self.ui2.label.setText(str(info))
        
        self.ssd_price = price
        self.updatePrice()

    def comboBox_8_Triger(self, id):
        code = 'power_supply'
        text, price, info = get_full_info(code, self.ui.comboBox_8.currentText())

        self.ui.label_42.setText(str(text))
        self.ui.label_32.setText(str(price))
        self.ui.label_33.setText(str(text))

        self.ui2.label.setText(str(info))

        self.power_supply_price = price
        self.updatePrice()


    def updatePrice(self):
        price = float(self.video_card_price) + float(self.motherboard_price) + float(self.ram_price) + float(self.hdd_price) + float(self.cpu_price) + float(self.cooling_price) + float(self.ssd_price) + float(self.power_supply_price)
        self.ui.label_38.setText(str(price))

    def open_description_window(self):
        code = 'video_card'
        text, price, info = get_full_info(code, self.ui.comboBox.currentText())

        self.ui2.label.setText(str(info))
        self.window.show()

    def open_description_window_2(self):
        code = 'motherboard'
        text, price, info = get_full_info(code, self.ui.comboBox_2.currentText())

        self.ui2.label.setText(str(info))
        self.window.show()

    def open_description_window_3(self):
        code = 'ram'
        text, price, info = get_full_info(code, self.ui.comboBox_3.currentText())
        
        self.ui2.label.setText(str(info))
        self.window.show()

    def open_description_window_4(self):
        code = 'hdd'
        text, price, info = get_full_info(code, self.ui.comboBox_4.currentText())

        self.ui2.label.setText(str(info))
        self.window.show()

    def open_description_window_5(self):
        code = 'cpu'
        text, price, info = get_full_info(code, self.ui.comboBox_5.currentText())

        self.ui2.label.setText(str(info))
        self.window.show()

    def open_description_window_6(self):
        code = 'cooling'
        text, price, info = get_full_info(code, self.ui.comboBox_6.currentText())

        self.ui2.label.setText(str(info))
        self.window.show()

    def open_description_window_7(self):
        code = 'ssd'
        text, price, info = get_full_info(code, self.ui.comboBox_7.currentText())

        self.ui2.label.setText(str(info))
        self.window.show()

    def open_description_window_8(self):
        code = 'power_supply'
        text, price, info = get_full_info(code, self.ui.comboBox_8.currentText())

        self.ui2.label.setText(str(info))
        self.window.show()


app = QtWidgets.QApplication([])
application = Configurator()
application.show()
sys.exit(app.exec())        
