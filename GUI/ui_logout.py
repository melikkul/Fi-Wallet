# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'logout.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QDialog, QLabel, QPushButton, QWidget, QVBoxLayout, QHBoxLayout)

class Ui_Logout(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 400)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(700, 400))
        self.centralwidget.setMaximumSize(QSize(700, 400))
        self.centralwidget.setStyleSheet(u"")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 700, 400))
        self.widget.setMinimumSize(QSize(700, 400))
        self.widget.setMaximumSize(QSize(700, 400))
        font = QFont()
        font.setFamilies([u"Poppins"])
        font.setPointSize(10)
        self.widget.setFont(font)
        self.widget.setStyleSheet(u"background-color: #1B1A55;\n"
"border-radius: 35px;\n")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(220, 80, 261, 51))
        font1 = QFont()
        font1.setFamilies([u"Poppins"])
        font1.setPointSize(24)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color:white;\n"
"background-color:transparent;")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 150, 541, 51))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background-color:transparent;\n"
"color:white;")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(110, 270, 181, 41))
        font2 = QFont()
        font2.setFamilies([u"Poppins"])
        font2.setPointSize(12)
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"background-color:transparent;\n"
"color:white;\n"
"border:1px solid white;\n"
"border-radius: 15px")
        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(374, 270, 181, 41))
        self.pushButton_2.setFont(font2)
        self.pushButton_2.setStyleSheet(u"background-color:#535C91;\n"
"color:white;\n"
"border-radius: 15px;")


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"LOGOUT", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"After logging out of your account you will be still able to access \n"
"the Dashboard, Settings and Explorer.", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
    # retranslateUi

