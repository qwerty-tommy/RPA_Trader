from pykiwoom.kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)

stock_cnt = kiwoom.GetMasterListedStockCnt("005930")
print("삼성전자 상장주식수: ", stock_cnt)
# 현재 키움증권의 API에는 버그가 있어서 상장 주식수가 21억을 넘더라도 21억까지만 표현할 수 있음


감리구분 = kiwoom.GetMasterConstruction("005930")
print(감리구분)
# 감리구분은 '정상', '투자주의', '투자경고', '투자위험', '투자주의환기종목'의 값을 갖음

상장일 = kiwoom.GetMasterListedStockDate("005930")
print(상장일)
print(type(상장일))  # datetime.datetime 객체

전일가 = kiwoom.GetMasterLastPrice("005930")
print(int(전일가))
print(type(전일가))

종목상태 = kiwoom.GetMasterStockState("005930")
print(종목상태)
