# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'forgetting_password.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)
import Register_rc

class Ui_en_main_widget(object):
    def setupUi(self, en_main_widget):
        if not en_main_widget.objectName():
            en_main_widget.setObjectName(u"en_main_widget")
        en_main_widget.resize(780, 589)
        en_main_widget.setMinimumSize(QSize(780, 589))
        en_main_widget.setMaximumSize(QSize(780, 589))
        self.merkez_widget = QWidget(en_main_widget)
        self.merkez_widget.setObjectName(u"merkez_widget")
        self.normal_widget = QWidget(self.merkez_widget)
        self.normal_widget.setObjectName(u"normal_widget")
        self.normal_widget.setGeometry(QRect(0, 0, 780, 590))
        self.normal_widget.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(83, 92, 145, 255), stop:1 rgba(27, 26, 85, 255));")
        self.logo = QPushButton(self.normal_widget)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(235, 70, 311, 61))
        font = QFont()
        font.setFamilies([u"Poppins"])
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        self.logo.setFont(font)
        self.logo.setStyleSheet(u"background-color:transparent;\n"
"color:white;\n"
"")
        icon = QIcon()
        icon.addFile(u":/img/img/Fewallet.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.logo.setIcon(icon)
        self.logo.setIconSize(QSize(150, 150))
        self.forget_widget = QLabel(self.normal_widget)
        self.forget_widget.setObjectName(u"forget_widget")
        self.forget_widget.setGeometry(QRect(290, 170, 211, 41))
        font1 = QFont()
        font1.setFamilies([u"Poppins"])
        font1.setPointSize(15)
        font1.setBold(False)
        font1.setItalic(False)
        self.forget_widget.setFont(font1)
        self.forget_widget.setStyleSheet(u"background-color:transparent;\n"
"color:white;")
        self.enter_email = QLabel(self.normal_widget)
        self.enter_email.setObjectName(u"enter_email")
        self.enter_email.setGeometry(QRect(225, 210, 351, 91))
        font2 = QFont()
        font2.setFamilies([u"Poppins"])
        font2.setPointSize(9)
        font2.setBold(False)
        font2.setItalic(False)
        self.enter_email.setFont(font2)
        self.enter_email.setStyleSheet(u"background-color:transparent;\n"
"color:white;\n"
"")
        self.enter_email.setAlignment(Qt.AlignCenter)
        self.email_adress = QLabel(self.normal_widget)
        self.email_adress.setObjectName(u"email_adress")
        self.email_adress.setGeometry(QRect(275, 310, 141, 21))
        font3 = QFont()
        font3.setFamilies([u"Poppins"])
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setItalic(False)
        self.email_adress.setFont(font3)
        self.email_adress.setStyleSheet(u"background-color:transparent;\n"
"color:white;")
        self.example = QLineEdit(self.normal_widget)
        self.example.setObjectName(u"example")
        self.example.setGeometry(QRect(275, 340, 231, 20))
        font4 = QFont()
        font4.setFamilies([u"Poppins"])
        font4.setPointSize(8)
        font4.setBold(False)
        self.example.setFont(font4)
        self.example.setStyleSheet(u"background-color:white;\n"
"border-radius:5px;\n"
"")
        self.password_reset = QPushButton(self.normal_widget)
        self.password_reset.setObjectName(u"password_reset")
        self.password_reset.setGeometry(QRect(305, 380, 171, 30))
        font5 = QFont()
        font5.setFamilies([u"Poppins"])
        font5.setPointSize(9)
        font5.setBold(True)
        self.password_reset.setFont(font5)
        self.password_reset.setStyleSheet(u"background-color:#9290C3;\n"
"border-radius:5px;\n"
"color:white;\n"
"")
        self.back_login = QPushButton(self.normal_widget)
        self.back_login.setObjectName(u"back_login")
        self.back_login.setGeometry(QRect(315, 440, 151, 20))
        font6 = QFont()
        font6.setFamilies([u"Poppins"])
        font6.setPointSize(8)
        font6.setBold(True)
        self.back_login.setFont(font6)
        self.back_login.setStyleSheet(u"background-color:#9290C3;\n"
"border-radius:5px;\n"
"color:white;")
        icon1 = QIcon()
        icon1.addFile(u":/yeni\u00d6nek/img/external-link (1).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.back_login.setIcon(icon1)
        self.back_login.setIconSize(QSize(15, 15))
        en_main_widget.setCentralWidget(self.merkez_widget)

        self.retranslateUi(en_main_widget)

        QMetaObject.connectSlotsByName(en_main_widget)
    # setupUi

    def retranslateUi(self, en_main_widget):
        en_main_widget.setWindowTitle(QCoreApplication.translate("en_main_widget", u"MainWindow", None))
        self.logo.setText(QCoreApplication.translate("en_main_widget", u"Fi-Wallet", None))
        self.forget_widget.setText(QCoreApplication.translate("en_main_widget", u"Forget Password", None))
        self.enter_email.setText(QCoreApplication.translate("en_main_widget", u"Enter your email addres to get the\n"
"password reset link.", None))
        self.email_adress.setText(QCoreApplication.translate("en_main_widget", u"Email Adress:", None))
        self.example.setText("")
        self.example.setPlaceholderText(QCoreApplication.translate("en_main_widget", u"  example@email.com", None))
        self.password_reset.setText(QCoreApplication.translate("en_main_widget", u"Password Reset", None))
        self.back_login.setText(QCoreApplication.translate("en_main_widget", u"    Back to Login", None))
    # retranslateUi

