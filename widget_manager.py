from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtCore import QRect, QSize
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QVBoxLayout  # Import QVBoxLayout

class WidgetManager:
    def __init__(self, parent):
        self.parent = parent
        self.widget_counter = 0  # Başlangıç widget sayısı

        # Ensure parent widget has a layout
        if not self.parent.layout():
            self.parent.setLayout(QVBoxLayout())  # Use QVBoxLayout from QtWidgets

    def create_total_balance_widget(self, x, y):
        widget = QWidget(self.parent)
        widget.setGeometry(QRect(x, y, 500, 350))
        widget.setMinimumSize(QSize(500, 350))
        widget.setMaximumSize(QSize(500, 350))
        widget.setStyleSheet(u"background-color: #535C91;\nborder-radius: 25px;")
        
        # İçerik oluştur
        label = QLabel(widget)
        label.setGeometry(QRect(70, 130, 291, 51))
        font = QFont()
        font.setFamilies([u"Poppins"])
        font.setPointSize(17)
        font.setBold(True)
        label.setFont(font)
        label.setStyleSheet(u"background-color:transparent;\nborder-radius:5px;\ncolor: white;")
        label.setText("Total Balance")

        return widget

    def add_widget(self):
        self.widget_counter += 1
        new_x = 40 + (self.widget_counter - 1) * 542
        new_total_balance_widget = self.create_total_balance_widget(new_x, 110)

        # Add widget to the layout of the parent widget
        self.parent.layout().addWidget(new_total_balance_widget)

        self.parent.adjustSize()
