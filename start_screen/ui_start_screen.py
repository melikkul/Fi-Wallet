# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'start_screen.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QSizePolicy, QWidget)
import start_screen_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(770, 590)
        MainWindow.setMinimumSize(QSize(770, 590))
        MainWindow.setMaximumSize(QSize(770, 590))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(770, 590))
        self.centralwidget.setMaximumSize(QSize(770, 590))
        self.FiWalletIntro = QFrame(self.centralwidget)
        self.FiWalletIntro.setObjectName(u"FiWalletIntro")
        self.FiWalletIntro.setGeometry(QRect(0, 0, 770, 590))
        self.FiWalletIntro.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:0.449, x2:1, y2:1, stop:0 rgba(83, 92, 145, 255), stop:1 rgba(27, 26, 85, 255));\n"
"border-radius: 75px;")
        self.FiWalletIntro.setFrameShape(QFrame.StyledPanel)
        self.FiWalletIntro.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.FiWalletIntro)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(220, 350, 311, 121))
        font = QFont()
        font.setFamilies([u"Poppins"])
        font.setPointSize(21)
        font.setBold(True)
        font.setStyleStrategy(QFont.PreferAntialias)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: transparent;\n"
"color: white;\n"
"\n"
"")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.FiWalletIntro)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(109, 50, 551, 451))
        self.label_2.setStyleSheet(u"background-color: transparent;\n"
"image: url(:/img/img/logo.drawio.svg);")
        self.label_2.setPixmap(QPixmap(u"../../Downloads/IMG_0466.png"))
        self.label_2.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Fi-Wallet", None))
        self.label_2.setText("")
    # retranslateUi

