# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_account.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QWidget)

class Ui_Add_Account(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(550, 620)
        MainWindow.setMinimumSize(QSize(550, 620))
        MainWindow.setMaximumSize(QSize(600, 700))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(600, 700))
        self.centralwidget.setMaximumSize(QSize(600, 700))
        self.centralwidget.setStyleSheet(u"background-color:transparent;")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 550, 620))
        font = QFont()
        font.setFamilies([u"Poppins"])
        font.setPointSize(10)
        self.widget.setFont(font)
        self.widget.setStyleSheet(u"background-color: #535C91;\n"
"border-radius: 25px;")
        self.account_name_lineedit = QLineEdit(self.widget)
        self.account_name_lineedit.setObjectName(u"account_name_lineedit")
        self.account_name_lineedit.setGeometry(QRect(40, 70, 431, 31))
        self.account_name_lineedit.setFont(font)
        self.account_name_lineedit.setStyleSheet(u"background-color:white;\n"
"border-radius:5px;")
        self.account_name = QLabel(self.widget)
        self.account_name.setObjectName(u"account_name")
        self.account_name.setGeometry(QRect(40, 30, 431, 16))
        font1 = QFont()
        font1.setFamilies([u"Poppins"])
        font1.setPointSize(11)
        self.account_name.setFont(font1)
        self.account_name.setStyleSheet(u"color:white;")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(30, 140, 431, 41))
        self.widget_2.setStyleSheet(u"QPushButton{\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton::checked{\n"
"	background-color:#1B1A55;\n"
"	color: white;\n"
"	font-weight: bold;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.card_button = QPushButton(self.widget_2)
        self.card_button.setObjectName(u"card_button")
        self.card_button.setFont(font)
        self.card_button.setStyleSheet(u"color:white;")
        self.card_button.setCheckable(True)
        self.card_button.setChecked(True)
        self.card_button.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.card_button)

        self.cash_button = QPushButton(self.widget_2)
        self.cash_button.setObjectName(u"cash_button")
        self.cash_button.setFont(font)
        self.cash_button.setStyleSheet(u"color:white;")
        self.cash_button.setCheckable(True)
        self.cash_button.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.cash_button)

        self.stackedWidget = QStackedWidget(self.widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 200, 501, 401))
        self.card_page = QWidget()
        self.card_page.setObjectName(u"card_page")
        self.acc_num_label = QLabel(self.card_page)
        self.acc_num_label.setObjectName(u"acc_num_label")
        self.acc_num_label.setGeometry(QRect(50, 40, 131, 20))
        self.acc_num_label.setFont(font)
        self.acc_num_label.setStyleSheet(u"background-color:transparent;\n"
"color:white;")
        self.card_number_lineedit = QLineEdit(self.card_page)
        self.card_number_lineedit.setObjectName(u"card_number_lineedit")
        self.card_number_lineedit.setGeometry(QRect(50, 80, 401, 31))
        self.card_number_lineedit.setFont(font)
        self.card_number_lineedit.setStyleSheet(u"background-color:white;\n"
"border-radius:5px;")
        self.amount_lineedit = QLineEdit(self.card_page)
        self.amount_lineedit.setObjectName(u"amount_lineedit")
        self.amount_lineedit.setGeometry(QRect(50, 190, 401, 31))
        self.amount_lineedit.setFont(font)
        self.amount_lineedit.setStyleSheet(u"background-color:white;\n"
"border-radius:5px;")
        self.amount_label = QLabel(self.card_page)
        self.amount_label.setObjectName(u"amount_label")
        self.amount_label.setGeometry(QRect(50, 150, 131, 20))
        self.amount_label.setFont(font)
        self.amount_label.setStyleSheet(u"background-color:transparent;\n"
"color:white;")
        self.widget_3 = QWidget(self.card_page)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(50, 310, 401, 58))
        self.widget_3.setStyleSheet(u"background-color: transparent;")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.card_cancel_button = QPushButton(self.widget_3)
        self.card_cancel_button.setObjectName(u"card_cancel_button")
        self.card_cancel_button.setMinimumSize(QSize(140, 40))
        self.card_cancel_button.setMaximumSize(QSize(140, 40))
        self.card_cancel_button.setStyleSheet(u"color:white;\n"
"border-radius: 15px;\n"
"border: 1px solid white;")

        self.horizontalLayout_2.addWidget(self.card_cancel_button)

        self.horizontalSpacer = QSpacerItem(88, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.card_save_button = QPushButton(self.widget_3)
        self.card_save_button.setObjectName(u"card_save_button")
        self.card_save_button.setMinimumSize(QSize(140, 40))
        self.card_save_button.setMaximumSize(QSize(140, 40))
        self.card_save_button.setStyleSheet(u"color:white;\n"
"border-radius: 15px;\n"
"background-color: #1B1A55;")

        self.horizontalLayout_2.addWidget(self.card_save_button)

        self.stackedWidget.addWidget(self.card_page)
        self.cash_page = QWidget()
        self.cash_page.setObjectName(u"cash_page")
        self.widget_4 = QWidget(self.cash_page)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(50, 310, 401, 58))
        self.widget_4.setStyleSheet(u"background-color: transparent;")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.cash_cancel_button = QPushButton(self.widget_4)
        self.cash_cancel_button.setObjectName(u"cash_cancel_button")
        self.cash_cancel_button.setMinimumSize(QSize(140, 40))
        self.cash_cancel_button.setMaximumSize(QSize(140, 40))
        self.cash_cancel_button.setStyleSheet(u"color:white;\n"
"border-radius: 15px;\n"
"border: 1px solid white;")

        self.horizontalLayout_3.addWidget(self.cash_cancel_button)

        self.horizontalSpacer_2 = QSpacerItem(88, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.cash_save_button = QPushButton(self.widget_4)
        self.cash_save_button.setObjectName(u"cash_save_button")
        self.cash_save_button.setMinimumSize(QSize(140, 40))
        self.cash_save_button.setMaximumSize(QSize(140, 40))
        self.cash_save_button.setStyleSheet(u"color:white;\n"
"border-radius: 15px;\n"
"background-color: #1B1A55;")

        self.horizontalLayout_3.addWidget(self.cash_save_button)

        self.amount_cash_label = QLabel(self.cash_page)
        self.amount_cash_label.setObjectName(u"amount_cash_label")
        self.amount_cash_label.setGeometry(QRect(50, 30, 381, 20))
        self.amount_cash_label.setFont(font)
        self.amount_cash_label.setStyleSheet(u"background-color:transparent;\n"
"color:white;")
        self.cash_amount_lineedit = QLineEdit(self.cash_page)
        self.cash_amount_lineedit.setObjectName(u"cash_amount_lineedit")
        self.cash_amount_lineedit.setGeometry(QRect(50, 70, 401, 31))
        self.cash_amount_lineedit.setFont(font)
        self.cash_amount_lineedit.setStyleSheet(u"background-color:white;\n"
"border-radius:5px;")
        self.stackedWidget.addWidget(self.cash_page)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.account_name_lineedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"   Name", None))
        self.account_name.setText(QCoreApplication.translate("MainWindow", u"Account Name", None))
        self.card_button.setText(QCoreApplication.translate("MainWindow", u"Cash", None))
        self.cash_button.setText(QCoreApplication.translate("MainWindow", u"Card", None))
        self.acc_num_label.setText(QCoreApplication.translate("MainWindow", u"Account Number", None))
        self.card_number_lineedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Card Number", None))
        self.amount_lineedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Amount", None))
        self.amount_label.setText(QCoreApplication.translate("MainWindow", u"Amount", None))
        self.card_cancel_button.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.card_save_button.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.cash_cancel_button.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.cash_save_button.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.amount_cash_label.setText(QCoreApplication.translate("MainWindow", u"Amount", None))
        self.cash_amount_lineedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Amount", None))
    # retranslateUi

