from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QStandardItemModel, QStandardItem
from PyQt5 import uic

class MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi("todogui.ui", self)
        self.show()

        self.setWindowTitle("Todo List v1.0.0")
        self.model = QStandardItemModel()
        self.listView.setModel(self.model)

        self.plusButton.clicked.connect(self.add_item)
        self.minusButton.clicked.connect(self.remove_item)
        self.actionOpen.triggered.connect(self.open_file)
        self.actionSave.triggered.connect(self.save_file)

    def add_item(self):
        print("Add")

    def remove_item(self):
        print("Remove")

    def open_file(self):
        print("Open")

    def save_file(self):
        print("Save")

app = QApplication([])
window = MyGUI()
app.exec_()