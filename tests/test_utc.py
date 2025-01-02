import sys
import os
from PyQt5.QtWidgets import QApplication, QDialog

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(project_root)

from src import sub_utc_localization as utc

if __name__ == '__main__':
    app = QApplication(sys.argv)
    utc_value = utc.show_dialog()
    if utc_value is not None:
        print(f"Returned UTC value: {utc_value}")
    else:
        print("Dialog was canceled or closed.")
    sys.exit(0)