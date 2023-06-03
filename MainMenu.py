import sys, util

from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from Add_Password_Menu import PasswordMenuType, PasswordMenu
from UserData import UserPasswordInfo


class MainMenu(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PASS VAULT")
        self.CreateTable()
        """
        for i in range(50):
            self.TableAddItem(
                userPasswordInfo=UserPasswordInfo(
                    title="MyTitle",
                    url="https://google.com",
                    username="MyUsername",
                    password="Nooobbb",
                ),
            )
        """
        self.addPasswordMenu = PasswordMenu(passwordMenuType=PasswordMenuType.ADD)

    def onAddPassword(self):
        print("Adding Password")
        userPasswordInfo = self.addPasswordMenu.exec()
        if userPasswordInfo == None:
            print("User Password info None")
            return
        else:
            self.TableAddItem(userPasswordInfo=userPasswordInfo)

        print("Getting: ")
        print(userPasswordInfo.__dict__)

    def CreateTable(self):
        self.resize(1000, 500)
        self.AddPassword = QPushButton("Add Password")
        self.AddPassword.clicked.connect(self.onAddPassword)
        self.SettingButton = QPushButton("Setting")
        self.Premium = QPushButton("Premium")

        self.Search = QLineEdit()
        self.Search.setPlaceholderText("Search Password....")

        self.table = QTableWidget()
        self.header_labels = ["Title", "Username", " "]
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(self.header_labels)

        self.table.setShowGrid(False)
        # set fixed height for row
        # in order to look better :D
        # https://stackoverflow.com/questions/19304653/how-to-set-row-height-of-qtableview
        # self.table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Fixed)
        self.table.verticalHeader().setDefaultSectionSize(50)
        # ===============================================
        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        self.vBox = QVBoxLayout()
        self.hBox = QHBoxLayout()
        self.hBox.addWidget(self.AddPassword)
        self.hBox.addWidget(self.SettingButton)
        self.hBox.addWidget(self.Premium)
        self.hBox.addWidget(self.Search)
        self.vBox.addLayout(self.hBox)
        self.vBox.addWidget(self.table)
        self.setLayout(self.vBox)

    def TableAddItem(self, userPasswordInfo: UserPasswordInfo):
        newRowIndex = self.table.rowCount()
        self.table.insertRow(newRowIndex)
        # ============= view,edit, delete button ============
        viewEditDeleteButton = QWidget()
        buttonLayout = QHBoxLayout(viewEditDeleteButton)
        View = QPushButton("View")
        Edit = QPushButton("Edit")
        Delete = QPushButton("Delete")
        buttonLayout.addWidget(View)
        buttonLayout.addWidget(Edit)
        buttonLayout.addWidget(Delete)
        # add information
        self.table.setItem(newRowIndex, 0, QTableWidgetItem(userPasswordInfo.title))
        self.table.setItem(newRowIndex, 1, QTableWidgetItem(userPasswordInfo.username))
        # add button
        self.table.setCellWidget(newRowIndex, 2, viewEditDeleteButton)
        # ===================================================
        # resize
        # self.table.verticalHeaderItem(newRowIndex).


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # sys.exit(app.exec())
    sys.exit(MainMenu().exec())
