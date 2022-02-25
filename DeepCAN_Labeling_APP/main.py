import sys
from PySide2.QtWidgets import *
from DeepCAN_Labeling_APP.app_functions.main_functions import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow(app)
    sys.exit(app.exec_())
