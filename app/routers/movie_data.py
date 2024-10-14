from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from app.movie_handler import get_movie_data_analysis, get_yearly_data, get_yearly_audience_data

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/movie-data/")
def movie_data_page(request: Request):
    file_path = "data/kobis_data.xlsx"
    
    # 기본 분석 데이터 가져오기
    data_count, avg_screen_cnt, avg_total_sales, avg_audience = get_movie_data_analysis(file_path)
    
    # 연도별 데이터 건수 및 스크린 수 가져오기
    yearly_data_count, yearly_screen_count = get_yearly_data(file_path)
    
    # 연도별 관객수 데이터 가져오기
    years, audience_counts = get_yearly_audience_data(file_path)
    
    # 데이터가 없을 경우 빈 값으로 대체
    years = years if years else []
    audience_counts = audience_counts if audience_counts else []
    
    # 데이터가 정상적으로 계산되었는지 확인
    if data_count and avg_screen_cnt and avg_total_sales and avg_audience and yearly_data_count and yearly_screen_count and audience_counts and years:
        return templates.TemplateResponse("movie_data.html", {
            "request": request,
            "data_count": data_count,
            "avg_screen_cnt": avg_screen_cnt,
            "avg_total_sales": avg_total_sales,
            "avg_audience": avg_audience,
            "yearly_data_count": yearly_data_count,
            "yearly_screen_count": yearly_screen_count,
            "years": years,
            "audience_counts": audience_counts
        })
    else:
        return {"message": "Data not available"}
