from pykiwoom.kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)

# 주식계좌
accounts = kiwoom.GetLoginInfo("ACCNO")

stock_account = accounts[0]

stock_account = stock_account

print(stock_account)

# 삼성전자, 10주, 시장가주문 매수
print(
    kiwoom.SendOrder(
        "주식매수",
        "1000",
        stock_account,
        1,
        "005930",
        10,
        0,
        "03",
        "",
    )
)
