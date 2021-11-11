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
        item, confirmed = QInputDialog.getText(self, "Add Item", "New Item:", QLineEdit.Normal, "")

        if confirmed and not item.isspace():
            item = QStandardItem(item)
            self.model.appendRow(item)

    def remove_item(self):
        if len(self.listView.selectedIndexes()) != 0:
            selected = self.listView.selectedIndexes()[0]

            dialog = QMessageBox()
            dialog.setText(f"Are you sure you want to remove '{selected.data()}'?")
            dialog.addButton(QPushButton("Yes"), QMessageBox.YesRole)
            dialog.addButton(QPushButton("No"), QMessageBox.NoRole)

            if dialog.exec_() == 0:
                self.model.removeRow(selected.row())

    def open_file(self):
        print("Open")

    def save_file(self):
        print("Save")

app = QApplication([])
window = MyGUI()
app.exec_()