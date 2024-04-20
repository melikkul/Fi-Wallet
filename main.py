import sys
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import Qt
import time

##########################  PAGES  ##########################
from ui_dashboard import Ui_Dashboard
from ui_forgetting_password import Ui_Forgetting_Password
from ui_login_screen import Ui_Login_Screen
from ui_register import Ui_Register
from ui_start_screen import Ui_Start_Screen
##############################################################



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()      
        self.ui = Ui_Start_Screen()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.show()
        QTimer.singleShot(5000, self.login)

    def login(self):
        self.ui = Ui_Login_Screen()
        self.ui.setupUi(self)
        self.show()
        self.ui.pushButton_3.clicked.connect(self.Click_to_Register)
        self.ui.pushButton_2.clicked.connect(self.dashboard)
        self.ui.label_3.clicked.connect(self.forgetting_password)

    def Click_to_Register(self):
        self.ui = Ui_Register()
        self.ui.setupUi(self)
        self.show()

    def dashboard(self):
        self.ui = Ui_Dashboard()
        self.ui.setupUi(self)
        self.show()
        self.showMaximized()
        self.ui.maximize_screen_button.stateChanged.connect(self.toggle_maximize)


    def toggle_maximize(self, state):
        if state == 2:
            self.showMaximized()  # Eğer buton işaretlenmişse ekranı tam ekran yap
        else:
            self.resize(1280, 720)  # Belirtilen boyutlara yeniden boyutlandır



    def forgetting_password(self):
        self.ui = Ui_Forgetting_Password()
        self.ui.setupUi(self)
        self.show()
        
                                        

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    app.exec()