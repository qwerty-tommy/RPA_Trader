from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, validator
import requests

router = APIRouter(
    prefix="/transaction",
)

WINDOW_SERVER = "http://localhost:8001"


class TransactionRequest(BaseModel):
    account_number: str
    password: str
    stock_name: str
    quantity: int

    # 모델 유효성 검사
    @validator("quantity")
    def validate_quantity(cls, value):
        if value <= 0:
            raise ValueError("Quantity must be greater than 0")
        return value


def get_Code(stock_name):
    query = WINDOW_SERVER + "/transaction/get_Code?target_name=" + stock_name
    result = requests.get(query)
    return result.json().get("code")


@router.post("/buying")
def buying(response: TransactionRequest):
    request = response

    # 주식명을 주식코드로 변경
    stock_code = get_Code(request.stock_name)

    # window 서버로 매수 거래 get 요청
    url = WINDOW_SERVER + "/transaction/transaction"
    data = {
        "account_number": request.account_number,
        "password": request.password,
        "stock_code": stock_code,
        "quantity": request.quantity,
        "order_type": 1,
    }

    response = requests.post(url, json=data)

    if response.status_code == 200:
        result = response.json().get("result")
        return {"result": result}
    else:
        raise HTTPException(status_code=400, detail="Failed to place order")


@router.post("/selling")
def selling(response: TransactionRequest):
    request = response

    # 주식명을 주식코드로 변경
    stock_code = get_Code(request.stock_name)

    # window 서버로 매도 거래 get 요청
    url = WINDOW_SERVER + "/transaction/transaction"
    data = {
        "account_number": request.account_number,
        "password": request.password,
        "stock_code": stock_code,
        "quantity": request.quantity,
        "order_type": 2,
    }

    response = requests.post(url, json=data)

    if response.status_code == 200:
        result = response.json().get("result")
        return {"result": result}
    else:
        raise HTTPException(status_code=400, detail="Failed to place order")
