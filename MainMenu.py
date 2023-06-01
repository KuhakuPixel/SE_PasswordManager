import sys, util

from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *

class MainMenu(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PASS VAULT")
        self.CreateTable()
        # self.show()

    def CreateTable(self):
        self.resize(1000,500)
        self.AddPassword = QPushButton('Add Password')
        self.SettingButton = QPushButton('Setting')
        self.Premium = QPushButton('Premium')

        self.Search = QLineEdit()
        self.Search.setPlaceholderText("Search Password....")

        self.table = QTableWidget()
        self.table.setRowCount(10)
        self.table.setColumnCount(3)
        
        for row in range(self.table.rowCount()):
            self.Button = QWidget()
            self.buttonLayout = QHBoxLayout(self.Button)
            self.View = QPushButton('View')
            self.Edit = QPushButton('Edit')
            self.Delete = QPushButton('Delete')
            self.buttonLayout.addWidget(self.View)
            self.buttonLayout.addWidget(self.Edit)
            self.buttonLayout.addWidget(self.Delete)
            self.table.setCellWidget(row, 2, self.Button)

        self.header_labels = ["Title", "Username", " "]
        self.table.setHorizontalHeaderLabels(self.header_labels)

        self.table.setShowGrid(False)
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)      
 
        self.vBox = QVBoxLayout()
        self.hBox = QHBoxLayout()
        self.hBox.addWidget(self.AddPassword)
        self.hBox.addWidget(self.SettingButton)
        self.hBox.addWidget(self.Premium)
        self.hBox.addWidget(self.Search)
        self.vBox.addLayout(self.hBox)
        self.vBox.addWidget(self.table)
        self.setLayout(self.vBox)

"""
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainMenu()
    sys.exit(app.exec())
"""
