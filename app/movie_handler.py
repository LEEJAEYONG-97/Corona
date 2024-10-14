import pandas as pd

# 영화 데이터를 로드하는 함수
def load_movie_data(file_path: str):
    try:
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        print(f"Error loading file: {e}")
        return None

# 2020년 1월 이후의 데이터 필터링 및 평균 계산
def get_movie_data_analysis(file_path: str):
    df = load_movie_data(file_path)

    if df is not None:
        # 날짜를 datetime 형식으로 변환
        df['date'] = pd.to_datetime(df['date'], format='%Y-%m')

        # 2020년 1월 이후 데이터 필터링
        filtered_df = df[df['date'] >= '2020-01-01']

        # 각 컬럼별 분석
        data_count = len(filtered_df)
        avg_screen_cnt = filtered_df['screen_cnt'].mean()
        avg_total_sales = filtered_df['total_sales'].mean()
        avg_audience = filtered_df['audience'].mean()

        return data_count, avg_screen_cnt, avg_total_sales, avg_audience

    return None, None, None, None

# 연도별 데이터 건수와 스크린 수를 계산하는 함수
def get_yearly_data(file_path: str):
    df = load_movie_data(file_path)
    
    if df is not None:
        # 'date' 컬럼에서 연도만 추출
        df['year'] = pd.to_datetime(df['date']).dt.year
        
        # 연도별 데이터 건수 계산
        yearly_data_count = df.groupby('year').size().to_dict()
        
        # 연도별 스크린 수 합계 계산
        yearly_screen_count = df.groupby('year')['screen_cnt'].sum().to_dict()

        return yearly_data_count, yearly_screen_count
    
    return None, None

# 연도별 관객수 데이터 분석 함수
def get_yearly_audience_data(file_path: str):
    df = load_movie_data(file_path)

    if df is not None:
        # 'date' 컬럼을 datetime으로 변환
        df['date'] = pd.to_datetime(df['date'])
        
        # 2019년 이후 데이터만 필터링
        df = df[df['date'].dt.year >= 2019]

        # 연도별 관객 수 분석
        yearly_audience_data = df.groupby(df['date'].dt.year)['audience'].sum().to_dict()

        # 연도와 관객 수 데이터를 리스트로 반환
        years = list(yearly_audience_data.keys())
        audience_counts = list(yearly_audience_data.values())

        return years, audience_counts

    return None, None
