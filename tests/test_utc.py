import sys
import os
from PyQt5.QtWidgets import QApplication
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'src'))

import sub_utc_localization as utc

if __name__ == '__main__':
    app = QApplication(sys.argv)
    test_window = utc.UtcSetup()
    test_window.show()
    sys.exit(app.exec_())
