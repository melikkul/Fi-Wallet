from GUI.ui_add_account import Ui_Add_Account
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QGridLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QToolButton, QMainWindow
from PySide6.QtCore import QSize , QRect, QCoreApplication
from PySide6.QtGui import QFont

class Add_Account(Ui_Add_Account, QMainWindow):
    def __init__(self):
        self.setupUi(self)