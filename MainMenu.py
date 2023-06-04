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
        # self.userInfos = []
        
        '''
        for i in range(50):
            self.TableAddItem(
                userPasswordInfo=UserPasswordInfo(
                    title="MyTitle",
                    url="https://google.com",
                    username="MyUsername",
                    password="Nooobbb",
                ),
            )
        '''

    def onAddPassword(self):
        print("Adding Password")
        
        userPasswordInfo = PasswordMenu(passwordMenuType=PasswordMenuType.ADD).exec()
        if userPasswordInfo == None:
            print("User Password info None")
            return
        else:
            self.TableAddItem(userPasswordInfo=userPasswordInfo, row = None)
            # self.userInfos.append(userPasswordInfo)

        print("Getting: ")
        print(userPasswordInfo.__dict__)
    
    def onEditPassword(self):
        print("Editing Password")
        button = self.sender()
        if button is not None:
            row = self.table.indexAt(button.parent().pos()).row()
            # existInfo = self.userInfos[row]
            userPasswordInfo = PasswordMenu(passwordMenuType=PasswordMenuType.EDIT).exec()
            if userPasswordInfo is None:
                print("User Password info None")
                return
            else:
                # self.userInfos[row] = userPasswordInfo
                self.TableAddItem(userPasswordInfo=userPasswordInfo, row=row)

    def onDeletePassword(self):
        print("Deleting Password")
        button = self.sender()
        if button is not None:
            row = self.table.indexAt(button.parent().pos()).row()

            if row >= 0 and row < self.table.rowCount():
            # Remove the cell widget (buttons) in the row
                viewEditDeleteButton = self.table.cellWidget(row, 2)
                if viewEditDeleteButton is not None:
                    self.table.removeCellWidget(row, 2)
                    viewEditDeleteButton.deleteLater()

            # Remove the row items
                self.table.removeRow(row)
                # self.userInfos.pop(row)

            

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

    def TableAddItem(self, userPasswordInfo: UserPasswordInfo, row):
        if row is not None and row < self.table.rowCount():
            newRowIndex = row
        else:
            newRowIndex = self.table.rowCount()
            self.table.insertRow(newRowIndex)
        
        # Remove the existing widgets in the row, if any
        for column in range(self.table.columnCount()):
            item = self.table.item(newRowIndex, column)
            if item is not None:
                self.table.takeItem(newRowIndex, column)

        # ============= view,edit, delete button ============
        viewEditDeleteButton = QWidget()
        buttonLayout = QHBoxLayout(viewEditDeleteButton)
        View = QPushButton("View")
        Edit = QPushButton("Edit")
        Delete = QPushButton("Delete")
        # Create a partial function to capture the current row index
        onEditClicked = lambda _: self.onEditPassword()
        onDeleteClicked = lambda _: self.onDeletePassword()

        Edit.clicked.connect(onEditClicked)
        Delete.clicked.connect(onDeleteClicked)
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
