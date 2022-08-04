from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox

import sys, os, os.path

def ShowErorMassageBox(text):
    msg = QMessageBox()
    msg.setWindowTitle("Ошибка")
    icondir = ""
    if hasattr(sys, "_MEIPASS"): icondir = os.path.join(sys._MEIPASS, './icons/warning.png')
    else: icondir = './UserInterface/icons/warning.png'
    msg.setWindowIcon(QIcon(icondir))
    msg.setInformativeText(text)
    msg.setStyleSheet("min-width: 200px;")
    msg.exec_()

def ShowInformationMassageBox(text):
    msg = QMessageBox()
    msg.setWindowTitle("Информация")
    icondir = ""
    if hasattr(sys, "_MEIPASS"): icondir = os.path.join(sys._MEIPASS, './icons/info.png')
    else: icondir = './UserInterface/icons/info.png'
    msg.setWindowIcon(QIcon(icondir))
    msg.setInformativeText(text)
    msg.setStyleSheet("min-width: 200px;")
    msg.exec_()