from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from app.covid_handler import calculate_totals, calculate_monthly_totals

# Jinja2 템플릿 디렉토리 설정
templates = Jinja2Templates(directory="app/templates")

router = APIRouter()

@router.get("/")
def get_dashboard(request: Request):
    # 엑셀 파일의 경로를 main_dash.py에서 지정
    file_path = "data/covid19.xlsx"
    
    # covid_handler에서 데이터를 계산하는 함수 호출
    total_cases, total_deaths = calculate_totals(file_path)
    months, monthly_cases, monthly_deaths = calculate_monthly_totals(file_path)
    
    # 세 자리마다 쉼표를 추가하고 '명'을 붙여서 HTML에 전달
    total_cases_formatted = f"{total_cases:,} 명"
    total_deaths_formatted = f"{total_deaths:,} 명"
    
    # HTML 템플릿(index.html)에 데이터를 전달
    return templates.TemplateResponse("index.html", {
        "request": request,
        "total_cases": total_cases_formatted,
        "total_deaths": total_deaths_formatted,
        "months": months,  # 월 정보
        "monthly_cases": monthly_cases,  # 월별 확진자
        "monthly_deaths": monthly_deaths  # 월별 사망자
    })
