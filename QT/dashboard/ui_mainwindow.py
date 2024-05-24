# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QSizePolicy, QSpacerItem, QToolButton, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 350)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.total_balance_widget_2 = QWidget(self.centralwidget)
        self.total_balance_widget_2.setObjectName(u"total_balance_widget_2")
        self.total_balance_widget_2.setGeometry(QRect(0, 0, 500, 350))
        self.total_balance_widget_2.setMinimumSize(QSize(500, 350))
        self.total_balance_widget_2.setMaximumSize(QSize(500, 350))
        self.total_balance_widget_2.setStyleSheet(u"background-color: #535C91;\n"
"border-radius: 25px;")
        self.label = QLabel(self.total_balance_widget_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 130, 291, 51))
        font = QFont()
        font.setFamilies([u"Poppins"])
        font.setPointSize(17)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color:transparent;\n"
"\n"
"border-radius:5px;\n"
"color: white;")
        self.label_3 = QLabel(self.total_balance_widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 110, 151, 31))
        font1 = QFont()
        font1.setFamilies([u"Poppins"])
        font1.setPointSize(10)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"background-color:transparent;\n"
"\n"
"border-radius:5px;\n"
"color:rgba(255,255,255,0.4);")
        self.label_4 = QLabel(self.total_balance_widget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(70, 210, 291, 41))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"background-color:transparent;\n"
"\n"
"border-radius:5px;\n"
"color: white;")
        self.label_5 = QLabel(self.total_balance_widget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(60, 180, 151, 31))
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"background-color:transparent;\n"
"\n"
"border-radius:5px;\n"
"color:rgba(255,255,255,0.4);")
        self.label_7 = QLabel(self.total_balance_widget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 80, 470, 1))
        self.label_7.setMinimumSize(QSize(470, 1))
        self.label_7.setMaximumSize(QSize(470, 1))
        self.label_7.setStyleSheet(u"background-color :rgba(255,255,255,0.4);")
        self.layoutWidget = QWidget(self.total_balance_widget_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(40, 20, 416, 53))
        self.horizontalLayout_42 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setFamilies([u"Poppins"])
        font2.setPointSize(12)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"background-color:transparent;\n"
"\n"
"border-radius:5px;\n"
"color: white;")

        self.horizontalLayout_42.addWidget(self.label_2)

        self.horizontalSpacer_60 = QSpacerItem(228, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_42.addItem(self.horizontalSpacer_60)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(81, 51))
        self.label_6.setMaximumSize(QSize(81, 51))
        self.label_6.setStyleSheet(u"background-color:transparent;\n"
"image: url(:/img/img/MasterCard.png);")

        self.horizontalLayout_42.addWidget(self.label_6)

        self.layoutWidget_2 = QWidget(self.total_balance_widget_2)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(40, 270, 443, 53))
        self.horizontalLayout_43 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.toolButton_4 = QToolButton(self.layoutWidget_2)
        self.toolButton_4.setObjectName(u"toolButton_4")
        self.toolButton_4.setMinimumSize(QSize(100, 51))
        self.toolButton_4.setMaximumSize(QSize(100, 51))
        font3 = QFont()
        font3.setFamilies([u"Poppins"])
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setUnderline(False)
        font3.setStrikeOut(False)
        self.toolButton_4.setFont(font3)
        self.toolButton_4.setStyleSheet(u"background-color:transparent;\n"
"\n"
"border-radius:5px;\n"
"color: white;")

        self.horizontalLayout_43.addWidget(self.toolButton_4)

        self.horizontalSpacer_61 = QSpacerItem(148, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_43.addItem(self.horizontalSpacer_61)

        self.toolButton_3 = QToolButton(self.layoutWidget_2)
        self.toolButton_3.setObjectName(u"toolButton_3")
        self.toolButton_3.setMinimumSize(QSize(181, 51))
        self.toolButton_3.setMaximumSize(QSize(181, 51))
        self.toolButton_3.setFont(font3)
        self.toolButton_3.setStyleSheet(u"background-color:#1B1A55;\n"
"border-radius:5px;\n"
"color: white;")

        self.horizontalLayout_43.addWidget(self.toolButton_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"3388 4556 8860 8*** ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Account Number", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"$250000", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Total Amount", None))
        self.label_7.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Credit Card", None))
        self.label_6.setText("")
        self.toolButton_4.setText(QCoreApplication.translate("MainWindow", u"REMOVE", None))
        self.toolButton_3.setText(QCoreApplication.translate("MainWindow", u"DETAILS           >", None))
    # retranslateUi

