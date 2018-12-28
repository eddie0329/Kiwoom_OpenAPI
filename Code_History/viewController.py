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
        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.login()

        # kiwoom Open API event Trigger
        self.kiwoom.OnEventConnect.connect(self.event_connect)

        # UI event Trigger
        self.searchItemButton.clicked.connect(self.searchItem)

    def login(self):
        self.kiwoom.dynamicCall("CommConnect()")

    def get_login_info(self):
        accCnt = self.kiwoom.dynamicCall("GetLoginInfo(QString)", "ACCOUNT_CNT")
        accList = self.kiwoom.dynamicCall("GetLoginInfo(QString)", "ACCLIST")
        userId = self.kiwoom.dynamicCall("GetLoginInfo(QString)", "USER_ID")
        userName = self.kiwoom.dynamicCall("GetLoginInfo(QString)", "USER_NAME")
        keyBSEC = self.kiwoom.dynamicCall("GetLoginInfo(QString)", "KEY_BSECGB")
        firew = self.kiwoom.dynamicCall("GetLoginInfo(QString)", "FRIEW_SECGB")
        serverGubun = self.kiwoom.dynamicCall("GetLoginInfo(QString)", "GetServerGubun")

        self.myModel.myLoginInfo = dm.DataModel.LoginInfo(accCnt, accList, userId, userName, keyBSEC, firew, serverGubun)

        #showing servergubun
        self.statusbar.showMessage(self.myModel.myLoginInfo.getServerGubun())

        #printing name
        #print("나의 이름:" + str(self.myModel.myLoginInfo.userName))


    def event_connect(self, nErrCode):
        if nErrCode == 0:
            print("로그인 성공")
            #self.statusbar.showMessage("로그인 성공")
            self.get_login_info()
            self.getItemList()

        elif nErrCode == 100:
            print("사용자 정보교환 실패")

        elif nErrCode == 101:
            print("서버접속 실패")

        elif nErrCode == 102:
            print("버전처리 실패")

    def setUI(self):
        self.setupUi(self)

    #종목 리스트 요청
    def getItemList(self):
        marketList = ["0", "10"]
        for market in marketList:
            codeList = self.kiwoom.dynamicCall("GetCodeListByMarket(QString)", market).split(";")
            for code in codeList:
                name = self.kiwoom.dynamicCall("GetMasterCodeName(QString", code)
                item = dm.DataModel.ItemInfo(code, name)
                self.myModel.itemList.append(item)
            #print(self.myModel.itemList[0].itemName)

    def searchItem(self):
        itemName = self.searchItemTextEdit.toPlainText()
        #print("입력 종목 명:" + itemName)
        for item in self.myModel.itemList:
            if item.itemName == itemName:
                print("종목 명: " + item.itemName)
                print("종목 코드: " + item.itemCode)
                break