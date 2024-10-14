import pandas as pd

# 데이터를 불러오는 함수
def load_covid_data(file_path: str):
    try:
        # 엑셀 파일을 판다스로 읽어오기
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        print(f"Error loading file: {e}")
        return None

# 누적 확진자 수와 사망자 수를 계산하는 함수
def calculate_totals(file_path: str):
    df = load_covid_data(file_path)

    if df is not None:
        # 누적 확진자 수와 사망자 수 계산
        total_cases = df['cnt'].sum()  # cnt 컬럼에서 확진자 수 합계
        total_deaths = df['death'].sum()  # death 컬럼에서 사망자 수 합계
        return total_cases, total_deaths
    
    return None, None

# 월별 확진자 및 사망자 수를 계산하는 함수
def calculate_monthly_totals(file_path: str):
    df = load_covid_data(file_path)
    
    if df is not None:
        # 날짜를 datetime 형식으로 변환
        df['date'] = pd.to_datetime(df['date'])

        # 월별로 그룹화하여 확진자와 사망자 합계를 계산
        monthly_data = df.resample('M', on='date').sum().reset_index()

        # 필요한 데이터 반환 (월, 확진자, 사망자)
        months = monthly_data['date'].dt.strftime('%Y-%m').tolist()  # 월 형식으로 변환
        monthly_cases = monthly_data['cnt'].tolist()  # 월별 확진자 수
        monthly_deaths = monthly_data['death'].tolist()  # 월별 사망자 수

        return months, monthly_cases, monthly_deaths

    return None, None, None

# 남녀 성비 데이터를 계산하는 함수
def calculate_gender_ratio(file_path: str):
    df = load_covid_data(file_path)
    
    if df is not None:
        # 남성과 여성 확진자 수 합산
        total_male = df['male'].sum()
        total_female = df['female'].sum()
        
        return total_male, total_female
    return None, None

# 월별 확진자 수를 연령대별로 집계하는 함수
def calculate_monthly_totals_by_age(file_path: str):
    df = load_covid_data(file_path)

    if df is not None:
        # 날짜를 datetime 형식으로 변환
        df['date'] = pd.to_datetime(df['date'])

        # 월 단위로 데이터를 그룹화하고 연령대별 확진자 수 합산
        monthly_data = df.resample('M', on='date').sum().reset_index()

        # 월별 레이블 (YYYY-MM 형식)
        months = monthly_data['date'].dt.strftime('%Y-%m').tolist()

        # 연령대별 확진자 수 추출
        age_groups = ['0_9', '10_19', '20_29', '30_39', '40_49', '50_59', '60_69', '70_79', '80_']
        total_by_age_group = {age: monthly_data[age].tolist() for age in age_groups}

        return months, total_by_age_group
    return None, None

# 연령별 사망자 데이터를 처리하는 함수 (연도별)
def calculate_yearly_age_deaths(file_path: str):
    df = load_covid_data(file_path)
    
    if df is not None:
        # 연령대 컬럼 목록
        age_columns = ['0_9', '10_19', '20_29', '30_39', '40_49', '50_59', '60_69', '70_79', '80_']

        # 연도별 데이터
        df_yearly = df.groupby('year')[age_columns].sum()

        # 연령대별 데이터를 딕셔너리로 반환
        age_deaths = {age: df_yearly[age].tolist() for age in age_columns}

        # 연도 데이터를 리스트로 반환
        years = df_yearly.index.tolist()

        return {"years": years, "age_deaths": age_deaths}
    
    return None

# int64 데이터를 int로 변환하는 함수
def convert_int64_to_int(data_dict):
    return {k: int(v) for k, v in data_dict.items()}

# 권역별 각 도시별 확진자와 사망자 데이터를 계산하는 함수
def calculate_region_city_data(occur_file_path: str, death_file_path: str):
    occur_df = load_covid_data(occur_file_path)
    death_df = load_covid_data(death_file_path)

    if occur_df is not None and death_df is not None:
        # 날짜를 datetime 형식으로 변환
        occur_df['date'] = pd.to_datetime(occur_df['date'])
        death_df['date'] = pd.to_datetime(death_df['date'])

        # 권역별 도시 그룹
        regions = {
            '수도권': ['seoul', 'gyeonggi', 'incheon', 'gangwon'],
            '충청권': ['daejeon', 'sejong', 'chungbuk', 'chungnam'],
            '영남권': ['daegu', 'busan', 'ulsan', 'gyeongbuk', 'gyeongnam'],
            '호남권': ['gwangju', 'jeonbuk', 'jeonnam', 'jeju']
        }

        region_city_confirmed = {}
        region_city_deaths = {}

        # 권역별 도시별 확진자 및 사망자 수 계산
        for region, cities in regions.items():
            region_city_confirmed[region] = {city: int(occur_df[city].sum()) for city in cities}
            region_city_deaths[region] = {city: int(death_df[city].sum()) for city in cities}

        return region_city_confirmed, region_city_deaths

    return None, None