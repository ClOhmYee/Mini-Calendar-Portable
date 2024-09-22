import sys
from PyQt5.QtWidgets import QWidget, QLabel, QDoubleSpinBox, QVBoxLayout, QMessageBox

class UtcSetup(QWidget):
    def __init__(self):
        super().__init__()
        self.init_UI()

    def init_UI(self):
        self.lbl1 = QLabel('Enter the UTC time according to your location')
        self.dspinbox = QDoubleSpinBox()
        self.dspinbox.setRange(-12,14)
        self.dspinbox.setSingleStep(0.5)
        self.dspinbox.setPrefix('UTC ')
        self.dspinbox.setSuffix('h')
        self.dspinbox.setDecimals(2)

        self.dspinbox.valueChanged.connect(self.value_changed)

        layout = QVBoxLayout()
        layout.addWidget(self.lbl1)
        layout.addWidget(self.dspinbox)
        layout.addStretch()
        self.setLayout(layout)

        self.setWindowTitle('UTC Localization')
        self.show()

    def value_changed(self):
        current_utc = self.dspinbox.value()
        print(f'current value is {current_utc}')

    def closeEvent(self, event):
        current_utc = self.dspinbox.value()
        if current_utc < 0:
            modify_check = QMessageBox.question(self, 'UTC Confirmation',
                                                f'Are you sure your standard time is UTC {current_utc:.2f} hour? ',
                                                QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        else:
            modify_check = QMessageBox.question(self, 'UTC Confirmation',
                                                f'Are you sure your standard time is UTC +{current_utc:.2f} hour? ',
                                                QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            
        if modify_check == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


