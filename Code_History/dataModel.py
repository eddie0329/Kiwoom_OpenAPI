from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QAxContainer import *
from PyQt5.QtGui import *

class DataModel:
    def __init__(self):
        print("데이터 모델입니다.")
        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.login()

        #kiwoom Open API event Trigger
        self.kiwoom.OnEventConnect.connect(self.event_connect)

    def login(self):
        self.kiwoom.dynamicCall("CommConnect()")

    def event_connect(self, nErrCode):
        if nErrCode == 0:
            print("로그인 성공")
        elif nErrCode == 100:
            print("사용자 정보교환 실패")
        elif nErrCode == 101:
            print("서버접속 실패")
        elif nErrCode == 102:
            print("버전처리 실패")
