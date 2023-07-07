from pykiwoom.kiwoom import Kiwoom


def find_stock_code_by_name(stock_name):
    kiwoom = Kiwoom()
    kiwoom.CommConnect()
    code_list = kiwoom.GetCodeListByMarket("0")  # 모든 종목 코드를 리스트로 반환

    for code in code_list:
        name = kiwoom.GetMasterCodeName(code)
        if stock_name == name:
            return code

    return None  # 종목 이름에 해당하는 종목 코드가 없을 경우 None 반환


# 사용 예시
stock_code = find_stock_code_by_name("삼성전자")
print(stock_code)  # 종목 이름 '삼성전자'에 해당하는 종목 코드 출력
