from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
import sys

class RegisterMenu(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Register Menu')

        # Labels and line edits for user input
        self.email_edit = QLineEdit()
        self.email_edit.setPlaceholderText('Email Address...')
        self.password_edit = QLineEdit()
        self.password_edit.setPlaceholderText('Password...')
        self.confirm_edit = QLineEdit()
        self.confirm_edit.setPlaceholderText('Confirm Password...')

        # Register button
        self.register_button = QPushButton('Register')
        self.register_button.clicked.connect(self.register)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.email_edit)
        layout.addWidget(self.password_edit)
        layout.addWidget(self.confirm_edit)
        layout.addWidget(self.register_button)
        self.setLayout(layout)

    def register(self):
        email = self.email_edit.text()
        password = self.password_edit.text()
        confirm = self.confirm_edit.text()

app = QApplication(sys.argv)
menu = RegisterMenu()
menu.show()
sys.exit(app.exec())