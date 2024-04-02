from PySide6.QtWidgets import *
from ui_login_screen import Ui_Login_Screen 
from PySide6.QtCore import Qt
from PySide6.QtGui import * 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        
        # Arayüzü oluşturmak için Ui_MainWindow sınıfından bir örnek oluşturun
        self.ui = Ui_Login_Screen()
        # Arayüzü setupUi metoduyla ayarlayın
        self.ui.setupUi(self)
        
        # Ana pencereyi göstermek için show metodunu çağırın
        self.show()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    app.exec()