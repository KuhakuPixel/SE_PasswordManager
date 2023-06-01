import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox, QHBoxLayout,QDialog
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
import random
import string

class PasswordMenu(QDialog):
    RANDOM_PASSWORD_LENGTH = 20
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Password Menu")

        # Create widgets
        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText('Title')

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText('Username')

        # password
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText('Password')
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText('URL')

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

        # Set layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.title_input)
        layout.addWidget(self.username_input)
        layout.addLayout(self.password_and_generate_layout)
        layout.addWidget(self.url_input)
        layout.addWidget(self.add_button)

        self.setLayout(layout)

    def add_password(self):
        # Add password logic here
        QMessageBox.information(self, "Password Successfully Added", "Password has been added successfully.")
        self.clear_inputs()
    def generate_password(self):
        self.password_input.setText("Generated")
        generated_password = ""
        for i in range(self.RANDOM_PASSWORD_LENGTH):
            generated_password += random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
        print("generated password: " + generated_password)
        self.password_input.setText(generated_password)

    def clear_inputs(self):
        self.title_input.clear()
        self.username_input.clear()
        self.password_input.clear()
        self.url_input.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordMenu()
    window.show()
    sys.exit(app.exec())

