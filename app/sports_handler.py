import pandas as pd

# 스포츠 데이터 로드 함수
def load_sports_data(file_path: str):
    try:
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        print(f"Error loading file: {e}")
        return None

# 월별 확진자 및 관중수를 계산하는 함수
def get_combined_sports_data(covid_file_path: str, sport_file_path: str):
    covid_df = load_sports_data(covid_file_path)
    sport_df = load_sports_data(sport_file_path)

    if covid_df is not None and sport_df is not None:
        # 코로나 확진자 데이터를 월별로 그룹화
        covid_df['date'] = pd.to_datetime(covid_df['date'])
        monthly_covid = covid_df.resample('M', on='date').sum().reset_index()
        months_covid = monthly_covid['date'].dt.strftime('%Y-%m').tolist()
        cases = monthly_covid['cnt'].tolist()

        # 스포츠 관중수 데이터를 월별로 그룹화
        sport_df['date'] = pd.to_datetime(sport_df['date'])
        monthly_sport = sport_df.resample('M', on='date').sum().reset_index()
        months_attendance = monthly_sport['date'].dt.strftime('%Y-%m').tolist()
        attendance = monthly_sport['attendance'].tolist()

        return months_covid, cases, months_attendance, attendance

    return None, None, None, None

# 조직별 무관중 경기 수 데이터를 추출하는 함수
def get_no_audience_data(file_path: str):
    df = load_sports_data(file_path)

    if df is not None:
        # 무관중 경기 데이터를 필터링
        no_audience_df = df[df['attendance'] == 0]
        
        # 조직별 무관중 경기 수 계산
        organization_no_audience = no_audience_df.groupby('organization')['attendance'].count()

        # 조직명과 무관중 경기 수 반환
        organizations = organization_no_audience.index.tolist()
        no_attendance_games = organization_no_audience.values.tolist()

        return organizations, no_attendance_games
    return [], []

# 협회별 월별 관중수 데이터를 계산하는 함수
def get_monthly_attendance_by_association(file_path: str):
    df = load_sports_data(file_path)

    if df is not None:
        df['date'] = pd.to_datetime(df['date'])

        # 월별 및 조직별로 그룹화한 후 관중 수 합산
        monthly_data = df.groupby([df['date'].dt.strftime('%Y-%m'), 'organization'])['attendance'].sum().unstack()

        months = monthly_data.index.tolist()  # 월 리스트
        monthly_attendance_by_association = monthly_data.to_dict(orient='list')  # 조직별 월별 관중수

        return months, monthly_attendance_by_association

    return None, None
