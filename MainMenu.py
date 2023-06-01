import sys, util

from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *

class MainMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PASS VAULT")
        self.CreateTable()
        self.show()

    def CreateTable(self):
        self.resize(1000,500)
        self.AddPassword = QPushButton('+')
        self.SettingButton = QPushButton('+')
        self.Premium = QPushButton('+')

        self.Search = QLineEdit()
        self.Search.setPlaceholderText("Search Password....")

        self.table = QTableWidget()
        self.table.setRowCount(10)
        self.table.setColumnCount(4)
        
        for row in range(self.table.rowCount()):
            self.Button = QWidget()
            self.buttonLayout = QHBoxLayout(self.Button)
            self.View = QPushButton('View')
            self.Edit = QPushButton('Edit')
            self.Delete = QPushButton('Delete')
            self.buttonLayout.addWidget(self.View)
            self.buttonLayout.addWidget(self.Edit)
            self.buttonLayout.addWidget(self.Delete)
            self.table.setCellWidget(row, 3, self.Button)

        self.table.horizontalHeader().setVisible(False)
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

app = QApplication(sys.argv)
window = MainMenu()
sys.exit(app.exec())