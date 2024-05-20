import sys
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt
from firmy_db import Data

##########################  PAGES  ##########################
from GUI.ui_dashboard import Ui_MainWindow as Ui_Dashboard
from GUI.ui_forgetting_password import Ui_Forgetting_Password
from GUI.ui_login_screen import Ui_Login_Screen
from GUI.ui_register import Ui_Register
from GUI.ui_start_screen import Ui_Start_Screen
##############################################################

from PySide6.QtGui import QBrush, QColor, QPainterPath
from PySide6 import QtCharts

class RoundedBar(QtCharts.QBarSet):
    def __init__(self, label):
        super().__init__(label)

    def paint(self, painter, option, widget):
        for i in range(len(self)):
            rect = self.barRect(i)
            path = QPainterPath()
            path.addRoundedRect(rect, 10, 10)  # Radius of 10
            # painter.fillPath(path, self.brush())

class ChartyApp(QMainWindow, Ui_Dashboard):
    def __init__(self, parent=None):
        super(ChartyApp, self).__init__(parent)
        self.setupUi(self)
        self.minimize_slider_menu_widget.setHidden(True)
        self.bar_graph()

        self.dashboard_minimize_button.clicked.connect(self.switch_to_dashboard_page)
        self.dashboard_button.clicked.connect(self.switch_to_dashboard_page)

        self.analist_minimize_button.clicked.connect(self.switch_to_analist_page)
        self.analist_button.clicked.connect(self.switch_to_analist_page)

        self.performance_minimize_button.clicked.connect(self.switch_to_performance_page)
        self.performance_button.clicked.connect(self.switch_to_performance_page)

        self.bills_minimize_button.clicked.connect(self.switch_to_bills_page)
        self.bills_button.clicked.connect(self.switch_to_bills_page)

        self.wallet_minimize_button.clicked.connect(self.switch_to_wallet_page)
        self.wallet_button.clicked.connect(self.switch_to_wallet_page)

        self.goal_minimize_button.clicked.connect(self.switch_to_goal_page)
        self.goal_button.clicked.connect(self.switch_to_goal_page)

        self.settings_minimize_button.clicked.connect(self.switch_to_settings_page)
        self.settings_button.clicked.connect(self.switch_to_settings_page)

        self.profile_minimize_button.clicked.connect(self.switch_to_profile_page)
        self.profile_button.clicked.connect(self.switch_to_profile_page)

    def switch_to_dashboard_page(self):
        self.main_screen_stacked_widget.setCurrentWidget(self.dashboard_widget)

    def switch_to_analist_page(self):
        self.main_screen_stacked_widget.setCurrentWidget(self.analist_page)

    def switch_to_performance_page(self):
        self.main_screen_stacked_widget.setCurrentWidget(self.performance_page)

    def switch_to_bills_page(self):
        self.main_screen_stacked_widget.setCurrentWidget(self.bills_page)

    def switch_to_wallet_page(self):
        self.main_screen_stacked_widget.setCurrentWidget(self.wallet_page)

    def switch_to_goal_page(self):
        self.main_screen_stacked_widget.setCurrentWidget(self.goal_page)

    def switch_to_settings_page(self):
        self.main_screen_stacked_widget.setCurrentWidget(self.settings_page)

    def switch_to_profile_page(self):
        self.main_screen_stacked_widget.setCurrentWidget(self.profile_page)

    def bar_graph(self):
        series = QtCharts.QBarSeries()
        series.setName("Weekly Comparisons")

        weeks = ["17 Sun", "18 Mon", "19 Tue", "20 Wed", "21 Thu", "22 Fri", "23 Sat"]
        this_week = [18, 120, 35, 25, 3, 45, 40]
        last_week = [12, 24, 31, 28, 5, 40, 24]

        bar_set_this_week = RoundedBar("This Week")
        bar_set_last_week = RoundedBar("Last Week")

        for i in range(len(weeks)):
            bar_set_last_week.append(last_week[i])
            bar_set_this_week.append(this_week[i])

        # Set bar colors using color codes
        bar_set_this_week.setBrush(QBrush(QColor("#ffffff")))  # Beyaz renk
        bar_set_last_week.setBrush(QBrush(QColor("#1B1A55")))  # Koyu mavi renk

        series.append(bar_set_this_week)
        series.append(bar_set_last_week)

        chart = QtCharts.QChart()
        chart.addSeries(series)
        chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

        axis_x = QtCharts.QBarCategoryAxis()
        axis_x.append(weeks)
        axis_x.setLabelsBrush(QBrush(QColor("#FFFFFF")))
        axis_x.setGridLineVisible(False)  # X eksenindeki çizgileri gizle
        chart.addAxis(axis_x, Qt.AlignBottom)
        series.attachAxis(axis_x)

        axis_y = QtCharts.QValueAxis()
        axis_y.setRange(0, max(max(this_week), max(last_week)) + 10)
        axis_y.setLabelsBrush(QBrush(QColor("#FFFFFF")))
        chart.addAxis(axis_y, Qt.AlignLeft)
        series.attachAxis(axis_y)

        # Set background color to light gray
        chart.setBackgroundBrush(QBrush(QColor("#535C91")))  # Açık gri renk

        # Remove title and legend
        chart.setTitle("")
        chart.legend().setVisible(False)

        self.barchart_view.setChart(chart)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Start_Screen()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.show()
        QTimer.singleShot(5000, self.login)

        self.database = Data('firmy_db.xlsx')

    def login(self):
        self.setWindowFlags(Qt.FramelessWindowHint)  # Frameless window for login screen
        self.ui = Ui_Login_Screen()
        self.ui.setupUi(self)
        self.show()
        self.ui.pushButton_3.clicked.connect(self.Click_to_Register)
        self.ui.pushButton_2.clicked.connect(self.check_login)
        self.ui.label_3.clicked.connect(self.forgetting_password)

    def Click_to_Register(self):
        self.setWindowFlags(Qt.FramelessWindowHint)  # Frameless window for register screen
        self.ui = Ui_Register()
        self.ui.setupUi(self)
        self.show()
        self.ui.kayitbuton.clicked.connect(self.register_user)
        #self.ui.kayitbuton.clicked.connect(self.reset_styles) 

    def register_user(self):
        name = self.ui.isim.text()
        surname = self.ui.soyadi.text()
        email = self.ui.mail.text()
        password = self.ui.sifre.text()

        # Reset styles before checking for empty fields
        self.reset_styles()

        if name == "":
            self.ui.isim.setStyleSheet("background-color:white;\n"
                                            "border: 2px solid red;\n"
                                            "border-radius: 5px;")
            return
        elif surname == "":
            self.ui.soyadi.setStyleSheet("background-color:white;\n"
                                            "border: 2px solid red;\n"
                                            "border-radius: 5px;")
            return
        elif email == "":
            self.ui.mail.setStyleSheet("background-color:white;\n"
                                            "border: 2px solid red;\n"
                                            "border-radius: 5px;")
            return
        elif password == "":
            self.ui.sifre.setStyleSheet("background-color:white;\n"
                                            "border: 2px solid red;\n"
                                            "border-radius: 5px;")
            return
        
            # Check if the checkbox is checked
        if not self.ui.onayla.isChecked():
            # Display an error message or raise an exception
            self.ui.onayla.setStyleSheet("background-color: transparent; color: red; font-weight: bold;")
            print("Hata: Onay kutusu işaretlenmemiş!")
            return

        # Veritabanı sınıfındaki update_db fonksiyonunu çağırarak kullanıcıyı kaydet
        reslut = self.database.update_db(name, surname, email, password)
        if reslut == 1:
            print("Kayıt Başarılı")
            self.login()
        elif reslut == 0:
            self.ui.mail.setStyleSheet("background-color:white;\n"
                                            "border: 2px solid red;\n"
                                            "border-radius: 5px;")
        else:
            print("Hata!")


        
    
    def reset_styles(self):
        self.ui.isim.setStyleSheet(u"background-color:white;\n"
"border-radius:5px;")
        self.ui.soyadi.setStyleSheet(u"background-color:white;\n"
"border-radius:5px;")
        self.ui.mail.setStyleSheet(u"background-color:white;\n"
"border-radius:5px;")
        self.ui.sifre.setStyleSheet(u"background-color:white;\n"
"border-radius:5px;")
        self.ui.onayla.setStyleSheet("background-color: transparent; color: white")

    def check_login(self):
        email = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        result = Data().sign_db(email, password)
        if result == True:
            self.open_dashboard()
        else:
            print("Şifre Hatalı")


    def open_dashboard(self):
        self.close()  # Mevcut pencereyi kapat
        self.dashboard_window = ChartyApp()  # Yeni dashboard penceresini oluştur
        self.dashboard_window.setWindowFlags(Qt.Window)  # Normal window for dashboard screen
        self.dashboard_window.showMaximized()  # Dashboard ekranını maximize yap

    def forgetting_password(self):
        self.setWindowFlags(Qt.FramelessWindowHint)  # Frameless window for forgetting password screen
        self.ui = Ui_Forgetting_Password()
        self.ui.setupUi(self)
        self.show()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    app.exec()
