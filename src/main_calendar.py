import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QCalendarWidget, QDialog, QLabel, QPushButton
from PyQt5.QtCore import Qt, QDate


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

    def show_schedule(self, date: QDate):  # function that triggers when the date is pressed
        # need a pop-up that displays the schedule for the day when clicked
        print(f"Now clicked : {date.toString('yyyy/MM/dd/dddd')}") # remove as needed
        date_info = DateMessageBox(date)
        date_info.exec_()


class DateMessageBox(QDialog):
    def __init__(self, date: QDate):
        super().__init__()
        info = 'put data here'        # stub
        self.setWindowTitle(f"{date.toString('yyyy/MM/dd')}")
        self.setFixedSize(300,200)
        
        layout = QVBoxLayout()
        label = QLabel(f"{info}")
        layout.addWidget(label)

        button = QPushButton("Done")
        button.clicked.connect(self.accept)
        layout.addWidget(button)
        
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = CalendarApp()
    main_window.show()
    sys.exit(app.exec_())
