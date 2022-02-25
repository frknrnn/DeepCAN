from DeepCAN_Labeling_APP.py_ui.ui_loadingPage import Ui_Dialog
from PySide2 import  QtCore
from PySide2.QtWidgets import *


class loadingPage(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.loading_ui = Ui_Dialog()
        self.loading_ui.setupUi(self)
        ## REMOVE TİTLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setModal(True)
        self.show()

    def close(self):
        self.hide()
