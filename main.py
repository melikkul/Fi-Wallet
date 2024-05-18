import sys
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import Qt
from firmy_db import UserRegistration as db
import time

##########################  PAGES  ##########################
from GUI.ui_dashboard import Ui_MainWindow
from charts import ChartyApp
from GUI.ui_forgetting_password import Ui_Forgetting_Password
from GUI.ui_login_screen import Ui_Login_Screen
from GUI.ui_register import Ui_Register
from GUI.ui_start_screen import Ui_Start_Screen
##############################################################

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()      
        self.ui = Ui_Start_Screen()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.show()
        self.db = db("firmy_database_register.xlsx")  # FirmyDB sınıfından bir örnek oluşturuluyor
        self.db.setup_database()  # Veritabanı kurulumu
        QTimer.singleShot(5000, self.login)

    def login(self):
        self.ui = Ui_Login_Screen()
        self.ui.setupUi(self)
        self.show()
        self.ui.pushButton_3.clicked.connect(self.Click_to_Register)
        self.ui.pushButton_2.clicked.connect(self.dashboard)
        self.ui.label_3.clicked.connect(self.forgetting_password)
        username = "example_username"
        password = "example_password"
        if self.db.authenticate_user(username, password):
            print("Kullanıcı girişi başarılı.")
        else:
            print("Kullanıcı girişi başarısız.")

    def Click_to_Register(self):
        self.ui = Ui_Register()
        self.ui.setupUi(self)
        self.show()
        self.ui.kayitbuton.clicked.connect(self.register_user)
        
    def register_user(self):
        first_name = self.ui.isim.text()
        last_name = self.ui.soyadi.text()
        email = self.ui.mail.text()
        password = self.ui.sifre.text()
        self.db.register_user(first_name, last_name, email, password)

        

    def dashboard(self):
        self.ui = ChartyApp()
        self.ui.setupUi(self)
        self.ui.showMaximized()


    def forgetting_password(self):
        self.ui = Ui_Forgetting_Password()
        self.ui.setupUi(self)
        self.show()
        
    def closeEvent(self, event):
        self.db.close()  # Uygulama kapatıldığında veritabanı bağlantısı kapatılıyor
                                        

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    app.exec()
    
