import dataModel as dm

#ptqt
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QAxContainer import *
from PyQt5.QtGui import *

form_class = uic.loadUiType("main_windows.ui")[0]

class ViewController(QMainWindow, form_class):
    def __init__(self, m_model):
        super().__init__()
        self.setUI()
        self.myModel = m_model
        print("뷰 컨트롤러 입니다.")

    def setUI(self):
        self.setupUi(self)