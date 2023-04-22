import sys, util

from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *

class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.w = None
        self.setupGUI()

    def setupGUI(self):
        self.resize(500,300)
        self.setWindowTitle("Login Menu")

        self.Title1 = QLabel("Hello, Enter Your Details To Log In ")
        self.Email = QLineEdit()
        self.Email.setPlaceholderText("Email Address ....")
        self.Password = QLineEdit()
        self.Password.setEchoMode(QLineEdit.EchoMode.Password)
        self.Password.setPlaceholderText("Password ....")
        self.LoginButton = QPushButton('Login')
        self.LoginButton.clicked.connect(self.login)
        self.Title2 = QLabel("Don't Have An Account?")
        self.Register = QPushButton('Register')
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
    
    def OpenRegisterMenu(self, checked):
        if self.w is None :
            self.w = RegisterMenu()
        self.w.show()

class RegisterMenu(QWidget):
    def __init__(self):
        super().__init__()

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
    
if __name__ == "__main__":
    app = QApplication(sys.argv)

    login = LoginForm()
    login.show()

    sys.exit(app.exec())