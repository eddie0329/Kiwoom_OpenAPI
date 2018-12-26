# 해결방법:
# 문제는 파이선 버전을 3.5, 32비트로 깔아야한다는거였음.. 무슨 dependencies문제가
# 있는 모양인데 정식 개발문서에 씨발놈들이 안써놓음... 진짜 개발하다보면 이런 환경설정
# 문제 (보통 만든놈 책임) 가 한둘이 아님... 특히 한국 개발자들...
# 암튼 내가 제대로된 버전을 다운받아서 깃허브에 올려놓았으니까 그걸 컴터에 깔아.
# 그리고 파이참의 인터프리터를 새로 깐걸로 바꾸고, 거기다가 PyQt5를 설치하셈..
# 그럼 이제 self.kiwoom.dynamicCall("CommConnect()") 를 하는순간
# 키움증권 로긴창이 나오면 sam0329/비번 넣으면 그순간 파이선에서 로긴이 된거임...
# 그럼 그때부터 뭐 주문넣을수있고... 등등 다 할수있음 작동함.. 아 그리고 굳이 동영상안봐도
# https://wikidocs.net/4240 여기에 코드 예제 다 잘 정리되어 있더라...ㅎㅎㅎ
# 근데 이거 은근 재밌긴하다 ㅎㅎ 여기선 디비도 구축하던데.. 여기다가 머신러닝
# 적용하면 꿀잼이겠다.. 근데 내가 주식알못이라... 어떻게 적용해야하는지는 모르겠네 ㅠㅠ
# 암튼 그럼 즐개발하셈....키움증권개객끼....
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import  *
from PyQt5.QAxContainer import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Kiwoom Login
        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.kiwoom.dynamicCall("CommConnect()")

        # OpenAPI+ Event
        self.kiwoom.OnEventConnect.connect(self.event_connect)
        self.kiwoom.OnReceiveTrData.connect(self.receive_trdata)

        self.setWindowTitle("PyStock")
        self.setGeometry(300, 300, 300, 150)

        label = QLabel('종목코드: ', self)
        label.move(20, 20)

        self.code_edit = QLineEdit(self)
        self.code_edit.move(80, 20)
        self.code_edit.setText("039490")

        btn1 = QPushButton("조회", self)
        btn1.move(190, 20)
        btn1.clicked.connect(self.btn1_clicked)

        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(10, 60, 280, 80)
        self.text_edit.setEnabled(False)

    def event_connect(self, err_code):
        if err_code == 0:
            self.text_edit.append("로그인 성공")

    def btn1_clicked(self):
        code = self.code_edit.text()
        self.text_edit.append("종목코드: " + code)

        # SetInputValue
        self.kiwoom.dynamicCall("SetInputValue(QString, QString)", "종목코드", code)

        # CommRqData
        self.kiwoom.dynamicCall("CommRqData(QString, QString, int, QString)", "opt10001_req", "opt10001", 0, "0101")

    def receive_trdata(self, screen_no, rqname, trcode, recordname, prev_next, data_len, err_code, msg1, msg2):
        if rqname == "opt10001_req":
            name = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "종목명")
            volume = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "거래량")

            self.text_edit.append("종목명: " + name.strip())
            self.text_edit.append("거래량: " + volume.strip())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()



