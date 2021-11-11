from PyQt5.QtWidgets import *
from PyQt5.QtGui import Qfont, QStandardItemModel, QStandardItem
from PyQt5 import uic

class MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi("todogui.ui", self)