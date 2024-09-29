import sys
from PyQt5.QtWidgets import QDialog, QLabel, QDoubleSpinBox, QVBoxLayout, QMessageBox

class UtcSetup(QDialog):
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

    def value_changed(self):
        self.current_utc = self.dspinbox.value()
        print(f'current value is {self.current_utc}')

    def get_value(self):
        return self.current_utc

    def closeEvent(self, event):
        self.current_utc = self.dspinbox.value()
        if self.current_utc < 0:
            modify_check = QMessageBox.question(self, 'UTC Confirmation',
                                                f'Are you sure your standard time is UTC {self.current_utc:.2f} hour? ',
                                                QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        else:
            modify_check = QMessageBox.question(self, 'UTC Confirmation',
                                                f'Are you sure your standard time is UTC +{self.current_utc:.2f} hour? ',
                                                QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            
        if modify_check == QMessageBox.Yes:
            self.accept()
        else:
            event.ignore()


def show_dialog():
    dialog = UtcSetup()
    
    if dialog.exec_() == QDialog.Accepted:
        return dialog.current_utc
    else:
        return None

