from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from pykiwoom.kiwoom import Kiwoom
from fastapi import BackgroundTasks


router = APIRouter(
    prefix="/transaction",
)

DEFAULT_WINDOW_NUM = "1000"


class TransactionRequest(BaseModel):
    account_number: str
    password: str
    stock_code: str
    quantity: int
    order_type: int  # 주문유형 1:신규매수, 2:신규매도 3:매수취소, 4:매도취소, 5:매수정정, 6:매도정정


async def get_kiwoom():
    kiwoom = Kiwoom()
    kiwoom.CommConnect(block=True)
    return kiwoom


# @router.post("/transaction")
# async def transaction(
#     response: TransactionRequest,
#     kiwoom: Kiwoom = Depends(get_kiwoom),
# ):
#     request = response
#     result = await kiwoom.SendOrder(
#         "buying",
#         DEFAULT_WINDOW_NUM,
#         request.account_number,
#         request.order_type,
#         request.stock_code,
#         request.quantity,
#         0,
#         "03",
#         "",
#     )

#     return {"result": True}


async def send_order_background(response: TransactionRequest, kiwoom: Kiwoom):
    request = response
    result = kiwoom.SendOrder(
        "buying",
        DEFAULT_WINDOW_NUM,
        request.account_number,
        request.order_type,
        request.stock_code,
        request.quantity,
        0,
        "03",
        "",
    )
    # 백그라운드 작업이 완료되면 결과를 처리하거나 저장할 수 있음


@router.post("/transaction")
def transaction(  # 일단은 DI의 형태로 백그라운드로 보내긴했는데 pyqt로 바꿔야함
    response: TransactionRequest,
    background_tasks: BackgroundTasks,
    kiwoom: Kiwoom = Depends(get_kiwoom),
):
    background_tasks.add_task(send_order_background, response, kiwoom)
    return {"result": True}


# @router.get("/get_Stock_Name")
# def get_Stock_Name(code: str, kiwoom: Kiwoom = Depends(get_kiwoom)):
#     name = kiwoom.GetMasterCodeName(
#         code,
#     )
#     if not name:
#         raise HTTPException(status_code=404, detail="Stock not found")

#     return {"stock_name": name}


@router.get("/get_Code")
def get_Code(target_name: str, kiwoom: Kiwoom = Depends(get_kiwoom)):
    code_list = kiwoom.GetCodeListByMarket("0")  # 모든 종목 코드를 리스트로 반환

    for code in code_list:
        name = kiwoom.GetMasterCodeName(code)
        if target_name == name:
            return {"code": code}

    raise HTTPException(
        status_code=404, detail="Stock not found"
    )  # 종목 이름에 해당하는 종목 코드가 없을 경우 404


@router.get("/test")
def test():
    return {"connection": "ok"}
