from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QMessageBox,
)
import sys
import re
import util


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


app = QApplication(sys.argv)
menu = RegisterMenu()
menu.show()
sys.exit(app.exec())
