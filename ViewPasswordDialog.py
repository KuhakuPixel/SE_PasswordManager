
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from UserData import UserPasswordInfo

class ViewPasswordDialog(QDialog):
    def __init__(self, userPasswordInfo: UserPasswordInfo):
        super().__init__()
        layout = QVBoxLayout(self)
        dictionary_contents = userPasswordInfo.__dict__
        for k, v in dictionary_contents.items():
            # font for attribute name 
            attributeNameFont = QFont()
            attributeNameFont.setBold(True)
            attributeName = QLabel(f"{k}:           ")
            attributeName.setFont(attributeNameFont)
            attributeValue = QLabel(f"{v}")
            # add column
            current_item_layout = QHBoxLayout()
            current_item_layout.addWidget(attributeName)
            current_item_layout.addWidget(attributeValue)
            # now finally add the attribute
            layout.addLayout(current_item_layout)

        self.setLayout(layout)
    
