from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QStandardItemModel, QStandardItem
from PyQt5 import uic

import pickle

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
        item, confirmed = QInputDialog.getText(self, "Add Item", "New Item:", QLineEdit.Normal, "")

        if confirmed and not item.isspace():
            item = QStandardItem(item)
            self.model.appendRow(item)

    def remove_item(self):
        if len(self.listView.selectedIndexes()) != 0:
            selected = self.listView.selectedIndexes()[0]

            dialog = QMessageBox()
            dialog.setText(f"Are you sure you want to remove '{selected.data()}'? This action can not be undone.")
            dialog.addButton(QPushButton("Yes"), QMessageBox.YesRole)
            dialog.addButton(QPushButton("No"), QMessageBox.NoRole)

            if dialog.exec_() == 0:
                self.model.removeRow(selected.row())

    def open_file(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Todo Files (*.todo)", options=options)
        if filename != "":
            with open(filename, "rb") as f:
                item_list = pickle.load(f)
                self.model = QStandardItemModel()
                self.listView.setModel(self.model)
                for item in item_list:
                    self.model.appendRow(QStandardItem(item))

    def save_file(self):
        item_list = []
        for x in range(self.model.rowCount()):
            item_list.append(self.model.item(x).text())
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Todo Files (*.todo)", options=options)
        if filename != "":
            with open(filename, "wb") as f:
                pickle.dump(item_list, f)

app = QApplication([])
window = MyGUI()
app.exec_()