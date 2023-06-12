import sys, util

from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from Add_Password_Menu import PasswordMenuType, PasswordMenu
from UserData import UserPasswordInfo
from ViewPasswordDialog import ViewPasswordDialog



class MainMenu(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PASS VAULT")
        self.CreateTable()
        
        '''
        for i in range(50):
            self.TableAddItem(
                userPasswordInfo=UserPasswordInfo(
                    title="MyTitle",
                    url="https://google.com",
                    username="MyUsername",
                    password="Nooobbb",
                ),
                row= i
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

        print("Getting: ")
        print(userPasswordInfo.__dict__)
    
    def onViewPassword(self, userPasswordInfo: UserPasswordInfo):
        viewPasswordDialog = ViewPasswordDialog(userPasswordInfo=userPasswordInfo)
        viewPasswordDialog.exec()
        """
        messageBox = QMessageBox()
        messageBox.setWindowTitle("View Content")
        dictionary_contents = userPasswordInfo.__dict__
        messageBox.setText(f"{dictionary_contents}")
        messageBox.exec()
        """

    def onEditPassword(self, existInfo : UserPasswordInfo):
        print("Editing Password")
        button = self.sender()
        if button is not None:
            row = self.table.indexAt(button.parent().pos()).row()
            userPasswordInfo = PasswordMenu(passwordMenuType=PasswordMenuType.EDIT, existingInfo=existInfo).exec()
            if userPasswordInfo is None:
                print("User Password info None")
                return
            else:
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

    def CreateTable(self):
        self.resize(1000, 500)
        self.HeaderLogo = QLabel()
        logoPixmap = QPixmap("./assets/Logo.png")
        self.HeaderLogo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.HeaderLogo.setStyleSheet("background-color: #ffffff")
        self.HeaderLogo.setPixmap(logoPixmap.scaledToWidth(150))
        self.AddPassword = QPushButton()
        self.AddPassword.clicked.connect(self.onAddPassword)
        self.SettingButton = QPushButton()
        self.Premium = QPushButton()

        self.AddPassword.setFixedSize(20, 20)
        self.AddPassword.setStyleSheet(
            """
            QPushButton {
                border-image: url(./assets/AddButton.png);
                background-color: transparent;
            }
            """
        )
        self.SettingButton.setFixedSize(20,20)
        self.SettingButton.setStyleSheet("border-image : url(./assets/SettingButton.png);")
        self.Premium.setFixedSize(20,20)
        self.Premium.setStyleSheet("border-image : url(./assets/PremiumButton.png);")

        self.Search = QLineEdit()
        self.Search.setStyleSheet(
            """
            border: 2px groove #202020;
            border-radius: 7px;
            background-color: #ffffff;
            color: #9c9c9c;
            height: 15px;
            padding: 2px;
            """
        )
        self.Search.setPlaceholderText("Search Password....")
        # search icon
        searchIcon = QIcon("./assets/Search.png")
        searchIcon.addPixmap(searchIcon.pixmap(QSize(5, 5)).scaled(5, 5), QIcon.Mode.Active, QIcon.State.On)
        searchAction = QAction(searchIcon, "", self.Search)
        
        self.Search.addAction(searchAction, QLineEdit.ActionPosition.LeadingPosition)

        # Create a layout for the search components
        searchLayout = QHBoxLayout()
        searchLayout.addWidget(self.Search)
        searchLayout.setContentsMargins(400,0,0,0)

        # Adjust the size of the search icon
        # searchAction.setIcon(searchIcon)

        # Adjust the padding to make room for the search icon/

        self.table = QTableWidget()
        self.header_labels = ["Title", "Username", " "]
        self.table.setColumnCount(3)
        self.table.setColumnWidth(2,100)
        self.table.setHorizontalHeaderLabels(self.header_labels)

        self.table.setShowGrid(False)
        # set fixed height for row
        # in order to look better :D
        # https://stackoverflow.com/questions/19304653/how-to-set-row-height-of-qtableview
        # self.table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Fixed)
        self.table.verticalHeader().setDefaultSectionSize(50)
        # ===============================================
        # self.table.horizontalHeader().setDefaultSectionSize(460)
        self.table.horizontalHeader().setSectionResizeMode(0,QHeaderView.ResizeMode.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(1,QHeaderView.ResizeMode.Stretch)
        self.table.horizontalHeader().setDefaultSectionSize(250)

        self.vBox = QVBoxLayout()
        self.hBox = QHBoxLayout()
        self.hBox.setSpacing(20)
        self.hBox.setContentsMargins(50,10,50,10)
        self.hBox.addWidget(self.AddPassword)
        self.hBox.addWidget(self.SettingButton)
        self.hBox.addWidget(self.Premium)
        self.hBox.addLayout(searchLayout)

        frame = QFrame()
        frame.setStyleSheet("background-color: #7286D3;")
        frame.setLayout(self.hBox)

        self.vBox.addWidget(self.HeaderLogo)
        self.vBox.addWidget(frame)
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
        # viewEditDeleteButton.setGeometry(0,0,300,100)
        buttonLayout = QHBoxLayout(viewEditDeleteButton)
        buttonLayout.setContentsMargins(50,0,50,0)
        # buttonLayout.minimumSize(20)
        buttonLayout.setSpacing(10)
    
        View = QPushButton()
        Edit = QPushButton()
        Delete = QPushButton()
        
        View.setFixedSize(45, 35)
        View.setStyleSheet(
            """
            QPushButton {
                border-image: url(./assets/ViewButton.png);
            }
            QPushButton:hover {
                border-image: url(./assets/InvertedViewButton.png);
            }
            """
        )
        #kalo ada ide hover yg lebih bagus ganti aja
        Edit.setFixedSize(45,35)
        Edit.setStyleSheet(
            """
            QPushButton {
                border-image: url(./assets/EditButton.png);
            }
            QPushButton:hover {
                border-image: url(./assets/InvertedEditButton.png);
            }
            """
        )
        Delete.setFixedSize(45,35)
        Delete.setStyleSheet(
            """
            QPushButton {
                border-image: url(./assets/DeleteButton.png);
            }
            QPushButton:hover {
                border-image: url(./assets/InvertedDeleteButton.png);
            }
            """
        )
        # Create a partial function to capture the current row index
        onViewClicked = lambda _: self.onViewPassword(userPasswordInfo)
        onEditClicked = lambda _: self.onEditPassword(userPasswordInfo)
        onDeleteClicked = lambda _: self.onDeletePassword()

        View.clicked.connect(onViewClicked)
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
