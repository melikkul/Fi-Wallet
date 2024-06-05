import sys
from PySide6.QtCore import QTimer, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from firmy_db import Data
from widget_manager import WidgetManager
from user_db import User
import time

##########################  PAGES  ##########################
from GUI.ui_dashboard import Ui_MainWindow as Ui_Dashboard
from GUI.ui_forgetting_password import Ui_Forgetting_Password
from GUI.ui_login_screen import Ui_Login_Screen
from GUI.ui_register import Ui_Register
from GUI.ui_start_screen import Ui_Start_Screen
from GUI.ui_logout import Ui_Logout
from GUI.ui_add_account import Ui_Add_Account
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
            path.addRoundedRect(rect, 10, 10)
            painter.fillPath(path, self.brush())

class LogoutDialog(QDialog, Ui_Logout):
    def __init__(self, parent=None):
        super(LogoutDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.pushButton.clicked.connect(self.close)
        self.pushButton_2.clicked.connect(self.close_application)

    def close_application(self):
        self.database = Data('firmy_db.xlsx')
        user = self.database.get_keep_me_signed_in_user()
        email = user['eMail']
        self.database.reset_keep_me_sign(email)
        self.parent().close()
        self.close()

class Add_Account(QMainWindow, Ui_Add_Account):
    def __init__(self, parent=None):
        super(Add_Account, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.card_cancel_button.clicked.connect(self.close)
        self.cash_cancel_button.clicked.connect(self.close)
        self.card_save_button.clicked.connect(self.save_card_account)
        self.cash_save_button.clicked.connect(self.save_cash_account)

    def save_card_account(self):
        print('save card account')

    def save_cash_account(self):
        print('save cash account')




class ChartyApp(QMainWindow, Ui_Dashboard):
    def __init__(self, parent=None):
        super(ChartyApp, self).__init__(parent)
        self.setupUi(self)
        self.minimize_slider_menu_widget.setHidden(True)
        self.bar_graph()

        self.toolButton.clicked.connect(self.open_addaccount)

        # Widget yönetimini sağlamak için WidgetManager örneği oluştur
        self.widget_manager = WidgetManager(self.wallet_page)

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

        self.logout_button.clicked.connect(self.open_logout)

    def add_new_widget(self):
        self.widget_manager.add_widget()

    def open_addaccount(self):
        self.dashboard_window = Add_Account()
        self.dashboard_window.setWindowFlags(Qt.FramelessWindowHint)
        self.dashboard_window.show()


    def open_logout(self):
        self.dashboard_button.setEnabled(False)
        self.analist_button.setEnabled(False)
        self.performance_button.setEnabled(False)
        self.bills_button.setEnabled(False)
        self.wallet_button.setEnabled(False)
        self.goal_button.setEnabled(False)
        self.settings_button.setEnabled(False)
        self.profile_button.setEnabled(False)
        self.thema_button.setEnabled(False)
        self.profiles_combobox.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        self.slider_button.setEnabled(False)
        self.search_line_edit.setEnabled(False)
        self.search_button.setEnabled(False)
        self.notification_button.setEnabled(False)
        self.calculator_button.setEnabled(False)

        self.logout_dialog = LogoutDialog(self)
        self.logout_dialog.exec()

        self.dashboard_button.setEnabled(True)
        self.analist_button.setEnabled(True)
        self.performance_button.setEnabled(True)
        self.bills_button.setEnabled(True)
        self.wallet_button.setEnabled(True)
        self.goal_button.setEnabled(True)
        self.settings_button.setEnabled(True)
        self.profile_button.setEnabled(True)
        self.thema_button.setEnabled(True)
        self.profiles_combobox.setEnabled(True)
        self.pushButton_2.setEnabled(True)
        self.slider_button.setEnabled(True)
        self.search_line_edit.setEnabled(True)
        self.search_button.setEnabled(True)
        self.notification_button.setEnabled(True)
        self.calculator_button.setEnabled(True)


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

        bar_set_this_week.setBrush(QBrush(QColor("#ffffff")))
        bar_set_last_week.setBrush(QBrush(QColor("#1B1A55")))

        series.append(bar_set_this_week)
        series.append(bar_set_last_week)

        chart = QtCharts.QChart()
        chart.addSeries(series)
        chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

        axis_x = QtCharts.QBarCategoryAxis()
        axis_x.append(weeks)
        axis_x.setLabelsBrush(QBrush(QColor("#FFFFFF")))
        axis_x.setGridLineVisible(False)
        chart.addAxis(axis_x, Qt.AlignBottom)
        series.attachAxis(axis_x)

        axis_y = QtCharts.QValueAxis()
        axis_y.setRange(0, max(max(this_week), max(last_week)) + 10)
        axis_y.setLabelsBrush(QBrush(QColor("#FFFFFF")))
        chart.addAxis(axis_y, Qt.AlignLeft)
        series.attachAxis(axis_y)

        chart.setBackgroundBrush(QBrush(QColor("#535C91")))

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
        QTimer.singleShot(5000, self.check_auto_login)

        self.database = Data('firmy_db.xlsx')

    def check_auto_login(self):
        user = self.database.get_keep_me_signed_in_user()
        if user is not None:
            email = user['eMail']
            keep_me_sign_count = user['keepMeSignCount']
            
            if keep_me_sign_count < 5:
                self.database.increment_keep_me_sign_count(email)
                self.open_dashboard()
                return
            else:
                self.database.reset_keep_me_sign(email)
        
        self.login()

    def login(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.ui = Ui_Login_Screen()
        self.ui.setupUi(self)
        self.show()
        self.ui.pushButton_3.clicked.connect(self.Click_to_Register)
        self.ui.pushButton_2.clicked.connect(self.check_login)
        self.ui.label_3.mouseReleaseEvent = self.forgetting_password

    def Click_to_Register(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.ui = Ui_Register()
        self.ui.setupUi(self)
        self.show()
        self.ui.kayitbuton.clicked.connect(self.register_user)

    def register_user(self):
        name = self.ui.isim.text()
        surname = self.ui.soyadi.text()
        email = self.ui.mail.text()
        password = self.ui.sifre.text()
        keep = self.ui.onayla.isChecked()

        self.reset_styles_register()

        if name == "":
            self.ui.isim.setStyleSheet("background-color:white;\n"
                                       "border: 2px solid red;\n"
                                       "border-radius: 5px;")
            self.ui.error.setText("Please enter your name!")
            return

        if surname == "":
            self.ui.soyadi.setStyleSheet("background-color:white;\n"
                                         "border: 2px solid red;\n"
                                         "border-radius: 5px;")
            self.ui.error.setText("Please enter your surname!")
            return

        if email == "":
            self.ui.mail.setStyleSheet("background-color:white;\n"
                                       "border: 2px solid red;\n"
                                       "border-radius: 5px;")
            self.ui.error.setText("Please enter your email!")
            return

        if password == "":
            self.ui.sifre.setStyleSheet("background-color:white;\n"
                                        "border: 2px solid red;\n"
                                        "border-radius: 5px;")
            self.ui.error.setText("Please enter your password!")
            return
        
        if keep == False:
            self.ui.onayla.setStyleSheet("background-color:transparent;\n"
                                         "color: red;\n"
                                       "font-weight: bold;\n")
            self.ui.error.setText("Please check the box!")
            return

        data_instance = Data('firmy_db.xlsx')
        result = data_instance.regis_db(email)
        if result == 0:
            self.ui.error.setText("User registration successful!")
            data_instance.update_db(name, surname, email, password)
            self.login()
        else:
            self.ui.error.setText("This email is already registered!")
            userid = User("user_db.xlsx")
            userid.save_user_id(result)
            self.login()

        

    def reset_styles_register(self):
        self.ui.isim.setStyleSheet(u"background-color:white;\n"
                                   "border-radius:5px;")
        self.ui.soyadi.setStyleSheet(u"background-color:white;\n"
                                     "border-radius:5px;")
        self.ui.mail.setStyleSheet(u"background-color:white;\n"
                                   "border-radius:5px;")
        self.ui.sifre.setStyleSheet(u"background-color:white;\n"
                                    "border-radius:5px;")
        self.ui.onayla.setStyleSheet("background-color: transparent; color: white")
        self.ui.error.setText("")

    def check_login(self):
        email = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()

        self.reset_stylesheet_login()

        if email == "":
            self.ui.lineEdit.setStyleSheet("background-color:white;\n"
                                           "border: 2px solid red;\n"
                                           "border-radius: 5px;")
            self.ui.error.setText("Please enter your email!")
            return

        elif password == "":
            self.ui.lineEdit_2.setStyleSheet("background-color:white;\n"
                                             "border: 2px solid red;\n"
                                             "border-radius: 5px;")
            self.ui.error.setText("Please enter your password!")
            return

        keep = self.ui.checkBox_2.isChecked()

        data_instance = Data('firmy_db.xlsx')
        result = data_instance.sign_db(email, password)
        if result:
            data_instance.update_keep_me_signed_in(email, keep)
            self.open_dashboard()
        else:
            self.ui.error.setText("Incorrect email or password!")

    def reset_stylesheet_login(self):
        self.ui.lineEdit_2.setStyleSheet(u"background-color:white;\n"
                                         "border-radius:5px;")
        self.ui.lineEdit.setStyleSheet(u"background-color:white;\n"
                                       "border-radius:5px;")
        self.ui.error.setText("")

    def open_dashboard(self):
        self.close()
        self.dashboard_window = ChartyApp()
        self.dashboard_window.setWindowFlags(Qt.Window)
        self.dashboard_window.showMaximized()

    def forgetting_password(self, event):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.ui = Ui_Forgetting_Password()
        self.ui.setupUi(self)
        self.show()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    app.exec()
