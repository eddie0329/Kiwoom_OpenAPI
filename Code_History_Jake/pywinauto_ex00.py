#관리자 권한으로 실행시켜야함
from pywinauto import application
from pywinauto import timings
import time
import os

app = application.Application()
app.start("C:/KiwoomHero4/bin/nkstarter.exe")

title = "영웅문4 Login"
dlg = timings.WaitUntilPasses(20, 0.5, lambda: app.window_(title=title))

#로그인 비밀번호
pass_ctrl = dlg.Edit2
pass_ctrl.SetFocus()
pass_ctrl.TypeKeys('qwer1357')

#인증서 비밀번호
#cert_ctrl = dlg.Edit3
#cert_ctrl.SetFocus()
#cert_ctrl.TypeKeys('xxxx')

#로그인 버튼 클릭
btn_ctrl = dlg.Button0
btn_ctrl.Click()

time.sleep(50)
os.system("taskkill /im nkstarter.exe")