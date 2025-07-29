from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# from dotenv import load_dotnv
from routers import procedures, tables

app = FastAPI()

# CORS 설정 추가
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 도메인 허용, 특정 도메인만 허용하려면 ["http://localhost:3000"] 과 같이 사용
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메서드 허용 (GET, POST, PUT, DELETE 등)
    allow_headers=["*"],  # 모든 HTTP 헤더 허용
)

app.include_router(procedures.router, tags=["Procedures"])
app.include_router(tables.router, tags=["Tables"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app"}

# __main__에서 uvicorn 실행
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
