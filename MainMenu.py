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
        
        
        self.Search = QLineEdit()
        self.Search.setPlaceholderText("Search Password....")
        self.table = QTableWidget()
        self.table.setRowCount(10)
        self.table.setColumnCount(10)
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)      
 
        self.vBox = QVBoxLayout()
        self.vBox.addWidget(self.AddPassword)
        self.vBox.addWidget(self.Setting)
        self.vBox.addWidget(self.Premium)
        self.vBox.addWidget(self.Search)
        self.vBox.addWidget(self.table)
        self.setLayout(self.vBox)

app = QApplication(sys.argv)
window = MainMenu()
sys.exit(app.exec())