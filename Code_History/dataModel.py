#pyqt
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QAxContainer import *
from PyQt5.QtGui import *

class DataModel:
    def __init__(self):
        self.myLoginInfo = None
        self.itemList = []

    class LoginInfo:
        #store login_info
        def __init__(self, accCnt, accList, userId, userName, keyBSEC, firew, serverGubun):
            self.accCnt = accCnt
            self.accList = accList
            self.userId = userId
            self.userName = userName
            self.keyBSEC = keyBSEC
            self.firew = firew
            self.serverGubun = serverGubun

        #server gubun
        def getServerGubun(self):
            if self.serverGubun == "1":
                return "모의투자"
            else:
                return "실서버"

    class ItemInfo:
        def __init__(self, itemCode, itemName):
            self.itemCode = itemCode
            self.itemName = itemName




