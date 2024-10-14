from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from app.covid_handler import load_covid_data, calculate_yearly_age_deaths, calculate_region_city_data, convert_int64_to_int
import pandas as pd

router = APIRouter()

# 템플릿 디렉토리 설정
templates = Jinja2Templates(directory="app/templates")

# 성별 데이터를 처리하고 비율을 계산하는 함수
def calculate_gender_ratio(file_path: str):
    df = load_covid_data(file_path)
    
    if df is not None:
        total_male = df['male'].sum()
        total_female = df['female'].sum()

        return {"male": total_male, "female": total_female}
    
    return None

# 연령별 확진자 데이터를 처리하는 함수
def calculate_age_distribution(file_path: str):
    df = load_covid_data(file_path)
    
    if df is not None:
        df['date'] = pd.to_datetime(df['date'])
        age_columns = ['0_9', '10_19', '20_29', '30_39', '40_49', '50_59', '60_69', '70_79', '80_']
        df_monthly = df.resample('M', on='date').sum()

        age_data = {age: df_monthly[age].tolist() for age in age_columns}
        months = df_monthly.index.strftime('%Y-%m').tolist()

        return {"months": months, "age_data": age_data}
    
    return None

# COVID19 Data 분석을 보여주는 페이지
@router.get("/covid-data/")
def covid_data_page(request: Request):
    # 엑셀 파일 경로 설정
    gender_file_path = "data/covid_gender.xlsx"
    age_file_path = "data/covid_year_occur.xlsx"
    age_death_file_path = "data/covid_year_death.xlsx"
    occur_file_path = "data/covid_city_occur.xlsx"
    death_file_path = "data/covid_city_death.xlsx"
    
    # 성별 확진자 데이터를 계산
    gender_data = calculate_gender_ratio(gender_file_path)
    
    # 연령대별 확진자 데이터를 계산
    age_data = calculate_age_distribution(age_file_path)
    
    # 연령대별 사망자 데이터를 계산 (연도별)
    age_death_data = calculate_yearly_age_deaths(age_death_file_path)
    
    # 권역별 각 도시별 확진자 및 사망자 데이터 계산
    region_city_confirmed, region_city_deaths = calculate_region_city_data(occur_file_path, death_file_path)

    # 이미 정의된 convert_int64_to_int 함수를 사용하여 int64 -> int 변환
    region_city_confirmed = {region: convert_int64_to_int(city_data) for region, city_data in region_city_confirmed.items()}
    region_city_deaths = {region: convert_int64_to_int(city_data) for region, city_data in region_city_deaths.items()}

    # 데이터가 있는지 확인
    if gender_data and age_data and age_death_data and region_city_confirmed and region_city_deaths:
        return templates.TemplateResponse("covid_data.html", {
            "request": request,
            "male": gender_data['male'],
            "female": gender_data['female'],
            "months": age_data['months'],
            "age_groups": age_data['age_data'],
            "years": age_death_data['years'],
            "age_deaths": age_death_data['age_deaths'],
            "region_city_confirmed": region_city_confirmed,  # 권역별 도시별 확진자 데이터
            "region_city_deaths": region_city_deaths  # 권역별 도시별 사망자 데이터
        })
    else:
        return {"message": "Data not available"}
