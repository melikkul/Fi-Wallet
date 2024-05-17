# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)
import register_rc

class Ui_Register(object):
                 
    def toggle_password_visibility(self):
        if self.sifre.echoMode() == QLineEdit.Password:
            self.sifre.setEchoMode(QLineEdit.Normal)
        else:
            self.sifre.setEchoMode(QLineEdit.Password)

    def setupUi(self, anasayfa):
        if not anasayfa.objectName():
            anasayfa.setObjectName(u"anasayfa")
        anasayfa.resize(780, 590)
        anasayfa.setMinimumSize(QSize(780, 590))
        anasayfa.setMaximumSize(QSize(780, 590))
        self.sayfa2 = QWidget(anasayfa)
        self.sayfa2.setObjectName(u"sayfa2")
        self.sayfa3 = QWidget(self.sayfa2)
        self.sayfa3.setObjectName(u"sayfa3")
        self.sayfa3.setGeometry(QRect(0, 0, 780, 590))
        self.sayfa3.setMinimumSize(QSize(780, 590))
        self.sayfa3.setMaximumSize(QSize(780, 590))
        font = QFont()
        font.setPointSize(25)
        self.sayfa3.setFont(font)
        self.sayfa3.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(83, 92, 145, 255), stop:1 rgba(27, 26, 85, 255));\n"
                                  "border-radius: 75px;")
        self.pushButton = QPushButton(self.sayfa3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(260, 0, 291, 141))
        font1 = QFont()
        font1.setFamilies([u"Poppins"])
        font1.setPointSize(25)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"background-color:transparent;\n"
