import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QAxContainer import *

# 다음 절차는 키움증권 공식 개발 문서에 따랐음..밑에 링크를 보셈
# https://download.kiwoom.com/web/openapi/kiwoom_openapi_plus_devguide_ver_1.4.pdf

# 1. KoA Studio를 실행한뒤 파일 -> 오픈 API 접속을 누르셈.
# 2. 아이디 비번 넣고 접속 누르셈, 그럼 뭐 파일을 막 받고 할거임...시간이 꽤 걸림...
# 3. 업데이트 할때 KOA Studio 를 포함한 모든 창을 다 닫고 하셈 아님 에러남.
# 4. 정상적으로 KOA Studio에서 접속되는지 확인하셈.. 나는
#    여기서 접속은되는데 계속 윈도우가 죽어버림... 컴퓨터가 그다음에
#    이상해지고 부팅이 몇번씩 껐다켜야 되서 더이상하다간 컴터 날라갈듯..
#    저 OCX ActiveX 기술이 무진장 오래된거고 요즘엔 거의 안쓰는건데 대체
#    왜 저 답안나오는 MS기술을 지금도 쓰는지.. 그문젠거같은데 모르겠고
#    님 컴터에서는 되는지 보고 저 위에 공식 개발문서를 잘 읽어보셈
#    난 여기서 더 진행은 힘들고 요즘은 다 이런문제때문에 웹 API 로 하는데...
#    키움증권 병신인듯...지금 시대가 어느땐데...

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyStock")
        self.setGeometry(300, 300, 300, 150)

        self.kiwoom = QAxWidget()
        self.kiwoom.setControl("KHOPENAPI.KHOpenAPICtrl.1")
        self.kiwoom.dynamicCall("CommConnect()")

        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(10, 60, 280, 80)
        self.text_edit.setEnabled(False)

        self.kiwoom.OnEventConnect.connect(self.event_connect)

    def event_connect(self, err_code):
        if err_code == 0:
            self.text_edit.append("로그인 성공")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()