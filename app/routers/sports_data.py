import pandas as pd
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from app.sports_handler import get_combined_sports_data, get_no_audience_data, get_monthly_attendance_by_association

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

def handle_nan_values(data):
    """NaN 값을 0으로 대체하는 함수"""
    return {k: [0 if pd.isna(x) else x for x in v] for k, v in data.items()}

@router.get("/sports-data/")
def sports_data_page(request: Request):
    # 엑셀 파일 경로
    covid_file_path = "data/covid19.xlsx"
    sport_file_path = "data/sport.xlsx"
    
    # 월별 누적 확진자와 관중수 데이터 가져오기
    months_covid, cases, months_attendance, attendance = get_combined_sports_data(covid_file_path, sport_file_path)
    
    # 조직별 무관중 경기 데이터 가져오기
    organizations, no_attendance_games = get_no_audience_data(sport_file_path)
    
    # 각 협회별 월별 관중 수 데이터 가져오기
    months, monthly_attendance_by_association = get_monthly_attendance_by_association(sport_file_path)
    
    # NaN 값을 처리
    monthly_attendance_by_association = handle_nan_values(monthly_attendance_by_association)
    
    # 데이터가 있는지 확인
    if months_covid and cases and months_attendance and attendance and organizations and no_attendance_games and months and monthly_attendance_by_association:
        return templates.TemplateResponse("sports_data.html", {
            "request": request,
            "months_covid": months_covid,
            "cases": cases,
            "months_attendance": months_attendance,
            "attendance": attendance,
            "organizations": organizations,
            "no_attendance_games": no_attendance_games,
            "months": months,  # 협회별 월별 관중 수 월
            "monthly_attendance_by_association": monthly_attendance_by_association  # 협회별 월별 관중 수
        })
    else:
        return {"message": "Data not available"}
