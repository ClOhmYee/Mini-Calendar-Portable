import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QCalendarWidget
from PyQt5.QtCore import Qt

# main calendar window
class CalendarApp(QMainWindow):
    def __init__(self):
        # value of window size
        WIDTH, HEIGHT = 400, 300

        # setting default position
        screen = QApplication.primaryScreen()
        resolution = screen.availableGeometry()
        spawn_x, spawn_y = resolution.width() - WIDTH, resolution.height() - HEIGHT # appears in bottom right
        
        super().__init__()
        self.setWindowTitle("Mini Calendar with Google Calendar")
        self.setGeometry(spawn_x, spawn_y, WIDTH, HEIGHT)

        self.calendar = QCalendarWidget(self)
        self.calendar.setVerticalHeaderFormat(0)    # exclude extra column
        self.calendar.setGridVisible(True)
        self.calendar.clicked.connect(self.show_schedule)

        layout = QVBoxLayout()
        layout.addWidget(self.calendar)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def show_schedule(self, date):  # function that triggers when the date is pressed
        # need a pop-up that displays the schedule for the day when clicked
        print(f"You clicked {date.toString()}") # remove as needed



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = CalendarApp()
    main_window.show()
    sys.exit(app.exec_())
