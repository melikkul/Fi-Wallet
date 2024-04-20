# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboard.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)
import dashboard_rc

class Ui_Dashboard(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setStyleSheet(u"background-color: transparent;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.maximize_slider_menu_widget = QWidget(self.centralwidget)
        self.maximize_slider_menu_widget.setObjectName(u"maximize_slider_menu_widget")
        self.maximize_slider_menu_widget.setStyleSheet(u"QWidget{\n"
"	background-color:#1B1A55;\n"
"}\n"
"QPushButton{\n"
"	height:50px;\n"
"	weight:220px;\n"
"	border:none;\n"
"	border-top-left-radius:5px;\n"
"	border-bottom-left-radius:5px;\n"
"}\n"
"QCheckBox{\n"
"	height:50px;\n"
"	weight:220px;\n"
"}\n"
"QPushButton:checked{\n"
"	background-color:#9290C3;\n"
"	color: #9290C3;\n"
"	font-weight:bold;\n"
"}\n"
"\n"
"")
        self.verticalLayout_5 = QVBoxLayout(self.maximize_slider_menu_widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, -1, 0, -1)
        self.profiles_combobox = QComboBox(self.maximize_slider_menu_widget)
        self.profiles_combobox.addItem("")
        self.profiles_combobox.addItem("")
        self.profiles_combobox.setObjectName(u"profiles_combobox")
        font = QFont()
        font.setFamilies([u"Poppins"])
        font.setPointSize(14)
        self.profiles_combobox.setFont(font)
        self.profiles_combobox.setStyleSheet(u"QComboBox\n"
"{\n"
"	color:white;\n"
"	background-color:#9290C3;\n"
"}\n"
"QComboBox:editable {\n"
"    background-color: white;\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"	border:none;\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"	image: url(:/img/img/chevron-down.svg);\n"
"	width:32px;\n"
"	height:32px;\n"
"	margin-right:20px;\n"
"}\n"
"QComboBox::down-arrow:on\n"
"{	\n"
"	image: url(:/img/img/chevron-up.svg);\n"
"	width:32px;\n"
"	height:32px;\n"
"	margin-right:20px;\n"
"}")

        self.verticalLayout_5.addWidget(self.profiles_combobox)

        self.verticalSpacer_3 = QSpacerItem(20, 61, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.dashboard_button = QPushButton(self.maximize_slider_menu_widget)
        self.dashboard_button.setObjectName(u"dashboard_button")
        self.dashboard_button.setFont(font)
        self.dashboard_button.setStyleSheet(u"color:white;\n"
"text-align: left;\n"
"padding-left: 10px;")
        icon = QIcon()
        icon.addFile(u":/img/img/grid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.dashboard_button.setIcon(icon)
        self.dashboard_button.setIconSize(QSize(32, 32))
        self.dashboard_button.setCheckable(True)
        self.dashboard_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.dashboard_button)

        self.analist_button = QPushButton(self.maximize_slider_menu_widget)
        self.analist_button.setObjectName(u"analist_button")
        self.analist_button.setFont(font)
        self.analist_button.setStyleSheet(u"color:white;\n"
"text-align: left;\n"
"padding-left: 10px;")
        icon1 = QIcon()
        icon1.addFile(u":/img/img/analist.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.analist_button.setIcon(icon1)
        self.analist_button.setIconSize(QSize(32, 32))
        self.analist_button.setCheckable(True)
        self.analist_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.analist_button)

        self.performance_button = QPushButton(self.maximize_slider_menu_widget)
        self.performance_button.setObjectName(u"performance_button")
        self.performance_button.setFont(font)
        self.performance_button.setStyleSheet(u"color:white;\n"
"text-align: left;\n"
"padding-left: 10px;")
        icon2 = QIcon()
        icon2.addFile(u":/img/img/performance.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.performance_button.setIcon(icon2)
        self.performance_button.setIconSize(QSize(32, 32))
        self.performance_button.setCheckable(True)
        self.performance_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.performance_button)

        self.bills_button = QPushButton(self.maximize_slider_menu_widget)
        self.bills_button.setObjectName(u"bills_button")
        self.bills_button.setFont(font)
        self.bills_button.setStyleSheet(u"color:white;\n"
"text-align: left;\n"
"padding-left: 10px;")
        icon3 = QIcon()
        icon3.addFile(u":/img/img/bills.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bills_button.setIcon(icon3)
        self.bills_button.setIconSize(QSize(32, 32))
        self.bills_button.setCheckable(True)
        self.bills_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.bills_button)

        self.wallet_button = QPushButton(self.maximize_slider_menu_widget)
        self.wallet_button.setObjectName(u"wallet_button")
        self.wallet_button.setFont(font)
        self.wallet_button.setStyleSheet(u"color:white;\n"
"text-align: left;\n"
"padding-left: 10px;")
        icon4 = QIcon()
        icon4.addFile(u":/img/img/wallet.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.wallet_button.setIcon(icon4)
        self.wallet_button.setIconSize(QSize(32, 32))
        self.wallet_button.setCheckable(True)
        self.wallet_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.wallet_button)

        self.goal_button = QPushButton(self.maximize_slider_menu_widget)
        self.goal_button.setObjectName(u"goal_button")
        self.goal_button.setFont(font)
        self.goal_button.setStyleSheet(u"color:white;\n"
"text-align: left;\n"
"padding-left: 10px;")
        icon5 = QIcon()
        icon5.addFile(u":/img/img/crosshair.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.goal_button.setIcon(icon5)
        self.goal_button.setIconSize(QSize(32, 32))
        self.goal_button.setCheckable(True)
        self.goal_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.goal_button)


        self.verticalLayout_5.addLayout(self.verticalLayout)

        self.verticalSpacer_4 = QSpacerItem(20, 97, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_4)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.thema_button = QCheckBox(self.maximize_slider_menu_widget)
        self.thema_button.setObjectName(u"thema_button")
        self.thema_button.setFont(font)
        self.thema_button.setStyleSheet(u"QCheckBox{\n"
"	color:white;\n"
"	padding-left: 10px;\n"
"}\n"
"QCheckBox::indicator {\n"
"	width: 32px;\n"
"	height: 32px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"	image: url(:/img/img/toggle-right.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked{\n"
"\n"
"	image: url(:/img/img/toggle-left.svg);\n"
"}")
        self.thema_button.setCheckable(True)
        self.thema_button.setAutoExclusive(False)

        self.verticalLayout_4.addWidget(self.thema_button)

        self.settings_button = QPushButton(self.maximize_slider_menu_widget)
        self.settings_button.setObjectName(u"settings_button")
        self.settings_button.setFont(font)
        self.settings_button.setStyleSheet(u"color:white;\n"
"text-align: left;\n"
"padding-left: 10px;")
        icon6 = QIcon()
        icon6.addFile(u":/img/img/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_button.setIcon(icon6)
        self.settings_button.setIconSize(QSize(32, 32))
        self.settings_button.setCheckable(True)
        self.settings_button.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.settings_button)

        self.logout_button = QPushButton(self.maximize_slider_menu_widget)
        self.logout_button.setObjectName(u"logout_button")
        self.logout_button.setFont(font)
        self.logout_button.setStyleSheet(u"color:white;\n"
"text-align: left;\n"
"padding-left: 10px;")
        icon7 = QIcon()
        icon7.addFile(u":/img/img/log-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.logout_button.setIcon(icon7)
        self.logout_button.setIconSize(QSize(32, 32))
        self.logout_button.setCheckable(True)
        self.logout_button.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.logout_button)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.verticalSpacer_6 = QSpacerItem(20, 62, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_6)

        self.profile_button = QPushButton(self.maximize_slider_menu_widget)
        self.profile_button.setObjectName(u"profile_button")
        self.profile_button.setFont(font)
        self.profile_button.setStyleSheet(u"color:white;\n"
"text-align: left;\n"
"padding-left: 10px;")
        icon8 = QIcon()
        icon8.addFile(u":/img/img/default_profile.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.profile_button.setIcon(icon8)
        self.profile_button.setIconSize(QSize(32, 32))
        self.profile_button.setCheckable(True)
        self.profile_button.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.profile_button)

        self.verticalSpacer_8 = QSpacerItem(20, 61, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_8)


        self.gridLayout.addWidget(self.maximize_slider_menu_widget, 1, 1, 1, 1)

        self.minimize_slider_menu_widget = QWidget(self.centralwidget)
        self.minimize_slider_menu_widget.setObjectName(u"minimize_slider_menu_widget")
        self.minimize_slider_menu_widget.setStyleSheet(u"QWidget{\n"
"	background-color:#1B1A55;\n"
"}\n"
"QPushButton{\n"
"	height:50px;\n"
"	weight:220px;\n"
"	border:none;\n"
"	border-radius:5px;\n"
"\n"
"}\n"
"QCheckBox{\n"
"	height:50px;\n"
"	weight:220px;\n"
"}\n"
"QPushButton:checked{\n"
"	background-color:#9290C3;\n"
"	color: #9290C3;\n"
"	font-weight:bold;\n"
"}\n"
"")
        self.verticalLayout_6 = QVBoxLayout(self.minimize_slider_menu_widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pushButton_2 = QPushButton(self.minimize_slider_menu_widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon9 = QIcon()
        icon9.addFile(u":/img/img/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon9)
        self.pushButton_2.setIconSize(QSize(32, 32))
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setAutoRepeat(False)
        self.pushButton_2.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.pushButton_2)

        self.verticalSpacer = QSpacerItem(20, 49, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.dashboard_minimize_button = QPushButton(self.minimize_slider_menu_widget)
        self.dashboard_minimize_button.setObjectName(u"dashboard_minimize_button")
        self.dashboard_minimize_button.setIcon(icon)
        self.dashboard_minimize_button.setIconSize(QSize(32, 32))
        self.dashboard_minimize_button.setCheckable(True)
        self.dashboard_minimize_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.dashboard_minimize_button)

        self.analist_minimize_button = QPushButton(self.minimize_slider_menu_widget)
        self.analist_minimize_button.setObjectName(u"analist_minimize_button")
        self.analist_minimize_button.setIcon(icon1)
        self.analist_minimize_button.setIconSize(QSize(32, 32))
        self.analist_minimize_button.setCheckable(True)
        self.analist_minimize_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.analist_minimize_button)

        self.performance_minimize_button = QPushButton(self.minimize_slider_menu_widget)
        self.performance_minimize_button.setObjectName(u"performance_minimize_button")
        self.performance_minimize_button.setIcon(icon2)
        self.performance_minimize_button.setIconSize(QSize(32, 32))
        self.performance_minimize_button.setCheckable(True)
        self.performance_minimize_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.performance_minimize_button)

        self.bills_minimize_button = QPushButton(self.minimize_slider_menu_widget)
        self.bills_minimize_button.setObjectName(u"bills_minimize_button")
        self.bills_minimize_button.setIcon(icon3)
        self.bills_minimize_button.setIconSize(QSize(32, 32))
        self.bills_minimize_button.setCheckable(True)
        self.bills_minimize_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.bills_minimize_button)

        self.wallet_minimize_button = QPushButton(self.minimize_slider_menu_widget)
        self.wallet_minimize_button.setObjectName(u"wallet_minimize_button")
        self.wallet_minimize_button.setIcon(icon4)
        self.wallet_minimize_button.setIconSize(QSize(32, 32))
        self.wallet_minimize_button.setCheckable(True)
        self.wallet_minimize_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.wallet_minimize_button)

        self.goal_minimize_button = QPushButton(self.minimize_slider_menu_widget)
        self.goal_minimize_button.setObjectName(u"goal_minimize_button")
        self.goal_minimize_button.setIcon(icon5)
        self.goal_minimize_button.setIconSize(QSize(32, 32))
        self.goal_minimize_button.setCheckable(True)
        self.goal_minimize_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.goal_minimize_button)


        self.verticalLayout_6.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 97, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.thema_minimize_button = QCheckBox(self.minimize_slider_menu_widget)
        self.thema_minimize_button.setObjectName(u"thema_minimize_button")
        self.thema_minimize_button.setFont(font)
        self.thema_minimize_button.setStyleSheet(u"QCheckBox{\n"
"	color:white;\n"
"	padding-left: 10px;\n"
"}\n"
"QCheckBox::indicator {\n"
"	width: 32px;\n"
"	height: 32px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"	image: url(:/img/img/toggle-right.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked{\n"
"\n"
"	image: url(:/img/img/toggle-left.svg);\n"
"}")
        self.thema_minimize_button.setCheckable(True)
        self.thema_minimize_button.setAutoExclusive(False)

        self.verticalLayout_3.addWidget(self.thema_minimize_button)

        self.settings_minimize_button = QPushButton(self.minimize_slider_menu_widget)
        self.settings_minimize_button.setObjectName(u"settings_minimize_button")
        self.settings_minimize_button.setIcon(icon6)
        self.settings_minimize_button.setIconSize(QSize(32, 32))
        self.settings_minimize_button.setCheckable(True)
        self.settings_minimize_button.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.settings_minimize_button)

        self.logout_minimize_button = QPushButton(self.minimize_slider_menu_widget)
        self.logout_minimize_button.setObjectName(u"logout_minimize_button")
        self.logout_minimize_button.setIcon(icon7)
        self.logout_minimize_button.setIconSize(QSize(32, 32))
        self.logout_minimize_button.setCheckable(True)
        self.logout_minimize_button.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.logout_minimize_button)


        self.verticalLayout_6.addLayout(self.verticalLayout_3)

        self.verticalSpacer_5 = QSpacerItem(20, 64, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_5)

        self.profile_minimize_button = QPushButton(self.minimize_slider_menu_widget)
        self.profile_minimize_button.setObjectName(u"profile_minimize_button")
        self.profile_minimize_button.setIcon(icon8)
        self.profile_minimize_button.setIconSize(QSize(32, 32))
        self.profile_minimize_button.setCheckable(True)
        self.profile_minimize_button.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.profile_minimize_button)

        self.verticalSpacer_7 = QSpacerItem(20, 59, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_7)


        self.gridLayout.addWidget(self.minimize_slider_menu_widget, 1, 0, 1, 1)

        self.main_screen_stacked_widget = QStackedWidget(self.centralwidget)
        self.main_screen_stacked_widget.setObjectName(u"main_screen_stacked_widget")
        self.main_screen_stacked_widget.setStyleSheet(u"background-color:#070F2B;")
        self.dashboard_widget = QWidget()
        self.dashboard_widget.setObjectName(u"dashboard_widget")
        self.verticalLayout_26 = QVBoxLayout(self.dashboard_widget)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalSpacer_35 = QSpacerItem(20, 22, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_26.addItem(self.verticalSpacer_35)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_3 = QSpacerItem(68, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_3)

        self.total_balance_widget = QWidget(self.dashboard_widget)
        self.total_balance_widget.setObjectName(u"total_balance_widget")
        self.total_balance_widget.setMinimumSize(QSize(247, 194))
        self.total_balance_widget.setMaximumSize(QSize(247, 194))
        self.total_balance_widget.setStyleSheet(u"background-color: #535C91;\n"
"border-radius: 25px;")
        self.verticalLayout_7 = QVBoxLayout(self.total_balance_widget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(19, -1, -1, -1)
        self.verticalSpacer_9 = QSpacerItem(20, 2, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_9)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, -1, -1, -1)
        self.total_balance_green_wallet_icon_button = QPushButton(self.total_balance_widget)
        self.total_balance_green_wallet_icon_button.setObjectName(u"total_balance_green_wallet_icon_button")
        self.total_balance_green_wallet_icon_button.setStyleSheet(u"background-color: rgba(7,15,43,0.2);\n"
"image: url(:/img/img/green_wallet.png);\n"
"width: 53px;\n"
"height: 53px;")

        self.horizontalLayout_5.addWidget(self.total_balance_green_wallet_icon_button)

        self.horizontalSpacer_4 = QSpacerItem(171, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)


        self.verticalLayout_7.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_10 = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_10)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.total_balance_label = QLabel(self.total_balance_widget)
        self.total_balance_label.setObjectName(u"total_balance_label")
        self.total_balance_label.setFont(font)
        self.total_balance_label.setStyleSheet(u"color: white;\n"
"text-align: left;")

        self.horizontalLayout_6.addWidget(self.total_balance_label)

        self.horizontalSpacer_6 = QSpacerItem(88, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)


        self.verticalLayout_7.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.tota_balance_value_label = QLabel(self.total_balance_widget)
        self.tota_balance_value_label.setObjectName(u"tota_balance_value_label")
        font1 = QFont()
        font1.setFamilies([u"Poppins"])
        font1.setPointSize(22)
        self.tota_balance_value_label.setFont(font1)
        self.tota_balance_value_label.setStyleSheet(u"color: white;\n"
"text-align: left;")

        self.horizontalLayout_7.addWidget(self.tota_balance_value_label)

        self.horizontalSpacer_8 = QSpacerItem(78, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_8)


        self.verticalLayout_7.addLayout(self.horizontalLayout_7)

        self.verticalSpacer_11 = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_11)


        self.horizontalLayout_11.addWidget(self.total_balance_widget)

        self.horizontalSpacer_5 = QSpacerItem(68, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_5)

        self.total_spending_widget = QWidget(self.dashboard_widget)
        self.total_spending_widget.setObjectName(u"total_spending_widget")
        self.total_spending_widget.setMinimumSize(QSize(254, 194))
        self.total_spending_widget.setMaximumSize(QSize(254, 194))
        self.total_spending_widget.setStyleSheet(u"background-color: #535C91;\n"
"border-radius: 25px;")
        self.verticalLayout_8 = QVBoxLayout(self.total_spending_widget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(19, -1, -1, -1)
        self.verticalSpacer_12 = QSpacerItem(20, 2, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_12)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.total_spending_wallet_icon_button = QPushButton(self.total_spending_widget)
        self.total_spending_wallet_icon_button.setObjectName(u"total_spending_wallet_icon_button")
        self.total_spending_wallet_icon_button.setStyleSheet(u"background-color: rgba(7,15,43,0.2);\n"
"image: url(:/img/img/dark_wallet.svg);\n"
"width: 53px;\n"
"height: 53px;")

        self.horizontalLayout_8.addWidget(self.total_spending_wallet_icon_button)

        self.horizontalSpacer_10 = QSpacerItem(171, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_10)


        self.verticalLayout_8.addLayout(self.horizontalLayout_8)

        self.verticalSpacer_13 = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_13)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.total_spending_label = QLabel(self.total_spending_widget)
        self.total_spending_label.setObjectName(u"total_spending_label")
        self.total_spending_label.setFont(font)
        self.total_spending_label.setStyleSheet(u"color: white;\n"
"text-align: left;")

        self.horizontalLayout_9.addWidget(self.total_spending_label)

        self.horizontalSpacer_12 = QSpacerItem(88, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_12)


        self.verticalLayout_8.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.tota_spending_value_label = QLabel(self.total_spending_widget)
        self.tota_spending_value_label.setObjectName(u"tota_spending_value_label")
        self.tota_spending_value_label.setFont(font1)
        self.tota_spending_value_label.setStyleSheet(u"color: white;\n"
"text-align: left;")

        self.horizontalLayout_10.addWidget(self.tota_spending_value_label)

        self.horizontalSpacer_14 = QSpacerItem(78, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_14)


        self.verticalLayout_8.addLayout(self.horizontalLayout_10)

        self.verticalSpacer_14 = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_14)


        self.horizontalLayout_11.addWidget(self.total_spending_widget)

        self.horizontalSpacer_7 = QSpacerItem(68, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_7)

        self.money_saved_widget = QWidget(self.dashboard_widget)
        self.money_saved_widget.setObjectName(u"money_saved_widget")
        self.money_saved_widget.setMinimumSize(QSize(247, 194))
        self.money_saved_widget.setMaximumSize(QSize(247, 194))
        self.money_saved_widget.setStyleSheet(u"background-color: #535C91;\n"
"border-radius: 25px;")
        self.verticalLayout_10 = QVBoxLayout(self.money_saved_widget)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(19, -1, -1, -1)
        self.verticalSpacer_18 = QSpacerItem(20, 2, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_18)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.money_saved_wallet_icon_button = QPushButton(self.money_saved_widget)
        self.money_saved_wallet_icon_button.setObjectName(u"money_saved_wallet_icon_button")
        self.money_saved_wallet_icon_button.setStyleSheet(u"background-color: rgba(7,15,43,0.2);\n"
"image: url(:/img/img/dark_wallet.svg);\n"
"width: 53px;\n"
"height: 53px;")

        self.horizontalLayout_14.addWidget(self.money_saved_wallet_icon_button)

        self.horizontalSpacer_22 = QSpacerItem(171, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_22)


        self.verticalLayout_10.addLayout(self.horizontalLayout_14)

        self.verticalSpacer_19 = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_19)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.money_saved_label = QLabel(self.money_saved_widget)
        self.money_saved_label.setObjectName(u"money_saved_label")
        self.money_saved_label.setFont(font)
        self.money_saved_label.setStyleSheet(u"color: white;\n"
"text-align: left;")

        self.horizontalLayout_15.addWidget(self.money_saved_label)

        self.horizontalSpacer_24 = QSpacerItem(88, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_24)


        self.verticalLayout_10.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.money_saved_value_label = QLabel(self.money_saved_widget)
        self.money_saved_value_label.setObjectName(u"money_saved_value_label")
        self.money_saved_value_label.setFont(font1)
        self.money_saved_value_label.setStyleSheet(u"color: white;\n"
"text-align: left;")

        self.horizontalLayout_16.addWidget(self.money_saved_value_label)

        self.horizontalSpacer_26 = QSpacerItem(78, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_26)


        self.verticalLayout_10.addLayout(self.horizontalLayout_16)

        self.verticalSpacer_20 = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_20)


        self.horizontalLayout_11.addWidget(self.money_saved_widget)

        self.horizontalSpacer_9 = QSpacerItem(68, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_9)

        self.money_sent_widget = QWidget(self.dashboard_widget)
        self.money_sent_widget.setObjectName(u"money_sent_widget")
        self.money_sent_widget.setMinimumSize(QSize(248, 194))
        self.money_sent_widget.setMaximumSize(QSize(248, 194))
        self.money_sent_widget.setStyleSheet(u"background-color: #535C91;\n"
"border-radius: 25px;")
        self.verticalLayout_11 = QVBoxLayout(self.money_sent_widget)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(19, -1, -1, -1)
        self.verticalSpacer_21 = QSpacerItem(20, 2, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_21)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.money_sent_wallet_icon_button = QPushButton(self.money_sent_widget)
        self.money_sent_wallet_icon_button.setObjectName(u"money_sent_wallet_icon_button")
        self.money_sent_wallet_icon_button.setStyleSheet(u"background-color: rgba(7,15,43,0.2);\n"
"image: url(:/img/img/dark_wallet.svg);\n"
"width: 53px;\n"
"height: 53px;")

        self.horizontalLayout_17.addWidget(self.money_sent_wallet_icon_button)

        self.horizontalSpacer_28 = QSpacerItem(171, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_28)


        self.verticalLayout_11.addLayout(self.horizontalLayout_17)

        self.verticalSpacer_22 = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_22)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(5, -1, -1, -1)
        self.money_sent_label = QLabel(self.money_sent_widget)
        self.money_sent_label.setObjectName(u"money_sent_label")
        self.money_sent_label.setFont(font)
        self.money_sent_label.setStyleSheet(u"color: white;\n"
"text-align: left;")

        self.horizontalLayout_18.addWidget(self.money_sent_label)

        self.horizontalSpacer_30 = QSpacerItem(88, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_30)


        self.verticalLayout_11.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.money_sent_value_label = QLabel(self.money_sent_widget)
        self.money_sent_value_label.setObjectName(u"money_sent_value_label")
        self.money_sent_value_label.setFont(font1)
        self.money_sent_value_label.setStyleSheet(u"color: white;\n"
"text-align: left;")

        self.horizontalLayout_19.addWidget(self.money_sent_value_label)

        self.horizontalSpacer_32 = QSpacerItem(78, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_32)


        self.verticalLayout_11.addLayout(self.horizontalLayout_19)

        self.verticalSpacer_23 = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_23)


        self.horizontalLayout_11.addWidget(self.money_sent_widget)

        self.horizontalSpacer_11 = QSpacerItem(68, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_11)

        self.online_payments_widget = QWidget(self.dashboard_widget)
        self.online_payments_widget.setObjectName(u"online_payments_widget")
        self.online_payments_widget.setMinimumSize(QSize(273, 194))
        self.online_payments_widget.setMaximumSize(QSize(273, 194))
        self.online_payments_widget.setStyleSheet(u"background-color: #535C91;\n"
"border-radius: 25px;")
        self.verticalLayout_14 = QVBoxLayout(self.online_payments_widget)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(19, -1, -1, -1)
        self.verticalSpacer_30 = QSpacerItem(20, 2, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_30)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.online_payments_wallet_icon_button = QPushButton(self.online_payments_widget)
        self.online_payments_wallet_icon_button.setObjectName(u"online_payments_wallet_icon_button")
        self.online_payments_wallet_icon_button.setStyleSheet(u"background-color: rgba(7,15,43,0.2);\n"
"image: url(:/img/img/dark_wallet.svg);\n"
"width: 53px;\n"
"height: 53px;")

        self.horizontalLayout_26.addWidget(self.online_payments_wallet_icon_button)

        self.horizontalSpacer_46 = QSpacerItem(171, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_46)


        self.verticalLayout_14.addLayout(self.horizontalLayout_26)

        self.verticalSpacer_31 = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_31)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.online_payments_label = QLabel(self.online_payments_widget)
        self.online_payments_label.setObjectName(u"online_payments_label")
        self.online_payments_label.setFont(font)
        self.online_payments_label.setStyleSheet(u"color: white;\n"
"text-align: left;")

        self.horizontalLayout_27.addWidget(self.online_payments_label)

        self.horizontalSpacer_48 = QSpacerItem(88, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_48)


        self.verticalLayout_14.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.online_payments_value_label = QLabel(self.online_payments_widget)
        self.online_payments_value_label.setObjectName(u"online_payments_value_label")
        self.online_payments_value_label.setFont(font1)
        self.online_payments_value_label.setStyleSheet(u"color: white;\n"
"text-align: left;")

        self.horizontalLayout_28.addWidget(self.online_payments_value_label)

        self.horizontalSpacer_50 = QSpacerItem(78, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_50)


        self.verticalLayout_14.addLayout(self.horizontalLayout_28)

        self.verticalSpacer_32 = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_32)


        self.horizontalLayout_11.addWidget(self.online_payments_widget)

        self.horizontalSpacer_13 = QSpacerItem(68, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_13)


        self.verticalLayout_26.addLayout(self.horizontalLayout_11)

        self.verticalSpacer_33 = QSpacerItem(20, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_26.addItem(self.verticalSpacer_33)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalSpacer_47 = QSpacerItem(58, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_47)

        self.cards_stacked_widget = QStackedWidget(self.dashboard_widget)
        self.cards_stacked_widget.setObjectName(u"cards_stacked_widget")
        self.cards_stacked_widget.setMinimumSize(QSize(596, 363))
        self.cards_stacked_widget.setMaximumSize(QSize(593, 363))
        self.cards_stacked_widget.setStyleSheet(u"background-color: #535C91;\n"
"border-radius: 35px;")
        self.card1 = QWidget()
        self.card1.setObjectName(u"card1")
        self.card1.setStyleSheet(u"background-color: #535C91;\n"
"border-radius: 35px;")
        self.verticalLayout_12 = QVBoxLayout(self.card1)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(20, -1, 20, -1)
        self.cards_topic_label = QLabel(self.card1)
        self.cards_topic_label.setObjectName(u"cards_topic_label")
        font2 = QFont()
        font2.setFamilies([u"Poppins"])
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setUnderline(True)
        self.cards_topic_label.setFont(font2)
        self.cards_topic_label.setStyleSheet(u"background-color: transparent;\n"
"color: white;")

        self.horizontalLayout_25.addWidget(self.cards_topic_label)

        self.horizontalSpacer_36 = QSpacerItem(418, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_36)

        self.all_accounts_label = QLabel(self.card1)
        self.all_accounts_label.setObjectName(u"all_accounts_label")
        font3 = QFont()
        font3.setFamilies([u"Poppins"])
        font3.setPointSize(10)
        font3.setUnderline(True)
        self.all_accounts_label.setFont(font3)
        self.all_accounts_label.setStyleSheet(u"background-color: transparent;\n"
"color: white;")

        self.horizontalLayout_25.addWidget(self.all_accounts_label)


        self.verticalLayout_12.addLayout(self.horizontalLayout_25)

        self.verticalSpacer_28 = QSpacerItem(10, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_28)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(20, -1, 20, -1)
        self.widget_11 = QWidget(self.card1)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setStyleSheet(u"background-color: #1B1A55;\n"
"border-radius: 30px;")
        self.verticalLayout_20 = QVBoxLayout(self.widget_11)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(25, 20, -1, 20)
        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.card_name_label = QLabel(self.widget_11)
        self.card_name_label.setObjectName(u"card_name_label")
        font4 = QFont()
        font4.setFamilies([u"Poppins"])
        font4.setPointSize(10)
        self.card_name_label.setFont(font4)
        self.card_name_label.setStyleSheet(u"color: white;")

        self.verticalLayout_21.addWidget(self.card_name_label)

        self.account_name_label = QLabel(self.widget_11)
        self.account_name_label.setObjectName(u"account_name_label")
        font5 = QFont()
        font5.setFamilies([u"Poppins"])
        font5.setPointSize(7)
        self.account_name_label.setFont(font5)
        self.account_name_label.setStyleSheet(u"color:rgba(255,255,255,0.4);\n"
"background-color: transparent;")

        self.verticalLayout_21.addWidget(self.account_name_label)


        self.horizontalLayout_33.addLayout(self.verticalLayout_21)

        self.horizontalSpacer_21 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_21)


        self.verticalLayout_20.addLayout(self.horizontalLayout_33)

        self.verticalSpacer_34 = QSpacerItem(20, 17, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_34)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.card1_card_number_label = QLabel(self.widget_11)
        self.card1_card_number_label.setObjectName(u"card1_card_number_label")
        font6 = QFont()
        font6.setFamilies([u"Poppins"])
        font6.setPointSize(19)
        self.card1_card_number_label.setFont(font6)
        self.card1_card_number_label.setStyleSheet(u"color: white;")

        self.horizontalLayout_34.addWidget(self.card1_card_number_label)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_23)


        self.verticalLayout_20.addLayout(self.horizontalLayout_34)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.card1_card_holder_label = QLabel(self.widget_11)
        self.card1_card_holder_label.setObjectName(u"card1_card_holder_label")
        font7 = QFont()
        font7.setFamilies([u"Poppins"])
        font7.setPointSize(8)
        self.card1_card_holder_label.setFont(font7)
        self.card1_card_holder_label.setStyleSheet(u"color:white;")

        self.verticalLayout_22.addWidget(self.card1_card_holder_label)

        self.card1_card_name_label = QLabel(self.widget_11)
        self.card1_card_name_label.setObjectName(u"card1_card_name_label")
        font8 = QFont()
        font8.setFamilies([u"Poppins"])
        font8.setPointSize(11)
        self.card1_card_name_label.setFont(font8)
        self.card1_card_name_label.setStyleSheet(u"color:white;\n"
"background-color:transparent;")

        self.verticalLayout_22.addWidget(self.card1_card_name_label)


        self.horizontalLayout_35.addLayout(self.verticalLayout_22)

        self.horizontalSpacer_25 = QSpacerItem(28, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_25)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.card1_expier_date_label = QLabel(self.widget_11)
        self.card1_expier_date_label.setObjectName(u"card1_expier_date_label")
        self.card1_expier_date_label.setFont(font7)
        self.card1_expier_date_label.setStyleSheet(u"color:white;\n"
"backgroundd-color: transparent;")

        self.verticalLayout_23.addWidget(self.card1_expier_date_label)

        self.card1_card_date_label = QLabel(self.widget_11)
        self.card1_card_date_label.setObjectName(u"card1_card_date_label")
        self.card1_card_date_label.setFont(font8)
        self.card1_card_date_label.setStyleSheet(u"color:white;\n"
"background-color:transparent;")

        self.verticalLayout_23.addWidget(self.card1_card_date_label)


        self.horizontalLayout_35.addLayout(self.verticalLayout_23)

        self.horizontalSpacer_27 = QSpacerItem(78, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_27)


        self.verticalLayout_20.addLayout(self.horizontalLayout_35)


        self.horizontalLayout_22.addWidget(self.widget_11)

        self.horizontalSpacer_29 = QSpacerItem(22, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_29)

        self.label_41 = QLabel(self.card1)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(1, 0))
        self.label_41.setMaximumSize(QSize(1, 16777215))
        self.label_41.setStyleSheet(u"background-color: white;")

        self.horizontalLayout_22.addWidget(self.label_41)

        self.horizontalSpacer_31 = QSpacerItem(78, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_31)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.card1_current_balance_value_label = QLabel(self.card1)
        self.card1_current_balance_value_label.setObjectName(u"card1_current_balance_value_label")
        font9 = QFont()
        font9.setFamilies([u"Poppins"])
        font9.setPointSize(17)
        self.card1_current_balance_value_label.setFont(font9)
        self.card1_current_balance_value_label.setStyleSheet(u"color:white;")
        self.card1_current_balance_value_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_24.addWidget(self.card1_current_balance_value_label)

        self.current_balance_label = QLabel(self.card1)
        self.current_balance_label.setObjectName(u"current_balance_label")
        font10 = QFont()
        font10.setFamilies([u"Poppins"])
        font10.setPointSize(8)
        font10.setUnderline(False)
        self.current_balance_label.setFont(font10)
        self.current_balance_label.setStyleSheet(u"background-color: transparent;\n"
"color: rgba(255,255,255,0.4);")
        self.current_balance_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_24.addWidget(self.current_balance_label)

        self.verticalSpacer_37 = QSpacerItem(20, 28, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacer_37)

        self.card1_income_value_label = QLabel(self.card1)
        self.card1_income_value_label.setObjectName(u"card1_income_value_label")
        self.card1_income_value_label.setFont(font)
        self.card1_income_value_label.setStyleSheet(u"color:white;")
        self.card1_income_value_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_24.addWidget(self.card1_income_value_label)

        self.income_label = QLabel(self.card1)
        self.income_label.setObjectName(u"income_label")
        self.income_label.setFont(font10)
        self.income_label.setStyleSheet(u"background-color: transparent;\n"
"color: rgba(255,255,255,0.4);")
        self.income_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_24.addWidget(self.income_label)

        self.verticalSpacer_38 = QSpacerItem(20, 48, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacer_38)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_33)

        self.deactive_card_button = QCheckBox(self.card1)
        self.deactive_card_button.setObjectName(u"deactive_card_button")
        self.deactive_card_button.setFont(font)
        self.deactive_card_button.setStyleSheet(u"QCheckBox{\n"
"	color:white;\n"
"	padding-left: 10px;\n"
"}\n"
"QCheckBox::indicator {\n"
"	width: 21px;\n"
"	height: 21px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"	image: url(:/img/img/toggle-right.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked{\n"
"\n"
"	image: url(:/img/img/toggle-left.svg);\n"
"}")
        self.deactive_card_button.setIconSize(QSize(10, 10))
        self.deactive_card_button.setCheckable(True)
        self.deactive_card_button.setAutoExclusive(False)

        self.horizontalLayout_36.addWidget(self.deactive_card_button)


        self.verticalLayout_24.addLayout(self.horizontalLayout_36)

        self.deactive_card_label = QLabel(self.card1)
        self.deactive_card_label.setObjectName(u"deactive_card_label")
        self.deactive_card_label.setFont(font10)
        self.deactive_card_label.setStyleSheet(u"background-color: transparent;\n"
"color: rgba(255,255,255,0.4);")
        self.deactive_card_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_24.addWidget(self.deactive_card_label)


        self.horizontalLayout_22.addLayout(self.verticalLayout_24)


        self.verticalLayout_12.addLayout(self.horizontalLayout_22)

        self.verticalSpacer_26 = QSpacerItem(10, 8, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_26)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(20, -1, 20, -1)
        self.card_limits_process_bar = QProgressBar(self.card1)
        self.card_limits_process_bar.setObjectName(u"card_limits_process_bar")
        self.card_limits_process_bar.setMinimumSize(QSize(317, 10))
        self.card_limits_process_bar.setMaximumSize(QSize(16777215, 10))
        self.card_limits_process_bar.setStyleSheet(u"QProgressBar{\n"
"	background-color:white;\n"
"	color:white;\n"
"	border-style: solid;\n"
"	border-radius:5px;\n"
"	text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius:5px;\n"
"	background-color:#1B1A55\n"
"}")
        self.card_limits_process_bar.setValue(24)
        self.card_limits_process_bar.setTextVisible(False)

        self.horizontalLayout_23.addWidget(self.card_limits_process_bar)

        self.horizontalSpacer_34 = QSpacerItem(220, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_34)


        self.verticalLayout_12.addLayout(self.horizontalLayout_23)

        self.verticalSpacer_25 = QSpacerItem(10, 8, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_25)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(20, -1, 20, -1)
        self.weeklypayments_limit_label = QLabel(self.card1)
        self.weeklypayments_limit_label.setObjectName(u"weeklypayments_limit_label")
        self.weeklypayments_limit_label.setFont(font7)
        self.weeklypayments_limit_label.setStyleSheet(u"color: white;")

        self.horizontalLayout_37.addWidget(self.weeklypayments_limit_label)

        self.horizontalSpacer_37 = QSpacerItem(98, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_37.addItem(self.horizontalSpacer_37)

        self.card1_weekl_payment_limit_label = QLabel(self.card1)
        self.card1_weekl_payment_limit_label.setObjectName(u"card1_weekl_payment_limit_label")
        self.card1_weekl_payment_limit_label.setFont(font7)
        self.card1_weekl_payment_limit_label.setStyleSheet(u"color: white;")
        self.card1_weekl_payment_limit_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_37.addWidget(self.card1_weekl_payment_limit_label)

        self.horizontalSpacer_38 = QSpacerItem(248, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_37.addItem(self.horizontalSpacer_38)


        self.verticalLayout_12.addLayout(self.horizontalLayout_37)

        self.verticalSpacer_27 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_27)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(20, -1, 20, -1)
        self.previous_button = QPushButton(self.card1)
        self.previous_button.setObjectName(u"previous_button")
        self.previous_button.setFont(font)
        self.previous_button.setStyleSheet(u"color:rgba(255,255,255,0.4);\n"
"background-color:transparent;")

        self.horizontalLayout_24.addWidget(self.previous_button)

        self.horizontalSpacer_35 = QSpacerItem(378, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_35)

        self.next_button = QPushButton(self.card1)
        self.next_button.setObjectName(u"next_button")
        self.next_button.setFont(font)
        self.next_button.setStyleSheet(u"color:white;\n"
"background-color:transparent;")

        self.horizontalLayout_24.addWidget(self.next_button)


        self.verticalLayout_12.addLayout(self.horizontalLayout_24)

        self.cards_stacked_widget.addWidget(self.card1)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.cards_stacked_widget.addWidget(self.page_3)

        self.horizontalLayout_32.addWidget(self.cards_stacked_widget)

        self.horizontalSpacer_40 = QSpacerItem(58, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_40)

        self.goal_widget = QWidget(self.dashboard_widget)
        self.goal_widget.setObjectName(u"goal_widget")
        self.goal_widget.setMinimumSize(QSize(487, 363))
        self.goal_widget.setMaximumSize(QSize(487, 363))
        self.goal_widget.setStyleSheet(u"background-color: #535C91;\n"
"border-radius: 35px;")
        self.gridLayout_17 = QGridLayout(self.goal_widget)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(20, 34, 20, 50)
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.goal_top_target_value_label = QLabel(self.goal_widget)
        self.goal_top_target_value_label.setObjectName(u"goal_top_target_value_label")
        font11 = QFont()
        font11.setFamilies([u"Poppins"])
        font11.setPointSize(16)
        self.goal_top_target_value_label.setFont(font11)
        self.goal_top_target_value_label.setStyleSheet(u"color:white;")

        self.horizontalLayout_20.addWidget(self.goal_top_target_value_label)

        self.pushButton_27 = QPushButton(self.goal_widget)
        self.pushButton_27.setObjectName(u"pushButton_27")
        icon10 = QIcon()
        icon10.addFile(u":/img/img/edit-3.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_27.setIcon(icon10)
        self.pushButton_27.setIconSize(QSize(25, 25))

        self.horizontalLayout_20.addWidget(self.pushButton_27)

        self.horizontalSpacer_19 = QSpacerItem(168, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_19)

        self.goal_target_date_label = QLabel(self.goal_widget)
        self.goal_target_date_label.setObjectName(u"goal_target_date_label")
        self.goal_target_date_label.setFont(font11)
        self.goal_target_date_label.setStyleSheet(u"color: white;")

        self.horizontalLayout_20.addWidget(self.goal_target_date_label)


        self.gridLayout_17.addLayout(self.horizontalLayout_20, 1, 0, 1, 2)

        self.goals_white_line = QWidget(self.goal_widget)
        self.goals_white_line.setObjectName(u"goals_white_line")
        self.goals_white_line.setMinimumSize(QSize(450, 1))
        self.goals_white_line.setMaximumSize(QSize(450, 1))
        self.goals_white_line.setStyleSheet(u"background-color: white;")

        self.gridLayout_17.addWidget(self.goals_white_line, 2, 0, 1, 2)

        self.gridLayout_16 = QGridLayout()
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setHorizontalSpacing(0)
        self.gridLayout_16.setVerticalSpacing(30)
        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.goal_this_month_target_icon_button = QPushButton(self.goal_widget)
        self.goal_this_month_target_icon_button.setObjectName(u"goal_this_month_target_icon_button")
        self.goal_this_month_target_icon_button.setStyleSheet(u"background-color:transparent;")
        icon11 = QIcon()
        icon11.addFile(u":/img/img/target.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.goal_this_month_target_icon_button.setIcon(icon11)
        self.goal_this_month_target_icon_button.setIconSize(QSize(35, 35))

        self.horizontalLayout_31.addWidget(self.goal_this_month_target_icon_button)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.goal_this_month_target_label = QLabel(self.goal_widget)
        self.goal_this_month_target_label.setObjectName(u"goal_this_month_target_label")
        self.goal_this_month_target_label.setFont(font8)
        self.goal_this_month_target_label.setStyleSheet(u"color: rgba(255,255,255,0.4);")

        self.verticalLayout_25.addWidget(self.goal_this_month_target_label)

        self.goal_this_month_target_value_label = QLabel(self.goal_widget)
        self.goal_this_month_target_value_label.setObjectName(u"goal_this_month_target_value_label")
        self.goal_this_month_target_value_label.setFont(font11)
        self.goal_this_month_target_value_label.setStyleSheet(u"color:white;")

        self.verticalLayout_25.addWidget(self.goal_this_month_target_value_label)


        self.horizontalLayout_31.addLayout(self.verticalLayout_25)


        self.gridLayout_16.addLayout(self.horizontalLayout_31, 1, 0, 1, 2)

        self.horizontalSpacer_39 = QSpacerItem(13, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_16.addItem(self.horizontalSpacer_39, 1, 2, 1, 1)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.goal_target_achived_icon_button = QPushButton(self.goal_widget)
        self.goal_target_achived_icon_button.setObjectName(u"goal_target_achived_icon_button")
        self.goal_target_achived_icon_button.setStyleSheet(u"background-color:transparent;")
        icon12 = QIcon()
        icon12.addFile(u":/img/img/award.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.goal_target_achived_icon_button.setIcon(icon12)
        self.goal_target_achived_icon_button.setIconSize(QSize(35, 35))

        self.horizontalLayout_21.addWidget(self.goal_target_achived_icon_button)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.goal_target_achived_label = QLabel(self.goal_widget)
        self.goal_target_achived_label.setObjectName(u"goal_target_achived_label")
        self.goal_target_achived_label.setFont(font8)
        self.goal_target_achived_label.setStyleSheet(u"color: rgba(255,255,255,0.4);")

        self.verticalLayout_19.addWidget(self.goal_target_achived_label)

        self.goal_target_achived_value_label = QLabel(self.goal_widget)
        self.goal_target_achived_value_label.setObjectName(u"goal_target_achived_value_label")
        self.goal_target_achived_value_label.setFont(font11)
        self.goal_target_achived_value_label.setStyleSheet(u"color:white;")

        self.verticalLayout_19.addWidget(self.goal_target_achived_value_label)


        self.horizontalLayout_21.addLayout(self.verticalLayout_19)


        self.gridLayout_16.addLayout(self.horizontalLayout_21, 0, 0, 1, 1)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_16.addItem(self.horizontalSpacer_20, 0, 1, 1, 2)


        self.gridLayout_17.addLayout(self.gridLayout_16, 3, 0, 1, 1)

        self.golas_graph_big_circle_widget = QWidget(self.goal_widget)
        self.golas_graph_big_circle_widget.setObjectName(u"golas_graph_big_circle_widget")
        self.golas_graph_big_circle_widget.setMinimumSize(QSize(200, 200))
        self.golas_graph_big_circle_widget.setMaximumSize(QSize(200, 200))
        self.golas_graph_big_circle_widget.setStyleSheet(u"QWidget{\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:180, stop:0.999 rgba(255, 0, 0, 0), stop:0.998 rgba(0, 170, 0, 255));\n"
"	border-radius: 100px;\n"
"}\n"
"QWidget::setFixedSize{\n"
"	width:200px;\n"
"	height:200px;\n"
"}")
        self.gridLayout_5 = QGridLayout(self.golas_graph_big_circle_widget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setVerticalSpacing(20)
        self.gridLayout_5.setContentsMargins(25, 25, 25, 25)
        self.goal_graph_widget = QWidget(self.golas_graph_big_circle_widget)
        self.goal_graph_widget.setObjectName(u"goal_graph_widget")
        self.goal_graph_widget.setStyleSheet(u"border-radius:75px;\n"
"background-color:#535C91;")
        self.gridLayout_4 = QGridLayout(self.goal_graph_widget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(0)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.goal_graph_label = QLabel(self.goal_graph_widget)
        self.goal_graph_label.setObjectName(u"goal_graph_label")
        self.goal_graph_label.setMinimumSize(QSize(150, 150))
        self.goal_graph_label.setMaximumSize(QSize(150, 150))
        self.goal_graph_label.setFont(font6)
        self.goal_graph_label.setStyleSheet(u"color: white;\n"
"width: 150px;\n"
"height: 150px;")
        self.goal_graph_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.goal_graph_label, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.goal_graph_widget, 0, 0, 1, 1)


        self.gridLayout_17.addWidget(self.golas_graph_big_circle_widget, 3, 1, 1, 1)

        self.goal_topic_label = QLabel(self.goal_widget)
        self.goal_topic_label.setObjectName(u"goal_topic_label")
        self.goal_topic_label.setFont(font2)
        self.goal_topic_label.setStyleSheet(u"color:white;")

        self.gridLayout_17.addWidget(self.goal_topic_label, 0, 0, 1, 2)


        self.horizontalLayout_32.addWidget(self.goal_widget)

        self.horizontalSpacer_49 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_49)

        self.upcoming_bill_widget = QWidget(self.dashboard_widget)
        self.upcoming_bill_widget.setObjectName(u"upcoming_bill_widget")
        self.upcoming_bill_widget.setMinimumSize(QSize(351, 374))
        self.upcoming_bill_widget.setMaximumSize(QSize(351, 374))
        font12 = QFont()
        font12.setBold(False)
        font12.setUnderline(False)
        self.upcoming_bill_widget.setFont(font12)
        self.upcoming_bill_widget.setStyleSheet(u"background-color: #535C91;\n"
"border-radius: 23px;")
        self.verticalLayout_33 = QVBoxLayout(self.upcoming_bill_widget)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.label_22 = QLabel(self.upcoming_bill_widget)
        self.label_22.setObjectName(u"label_22")
        font13 = QFont()
        font13.setFamilies([u"Poppins"])
        font13.setPointSize(11)
        font13.setBold(True)
        font13.setItalic(False)
        font13.setUnderline(True)
        self.label_22.setFont(font13)
        self.label_22.setStyleSheet(u"color:white;")
        self.label_22.setAlignment(Qt.AlignCenter)

        self.verticalLayout_33.addWidget(self.label_22)

        self.first_bill_widget = QWidget(self.upcoming_bill_widget)
        self.first_bill_widget.setObjectName(u"first_bill_widget")
        self.first_bill_widget.setStyleSheet(u"background-color:transparent;")
        self.gridLayout_7 = QGridLayout(self.first_bill_widget)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.first_bill_date_widget = QWidget(self.first_bill_widget)
        self.first_bill_date_widget.setObjectName(u"first_bill_date_widget")
        self.first_bill_date_widget.setStyleSheet(u"background-color:#1B1A55;\n"
"border-radius: 10px;")
        self.verticalLayout_9 = QVBoxLayout(self.first_bill_date_widget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.first_bill_date_month_label = QLabel(self.first_bill_date_widget)
        self.first_bill_date_month_label.setObjectName(u"first_bill_date_month_label")
        self.first_bill_date_month_label.setFont(font8)
        self.first_bill_date_month_label.setStyleSheet(u"color:white;")
        self.first_bill_date_month_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.first_bill_date_month_label)

        self.first_bill_date_day_label = QLabel(self.first_bill_date_widget)
        self.first_bill_date_day_label.setObjectName(u"first_bill_date_day_label")
        self.first_bill_date_day_label.setFont(font)
        self.first_bill_date_day_label.setStyleSheet(u"color: white;")
        self.first_bill_date_day_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.first_bill_date_day_label)


        self.horizontalLayout_12.addWidget(self.first_bill_date_widget)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(10, -1, -1, -1)
        self.first_bill_topic_label = QLabel(self.first_bill_widget)
        self.first_bill_topic_label.setObjectName(u"first_bill_topic_label")
        self.first_bill_topic_label.setFont(font8)
        self.first_bill_topic_label.setStyleSheet(u"color: white;")

        self.verticalLayout_13.addWidget(self.first_bill_topic_label)

        self.first_bill_status_label = QLabel(self.first_bill_widget)
        self.first_bill_status_label.setObjectName(u"first_bill_status_label")
        font14 = QFont()
        font14.setFamilies([u"Poppins"])
        font14.setPointSize(11)
        font14.setBold(True)
        self.first_bill_status_label.setFont(font14)
        self.first_bill_status_label.setStyleSheet(u"color: white;")

        self.verticalLayout_13.addWidget(self.first_bill_status_label)

        self.first_bill_last_charge_label = QLabel(self.first_bill_widget)
        self.first_bill_last_charge_label.setObjectName(u"first_bill_last_charge_label")
        self.first_bill_last_charge_label.setFont(font7)
        self.first_bill_last_charge_label.setStyleSheet(u"color: white;")

        self.verticalLayout_13.addWidget(self.first_bill_last_charge_label)


        self.horizontalLayout_12.addLayout(self.verticalLayout_13)

        self.horizontalSpacer_15 = QSpacerItem(55, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_15)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalSpacer_15 = QSpacerItem(20, 18, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_15)

        self.first_bill_value_widget = QWidget(self.first_bill_widget)
        self.first_bill_value_widget.setObjectName(u"first_bill_value_widget")
        self.first_bill_value_widget.setStyleSheet(u"background-color: #1B1A55;\n"
"border-radius: 10px;")
        self.gridLayout_2 = QGridLayout(self.first_bill_value_widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.first_bill_value_label = QLabel(self.first_bill_value_widget)
        self.first_bill_value_label.setObjectName(u"first_bill_value_label")
        self.first_bill_value_label.setFont(font)
        self.first_bill_value_label.setStyleSheet(u"color:white;")
        self.first_bill_value_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.first_bill_value_label, 0, 0, 1, 1)


        self.verticalLayout_15.addWidget(self.first_bill_value_widget)

        self.verticalSpacer_16 = QSpacerItem(20, 8, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_16)


        self.horizontalLayout_12.addLayout(self.verticalLayout_15)

        self.horizontalSpacer_16 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_16)


        self.gridLayout_7.addLayout(self.horizontalLayout_12, 0, 0, 1, 1)


        self.verticalLayout_33.addWidget(self.first_bill_widget)

        self.second_bill_widget = QWidget(self.upcoming_bill_widget)
        self.second_bill_widget.setObjectName(u"second_bill_widget")
        self.second_bill_widget.setStyleSheet(u"background-color:transparent;")
        self.gridLayout_8 = QGridLayout(self.second_bill_widget)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.second_bill_date_widget = QWidget(self.second_bill_widget)
        self.second_bill_date_widget.setObjectName(u"second_bill_date_widget")
        self.second_bill_date_widget.setStyleSheet(u"background-color:#1B1A55;\n"
"border-radius: 10px;")
        self.verticalLayout_16 = QVBoxLayout(self.second_bill_date_widget)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.second_bill_date_month_label = QLabel(self.second_bill_date_widget)
        self.second_bill_date_month_label.setObjectName(u"second_bill_date_month_label")
        self.second_bill_date_month_label.setFont(font8)
        self.second_bill_date_month_label.setStyleSheet(u"color:white;")
        self.second_bill_date_month_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.second_bill_date_month_label)

        self.second_bill_date_day_label = QLabel(self.second_bill_date_widget)
        self.second_bill_date_day_label.setObjectName(u"second_bill_date_day_label")
        self.second_bill_date_day_label.setFont(font)
        self.second_bill_date_day_label.setStyleSheet(u"color: white;")
        self.second_bill_date_day_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.second_bill_date_day_label)


        self.horizontalLayout_13.addWidget(self.second_bill_date_widget)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(10, -1, -1, -1)
        self.second_bill_topic_label = QLabel(self.second_bill_widget)
        self.second_bill_topic_label.setObjectName(u"second_bill_topic_label")
        self.second_bill_topic_label.setFont(font8)
        self.second_bill_topic_label.setStyleSheet(u"color: white;")

        self.verticalLayout_17.addWidget(self.second_bill_topic_label)

        self.second_bill_status_label = QLabel(self.second_bill_widget)
        self.second_bill_status_label.setObjectName(u"second_bill_status_label")
        self.second_bill_status_label.setFont(font14)
        self.second_bill_status_label.setStyleSheet(u"color: white;")

        self.verticalLayout_17.addWidget(self.second_bill_status_label)

        self.second_bill_last_charge_label = QLabel(self.second_bill_widget)
        self.second_bill_last_charge_label.setObjectName(u"second_bill_last_charge_label")
        self.second_bill_last_charge_label.setFont(font7)
        self.second_bill_last_charge_label.setStyleSheet(u"color: white;")

        self.verticalLayout_17.addWidget(self.second_bill_last_charge_label)


        self.horizontalLayout_13.addLayout(self.verticalLayout_17)

        self.horizontalSpacer_17 = QSpacerItem(55, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_17)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalSpacer_17 = QSpacerItem(20, 18, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_17)

        self.second_bill_value_widget = QWidget(self.second_bill_widget)
        self.second_bill_value_widget.setObjectName(u"second_bill_value_widget")
        self.second_bill_value_widget.setStyleSheet(u"background-color: #1B1A55;\n"
"border-radius: 10px;")
        self.gridLayout_3 = QGridLayout(self.second_bill_value_widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.second_bill_value_label = QLabel(self.second_bill_value_widget)
        self.second_bill_value_label.setObjectName(u"second_bill_value_label")
        self.second_bill_value_label.setFont(font)
        self.second_bill_value_label.setStyleSheet(u"color:white;")
        self.second_bill_value_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.second_bill_value_label, 0, 0, 1, 1)


        self.verticalLayout_18.addWidget(self.second_bill_value_widget)

        self.verticalSpacer_24 = QSpacerItem(20, 8, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_24)


        self.horizontalLayout_13.addLayout(self.verticalLayout_18)

        self.horizontalSpacer_18 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_18)


        self.gridLayout_8.addLayout(self.horizontalLayout_13, 0, 0, 1, 1)


        self.verticalLayout_33.addWidget(self.second_bill_widget)

        self.third_bill_widget = QWidget(self.upcoming_bill_widget)
        self.third_bill_widget.setObjectName(u"third_bill_widget")
        self.third_bill_widget.setStyleSheet(u"background-color:transparent;")
        self.gridLayout_9 = QGridLayout(self.third_bill_widget)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.third_bill_date_widget = QWidget(self.third_bill_widget)
        self.third_bill_date_widget.setObjectName(u"third_bill_date_widget")
        self.third_bill_date_widget.setStyleSheet(u"background-color:#1B1A55;\n"
"border-radius: 10px;")
        self.verticalLayout_30 = QVBoxLayout(self.third_bill_date_widget)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.third_bill_date_month_label = QLabel(self.third_bill_date_widget)
        self.third_bill_date_month_label.setObjectName(u"third_bill_date_month_label")
        self.third_bill_date_month_label.setFont(font8)
        self.third_bill_date_month_label.setStyleSheet(u"color:white;")
        self.third_bill_date_month_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_30.addWidget(self.third_bill_date_month_label)

        self.third_bill_date_day_label = QLabel(self.third_bill_date_widget)
        self.third_bill_date_day_label.setObjectName(u"third_bill_date_day_label")
        self.third_bill_date_day_label.setFont(font)
        self.third_bill_date_day_label.setStyleSheet(u"color: white;")
        self.third_bill_date_day_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_30.addWidget(self.third_bill_date_day_label)


        self.horizontalLayout_29.addWidget(self.third_bill_date_widget)

        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(10, -1, -1, -1)
        self.third_bill_topic_label = QLabel(self.third_bill_widget)
        self.third_bill_topic_label.setObjectName(u"third_bill_topic_label")
        self.third_bill_topic_label.setFont(font8)
        self.third_bill_topic_label.setStyleSheet(u"color: white;")

        self.verticalLayout_31.addWidget(self.third_bill_topic_label)

        self.third_bill_status_label = QLabel(self.third_bill_widget)
        self.third_bill_status_label.setObjectName(u"third_bill_status_label")
        self.third_bill_status_label.setFont(font14)
        self.third_bill_status_label.setStyleSheet(u"color: white;")

        self.verticalLayout_31.addWidget(self.third_bill_status_label)

        self.third_bill_last_charge_label = QLabel(self.third_bill_widget)
        self.third_bill_last_charge_label.setObjectName(u"third_bill_last_charge_label")
        self.third_bill_last_charge_label.setFont(font7)
        self.third_bill_last_charge_label.setStyleSheet(u"color: white;")

        self.verticalLayout_31.addWidget(self.third_bill_last_charge_label)


        self.horizontalLayout_29.addLayout(self.verticalLayout_31)

        self.horizontalSpacer_41 = QSpacerItem(55, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_41)

        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalSpacer_39 = QSpacerItem(20, 18, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_32.addItem(self.verticalSpacer_39)

        self.third_bill_value_widget = QWidget(self.third_bill_widget)
        self.third_bill_value_widget.setObjectName(u"third_bill_value_widget")
        self.third_bill_value_widget.setStyleSheet(u"background-color: #1B1A55;\n"
"border-radius: 10px;")
        self.gridLayout_6 = QGridLayout(self.third_bill_value_widget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.third_bill_value_label = QLabel(self.third_bill_value_widget)
        self.third_bill_value_label.setObjectName(u"third_bill_value_label")
        self.third_bill_value_label.setFont(font)
        self.third_bill_value_label.setStyleSheet(u"color:white;")
        self.third_bill_value_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.third_bill_value_label, 0, 0, 1, 1)


        self.verticalLayout_32.addWidget(self.third_bill_value_widget)

        self.verticalSpacer_40 = QSpacerItem(20, 8, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_32.addItem(self.verticalSpacer_40)


        self.horizontalLayout_29.addLayout(self.verticalLayout_32)

        self.horizontalSpacer_42 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_42)


        self.gridLayout_9.addLayout(self.horizontalLayout_29, 0, 0, 1, 1)


        self.verticalLayout_33.addWidget(self.third_bill_widget)


        self.horizontalLayout_32.addWidget(self.upcoming_bill_widget)

        self.horizontalSpacer_51 = QSpacerItem(28, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_51)


        self.verticalLayout_26.addLayout(self.horizontalLayout_32)

        self.verticalSpacer_36 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_26.addItem(self.verticalSpacer_36)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalSpacer_52 = QSpacerItem(68, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_52)

        self.transaction_history_widget = QWidget(self.dashboard_widget)
        self.transaction_history_widget.setObjectName(u"transaction_history_widget")
        self.transaction_history_widget.setMinimumSize(QSize(595, 300))
        self.transaction_history_widget.setMaximumSize(QSize(595, 300))
        self.transaction_history_widget.setStyleSheet(u"background-color: #535C91;\n"
"border-radius: 23px;")
        self.gridLayout_15 = QGridLayout(self.transaction_history_widget)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(20, -1, 15, 30)
        self.widget_33 = QWidget(self.transaction_history_widget)
        self.widget_33.setObjectName(u"widget_33")
        self.gridLayout_12 = QGridLayout(self.widget_33)
        self.gridLayout_12.setSpacing(0)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(10, 0, 0, 0)
        self.transaction_history_third_line_reciever_label = QLabel(self.widget_33)
        self.transaction_history_third_line_reciever_label.setObjectName(u"transaction_history_third_line_reciever_label")
        self.transaction_history_third_line_reciever_label.setFont(font4)
        self.transaction_history_third_line_reciever_label.setStyleSheet(u"color: white;")

        self.gridLayout_12.addWidget(self.transaction_history_third_line_reciever_label, 0, 0, 1, 1)

        self.transaction_history_third_line_type_label = QLabel(self.widget_33)
        self.transaction_history_third_line_type_label.setObjectName(u"transaction_history_third_line_type_label")
        self.transaction_history_third_line_type_label.setFont(font4)
        self.transaction_history_third_line_type_label.setStyleSheet(u"color:rgba(255,255,255,0.8);")

        self.gridLayout_12.addWidget(self.transaction_history_third_line_type_label, 0, 1, 1, 1)

        self.transaction_history_third_line_value_label = QLabel(self.widget_33)
        self.transaction_history_third_line_value_label.setObjectName(u"transaction_history_third_line_value_label")
        self.transaction_history_third_line_value_label.setFont(font4)
        self.transaction_history_third_line_value_label.setStyleSheet(u"color: white;")
        self.transaction_history_third_line_value_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.transaction_history_third_line_value_label, 0, 3, 1, 1)

        self.transaction_history_third_line_date_label = QLabel(self.widget_33)
        self.transaction_history_third_line_date_label.setObjectName(u"transaction_history_third_line_date_label")
        self.transaction_history_third_line_date_label.setFont(font4)
        self.transaction_history_third_line_date_label.setStyleSheet(u"color:rgba(255,255,255,0.8);")

        self.gridLayout_12.addWidget(self.transaction_history_third_line_date_label, 0, 2, 1, 1)


        self.gridLayout_15.addWidget(self.widget_33, 6, 0, 1, 1)

        self.widget_34 = QWidget(self.transaction_history_widget)
        self.widget_34.setObjectName(u"widget_34")
        self.gridLayout_13 = QGridLayout(self.widget_34)
        self.gridLayout_13.setSpacing(0)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(10, 0, 0, 0)
        self.transaction_history_fourth_line_type_label = QLabel(self.widget_34)
        self.transaction_history_fourth_line_type_label.setObjectName(u"transaction_history_fourth_line_type_label")
        self.transaction_history_fourth_line_type_label.setFont(font4)
        self.transaction_history_fourth_line_type_label.setStyleSheet(u"color:rgba(255,255,255,0.8);")

        self.gridLayout_13.addWidget(self.transaction_history_fourth_line_type_label, 0, 1, 1, 1)

        self.transaction_history_fourth_line_date_label = QLabel(self.widget_34)
        self.transaction_history_fourth_line_date_label.setObjectName(u"transaction_history_fourth_line_date_label")
        self.transaction_history_fourth_line_date_label.setFont(font4)
        self.transaction_history_fourth_line_date_label.setStyleSheet(u"color:rgba(255,255,255,0.8);")

        self.gridLayout_13.addWidget(self.transaction_history_fourth_line_date_label, 0, 2, 1, 1)

        self.transaction_history_fourth_line_reciever_label = QLabel(self.widget_34)
        self.transaction_history_fourth_line_reciever_label.setObjectName(u"transaction_history_fourth_line_reciever_label")
        self.transaction_history_fourth_line_reciever_label.setFont(font4)
        self.transaction_history_fourth_line_reciever_label.setStyleSheet(u"color: white;")

        self.gridLayout_13.addWidget(self.transaction_history_fourth_line_reciever_label, 0, 0, 1, 1)

        self.transaction_history_fourth_line_value_label = QLabel(self.widget_34)
        self.transaction_history_fourth_line_value_label.setObjectName(u"transaction_history_fourth_line_value_label")
        self.transaction_history_fourth_line_value_label.setFont(font4)
        self.transaction_history_fourth_line_value_label.setStyleSheet(u"color: white;")
        self.transaction_history_fourth_line_value_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_13.addWidget(self.transaction_history_fourth_line_value_label, 0, 3, 1, 1)


        self.gridLayout_15.addWidget(self.widget_34, 8, 0, 1, 1)

        self.transaction_history_topic_label = QLabel(self.transaction_history_widget)
        self.transaction_history_topic_label.setObjectName(u"transaction_history_topic_label")
        self.transaction_history_topic_label.setFont(font2)
        self.transaction_history_topic_label.setStyleSheet(u"color: white;")

        self.gridLayout_15.addWidget(self.transaction_history_topic_label, 0, 0, 1, 1)

        self.widget_31 = QWidget(self.transaction_history_widget)
        self.widget_31.setObjectName(u"widget_31")
        self.gridLayout_10 = QGridLayout(self.widget_31)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(10, 0, 0, 0)
        self.transaction_history_first_line_reciever_label = QLabel(self.widget_31)
        self.transaction_history_first_line_reciever_label.setObjectName(u"transaction_history_first_line_reciever_label")
        self.transaction_history_first_line_reciever_label.setFont(font4)
        self.transaction_history_first_line_reciever_label.setStyleSheet(u"color: white;")

        self.gridLayout_10.addWidget(self.transaction_history_first_line_reciever_label, 0, 0, 1, 1)

        self.transaction_history_first_line_type_label = QLabel(self.widget_31)
        self.transaction_history_first_line_type_label.setObjectName(u"transaction_history_first_line_type_label")
        self.transaction_history_first_line_type_label.setFont(font4)
        self.transaction_history_first_line_type_label.setStyleSheet(u"color:rgba(255,255,255,0.8);")

        self.gridLayout_10.addWidget(self.transaction_history_first_line_type_label, 0, 1, 1, 1)

        self.transaction_history_first_line_value_label = QLabel(self.widget_31)
        self.transaction_history_first_line_value_label.setObjectName(u"transaction_history_first_line_value_label")
        self.transaction_history_first_line_value_label.setFont(font4)
        self.transaction_history_first_line_value_label.setStyleSheet(u"color: white;")
        self.transaction_history_first_line_value_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.transaction_history_first_line_value_label, 0, 3, 1, 1)

        self.transaction_history_first_line_date_label = QLabel(self.widget_31)
        self.transaction_history_first_line_date_label.setObjectName(u"transaction_history_first_line_date_label")
        self.transaction_history_first_line_date_label.setFont(font4)
        self.transaction_history_first_line_date_label.setStyleSheet(u"color:rgba(255,255,255,0.8);")

        self.gridLayout_10.addWidget(self.transaction_history_first_line_date_label, 0, 2, 1, 1)


        self.gridLayout_15.addWidget(self.widget_31, 2, 0, 1, 1)

        self.widget_35 = QWidget(self.transaction_history_widget)
        self.widget_35.setObjectName(u"widget_35")
        self.gridLayout_14 = QGridLayout(self.widget_35)
        self.gridLayout_14.setSpacing(0)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(10, 0, 0, 0)
        self.transaction_history_fifth_line_reciever_label = QLabel(self.widget_35)
        self.transaction_history_fifth_line_reciever_label.setObjectName(u"transaction_history_fifth_line_reciever_label")
        self.transaction_history_fifth_line_reciever_label.setFont(font4)
        self.transaction_history_fifth_line_reciever_label.setStyleSheet(u"color: white;")

        self.gridLayout_14.addWidget(self.transaction_history_fifth_line_reciever_label, 0, 0, 1, 1)

        self.transaction_history_fifth_line_value_label = QLabel(self.widget_35)
        self.transaction_history_fifth_line_value_label.setObjectName(u"transaction_history_fifth_line_value_label")
        self.transaction_history_fifth_line_value_label.setFont(font4)
        self.transaction_history_fifth_line_value_label.setStyleSheet(u"color: white;")
        self.transaction_history_fifth_line_value_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_14.addWidget(self.transaction_history_fifth_line_value_label, 0, 3, 1, 1)

        self.transaction_history_fifth_line_type_label = QLabel(self.widget_35)
        self.transaction_history_fifth_line_type_label.setObjectName(u"transaction_history_fifth_line_type_label")
        self.transaction_history_fifth_line_type_label.setFont(font4)
        self.transaction_history_fifth_line_type_label.setStyleSheet(u"color:rgba(255,255,255,0.8);")

        self.gridLayout_14.addWidget(self.transaction_history_fifth_line_type_label, 0, 1, 1, 1)

        self.transaction_history_fifth_line_date_label = QLabel(self.widget_35)
        self.transaction_history_fifth_line_date_label.setObjectName(u"transaction_history_fifth_line_date_label")
        self.transaction_history_fifth_line_date_label.setFont(font4)
        self.transaction_history_fifth_line_date_label.setStyleSheet(u"color:rgba(255,255,255,0.8);")

        self.gridLayout_14.addWidget(self.transaction_history_fifth_line_date_label, 0, 2, 1, 1)


        self.gridLayout_15.addWidget(self.widget_35, 10, 0, 1, 1)

        self.widget_32 = QWidget(self.transaction_history_widget)
        self.widget_32.setObjectName(u"widget_32")
        self.gridLayout_11 = QGridLayout(self.widget_32)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(10, 0, 0, 0)
        self.transaction_history_second_line_date_label = QLabel(self.widget_32)
        self.transaction_history_second_line_date_label.setObjectName(u"transaction_history_second_line_date_label")
        self.transaction_history_second_line_date_label.setFont(font4)
        self.transaction_history_second_line_date_label.setStyleSheet(u"color:rgba(255,255,255,0.8);")

        self.gridLayout_11.addWidget(self.transaction_history_second_line_date_label, 0, 2, 1, 1)

        self.transaction_history_second_line_reciever_label = QLabel(self.widget_32)
        self.transaction_history_second_line_reciever_label.setObjectName(u"transaction_history_second_line_reciever_label")
        self.transaction_history_second_line_reciever_label.setFont(font4)
        self.transaction_history_second_line_reciever_label.setStyleSheet(u"color: white;")

        self.gridLayout_11.addWidget(self.transaction_history_second_line_reciever_label, 0, 0, 1, 1)

        self.transaction_history_second_line_value_label = QLabel(self.widget_32)
        self.transaction_history_second_line_value_label.setObjectName(u"transaction_history_second_line_value_label")
        self.transaction_history_second_line_value_label.setFont(font4)
        self.transaction_history_second_line_value_label.setStyleSheet(u"color: white;")
        self.transaction_history_second_line_value_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_11.addWidget(self.transaction_history_second_line_value_label, 0, 3, 1, 1)

        self.transaction_history_second_line_type_label = QLabel(self.widget_32)
        self.transaction_history_second_line_type_label.setObjectName(u"transaction_history_second_line_type_label")
        self.transaction_history_second_line_type_label.setFont(font4)
        self.transaction_history_second_line_type_label.setStyleSheet(u"color:rgba(255,255,255,0.8);")

        self.gridLayout_11.addWidget(self.transaction_history_second_line_type_label, 0, 1, 1, 1)


        self.gridLayout_15.addWidget(self.widget_32, 4, 0, 1, 1)

        self.widget_3 = QWidget(self.transaction_history_widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMaximumSize(QSize(16777215, 1))
        self.widget_3.setStyleSheet(u"background-color:white;\n"
"border-radius:0.5px;")

        self.gridLayout_15.addWidget(self.widget_3, 7, 0, 1, 1)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.transaction_history_topic_reciever_label = QLabel(self.transaction_history_widget)
        self.transaction_history_topic_reciever_label.setObjectName(u"transaction_history_topic_reciever_label")
        self.transaction_history_topic_reciever_label.setFont(font3)
        self.transaction_history_topic_reciever_label.setStyleSheet(u"color:rgba(255,255,255,0.8);")

        self.horizontalLayout_30.addWidget(self.transaction_history_topic_reciever_label)

        self.horizontalSpacer_43 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_43)

        self.transaction_history_topic_type_label = QLabel(self.transaction_history_widget)
        self.transaction_history_topic_type_label.setObjectName(u"transaction_history_topic_type_label")
        self.transaction_history_topic_type_label.setFont(font3)
        self.transaction_history_topic_type_label.setStyleSheet(u"color:rgba(255,255,255,0.8);")

        self.horizontalLayout_30.addWidget(self.transaction_history_topic_type_label)

        self.horizontalSpacer_44 = QSpacerItem(90, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_44)

        self.transaction_history_topic_date_label = QLabel(self.transaction_history_widget)
        self.transaction_history_topic_date_label.setObjectName(u"transaction_history_topic_date_label")
        self.transaction_history_topic_date_label.setFont(font3)
        self.transaction_history_topic_date_label.setStyleSheet(u"color:rgba(255,255,255,0.8);")

        self.horizontalLayout_30.addWidget(self.transaction_history_topic_date_label)

        self.horizontalSpacer_45 = QSpacerItem(228, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_45)


        self.gridLayout_15.addLayout(self.horizontalLayout_30, 1, 0, 1, 1)

        self.widget = QWidget(self.transaction_history_widget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 1))
        self.widget.setMaximumSize(QSize(16777215, 1))
        self.widget.setStyleSheet(u"background-color:white;\n"
"border-radius:0.5px;")

        self.gridLayout_15.addWidget(self.widget, 3, 0, 1, 1)

        self.widget_2 = QWidget(self.transaction_history_widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(16777215, 1))
        self.widget_2.setStyleSheet(u"background-color:white;\n"
"border-radius:0.5px;")

        self.gridLayout_15.addWidget(self.widget_2, 5, 0, 1, 1)

        self.widget_4 = QWidget(self.transaction_history_widget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMaximumSize(QSize(16777215, 1))
        self.widget_4.setStyleSheet(u"background-color:white;\n"
"border-radius:0.5px;")

        self.gridLayout_15.addWidget(self.widget_4, 9, 0, 1, 1)


        self.horizontalLayout_38.addWidget(self.transaction_history_widget)

        self.horizontalSpacer_53 = QSpacerItem(48, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_53)

        self.graph_comparison_widget_stacked = QStackedWidget(self.dashboard_widget)
        self.graph_comparison_widget_stacked.setObjectName(u"graph_comparison_widget_stacked")
        self.graph_comparison_widget_stacked.setMinimumSize(QSize(890, 300))
        self.graph_comparison_widget_stacked.setMaximumSize(QSize(890, 300))
        self.graph_comparison_widget_stacked.setStyleSheet(u"background-color: #535C91;\n"
"border-radius: 23px;")
        self.weekly_compariso_page = QWidget()
        self.weekly_compariso_page.setObjectName(u"weekly_compariso_page")
        self.graph_comparison_sixth_day_label = QLabel(self.weekly_compariso_page)
        self.graph_comparison_sixth_day_label.setObjectName(u"graph_comparison_sixth_day_label")
        self.graph_comparison_sixth_day_label.setGeometry(QRect(680, 240, 47, 13))
        font15 = QFont()
        font15.setFamilies([u"Poppins"])
        self.graph_comparison_sixth_day_label.setFont(font15)
        self.graph_comparison_sixth_day_label.setStyleSheet(u"color: rgba(255,250,250,1);")
        self.graph_comparison_sixth_day_label.setAlignment(Qt.AlignCenter)
        self.graph_comparison_third_line_label = QLabel(self.weekly_compariso_page)
        self.graph_comparison_third_line_label.setObjectName(u"graph_comparison_third_line_label")
        self.graph_comparison_third_line_label.setGeometry(QRect(30, 145, 47, 13))
        self.graph_comparison_third_line_label.setFont(font15)
        self.graph_comparison_third_line_label.setStyleSheet(u"color: rgba(255,250,250,0.6);")
        self.graph_comparison_third_line_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_153 = QLabel(self.weekly_compariso_page)
        self.label_153.setObjectName(u"label_153")
        self.label_153.setGeometry(QRect(100, 150, 771, 1))
        self.label_153.setStyleSheet(u"background-color:rgba(250, 250, 250, 0.6);")
        self.graph_comparison_second_this_week_label = QLabel(self.weekly_compariso_page)
        self.graph_comparison_second_this_week_label.setObjectName(u"graph_comparison_second_this_week_label")
        self.graph_comparison_second_this_week_label.setGeometry(QRect(264, 120, 20, 111))
        self.graph_comparison_second_this_week_label.setStyleSheet(u"background-color:#1B1A55;\n"
"border-top-left-radius:5px;\n"
"border-top-right-radius:5px;")
        self.graph_comparison_fourth_last_week_label = QLabel(self.weekly_compariso_page)
        self.graph_comparison_fourth_last_week_label.setObjectName(u"graph_comparison_fourth_last_week_label")
        self.graph_comparison_fourth_last_week_label.setGeometry(QRect(464, 90, 16, 141))
        self.graph_comparison_fourth_last_week_label.setStyleSheet(u"background-color:white;\n"
"border-top-left-radius:5px;\n"
"border-top-right-radius:5px;")
        self.graph_comparison_fourth_line_label = QLabel(self.weekly_compariso_page)
        self.graph_comparison_fourth_line_label.setObjectName(u"graph_comparison_fourth_line_label")
        self.graph_comparison_fourth_line_label.setGeometry(QRect(30, 185, 47, 13))
        self.graph_comparison_fourth_line_label.setFont(font15)
        self.graph_comparison_fourth_line_label.setStyleSheet(u"color: rgba(255,250,250,0.6);")
        self.graph_comparison_fourth_line_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_157 = QLabel(self.weekly_compariso_page)
        self.label_157.setObjectName(u"label_157")
        self.label_157.setGeometry(QRect(100, 230, 771, 1))
        self.label_157.setStyleSheet(u"background-color:rgba(250, 250, 250, 0.6);")
        self.graph_comparison_third_last_week_label = QLabel(self.weekly_compariso_page)
        self.graph_comparison_third_last_week_label.setObjectName(u"graph_comparison_third_last_week_label")
        self.graph_comparison_third_last_week_label.setGeometry(QRect(354, 90, 16, 141))
        self.graph_comparison_third_last_week_label.setStyleSheet(u"background-color:white;\n"
"border-top-left-radius:5px;\n"
"border-top-right-radius:5px;")
        self.label_159 = QLabel(self.weekly_compariso_page)
        self.label_159.setObjectName(u"label_159")
        self.label_159.setGeometry(QRect(100, 190, 771, 1))
        self.label_159.setStyleSheet(u"background-color:rgba(250, 250, 250, 0.6);")
        self.graph_comparison_fourth_this_week_label = QLabel(self.weekly_compariso_page)
        self.graph_comparison_fourth_this_week_label.setObjectName(u"graph_comparison_fourth_this_week_label")
        self.graph_comparison_fourth_this_week_label.setGeometry(QRect(484, 120, 20, 111))
        self.graph_comparison_fourth_this_week_label.setStyleSheet(u"background-color:#1B1A55;\n"
"border-top-left-radius:5px;\n"
"border-top-right-radius:5px;")
        self.graph_comparison_sixth_this_week_label = QLabel(self.weekly_compariso_page)
        self.graph_comparison_sixth_this_week_label.setObjectName(u"graph_comparison_sixth_this_week_label")
        self.graph_comparison_sixth_this_week_label.setGeometry(QRect(704, 120, 20, 111))
        self.graph_comparison_sixth_this_week_label.setStyleSheet(u"background-color:#1B1A55;\n"
"border-top-left-radius:5px;\n"
"border-top-right-radius:5px;")
        self.graph_comparison_first_line_label = QLabel(self.weekly_compariso_page)
        self.graph_comparison_first_line_label.setObjectName(u"graph_comparison_first_line_label")
        self.graph_comparison_first_line_label.setGeometry(QRect(30, 65, 47, 13))
        self.graph_comparison_first_line_label.setFont(font15)
        self.graph_comparison_first_line_label.setStyleSheet(u"color: rgba(255,250,250,0.6);")
        self.graph_comparison_first_line_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.graph_comparison_fourth_day_label = QLabel(self.weekly_compariso_page)
        self.graph_comparison_fourth_day_label.setObjectName(u"graph_comparison_fourth_day_label")
        self.graph_comparison_fourth_day_label.setGeometry(QRect(460, 240, 47, 13))
        self.graph_comparison_fourth_day_label.setFont(font15)
        self.graph_comparison_fourth_day_label.setStyleSheet(u"color: rgba(255,250,250,1);")
        self.graph_comparison_fourth_day_label.setAlignment(Qt.AlignCenter)
        self.graph_comparison_seventh_this_week_label = QLabel(self.weekly_compariso_page)
        self.graph_comparison_seventh_this_week_label.setObjectName(u"graph_comparison_seventh_this_week_label")
        self.graph_comparison_seventh_this_week_label.setGeometry(QRect(824, 120, 20, 111))
        self.graph_comparison_seventh_this_week_label.setStyleSheet(u"background-color:#1B1A55;\n"
"border-top-left-radius:5px;\n"
"border-top-right-radius:5px;")
        self.graph_comparison_fifth_day_label = QLabel(self.weekly_compariso_page)
        self.graph_comparison_fifth_day_label.setObjectName(u"graph_comparison_fifth_day_label")
        self.graph_comparison_fifth_day_label.setGeometry(QRect(560, 240, 47, 13))
        self.graph_comparison_fifth_day_label.setFont(font15)
        self.graph_comparison_fifth_day_label.setStyleSheet(u"color: rgba(255,250,250,1);")
        self.graph_comparison_fifth_day_label.setAlignment(Qt.AlignCenter)
        self.label_166 = QLabel(self.weekly_compariso_page)
        self.label_166.setObjectName(u"label_166")
        self.label_166.setGeometry(QRect(100, 70, 771, 1))
        self.label_166.setStyleSheet(u"background-color:rgba(250, 250, 250, 0.6);")
        self.graph_comparison_second_line_label = QLabel(self.weekly_compariso_page)
        self.graph_comparison_second_line_label.setObjectName(u"graph_comparison_second_line_label")
        self.graph_comparison_second_line_label.setGeometry(QRect(30, 105, 47, 13))
        self.graph_comparison_second_line_label.setFont(font15)
        self.graph_comparison_second_line_label.setStyleSheet(u"color: rgba(255,250,250,0.6);")
        self.graph_comparison_second_line_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.graph_comparison_third_day_label = QLabel(self.weekly_compariso_page)
        self.graph_comparison_third_day_label.setObjectName(u"graph_comparison_third_day_label")
        self.graph_comparison_third_day_label.setGeometry(QRect(350, 240, 47, 13))
        self.graph_comparison_third_day_label.setFont(font15)
        self.graph_comparison_third_day_label.setStyleSheet(u"color: rgba(255,250,250,1);")
        self.graph_comparison_third_day_label.setAlignment(Qt.AlignCenter)
        self.graph_comparison_third_this_week_label = QLabel(self.weekly_compariso_page)
        self.graph_comparison_third_this_week_label.setObjectName(u"graph_comparison_third_this_week_label")
        self.graph_comparison_third_this_week_label.setGeometry(QRect(374, 120, 20, 111))
        self.graph_comparison_third_this_week_label.setStyleSheet(u"background-color:#1B1A55;\n"
"border-top-left-radius:5px;\n"
"border-top-right-radius:5px;")
        self.label_170 = QLabel(self.weekly_compariso_page)
        self.label_170.setObjectName(u"label_170")
        self.label_170.setGeometry(QRect(100, 110, 771, 1))
        self.label_170.setStyleSheet(u"background-color:rgba(250, 250, 250, 0.6);")
        self.graph_comparison_fifth_this_week_label = QLabel(self.weekly_compariso_page)
        self.graph_comparison_fifth_this_week_label.setObjectName(u"graph_comparison_fifth_this_week_label")
        self.graph_comparison_fifth_this_week_label.setGeometry(QRect(584, 120, 20, 111))
        self.graph_comparison_fifth_this_week_label.setStyleSheet(u"background-color:#1B1A55;\n"
"border-top-left-radius:5px;\n"
"border-top-right-radius:5px;")
        self.graph_comparison_seventh_day_label = QLabel(self.weekly_compariso_page)
        self.graph_comparison_seventh_day_label.setObjectName(u"graph_comparison_seventh_day_label")
        self.graph_comparison_seventh_day_label.setGeometry(QRect(800, 240, 47, 13))
        self.graph_comparison_seventh_day_label.setFont(font15)
        self.graph_comparison_seventh_day_label.setStyleSheet(u"color: rgba(255,250,250,1);")
        self.graph_comparison_seventh_day_label.setAlignment(Qt.AlignCenter)
        self.graph_comparison_combobox = QComboBox(self.weekly_compariso_page)
        self.graph_comparison_combobox.addItem("")
        self.graph_comparison_combobox.addItem("")
        self.graph_comparison_combobox.setObjectName(u"graph_comparison_combobox")
        self.graph_comparison_combobox.setGeometry(QRect(40, 25, 171, 21))
        self.graph_comparison_combobox.setFont(font4)
        self.graph_comparison_combobox.setStyleSheet(u"QComboBox\n"
"{\n"
"	color:white;\n"
"	background-color:transparent;\n"
"}\n"
"QComboBox:editable {\n"
"    color: white;\n"
"	background-color:transparent;\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"	border:none;\n"
"    color: white;\n"
"	background-color:transparent;\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"	image: url(:/img/img/chevron-down.svg);\n"
"	width:32px;\n"
"	height:32px;\n"
"	margin-right:20px;\n"
"    color: white;\n"
"	background-color:transparent;\n"
"}\n"
"QComboBox::down-arrow:on\n"
"{	\n"
"	image: url(:/img/img/chevron-up.svg);\n"
"	width:32px;\n"
"	height:32px;\n"
"	margin-right:20px;\n"
"    color: white;\n"
"	background-color:transparent;\n"
"}")
        self.graph_comparison_first_day_label = QLabel(self.weekly_compariso_page)
        self.graph_comparison_first_day_label.setObjectName(u"graph_comparison_first_day_label")
        self.graph_comparison_first_day_label.setGeometry(QRect(150, 240, 47, 13))
        self.graph_comparison_first_day_label.setFont(font15)
        self.graph_comparison_first_day_label.setStyleSheet(u"color: rgba(255,250,250,1);")
        self.graph_comparison_first_day_label.setAlignment(Qt.AlignCenter)
        self.graph_comparison_second_last_week_label = QLabel(self.weekly_compariso_page)
        self.graph_comparison_second_last_week_label.setObjectName(u"graph_comparison_second_last_week_label")
        self.graph_comparison_second_last_week_label.setGeometry(QRect(244, 90, 16, 141))
        self.graph_comparison_second_last_week_label.setStyleSheet(u"background-color:white;\n"
"border-top-left-radius:5px;\n"
"border-top-right-radius:5px;")
        self.graph_comparison_fifth_line_label = QLabel(self.weekly_compariso_page)
        self.graph_comparison_fifth_line_label.setObjectName(u"graph_comparison_fifth_line_label")
        self.graph_comparison_fifth_line_label.setGeometry(QRect(30, 225, 47, 13))
        self.graph_comparison_fifth_line_label.setFont(font15)
        self.graph_comparison_fifth_line_label.setStyleSheet(u"color: rgba(255,250,250,0.6);")
        self.graph_comparison_fifth_line_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.graph_comparison_sixth_last_week_label = QLabel(self.weekly_compariso_page)
        self.graph_comparison_sixth_last_week_label.setObjectName(u"graph_comparison_sixth_last_week_label")
        self.graph_comparison_sixth_last_week_label.setGeometry(QRect(684, 90, 16, 141))
        self.graph_comparison_sixth_last_week_label.setStyleSheet(u"background-color:white;\n"
"border-top-left-radius:5px;\n"
"border-top-right-radius:5px;")
        self.graph_comparison_first_this_week_label = QLabel(self.weekly_compariso_page)
        self.graph_comparison_first_this_week_label.setObjectName(u"graph_comparison_first_this_week_label")
        self.graph_comparison_first_this_week_label.setGeometry(QRect(174, 120, 20, 111))
        self.graph_comparison_first_this_week_label.setStyleSheet(u"background-color:#1B1A55;\n"
"border-top-left-radius:5px;\n"
"border-top-right-radius:5px;")
        self.graph_comparison_seventh_last_week_label = QLabel(self.weekly_compariso_page)
        self.graph_comparison_seventh_last_week_label.setObjectName(u"graph_comparison_seventh_last_week_label")
        self.graph_comparison_seventh_last_week_label.setGeometry(QRect(804, 90, 16, 141))
        self.graph_comparison_seventh_last_week_label.setStyleSheet(u"background-color:white;\n"
"border-top-left-radius:5px;\n"
"border-top-right-radius:5px;")
        self.graph_comparison_first_last_week_label = QLabel(self.weekly_compariso_page)
        self.graph_comparison_first_last_week_label.setObjectName(u"graph_comparison_first_last_week_label")
        self.graph_comparison_first_last_week_label.setGeometry(QRect(154, 90, 16, 141))
        self.graph_comparison_first_last_week_label.setStyleSheet(u"background-color:white;\n"
"border-top-left-radius:5px;\n"
"border-top-right-radius:5px;")
        self.graph_comparison_second_day_label = QLabel(self.weekly_compariso_page)
        self.graph_comparison_second_day_label.setObjectName(u"graph_comparison_second_day_label")
        self.graph_comparison_second_day_label.setGeometry(QRect(240, 240, 47, 13))
        self.graph_comparison_second_day_label.setFont(font15)
        self.graph_comparison_second_day_label.setStyleSheet(u"color: rgba(255,250,250,1);")
        self.graph_comparison_second_day_label.setAlignment(Qt.AlignCenter)
        self.graph_comparison_fifth_last_week_label = QLabel(self.weekly_compariso_page)
        self.graph_comparison_fifth_last_week_label.setObjectName(u"graph_comparison_fifth_last_week_label")
        self.graph_comparison_fifth_last_week_label.setGeometry(QRect(564, 90, 16, 141))
        self.graph_comparison_fifth_last_week_label.setStyleSheet(u"background-color:white;\n"
"border-top-left-radius:5px;\n"
"border-top-right-radius:5px;")
        self.thi_week_color_widget = QWidget(self.weekly_compariso_page)
        self.thi_week_color_widget.setObjectName(u"thi_week_color_widget")
        self.thi_week_color_widget.setGeometry(QRect(660, 10, 16, 11))
        self.thi_week_color_widget.setMinimumSize(QSize(16, 11))
        self.thi_week_color_widget.setMaximumSize(QSize(16, 11))
        self.thi_week_color_widget.setStyleSheet(u"background-color:#1B1A55;\n"
"border-radius:3px;")
        self.last_week_color_widget = QWidget(self.weekly_compariso_page)
        self.last_week_color_widget.setObjectName(u"last_week_color_widget")
        self.last_week_color_widget.setGeometry(QRect(770, 10, 16, 11))
        self.last_week_color_widget.setMinimumSize(QSize(16, 11))
        self.last_week_color_widget.setMaximumSize(QSize(16, 11))
        self.last_week_color_widget.setStyleSheet(u"background-color:white;\n"
"border-radius:3px;")
        self.this_week_label = QLabel(self.weekly_compariso_page)
        self.this_week_label.setObjectName(u"this_week_label")
        self.this_week_label.setGeometry(QRect(680, 9, 81, 16))
        self.this_week_label.setFont(font4)
        self.this_week_label.setStyleSheet(u"background-color:transparent;\n"
"color:white;")
        self.last_week_label = QLabel(self.weekly_compariso_page)
        self.last_week_label.setObjectName(u"last_week_label")
        self.last_week_label.setGeometry(QRect(790, 9, 81, 16))
        self.last_week_label.setFont(font4)
        self.last_week_label.setStyleSheet(u"background-color:transparent;\n"
"color:white;")
        self.graph_comparison_widget_stacked.addWidget(self.weekly_compariso_page)
        self.graph_comparison_sixth_day_label.raise_()
        self.graph_comparison_third_line_label.raise_()
        self.label_153.raise_()
        self.graph_comparison_fourth_last_week_label.raise_()
        self.graph_comparison_fourth_line_label.raise_()
        self.label_157.raise_()
        self.graph_comparison_third_last_week_label.raise_()
        self.label_159.raise_()
        self.graph_comparison_sixth_this_week_label.raise_()
        self.graph_comparison_first_line_label.raise_()
        self.graph_comparison_fourth_day_label.raise_()
        self.graph_comparison_seventh_this_week_label.raise_()
        self.graph_comparison_fifth_day_label.raise_()
        self.label_166.raise_()
        self.graph_comparison_second_line_label.raise_()
        self.graph_comparison_third_day_label.raise_()
        self.label_170.raise_()
        self.graph_comparison_seventh_day_label.raise_()
        self.graph_comparison_combobox.raise_()
        self.graph_comparison_first_day_label.raise_()
        self.graph_comparison_second_last_week_label.raise_()
        self.graph_comparison_fifth_line_label.raise_()
        self.graph_comparison_sixth_last_week_label.raise_()
        self.graph_comparison_first_this_week_label.raise_()
        self.graph_comparison_seventh_last_week_label.raise_()
        self.graph_comparison_first_last_week_label.raise_()
        self.graph_comparison_second_day_label.raise_()
        self.graph_comparison_fifth_last_week_label.raise_()
        self.graph_comparison_fifth_this_week_label.raise_()
        self.graph_comparison_fourth_this_week_label.raise_()
        self.graph_comparison_third_this_week_label.raise_()
        self.graph_comparison_second_this_week_label.raise_()
        self.thi_week_color_widget.raise_()
        self.last_week_color_widget.raise_()
        self.this_week_label.raise_()
        self.last_week_label.raise_()
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.graph_comparison_widget_stacked.addWidget(self.page_5)

        self.horizontalLayout_38.addWidget(self.graph_comparison_widget_stacked)

        self.horizontalSpacer_54 = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_54)


        self.verticalLayout_26.addLayout(self.horizontalLayout_38)

        self.verticalSpacer_41 = QSpacerItem(20, 3, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_26.addItem(self.verticalSpacer_41)

        self.main_screen_stacked_widget.addWidget(self.dashboard_widget)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.main_screen_stacked_widget.addWidget(self.page_2)

        self.gridLayout.addWidget(self.main_screen_stacked_widget, 1, 2, 1, 1)

        self.top_bar_widget = QWidget(self.centralwidget)
        self.top_bar_widget.setObjectName(u"top_bar_widget")
        self.top_bar_widget.setStyleSheet(u"QWidget{\n"
"	background-color:#1B1A55;\n"
"}\n"
"QPushButton{\n"
"	border:none;\n"
"}\n"
"")
        self.horizontalLayout_39 = QHBoxLayout(self.top_bar_widget)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.slider_button = QPushButton(self.top_bar_widget)
        self.slider_button.setObjectName(u"slider_button")
        font16 = QFont()
        font16.setFamilies([u"Poppins"])
        font16.setPointSize(14)
        font16.setBold(True)
        self.slider_button.setFont(font16)
        self.slider_button.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	height:42px;\n"
"	width: 32px;\n"
"	padding-left: 10px;\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/img/img/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.slider_button.setIcon(icon13)
        self.slider_button.setIconSize(QSize(32, 32))
        self.slider_button.setCheckable(True)
        self.slider_button.setAutoRepeat(False)
        self.slider_button.setAutoExclusive(False)

        self.horizontalLayout_2.addWidget(self.slider_button)

        self.fi_wallet_button = QPushButton(self.top_bar_widget)
        self.fi_wallet_button.setObjectName(u"fi_wallet_button")
        self.fi_wallet_button.setFont(font16)
        self.fi_wallet_button.setStyleSheet(u"color: white;\n"
"height:50px;\n"
"text-align: left;")
        icon14 = QIcon()
        icon14.addFile(u":/img/img/fi_wallet.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.fi_wallet_button.setIcon(icon14)
        self.fi_wallet_button.setIconSize(QSize(75, 75))
        self.fi_wallet_button.setCheckable(True)
        self.fi_wallet_button.setAutoRepeat(False)
        self.fi_wallet_button.setAutoExclusive(False)

        self.horizontalLayout_2.addWidget(self.fi_wallet_button)


        self.horizontalLayout_39.addLayout(self.horizontalLayout_2)

        self.horizontalSpacer_2 = QSpacerItem(503, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_39.addItem(self.horizontalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.search_line_edit = QLineEdit(self.top_bar_widget)
        self.search_line_edit.setObjectName(u"search_line_edit")
        self.search_line_edit.setMinimumSize(QSize(700, 36))
        self.search_line_edit.setMaximumSize(QSize(700, 36))
        self.search_line_edit.setStyleSheet(u"background-color: rgb(146, 144, 195);\n"
"font: 14pt \"Poppins\";\n"
"color:rgba(255,255,255,0.4);\n"
"border-top-left-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
" width: 700px;")
        self.search_line_edit.setFrame(False)
        self.search_line_edit.setAlignment(Qt.AlignCenter)
        self.search_line_edit.setReadOnly(False)
        self.search_line_edit.setClearButtonEnabled(True)

        self.horizontalLayout.addWidget(self.search_line_edit)

        self.search_button = QPushButton(self.top_bar_widget)
        self.search_button.setObjectName(u"search_button")
        self.search_button.setMinimumSize(QSize(32, 36))
        self.search_button.setMaximumSize(QSize(32, 36))
        self.search_button.setStyleSheet(u"background-color: rgb(146, 144, 195);\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"height:36px;")
        icon15 = QIcon()
        icon15.addFile(u":/img/img/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.search_button.setIcon(icon15)
        self.search_button.setIconSize(QSize(28, 28))
        self.search_button.setCheckable(True)
        self.search_button.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.search_button)


        self.horizontalLayout_39.addLayout(self.horizontalLayout)

        self.horizontalSpacer_55 = QSpacerItem(150, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_39.addItem(self.horizontalSpacer_55)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.notification_button = QPushButton(self.top_bar_widget)
        self.notification_button.setObjectName(u"notification_button")
        self.notification_button.setMinimumSize(QSize(40, 40))
        self.notification_button.setMaximumSize(QSize(40, 40))
        self.notification_button.setStyleSheet(u"QPushButton{\n"
"	wight: 40px;\n"
"	height: 40px;\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton:checked{\n"
"	background-color:#9290C3;\n"
"	color: #9290C3;\n"
"	font-weight:bold;\n"
"}")
        icon16 = QIcon()
        icon16.addFile(u":/img/img/bell.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.notification_button.setIcon(icon16)
        self.notification_button.setIconSize(QSize(25, 25))
        self.notification_button.setCheckable(True)
        self.notification_button.setAutoExclusive(True)

        self.horizontalLayout_3.addWidget(self.notification_button)

        self.calculator_button = QPushButton(self.top_bar_widget)
        self.calculator_button.setObjectName(u"calculator_button")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calculator_button.sizePolicy().hasHeightForWidth())
        self.calculator_button.setSizePolicy(sizePolicy)
        self.calculator_button.setMinimumSize(QSize(40, 40))
        self.calculator_button.setMaximumSize(QSize(40, 40))
        self.calculator_button.setStyleSheet(u"QPushButton{\n"
"	wight: 40px;\n"
"	height: 40px;\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton:checked{\n"
"	background-color:#9290C3;\n"
"	color: #9290C3;\n"
"	font-weight:bold;\n"
"}")
        icon17 = QIcon()
        icon17.addFile(u":/img/img/calculator.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.calculator_button.setIcon(icon17)
        self.calculator_button.setIconSize(QSize(35, 35))
        self.calculator_button.setCheckable(True)
        self.calculator_button.setAutoExclusive(True)

        self.horizontalLayout_3.addWidget(self.calculator_button)


        self.horizontalLayout_39.addLayout(self.horizontalLayout_3)

        self.horizontalSpacer = QSpacerItem(24, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_39.addItem(self.horizontalSpacer)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.full_screen_button = QPushButton(self.top_bar_widget)
        self.full_screen_button.setObjectName(u"full_screen_button")
        self.full_screen_button.setStyleSheet(u"wight: 40px;\n"
"height: 40px;")
        icon18 = QIcon()
        icon18.addFile(u":/img/img/maximize-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.full_screen_button.setIcon(icon18)
        self.full_screen_button.setIconSize(QSize(25, 25))
        self.full_screen_button.setCheckable(True)
        self.full_screen_button.setAutoExclusive(True)

        self.horizontalLayout_4.addWidget(self.full_screen_button)

        self.screen_minimize_button = QPushButton(self.top_bar_widget)
        self.screen_minimize_button.setObjectName(u"screen_minimize_button")
        self.screen_minimize_button.setStyleSheet(u"wight: 40px;\n"
"height: 40px;")
        icon19 = QIcon()
        icon19.addFile(u":/img/img/window_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.screen_minimize_button.setIcon(icon19)
        self.screen_minimize_button.setIconSize(QSize(25, 25))
        self.screen_minimize_button.setCheckable(True)
        self.screen_minimize_button.setAutoExclusive(True)

        self.horizontalLayout_4.addWidget(self.screen_minimize_button)

        self.maximize_screen_button = QCheckBox(self.top_bar_widget)
        self.maximize_screen_button.setObjectName(u"maximize_screen_button")
        self.maximize_screen_button.setFont(font)
        self.maximize_screen_button.setStyleSheet(u"QCheckBox{\n"
"	color:white;\n"
"	padding-left: 10px;\n"
"	background-color:transparent;\n"
"}\n"
"QCheckBox::indicator {\n"
"	width: 28px;\n"
"	height: 28px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"	image: url(:/img/img/window_screen.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked{\n"
"	image: url(:/img/img/square.svg);\n"
"}")
        self.maximize_screen_button.setCheckable(True)
        self.maximize_screen_button.setAutoExclusive(True)

        self.horizontalLayout_4.addWidget(self.maximize_screen_button)



        self.close_button = QPushButton(self.top_bar_widget)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setStyleSheet(u"wight: 40px;\n"
"height: 40px;")
        icon20 = QIcon()
        icon20.addFile(u":/img/img/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_button.setIcon(icon20)
        self.close_button.setIconSize(QSize(32, 32))
        self.close_button.setCheckable(True)
        self.close_button.setAutoExclusive(True)

        self.horizontalLayout_4.addWidget(self.close_button)


        self.horizontalLayout_39.addLayout(self.horizontalLayout_4)


        self.gridLayout.addWidget(self.top_bar_widget, 0, 0, 1, 3)
        self.close_button.clicked.connect(MainWindow.close)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.slider_button.toggled.connect(self.minimize_slider_menu_widget.setHidden)
        self.slider_button.toggled.connect(self.maximize_slider_menu_widget.setVisible)
        self.dashboard_minimize_button.toggled.connect(self.dashboard_button.setChecked)
        self.analist_minimize_button.toggled.connect(self.analist_button.setChecked)
        self.performance_minimize_button.toggled.connect(self.performance_button.setChecked)
        self.bills_minimize_button.toggled.connect(self.bills_button.setChecked)
        self.wallet_minimize_button.toggled.connect(self.wallet_button.setChecked)
        self.goal_minimize_button.toggled.connect(self.goal_button.setChecked)
        self.settings_minimize_button.toggled.connect(self.settings_button.setChecked)
        self.thema_minimize_button.toggled.connect(self.thema_button.setChecked)
        self.logout_minimize_button.toggled.connect(self.logout_button.setChecked)
        self.profile_minimize_button.toggled.connect(self.profile_button.setChecked)
        self.dashboard_button.toggled.connect(self.dashboard_minimize_button.setChecked)
        self.analist_button.toggled.connect(self.analist_minimize_button.setChecked)
        self.performance_button.toggled.connect(self.performance_minimize_button.setChecked)
        self.bills_button.toggled.connect(self.bills_minimize_button.setChecked)
        self.wallet_button.toggled.connect(self.wallet_minimize_button.setChecked)
        self.goal_button.toggled.connect(self.goal_minimize_button.setChecked)
        self.thema_button.toggled.connect(self.thema_minimize_button.setChecked)
        self.settings_button.toggled.connect(self.settings_minimize_button.setChecked)
        self.logout_button.toggled.connect(self.logout_minimize_button.setChecked)
        self.profile_button.toggled.connect(self.profile_minimize_button.setChecked)
        self.fi_wallet_button.toggled.connect(self.minimize_slider_menu_widget.setHidden)
        self.fi_wallet_button.toggled.connect(self.maximize_slider_menu_widget.setVisible)

        self.cards_stacked_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.profiles_combobox.setItemText(0, QCoreApplication.translate("MainWindow", u"Add Profile", None))
        self.profiles_combobox.setItemText(1, QCoreApplication.translate("MainWindow", u"Deneme", None))

        self.dashboard_button.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.analist_button.setText(QCoreApplication.translate("MainWindow", u"Analist", None))
        self.performance_button.setText(QCoreApplication.translate("MainWindow", u"Perfomance", None))
        self.bills_button.setText(QCoreApplication.translate("MainWindow", u"Bills", None))
        self.wallet_button.setText(QCoreApplication.translate("MainWindow", u"Wallet", None))
        self.goal_button.setText(QCoreApplication.translate("MainWindow", u"Goal", None))
        self.thema_button.setText(QCoreApplication.translate("MainWindow", u"Thema Mode", None))
        self.settings_button.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.logout_button.setText(QCoreApplication.translate("MainWindow", u"Log Out", None))
        self.profile_button.setText(QCoreApplication.translate("MainWindow", u"User Name", None))
        self.pushButton_2.setText("")
        self.dashboard_minimize_button.setText("")
        self.analist_minimize_button.setText("")
        self.performance_minimize_button.setText("")
        self.bills_minimize_button.setText("")
        self.wallet_minimize_button.setText("")
        self.goal_minimize_button.setText("")
        self.thema_minimize_button.setText("")
        self.settings_minimize_button.setText("")
        self.logout_minimize_button.setText("")
        self.profile_minimize_button.setText("")
        self.total_balance_green_wallet_icon_button.setText("")
        self.total_balance_label.setText(QCoreApplication.translate("MainWindow", u"Total Balance", None))
        self.tota_balance_value_label.setText(QCoreApplication.translate("MainWindow", u"$13256.20", None))
        self.total_spending_wallet_icon_button.setText("")
        self.total_spending_label.setText(QCoreApplication.translate("MainWindow", u"Total Spending", None))
        self.tota_spending_value_label.setText(QCoreApplication.translate("MainWindow", u"$13256.20", None))
        self.money_saved_wallet_icon_button.setText("")
        self.money_saved_label.setText(QCoreApplication.translate("MainWindow", u"Money Saved", None))
        self.money_saved_value_label.setText(QCoreApplication.translate("MainWindow", u"$13256.20", None))
        self.money_sent_wallet_icon_button.setText("")
        self.money_sent_label.setText(QCoreApplication.translate("MainWindow", u"Money Sent", None))
        self.money_sent_value_label.setText(QCoreApplication.translate("MainWindow", u"$13256.20", None))
        self.online_payments_wallet_icon_button.setText("")
        self.online_payments_label.setText(QCoreApplication.translate("MainWindow", u"Online Payments", None))
        self.online_payments_value_label.setText(QCoreApplication.translate("MainWindow", u"$13256.20", None))
        self.cards_topic_label.setText(QCoreApplication.translate("MainWindow", u"Cards", None))
        self.all_accounts_label.setText(QCoreApplication.translate("MainWindow", u"All Accounts", None))
        self.card_name_label.setText(QCoreApplication.translate("MainWindow", u"Money Pay", None))
        self.account_name_label.setText(QCoreApplication.translate("MainWindow", u"PREMIUM ACCOUNT", None))
        self.card1_card_number_label.setText(QCoreApplication.translate("MainWindow", u"6743 **** **** 5634", None))
        self.card1_card_holder_label.setText(QCoreApplication.translate("MainWindow", u"Card Holder", None))
        self.card1_card_name_label.setText(QCoreApplication.translate("MainWindow", u"Angela Bowler", None))
        self.card1_expier_date_label.setText(QCoreApplication.translate("MainWindow", u"Expire Date", None))
        self.card1_card_date_label.setText(QCoreApplication.translate("MainWindow", u"06/21", None))
        self.label_41.setText("")
        self.card1_current_balance_value_label.setText(QCoreApplication.translate("MainWindow", u"$5680.65", None))
        self.current_balance_label.setText(QCoreApplication.translate("MainWindow", u"Currnet Balance", None))
        self.card1_income_value_label.setText(QCoreApplication.translate("MainWindow", u"$1600.00", None))
        self.income_label.setText(QCoreApplication.translate("MainWindow", u"Income", None))
        self.deactive_card_button.setText("")
        self.deactive_card_label.setText(QCoreApplication.translate("MainWindow", u"Deactive Card", None))
        self.weeklypayments_limit_label.setText(QCoreApplication.translate("MainWindow", u"Weekly payments limit", None))
        self.card1_weekl_payment_limit_label.setText(QCoreApplication.translate("MainWindow", u"$320,6 / $4000", None))
        self.previous_button.setText(QCoreApplication.translate("MainWindow", u"< Previous", None))
        self.next_button.setText(QCoreApplication.translate("MainWindow", u"Next >", None))
        self.goal_top_target_value_label.setText(QCoreApplication.translate("MainWindow", u"$20,000", None))
        self.pushButton_27.setText("")
        self.goal_target_date_label.setText(QCoreApplication.translate("MainWindow", u"Feb, 2024", None))
        self.goal_this_month_target_icon_button.setText("")
        self.goal_this_month_target_label.setText(QCoreApplication.translate("MainWindow", u"This month Target", None))
        self.goal_this_month_target_value_label.setText(QCoreApplication.translate("MainWindow", u"$20,000", None))
        self.goal_target_achived_icon_button.setText("")
        self.goal_target_achived_label.setText(QCoreApplication.translate("MainWindow", u"Target Achived", None))
        self.goal_target_achived_value_label.setText(QCoreApplication.translate("MainWindow", u"$12,000", None))
        self.goal_graph_label.setText(QCoreApplication.translate("MainWindow", u"$12K", None))
        self.goal_topic_label.setText(QCoreApplication.translate("MainWindow", u"Goals", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Upcoming Bill", None))
        self.first_bill_date_month_label.setText(QCoreApplication.translate("MainWindow", u"May", None))
        self.first_bill_date_day_label.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.first_bill_topic_label.setText(QCoreApplication.translate("MainWindow", u"Turkcell", None))
        self.first_bill_status_label.setText(QCoreApplication.translate("MainWindow", u"Turkcell - Monthly", None))
        self.first_bill_last_charge_label.setText(QCoreApplication.translate("MainWindow", u"Last Charge - 14 May, 2024", None))
        self.first_bill_value_label.setText(QCoreApplication.translate("MainWindow", u"$150", None))
        self.second_bill_date_month_label.setText(QCoreApplication.translate("MainWindow", u"May", None))
        self.second_bill_date_day_label.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.second_bill_topic_label.setText(QCoreApplication.translate("MainWindow", u"Netflix", None))
        self.second_bill_status_label.setText(QCoreApplication.translate("MainWindow", u"Netflix - Monthly", None))
        self.second_bill_last_charge_label.setText(QCoreApplication.translate("MainWindow", u"Last Charge - 19 Jun, 2024", None))
        self.second_bill_value_label.setText(QCoreApplication.translate("MainWindow", u"$210", None))
        self.third_bill_date_month_label.setText(QCoreApplication.translate("MainWindow", u"May", None))
        self.third_bill_date_day_label.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.third_bill_topic_label.setText(QCoreApplication.translate("MainWindow", u"Spotify", None))
        self.third_bill_status_label.setText(QCoreApplication.translate("MainWindow", u"Spotify - Monthly", None))
        self.third_bill_last_charge_label.setText(QCoreApplication.translate("MainWindow", u"Last Charge - 23 Fab, 2024", None))
        self.third_bill_value_label.setText(QCoreApplication.translate("MainWindow", u"$310", None))
        self.transaction_history_third_line_reciever_label.setText(QCoreApplication.translate("MainWindow", u"Michael Knigth", None))
        self.transaction_history_third_line_type_label.setText(QCoreApplication.translate("MainWindow", u"Electronic", None))
        self.transaction_history_third_line_value_label.setText(QCoreApplication.translate("MainWindow", u"$80.76", None))
        self.transaction_history_third_line_date_label.setText(QCoreApplication.translate("MainWindow", u"11 Dec 2024", None))
        self.transaction_history_fourth_line_type_label.setText(QCoreApplication.translate("MainWindow", u"Electronic", None))
        self.transaction_history_fourth_line_date_label.setText(QCoreApplication.translate("MainWindow", u"11 Dec 2024", None))
        self.transaction_history_fourth_line_reciever_label.setText(QCoreApplication.translate("MainWindow", u"Michael Knigth", None))
        self.transaction_history_fourth_line_value_label.setText(QCoreApplication.translate("MainWindow", u"$80.76", None))
        self.transaction_history_topic_label.setText(QCoreApplication.translate("MainWindow", u"Transaction History", None))
        self.transaction_history_first_line_reciever_label.setText(QCoreApplication.translate("MainWindow", u"Michael Knigth", None))
        self.transaction_history_first_line_type_label.setText(QCoreApplication.translate("MainWindow", u"Electronic", None))
        self.transaction_history_first_line_value_label.setText(QCoreApplication.translate("MainWindow", u"$80.76", None))
        self.transaction_history_first_line_date_label.setText(QCoreApplication.translate("MainWindow", u"11 Dec 2024", None))
        self.transaction_history_fifth_line_reciever_label.setText(QCoreApplication.translate("MainWindow", u"Michael Knigth", None))
        self.transaction_history_fifth_line_value_label.setText(QCoreApplication.translate("MainWindow", u"$80.76", None))
        self.transaction_history_fifth_line_type_label.setText(QCoreApplication.translate("MainWindow", u"Electronic", None))
        self.transaction_history_fifth_line_date_label.setText(QCoreApplication.translate("MainWindow", u"11 Dec 2024", None))
        self.transaction_history_second_line_date_label.setText(QCoreApplication.translate("MainWindow", u"11 Dec 2024", None))
        self.transaction_history_second_line_reciever_label.setText(QCoreApplication.translate("MainWindow", u"Michael Knigth", None))
        self.transaction_history_second_line_value_label.setText(QCoreApplication.translate("MainWindow", u"$80.76", None))
        self.transaction_history_second_line_type_label.setText(QCoreApplication.translate("MainWindow", u"Electronic", None))
        self.transaction_history_topic_reciever_label.setText(QCoreApplication.translate("MainWindow", u"Reciever", None))
        self.transaction_history_topic_type_label.setText(QCoreApplication.translate("MainWindow", u"Type", None))
        self.transaction_history_topic_date_label.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.graph_comparison_sixth_day_label.setText(QCoreApplication.translate("MainWindow", u"22 Fri", None))
        self.graph_comparison_third_line_label.setText(QCoreApplication.translate("MainWindow", u"$10k", None))
        self.label_153.setText("")
        self.graph_comparison_second_this_week_label.setText("")
        self.graph_comparison_fourth_last_week_label.setText("")
        self.graph_comparison_fourth_line_label.setText(QCoreApplication.translate("MainWindow", u"$2k", None))
        self.label_157.setText("")
        self.graph_comparison_third_last_week_label.setText("")
        self.label_159.setText("")
        self.graph_comparison_fourth_this_week_label.setText("")
        self.graph_comparison_sixth_this_week_label.setText("")
        self.graph_comparison_first_line_label.setText(QCoreApplication.translate("MainWindow", u"$250k", None))
        self.graph_comparison_fourth_day_label.setText(QCoreApplication.translate("MainWindow", u"20 Wed", None))
        self.graph_comparison_seventh_this_week_label.setText("")
        self.graph_comparison_fifth_day_label.setText(QCoreApplication.translate("MainWindow", u"21 Thu", None))
        self.label_166.setText("")
        self.graph_comparison_second_line_label.setText(QCoreApplication.translate("MainWindow", u"$50k", None))
        self.graph_comparison_third_day_label.setText(QCoreApplication.translate("MainWindow", u"19 Tue", None))
        self.graph_comparison_third_this_week_label.setText("")
        self.label_170.setText("")
        self.graph_comparison_fifth_this_week_label.setText("")
        self.graph_comparison_seventh_day_label.setText(QCoreApplication.translate("MainWindow", u"23 Sat", None))
        self.graph_comparison_combobox.setItemText(0, QCoreApplication.translate("MainWindow", u"Weekly Comparison", None))
        self.graph_comparison_combobox.setItemText(1, QCoreApplication.translate("MainWindow", u"Deneme", None))

        self.graph_comparison_first_day_label.setText(QCoreApplication.translate("MainWindow", u"17 Sun", None))
        self.graph_comparison_second_last_week_label.setText("")
        self.graph_comparison_fifth_line_label.setText(QCoreApplication.translate("MainWindow", u"$0", None))
        self.graph_comparison_sixth_last_week_label.setText("")
        self.graph_comparison_first_this_week_label.setText("")
        self.graph_comparison_seventh_last_week_label.setText("")
        self.graph_comparison_first_last_week_label.setText("")
        self.graph_comparison_second_day_label.setText(QCoreApplication.translate("MainWindow", u"18 Mon", None))
        self.graph_comparison_fifth_last_week_label.setText("")
        self.this_week_label.setText(QCoreApplication.translate("MainWindow", u"This week", None))
        self.last_week_label.setText(QCoreApplication.translate("MainWindow", u"Last week", None))
        self.slider_button.setText("")
        self.fi_wallet_button.setText(QCoreApplication.translate("MainWindow", u"Fi-Wallet", None))
        self.search_line_edit.setText("")
        self.search_line_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.search_button.setText("")
        self.notification_button.setText("")
        self.calculator_button.setText("")
        self.full_screen_button.setText("")
        self.screen_minimize_button.setText("")
        self.maximize_screen_button.setText("")
        self.close_button.setText("")
    # retranslateUi
