from GUI.ui_dashboard import Ui_MainWindow
from PySide6.QtGui import Qt, QIcon, QBrush, QColor, QPainterPath, QFont
from PySide6.QtWidgets import QMainWindow
from PySide6 import QtCharts

        
class RoundedBar(QtCharts.QBarSet):
    def __init__(self, label):
        super().__init__(label)

    def paint(self, painter, option, widget):
        for i in range(len(self)):
            rect = self.barRect(i)
            path = QPainterPath()
            path.addRoundedRect(rect, 10, 10)  # Radius of 10
            #painter.fillPath(path, self.brush())


class ChartyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.minimize_slider_menu_widget.setHidden(True)
        self.bar_graph()


        self.dashboard_minimize_button.clicked.connect(self.switch_to_dashboard_page)
        self.dashboard_button.clicked.connect(self.switch_to_dashboard_page)

        self.analist_minimize_button.clicked.connect(self.switch_to_analist_page)
        self.analist_button.clicked.connect(self.switch_to_analist_page)

        self.performance_minimize_button.clicked.connect(self.switch_to_performance_page)
        self.performance_button.clicked.connect(self.switch_to_performance_page)

        self.bills_minimize_button.clicked.connect(self.switch_to_bills_page)
        self.bills_button.clicked.connect(self.switch_to_bills_page)

        self.wallet_minimize_button.clicked.connect(self.switch_to_wallet_page)
        self.wallet_button.clicked.connect(self.switch_to_wallet_page)

        self.goal_minimize_button.clicked.connect(self.switch_to_goal_page)
        self.goal_button.clicked.connect(self.switch_to_goal_page)

        self.settings_minimize_button.clicked.connect(self.switch_to_settings_page)
        self.settings_button.clicked.connect(self.switch_to_settings_page)

        self.profile_minimize_button.clicked.connect(self.switch_to_profile_page)
        self.profile_button.clicked.connect(self.switch_to_profile_page)

    def switch_to_dashboard_page(self):
        self.main_screen_stacked_widget.setCurrentWidget(self.dashboard_widget)

    def switch_to_analist_page(self):
        self.main_screen_stacked_widget.setCurrentWidget(self.analist_page)

    def switch_to_performance_page(self):
        self.main_screen_stacked_widget.setCurrentWidget(self.performance_page)

    def switch_to_bills_page(self):
        self.main_screen_stacked_widget.setCurrentWidget(self.bills_page)

    def switch_to_wallet_page(self):
        self.main_screen_stacked_widget.setCurrentWidget(self.wallet_page)

    def switch_to_goal_page(self):
        self.main_screen_stacked_widget.setCurrentWidget(self.goal_page)

    def switch_to_settings_page(self):
        self.main_screen_stacked_widget.setCurrentWidget(self.settings_page)

    def switch_to_profile_page(self):
        self.main_screen_stacked_widget.setCurrentWidget(self.profile_page)


    def bar_graph(self):
        series = QtCharts.QBarSeries()
        series.setName("Weekly Comparisons")

        weeks = ["17 Sun", "18 Mon", "19 Tue", "20 Wed", "21 Thu", "22 Fri", "23 Sat"]
        this_week = [18, 120, 35, 25, 3, 45, 40]
        last_week = [12, 24, 31, 28, 5, 40, 24]

        bar_set_this_week = RoundedBar("This Week")
        bar_set_last_week = RoundedBar("Last Week")

        for i in range(len(weeks)):
            bar_set_last_week.append(last_week[i])
            bar_set_this_week.append(this_week[i])

        # Set bar colors using color codes
        bar_set_this_week.setBrush(QBrush(QColor("#ffffff")))  # Beyaz renk
        bar_set_last_week.setBrush(QBrush(QColor("#1B1A55")))  # Koyu mavi renk

        series.append(bar_set_this_week)
        series.append(bar_set_last_week)

        chart = QtCharts.QChart()
        chart.addSeries(series)
        chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

        axis_x = QtCharts.QBarCategoryAxis()
        axis_x.append(weeks)
        axis_x.setLabelsBrush(QBrush(QColor("#FFFFFF")))
        axis_x.setGridLineVisible(False)  # X eksenindeki çizgileri gizle
        chart.addAxis(axis_x, Qt.AlignBottom)
        series.attachAxis(axis_x)

        axis_y = QtCharts.QValueAxis()
        axis_y.setRange(0, max(max(this_week), max(last_week)) + 10)
        axis_y.setLabelsBrush(QBrush(QColor("#FFFFFF")))
        chart.addAxis(axis_y, Qt.AlignLeft)
        series.attachAxis(axis_y)

        # Set background color to light gray
        chart.setBackgroundBrush(QBrush(QColor("#535C91")))  # Açık gri renk

        # Remove title and legend
        chart.setTitle("")
        chart.legend().setVisible(False)

        self.barchart_view.setChart(chart)
