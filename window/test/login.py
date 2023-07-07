import sys
from PyQt5.QAxContainer import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# "ACCOUNT_CNT" : 보유계좌 갯수를 반환합니다.
# "ACCLIST" 또는 "ACCNO" : 구분자 ';'로 연결된 보유계좌 목록을 반환합니다.
# "USER_ID" : 사용자 ID를 반환합니다.
# "USER_NAME" : 사용자 이름을 반환합니다.
# "GetServerGubun" : 접속서버 구분을 반환합니다.(1 : 모의투자, 나머지 : 실거래서버)
# "KEY_BSECGB" : 키보드 보안 해지여부를 반환합니다.(0 : 정상, 1 : 해지)
# "FIREW_SECGB" : 방화벽 설정여부를 반환합니다.(0 : 미설정, 1 : 설정, 2 : 해지)

info_target = [
    "ACCOUNT_CNT",
    "ACCLIST",
    "USER_ID",
    "USER_NAME",
    "GetServerGubun",
    "KEY_BSECGB",
    "FIREW_SECGB",
]


class btl_system:
    def __init__(self):
        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        print("연결되었습니다.")

        self.kiwoom.OnEventConnect.connect(self.OnEventConnect)

        self.kiwoom.dynamicCall("CommConnect()")
        self.login_event_loop = QEventLoop()
        self.login_event_loop.exec_()

        print("\n\n=======account info========")

        account_info = []

        for info in info_target:
            account_info.append(self.kiwoom.dynamicCall("GetLoginInfo(String)", info))

        print(account_info)

    def OnEventConnect(self, err_code):
        if err_code == 0:
            print("로그인에 성공하였습니다.")
        else:
            print("로그인에 실패하였습니다.")
        self.login_event_loop.exit()
        QTimer.singleShot(0, QApplication.instance().quit)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    btl = btl_system()
    app.exec_()


# pykiwoom으로 로그인
# from pykiwoom.kiwoom import *

# kiwoom = Kiwoom()
# kiwoom.CommConnect(block=True)
# print("블록킹 로그인 완료")
# account_num = kiwoom.GetLoginInfo("ACCOUNT_CNT")        # 전체 계좌수
# accounts = kiwoom.GetLoginInfo("ACCNO")                 # 전체 계좌 리스트
# user_id = kiwoom.GetLoginInfo("USER_ID")                # 사용자 ID
# user_name = kiwoom.GetLoginInfo("USER_NAME")            # 사용자명
# keyboard = kiwoom.GetLoginInfo("KEY_BSECGB")            # 키보드보안 해지여부
# firewall = kiwoom.GetLoginInfo("FIREW_SECGB")           # 방화벽 설정 여부

# print(account_num)
# print(accounts)
# print(user_id)
# print(user_name)
# print(keyboard)
# print(firewall)

# state = kiwoom.GetConnectState()
# if state == 0:
#     print("미연결")
# elif state == 1:
#     print("연결완료")
