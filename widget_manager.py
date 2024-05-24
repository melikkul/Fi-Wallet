from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QGridLayout
from PySide6.QtCore import QSize , QRect
from PySide6.QtGui import QFont

class WidgetManager:
    def __init__(self, parent):
        self.parent = parent
        self.widget_counter = 0  # Başlangıç widget sayısı
        self.columns = 3  # Ekrana sığan widget sayısı

        # Ensure parent widget has a layout
        if not self.parent.layout():
            self.parent.setLayout(QVBoxLayout())

        # Create a grid layout to manage the widgets
        self.grid_layout = QGridLayout()
        self.parent.layout().addLayout(self.grid_layout)

    def create_total_balance_widget(self):
        widget = QWidget(self.parent)
        widget.setMinimumSize(QSize(500, 350))
        widget.setMaximumSize(QSize(500, 350))
        widget.setStyleSheet(u"background-color: #535C91;\nborder-radius: 25px;")
        
        # İçerik oluştur
        label = QLabel(widget)
        font = QFont()
        font.setFamilies([u"Poppins"])
        font.setPointSize(17)
        font.setBold(True)
        label.setFont(font)
        label.setStyleSheet(u"background-color:transparent;\nborder-radius:5px;\ncolor: white;")
        label.setText("Total Balance")

        # Create a layout for the widget content
        layout = QVBoxLayout(widget)
        layout.addWidget(label)
        
        return widget

    def add_widget(self):
        self.widget_counter += 1
        new_total_balance_widget = self.create_total_balance_widget()

        # Calculate row and column based on widget_counter
        row = (self.widget_counter - 1) // self.columns
        column = (self.widget_counter - 1) % self.columns

        # Add widget to the grid layout at calculated position
        self.grid_layout.addWidget(new_total_balance_widget, row, column)

        self.parent.adjustSize()
