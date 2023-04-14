import sys

from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *

class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupGUI()

    def setupGUI(self):
        self.resize(500,300)
        self.setWindowTitle("Login Menu")

        self.Title1 = QLabel("Hello, Enter Your Details To Log In ")
        self.Email = QLineEdit()
        self.Email.setPlaceholderText("Email Address ....")
        self.Password = QLineEdit()
        self.Password.setPlaceholderText("Password ....")
        self.LoginButton = QPushButton('Login')
        self.Title2 = QLabel("Don't Have An Account?")
        self.Register = QPushButton('Register')

        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.Title1)
        vbox1.addWidget(self.Email)
        vbox1.addWidget(self.Password)
        vbox1.addWidget(self.LoginButton)
        vbox1.addWidget(self.Title2)
        vbox1.addWidget(self.Register)
        vbox1.addStretch()

        self.setLayout(vbox1)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)

    login = LoginForm()
    login.show()

    app.exec()