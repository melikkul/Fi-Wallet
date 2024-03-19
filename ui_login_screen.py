# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_screen.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)
import login_screen_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(780, 590)
        MainWindow.setMinimumSize(QSize(780, 590))
        MainWindow.setMaximumSize(QSize(780, 590))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 781, 591))
        self.widget.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(83, 92, 145, 255), stop:1 rgba(27, 26, 85, 255));")
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(240, 40, 311, 161))
        font = QFont()
        font.setFamilies([u"Poppins"])
        font.setPointSize(20)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"background-color:transparent;\n"
"color:white;")
        icon = QIcon()
        icon.addFile(u":/img/img/logo.drawio.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(150, 150))
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(210, 200, 141, 31))
        font1 = QFont()
        font1.setFamilies([u"Poppins"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background-color:transparent;\n"
"color: white;")
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(210, 240, 381, 31))
        font2 = QFont()
        font2.setFamilies([u"Poppins"])
        font2.setBold(False)
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setStrikeOut(False)
        font2.setKerning(True)
        self.lineEdit.setFont(font2)
        self.lineEdit.setStyleSheet(u"background-color:white;\n"
"border-radius:5px;")
        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(210, 320, 381, 31))
        self.lineEdit_2.setFont(font2)
        self.lineEdit_2.setStyleSheet(u"background-color:white;\n"
"border-radius:5px;")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(210, 280, 141, 31))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"background-color:transparent;\n"
"color: white;")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(490, 290, 141, 31))
        font3 = QFont()
        font3.setFamilies([u"Poppins"])
        font3.setPointSize(8)
        font3.setBold(True)
        font3.setUnderline(False)
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"background-color:transparent;\n"
"color: white;")
        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(340, 410, 121, 31))
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(u"background-color:#9290C3;\n"
"border-radius:5px;\n"
"color: white;")
        icon1 = QIcon()
        icon1.addFile(u":/img/img/log-in.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(300, 470, 221, 31))
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setStyleSheet(u"background-color:#9290C3;\n"
"border-radius:5px;\n"
"color: white;")
        icon2 = QIcon()
        icon2.addFile(u":/img/img/arrow-right-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.checkBox = QCheckBox(self.widget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(560, 325, 21, 21))
        self.checkBox.setStyleSheet(u"QCheckBox{\n"
"    background-color:white;\n"
"    border-top-right-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    text-align: center;\n"
"}\n"
"QCheckBox::indicator{\n"
"\n"
"    width:21px;\n"
"    height:21px;\n"
"}\n"
"QCheckBox::indicator:checked{\n"
"    \n"
"    \n"
"	image: url(:/img/img/eye (1).svg);\n"
"}\n"
"QCheckBox::indicator:unchecked{\n"
"    \n"
"     \n"
"	image: url(:/img/img/eye-off.svg);\n"
"}")
        self.checkBox_2 = QCheckBox(self.widget)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(210, 360, 151, 21))
        font4 = QFont()
        font4.setFamilies([u"Poppins"])
        font4.setBold(True)
        self.checkBox_2.setFont(font4)
        self.checkBox_2.setStyleSheet(u"QCheckBox{\n"
"	 color: white;\n"
"	background-color:transparent;\n"
"}\n"
"QCheckBox::indicator{\n"
"\n"
"    width:21px;\n"
"    height:21px;\n"
"}\n"
"QCheckBox::indicator:checked{\n"
"    \n"
"    image: url(:/img/img/check-circle (1).svg);\n"
"	\n"
"\n"
"}\n"
"QCheckBox::indicator:unchecked{\n"
"    \n"
"     \n"
"		image: url(:/img/img/circle.svg);\n"
"\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Fi-Wallet", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Email Address: ", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"example@email.com", None))
        self.lineEdit_2.setPlaceholderText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Forgot password?", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"  Login", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"    Create an account", None))
        self.checkBox.setText("")
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Keep me signed in  ", None))
    # retranslateUi

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())