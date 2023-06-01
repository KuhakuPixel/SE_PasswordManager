import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt

class EditPasswordMenu(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Password Menu")

        # Create widgets
        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText('Title')

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText('Username')

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText('Password')
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText('URL')

        self.generate_button = QPushButton()
        self.generate_button.setIcon(QIcon("download.png"))  # Replace with your icon file

        self.edit_button = QPushButton("Edit")
        self.edit_button.clicked.connect(self.edit_password)

        # Set layout
        layout = QVBoxLayout()
        layout.addWidget(self.title_input)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_input)
        layout.addWidget(self.url_input)
        layout.addWidget(self.edit_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def edit_password(self):
        # Add password logic here
        QMessageBox.information(self, "Success", "Password Successfully Edited")
        self.clear_inputs()

    def clear_inputs(self):
        self.title_input.clear()
        self.username_input.clear()
        self.password_input.clear()
        self.url_input.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EditPasswordMenu()
    window.show()
    sys.exit(app.exec())
