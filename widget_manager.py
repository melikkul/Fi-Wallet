from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QGridLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QToolButton
from PySide6.QtCore import QSize , QRect, QCoreApplication
from PySide6.QtGui import QFont

class WidgetManager:
    def __init__(self, parent):
        self.parent = parent
        self.widget_counter = 0  # Başlangıç widget sayısı
        self.columns = 3  # Ekrana sığan widget sayısı
        self.rows = 2
        self.column_spacing = 42  # Sütunlar arası boşluk
        self.row_spacing = 50  # Satırlar arası boşluk


        # Ensure parent widget has a layout
        if not self.parent.layout():
            self.parent.setLayout(QVBoxLayout())

        # Create a grid layout to manage the widgets
        self.grid_layout = QGridLayout()
        self.parent.layout().addLayout(self.grid_layout)

        self.column_width = (self.parent.width() - (self.columns + 1) * self.column_spacing) // self.columns

    def create_total_balance_widget(self):
        widget = QWidget(self.parent)
        widget.setObjectName(u"total_balance_widget_2")
        # Widgetin başlangıç konumu
        x = 40
        y = 110

        # Yeni widgetin yatay ve dikey konumunu hesapla
        row = self.widget_counter // self.columns
        column = self.widget_counter % self.columns
        new_x = x + column * (self.column_width + self.column_spacing)
        new_y = y + row * (350 + self.row_spacing)

        widget.setGeometry(QRect(new_x, new_y, self.column_width, 350))
        widget.setMinimumSize(QSize(500, 350))
        widget.setMaximumSize(QSize(500, 350))
        widget.setStyleSheet(u"background-color: #535C91;\n"
"border-radius: 25px;")
        self.label = QLabel(widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 130, 291, 51))
        self.label.setText(QCoreApplication.translate("MainWindow", u"3388 4556 8860 8*** ", None))
        font = QFont()
        font.setFamilies([u"Poppins"])
        font.setPointSize(17)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color:transparent;\n"
"\n"
"border-radius:5px;\n"
"color: white;")
        self.label_3 = QLabel(widget)
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
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Account Number", None))
        self.label_4 = QLabel(widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(70, 210, 291, 41))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"background-color:transparent;\n"
"\n"
"border-radius:5px;\n"
"color: white;")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"$250000", None))
        self.label_5 = QLabel(widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(60, 180, 151, 31))
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"background-color:transparent;\n"
"\n"
"border-radius:5px;\n"
"color:rgba(255,255,255,0.4);")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Total Amount", None))
        self.label_7 = QLabel(widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 80, 470, 1))
        self.label_7.setMinimumSize(QSize(470, 1))
        self.label_7.setMaximumSize(QSize(470, 1))
        self.label_7.setStyleSheet(u"background-color :rgba(255,255,255,0.4);")
        self.layoutWidget = QWidget(widget)
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
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Credit Card", None))
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

        self.layoutWidget_2 = QWidget(widget)
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
        self.toolButton_4.setText(QCoreApplication.translate("MainWindow", u"REMOVE", None))

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
        self.toolButton_3.setText(QCoreApplication.translate("MainWindow", u"DETAILS           >", None))

        self.horizontalLayout_43.addWidget(self.toolButton_3)
        
        return widget

    def add_widget(self):
        if self.widget_counter < self.columns * self.rows:
                new_total_balance_widget = self.create_total_balance_widget()
                # Add widget to the grid layout
                self.grid_layout.addWidget(new_total_balance_widget, self.widget_counter // self.columns, self.widget_counter % self.columns)
                self.widget_counter += 1
                # Set both column and row spacing
                self.grid_layout.setSpacing(self.column_spacing)