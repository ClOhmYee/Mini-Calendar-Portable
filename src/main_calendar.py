import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QCalendarWidget,
    QDialog, QPushButton, QListWidget, QAction, QMessageBox
)
from PyQt5.QtGui import QTextCharFormat, QBrush, QColor
from PyQt5.QtCore import Qt, QDate
import google_api as api
import sub_utc_localization as utc

# main calendar window
class CalendarApp(QMainWindow):
    def __init__(self):
        self.WIDTH, self.HEIGHT = 400, 300
        self.local_utc = None
        super().__init__()
        self.init_UI()

    def init_UI(self):
        # setting default position
        screen = QApplication.primaryScreen()
        resolution = screen.availableGeometry()

        # appears in bottom right
        self.spawn_x, self.spawn_y = resolution.width() - self.WIDTH, resolution.height() - self.HEIGHT
        self.setWindowTitle("Mini Calendar with Google Calendar")
        self.setGeometry(self.spawn_x, self.spawn_y, self.WIDTH, self.HEIGHT)

        self.calendar = QCalendarWidget(self)
        self.calendar.setVerticalHeaderFormat(0)    # exclude extra column
        self.calendar.setGridVisible(True)
        self.calendar.clicked.connect(self.get_selected_events)

        layout = QVBoxLayout()
        layout.addWidget(self.calendar)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        menubar = self.menuBar()
        setting_menu = menubar.addMenu("Setting")
        utc_action = QAction("Edit UTC", self)
        utc_action.triggered.connect(self.get_utc_value)
        setting_menu.addAction(utc_action)

    def showEvent(self, event):
        if self.local_utc is None:
            self.get_utc_value()

    def get_selected_events(self, date):
        selected_date = date.toPyDate()
        text_format = QTextCharFormat()
        text_format.setBackground(QBrush(QColor("lightblue")))
        events_result = api.get_picked_events(selected_date, self.local_utc)

        popup = DateMessageBox(date)

        if events_result == []:     # there is no event
            popup.event_list.addItem(f"Events on that date do not exist.")
        else:
            self.calendar.setDateTextFormat(date, text_format)
            for event in events_result:
                start = event['start'].get('dateTime', event['start'].get('date'))
                popup.event_list.addItem(f"{start}: {event['summary']}")
        
        popup.setGeometry(self.spawn_x, self.spawn_y, self.WIDTH, self.HEIGHT)
        popup.exec_()
        
    def get_utc_value(self):
        while True:
            i_utc_value = utc.show_dialog()
            if i_utc_value is not None:
                sign = '+' if i_utc_value >= 0 else '-'
                absolute_value = abs(i_utc_value)
                hours = int(absolute_value)
                minutes = int((absolute_value - hours) * 60)
                self.local_utc = f"{sign}{hours:02}:{minutes:02}"
                break
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Warning")
                msg.setText("UTC set failed. Try it again.")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
            

# pop-up that displays the schedule on click event
class DateMessageBox(QDialog):
    def __init__(self, date: QDate):
        super().__init__()
        layout = QVBoxLayout()
        self.setWindowTitle(f"{date.toString('yyyy/MM/dd')}")
        self.setFixedSize(300,200)

        self.event_list = QListWidget(self)
        layout.addWidget(self.event_list)

        button = QPushButton("Done")
        button.clicked.connect(self.accept)
        layout.addWidget(button)
        
        self.setLayout(layout)


# run directly to execute
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = CalendarApp()
    main_window.show()
    sys.exit(app.exec_())
