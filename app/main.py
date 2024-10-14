from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles  # 추가
from app.routers import main_dash, covid_data, sports_data, movie_data, ml_model   # main_dash 라우터 임포트

# FastAPI 애플리케이션 생성
app = FastAPI()

# 정적 파일 경로 설정
app.mount("/static", StaticFiles(directory="app/static"), name="static")  # 정적 파일 제공 설정 추가

# 라우터 등록
app.include_router(main_dash.router)
app.include_router(covid_data.router)
app.include_router(sports_data.router)
app.include_router(movie_data.router)
app.include_router(ml_model.router)

# 루트 엔드포인트
@app.get("/")
def read_root():
    return {"message": "COVID-19 Project"}