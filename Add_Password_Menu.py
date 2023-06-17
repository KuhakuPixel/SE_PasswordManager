import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QMessageBox,
    QHBoxLayout,
    QDialog,
)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
import random
import string
from enum import Enum
from UserData import UserPasswordInfo


class PasswordMenuType(Enum):
    EDIT = 0
    ADD = 1


class PasswordMenu(QDialog):
    RANDOM_PASSWORD_LENGTH = 20

    def __init__(self,passwordMenuType: PasswordMenuType, existingInfo = UserPasswordInfo):
        super().__init__()
        self.existingInfo = existingInfo
        self.passwordMenuType = passwordMenuType
        self.setWindowTitle("Password Menu")

        # Create widgets
        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText("Title")

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")

        # password
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        # url
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("URL")

        # generate
        self.generate_button = QPushButton()
        self.generate_button.setIcon(QIcon("icon.png"))  # Replace with your icon file
        self.generate_button.clicked.connect(self.generate_password)

        # password and generate
        self.password_and_generate_layout = QHBoxLayout()
        self.password_and_generate_layout.addWidget(self.password_input)
        self.password_and_generate_layout.addWidget(self.generate_button)

        self.add_button = QPushButton("Add Password")
        self.add_button.clicked.connect(self.add_password)

        self.edit_button = QPushButton("Edit")
        self.edit_button.clicked.connect(self.edit_password)

        # Set layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.title_input)
        layout.addWidget(self.username_input)
        layout.addLayout(self.password_and_generate_layout)
        layout.addWidget(self.url_input)
        if passwordMenuType == PasswordMenuType.ADD:
            layout.addWidget(self.add_button)

        if passwordMenuType == PasswordMenuType.EDIT:
            layout.addWidget(self.edit_button)
            self.title_input.setText(existingInfo.title)
            self.username_input.setText(existingInfo.username)
            self.password_input.setText(existingInfo.password)
            self.url_input.setText(existingInfo.url)

        self.setLayout(layout)

    def get_UserPasswordInfo(self):
        title = self.title_input.text()
        username = self.username_input.text()
        password = self.password_input.text()
        url = self.url_input.text()

        # if one of the input is missing, just return None
        if title == "" or username == "" or password == "" or url == "":
            return None
        else:
            return UserPasswordInfo(
                password=password,
                title=title,
                url=url,
                username=username,
            )
    def is_valid_input(self):
        if self.get_UserPasswordInfo() == None:
            return False
        else:
            return True

    def add_password(self):
        """
        # Add password logic here
        """
        if self.is_valid_input():
            QMessageBox.information(
                self, "Password Successfully Added", "Password has been added successfully."
            )
            self.close()
        else:
            QMessageBox.warning(self, "Invalid Input", "Please fill in all fields.")


    def edit_password(self):
        # Add password logic here

        if self.is_valid_input():
            QMessageBox.information(self, "Success", "Password Successfully Edited")
            self.close()
        else:
            QMessageBox.warning(self, "Invalid Input", "Please fill in all fields.")
    

    def exec(self) -> UserPasswordInfo:
        """
        will return the value after dialog is closed
        this basically override Dialog.exec() ?
        I use similliar method like QMessageBox.exec()
        where it returns value
        """
        super().exec()
        return self.get_UserPasswordInfo()

    def generate_password(self):
        self.password_input.setText("Generated")
        generated_password = ""
        for i in range(self.RANDOM_PASSWORD_LENGTH):
            generated_password += random.choice(
                string.ascii_uppercase + string.ascii_lowercase + string.digits
            )
        print("generated password: " + generated_password)
        self.password_input.setText(generated_password)

    def clear_inputs(self):
        self.title_input.clear()
        self.username_input.clear()
        self.password_input.clear()
        self.url_input.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordMenu(passwordMenuType=PasswordMenuType.EDIT)
    window.show()
    sys.exit(app.exec())
