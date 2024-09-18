import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QCalendarWidget, QDialog, QPushButton, QListWidget
from PyQt5.QtCore import Qt, QDate
import google_api as api


# main calendar window
class CalendarApp(QMainWindow):
    def __init__(self):
        # value of window size
        self.WIDTH, self.HEIGHT = 400, 300

        # setting default position
        screen = QApplication.primaryScreen()
        resolution = screen.availableGeometry()

        # appears in bottom right
        self.spawn_x, self.spawn_y = resolution.width() - self.WIDTH, resolution.height() - self.HEIGHT         
        super().__init__()
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

    def get_selected_events(self, date):
        selected_date = date.toPyDate()
        events_result = api.get_picked_events(selected_date)

        popup = DateMessageBox(date)

        if events_result == []:     # there is no event
            popup.event_list.addItem(f"Events on that date do not exist.")
        else:
            for event in events_result:
                start = event['start'].get('dateTime', event['start'].get('date'))
                popup.event_list.addItem(f"{start}: {event['summary']}")
        
        popup.setGeometry(self.spawn_x, self.spawn_y, self.WIDTH, self.HEIGHT)
        popup.exec_()


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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = CalendarApp()
    main_window.show()
    sys.exit(app.exec_())
    api.list_calendars()
