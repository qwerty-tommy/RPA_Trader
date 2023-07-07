import sys
from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *
from PyQt5.QtCore import *
import pythoncom

# [CommRqData() 함수]

# CommRqData(
# BSTR sRQName,    // 사용자 구분명 (임의로 지정, 한글지원)
# BSTR sTrCode,    // 조회하려는 TR이름
# long nPrevNext,  // 연속조회여부
# BSTR sScreenNo  // 화면번호 (4자리 숫자 임의로 지정)
# )

# 조회요청 함수입니다.
# 리턴값 0이면 조회요청 정상 나머지는 에러

# [GetCommData() 함수]

# GetCommData(
# BSTR strTrCode,   // TR 이름
# BSTR strRecordName,   // 레코드이름
# long nIndex,      // nIndex번째
# BSTR strItemName) // TR에서 얻어오려는 출력항목이름

# OnReceiveTRData()이벤트가 발생될때 수신한 데이터를 얻어오는 함수입니다.
# 이 함수는 OnReceiveTRData()이벤트가 발생될때 그 안에서 사용해야 합니다.


class Kiwoom:
    def __init__(self):
        self.login = False
        self.ocx = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.ocx.OnEventConnect.connect(self.OnEventConnect)
        self.ocx.OnReceiveTrData.connect(self.OnReceiveTrData)

    def CommConnect(self):
        self.ocx.dynamicCall("CommConnect()")
        while not self.login:
            pythoncom.PumpWaitingMessages()

    def OnReceiveTrData(self, screen, rqname, trcode, record, next):
        print(screen, rqname, trcode, record, next)
        per = self.GetCommData(trcode, rqname, 0, "PER")
        pbr = self.GetCommData(trcode, rqname, 0, "PBR")
        print("per : " + per, "pbr : " + pbr)

    def GetMasterCodeName(self, code):
        name = self.ocx.dynamicCall("GetMasterCodeName(QString)", code)
        return name

    def OnEventConnect(self, err_code):
        self.login = True

    def SetInputValue(self, id, value):
        self.ocx.dynamicCall("SetInputValue(QString, QString)", id, value)

    def CommRqData(self, rqname, trcode, next, screen):
        self.ocx.dynamicCall(
            "CommRqData(QString, QString, int, QString)", rqname, trcode, next, screen
        )

    def GetCommData(self, trcode, rqname, index, item):
        data = self.ocx.dynamicCall(
            "GetCommData(QString, QString, int, QString)", trcode, rqname, index, item
        )
        return data.strip()


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.kiwoom = Kiwoom()
        self.kiwoom.CommConnect()

        # tr request
        self.kiwoom.SetInputValue("종목코드", "005930")
        self.kiwoom.CommRqData("opt10001", "opt10001", 0, "0101")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()
