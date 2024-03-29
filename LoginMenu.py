import sys, util, os, jsonpickle, UserData

from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from MainMenu import MainMenu


class LoginData:
    def __init__(self, filename: str):
        self.filename = filename
        self.data = self.load_data_from_file()

    def load_data_from_file(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                json_data = file.read()
                data = jsonpickle.decode(json_data)
            return data
        else:
            return []

    def add_data(self, new_data: UserData.UserData):
        self.data.append(new_data)

    def save_data_to_file(self):
        # Create the file if it doesn't exist
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as file:
                pass

        json_data = jsonpickle.encode(self.data)

        with open(self.filename, "w") as file:
            file.write(json_data)


class LoginForm(QWidget):
    def __init__(self, data_class: LoginData):
        super().__init__()
        self.registerMenu = None

        self.mainMenu = MainMenu()
        self.data_class = data_class
        self.setupGUI()

    def setupGUI(self):
        self.resize(500, 300)
        self.setWindowTitle("Login Menu")

        self.Title1 = QLabel("Hello, Enter Your Details To Log In ")
        self.Email = QLineEdit()
        self.Email.setPlaceholderText("Email Address ....")
        self.Password = QLineEdit()
        self.Password.setEchoMode(QLineEdit.EchoMode.Password)
        self.Password.setPlaceholderText("Password ....")
        self.LoginButton = QPushButton("Login")
        self.LoginButton.clicked.connect(self.login)
        self.Title2 = QLabel("Don't Have An Account?")
        self.Register = QPushButton("Register")
        self.Register.clicked.connect(self.OpenRegisterMenu)

        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.Title1)
        vbox1.addWidget(self.Email)
        vbox1.addWidget(self.Password)
        vbox1.addWidget(self.LoginButton)
        vbox1.addWidget(self.Title2)
        vbox1.addWidget(self.Register)
        vbox1.addStretch()

        self.setLayout(vbox1)

    def login(self):
        email = self.Email.text()
        password = self.Password.text()

        if email == "":
            QMessageBox.critical(
                self,
                "Error",
                f"Email Address is empty",
            )
            return

        if password == "":
            QMessageBox.critical(
                self,
                "Error",
                f"password is empty",
            )
            return

        if not util.is_email_valid(email):
            QMessageBox.critical(
                self,
                "Error",
                f"Email {email} is not valid",
            )
            return

        if util.is_login_info_valid(email, password, self.data_class):
            self.mainMenu.exec()
            print("show")
            return
        else:
            QMessageBox.critical(
                self,
                "Error",
                f"Invalid email or password",
            )

    def OpenRegisterMenu(self, checked):
        if self.registerMenu is None:
            self.registerMenu = RegisterMenu(self.data_class)
        self.registerMenu.exec()


class RegisterMenu(QDialog):
    def __init__(self, data_class: LoginData):
        super().__init__()
        self.data_class = data_class

        self.setWindowTitle("Register Menu")

        # Labels and line edits for user input
        self.email_edit = QLineEdit()
        self.email_edit.setPlaceholderText("Email Address...")
        # password
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_edit.setPlaceholderText("Password...")
        # password confirm
        self.password_confirm_edit = QLineEdit()
        self.password_confirm_edit.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_confirm_edit.setPlaceholderText("Confirm Password...")

        # Register button
        self.register_button = QPushButton("Register")
        self.register_button.clicked.connect(self.register)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.email_edit)
        layout.addWidget(self.password_edit)
        layout.addWidget(self.password_confirm_edit)
        layout.addWidget(self.register_button)
        self.setLayout(layout)

    def register(self):
        email = self.email_edit.text()
        password = self.password_edit.text()
        password_confirm = self.password_confirm_edit.text()

        # check if register is valid
        if email == "":
            QMessageBox.critical(
                self,
                "Error",
                f"Email Address is empty",
            )
            return

        if password == "":
            QMessageBox.critical(
                self,
                "Error",
                f"password is empty",
            )
            return

        if password_confirm == "":
            QMessageBox.critical(
                self,
                "Error",
                f"password confirmation is empty",
            )
            return
        if not util.is_email_valid(email):
            QMessageBox.critical(
                self,
                "Error",
                f"Email {email} is not valid",
            )
            return
        if password != password_confirm:
            QMessageBox.critical(
                self,
                "Error",
                f"Password and password confirmation aren't equal",
            )
            return

        # when everything is valid ...
        QMessageBox.information(
            self,
            "Successful",
            f"Your account has been created",
        )

        loginInfoData = UserData.UserData(email, password)
        self.data_class.add_data(loginInfoData)
        self.data_class.save_data_to_file()
        # close dialog after finished
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    data_class = LoginData("login_info.json")
    login = LoginForm(data_class)
    login.show()

    sys.exit(app.exec())
