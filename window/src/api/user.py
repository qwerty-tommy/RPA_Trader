from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from pykiwoom.kiwoom import Kiwoom

router = APIRouter(prefix="/user")


class UserRequest(BaseModel):
    account_number: str
    password: str


async def get_kiwoom():
    kiwoom = Kiwoom()
    kiwoom.CommConnect(block=True)
    return kiwoom


@router.post("/info")
def info(
    request: UserRequest,
    kiwoom: Kiwoom = Depends(get_kiwoom),
):
    kiwoom.GetLoginInfo("ACCOUNT_CNT")  # 로그인 후 사용 가능한 정보

    # 사용자 정보 조회
    account_count = kiwoom.GetLoginInfo("ACCOUNT_CNT")  # 보유계좌 갯수
    account_list = kiwoom.GetLoginInfo("ACCLIST")  # 보유계좌 목록
    user_id = kiwoom.GetLoginInfo("USER_ID")  # 사용자 ID
    user_name = kiwoom.GetLoginInfo("USER_NAME")  # 사용자 이름
    server_gubun = kiwoom.GetLoginInfo("GetServerGubun")  # 접속서버 구분

    # 모의투자 여부 판단
    is_demo_trading = True if server_gubun == "1" else False

    # 결과를 JSON 형식으로 반환
    result = {
        "account_count": account_count,
        "account_list": account_list.split(";") if account_list else [],
        "user_id": user_id,
        "user_name": user_name,
        "is_demo_trading": is_demo_trading,
    }

    return result