"color:rgb(255, 255, 255);")
        icon = QIcon()
        icon.addFile(u":/img/img/icon.drawio.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(150, 150))
        self.aciklama = QLabel(self.sayfa3)
        self.aciklama.setObjectName(u"aciklama")
        self.aciklama.setGeometry(QRect(190, 150, 691, 111))
        font2 = QFont()
        font2.setFamilies([u"Poppins"])
        font2.setPointSize(12)
        self.aciklama.setFont(font2)
        self.aciklama.setStyleSheet(u"background-color:transparent;\n"
"color:white;")
        self.registerbaslik = QLabel(self.sayfa3)
        self.registerbaslik.setObjectName(u"registerbaslik")
        self.registerbaslik.setGeometry(QRect(350, 120, 111, 51))
        font3 = QFont()
        font3.setFamilies([u"Poppins"])
        font3.setPointSize(20)
        font3.setKerning(True)
        self.registerbaslik.setFont(font3)
        self.registerbaslik.setStyleSheet(u"background-color:transparent;\n"
"color:white;")
        self.firstname = QLabel(self.sayfa3)
        self.firstname.setObjectName(u"firstname")
        self.firstname.setGeometry(QRect(250, 260, 101, 31))
        font4 = QFont()
        font4.setPointSize(9)
        self.firstname.setFont(font4)
        self.firstname.setStyleSheet(u"background-color:transparent;\n"
"color:white;")
        self.lastname = QLabel(self.sayfa3)
        self.lastname.setObjectName(u"lastname")
        self.lastname.setGeometry(QRect(450, 260, 91, 31))
        self.lastname.setFont(font4)
        self.lastname.setStyleSheet(u"background-color:transparent;\n"
"color:white;")
        self.email = QLabel(self.sayfa3)
        self.email.setObjectName(u"email")
        self.email.setGeometry(QRect(250, 310, 101, 31))
        self.email.setFont(font4)
        self.email.setStyleSheet(u"background-color:transparent;\n"
"color:white;")
        self.password = QLabel(self.sayfa3)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(250, 360, 101, 31))
        self.password.setFont(font4)
        self.password.setStyleSheet(u"background-color:transparent;\n"
"color:white;")
        self.isim = QLineEdit(self.sayfa3)
        self.isim.setObjectName(u"isim")
        self.isim.setGeometry(QRect(250, 290, 113, 25))
        font5 = QFont()
        font5.setFamilies([u"Poppins"])
        font5.setPointSize(8)
        self.isim.setFont(font5)
        self.isim.setStyleSheet(u"background-color:white;\n"
"border-radius:5px;")
        self.soyadi = QLineEdit(self.sayfa3)
        self.soyadi.setObjectName(u"soyadi")
        self.soyadi.setGeometry(QRect(450, 290, 111, 25))
        self.soyadi.setFont(font5)
        self.soyadi.setStyleSheet(u"background-color:white;\n"
"border-radius:5px;")
        self.mail = QLineEdit(self.sayfa3)
        self.mail.setObjectName(u"mail")
        self.mail.setGeometry(QRect(250, 340, 311, 25))
        self.mail.setFont(font5)
        self.mail.setStyleSheet(u"background-color:white;\n"
"border-radius:5px;")
        self.onayla = QCheckBox(self.sayfa3)
        self.onayla.setObjectName(u"onayla")
        self.onayla.setGeometry(QRect(260, 420, 351, 20))
        self.onayla.setFont(font5)
        self.onayla.setStyleSheet(u"background-color:transparent;\n"
"color:white;")
        self.sifre = QLineEdit(self.sayfa3)
        self.sifre.setObjectName(u"sifre")
        self.sifre.setGeometry(QRect(250, 390, 311, 25))
        self.sifre.setFont(font5)
        self.sifre.setStyleSheet(u"background-color:white;\n"
"border-radius:5px;")
        self.sifre.setEchoMode(QLineEdit.Password)
        self.kayitbuton = QPushButton(self.sayfa3)
        self.kayitbuton.setObjectName(u"kayitbuton")
        self.kayitbuton.setGeometry(QRect(340, 460, 111, 41))
        font6 = QFont()
        font6.setFamilies([u"Poppins"])
        font6.setPointSize(15)
        font6.setUnderline(False)
        self.kayitbuton.setFont(font6)
        self.kayitbuton.setStyleSheet(u"background-color:#9290C3;\n"
"color:white;\n"
"border-radius:5px;")
        self.sifregoster = QCheckBox(self.sayfa3)
        self.sifregoster.setObjectName(u"sifregoster")
        self.sifregoster.setGeometry(QRect(530, 390, 21, 20))
        self.sifregoster.setStyleSheet(u"QCheckBox{\n"
"    background-color:white;\n"
"    border-top-right-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    text-align: center;\n"
"}\n"
"QCheckBox::indicator{\n"
"\n"
"    width:18px;\n"
"    height:18px;\n"
"}\n"
"QCheckBox::indicator:checked{\n"
"    \n"
"	image: url(:/img/img/eye-off (1).svg);\n"
" \n"
"}\n"
"QCheckBox::indicator:unchecked{\n"
"	image: url(:/img/img/eye.svg);\n"
"    \n"
"\n"
"}")
        anasayfa.setCentralWidget(self.sayfa2)

        
        self.sifregoster.clicked.connect(self.toggle_password_visibility)

        self.retranslateUi(anasayfa)

        QMetaObject.connectSlotsByName(anasayfa)
    # setupUi

    def retranslateUi(self, anasayfa):
        anasayfa.setWindowTitle(QCoreApplication.translate("anasayfa", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("anasayfa", u"Fi-Wallet", None))
        self.aciklama.setText(QCoreApplication.translate("anasayfa", u"To register,you must fill in the boxes below completely.", None))
        self.registerbaslik.setText(QCoreApplication.translate("anasayfa", u"Register", None))
        self.firstname.setText(QCoreApplication.translate("anasayfa", u"First Name", None))
        self.lastname.setText(QCoreApplication.translate("anasayfa", u"Last Name", None))
        self.email.setText(QCoreApplication.translate("anasayfa", u"Email", None))
        self.password.setText(QCoreApplication.translate("anasayfa", u"Password", None))
#if QT_CONFIG(accessibility)
        self.isim.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.isim.setPlaceholderText(QCoreApplication.translate("anasayfa", u"John", None))
#if QT_CONFIG(accessibility)
        self.soyadi.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.soyadi.setPlaceholderText(QCoreApplication.translate("anasayfa", u"Stone", None))
#if QT_CONFIG(accessibility)
        self.mail.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.mail.setText("")
        self.mail.setPlaceholderText(QCoreApplication.translate("anasayfa", u"johnstone@gmail.com", None))
        self.onayla.setText(QCoreApplication.translate("anasayfa", u"I agree to all the Term, Privacy Policy and Fees.", None))
#if QT_CONFIG(accessibility)
        self.sifre.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.sifre.setText("")
        self.sifre.setPlaceholderText(QCoreApplication.translate("anasayfa", u"*************", None))
        self.kayitbuton.setText(QCoreApplication.translate("anasayfa", u"Register", None))
        self.sifregoster.setText("")
    # retranslateUi

