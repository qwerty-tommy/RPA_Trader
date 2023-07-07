from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api import transaction, user

app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 도메인 허용, 배포시 수정해야함!
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메서드 허용
    allow_headers=["*"],  # 모든 헤더 허용
)

app.include_router(transaction.router)
app.include_router(user.router)
