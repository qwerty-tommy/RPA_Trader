from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import requests

router = APIRouter(
    prefix="/user",
)

WINDOW_SERVER = "http://localhost:8001"


class UserRequest(BaseModel):
    account_number: str
    password: str


@router.post("/info")
def info(response: UserRequest):
    request = response

    # window 서버로 사용자 정보 get 요청
    url = WINDOW_SERVER + "/user/info"
    data = {
        "account_number": request.account_number,
        "password": request.password,
    }
    response = requests.post(url, json=data)

    if response.status_code == 200:
        result = response.json()
        return {"result": result}
    else:
        raise HTTPException(status_code=400, detail="Failed to place order")
