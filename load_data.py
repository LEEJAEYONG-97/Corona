import pandas as pd
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import crud  # CRUD 함수들을 사용
from app import models

# 엑셀 파일에서 데이터를 불러와 삽입하는 함수
def load_excel_data(file_path: str, sheet_name: str, columns: list):
    try:
        # 데이터프레임으로 엑셀 파일 읽기
        df = pd.read_excel(file_path, sheet_name=sheet_name)

        # 'year' 컬럼이 있을 경우 문자열에서 숫자로 변환
        if 'year' in df.columns:
            df['year'] = df['year'].apply(lambda x: int(str(x).replace('년', '')) if isinstance(x, str) else x)

        return df[columns]
    except Exception as e:
        print(f"Error loading {sheet_name} from {file_path}: {e}")
        return pd.DataFrame()  # 오류 발생 시 빈 데이터 반환

# 데이터베이스에 데이터를 삽입하는 함수
def save_data_to_db():
    # 데이터베이스 세션 생성
    db: Session = SessionLocal()

    # covid19 데이터 삽입
    covid_data = load_excel_data("data/covid19.xlsx", "covid19", ['date', 'cnt', 'domestic_case', 'imported_case', 'death'])
    crud.insert_covid_data(db, covid_data)

    # covid_gender 데이터 삽입
    covid_gender_data = load_excel_data("data/covid_gender.xlsx", "gender", ['date', 'male', 'female'])
    crud.insert_covid_gender_data(db, covid_gender_data)

    # covid_year_occur 데이터 삽입
    covid_year_occur = load_excel_data("data/covid_year_occur.xlsx", "years_occur", ['date', 'cnt', '0_9', '10_19', '20_29', '30_39', '40_49', '50_59', '60_69', '70_79', '80_'])
    crud.insert_covid_year_occurrence(db, covid_year_occur)

    # covid_year_death 데이터 삽입
    covid_year_death = load_excel_data("data/covid_year_death.xlsx", "years_death", ['year', 'cnt', '0_9', '10_19', '20_29', '30_39', '40_49', '50_59', '60_69', '70_79', '80_'])
    crud.insert_covid_year_death(db, covid_year_death)

    # covid_city_occur 데이터 삽입
    covid_city_occur = load_excel_data("data/covid_city_occur.xlsx", "city_occur", ['date', 'cnt', 'seoul', 'busan', 'daegu', 'incheon', 'gwangju', 'daejeon', 'ulsan', 'sejong', 'gyeonggi', 'gangwon', 'chungbuk', 'chungnam', 'jeonbuk', 'jeonnam', 'gyeongbuk', 'gyeongnam', 'jeju', 'quarantine'])
    crud.insert_covid_city_occurrence(db, covid_city_occur)

    # covid_city_death 데이터 삽입
    covid_city_death = load_excel_data("data/covid_city_death.xlsx", "city_death", ['date', 'cnt', 'seoul', 'busan', 'daegu', 'incheon', 'gwangju', 'daejeon', 'ulsan', 'sejong', 'gyeonggi', 'gangwon', 'chungbuk', 'chungnam', 'jeonbuk', 'jeonnam', 'gyeongbuk', 'gyeongnam', 'jeju', 'quarantine'])
    crud.insert_covid_city_death(db, covid_city_death)

    # covid_city_total 데이터 삽입
    covid_city_total = load_excel_data("data/covid_city_total.xlsx", "detail_city", ['city', 'si_gun_gu', 'total_cnt', 'total_death', 'occurrence_rate', 'death_rate'])
    crud.insert_covid_city_total(db, covid_city_total)

    # sports_event 데이터 삽입
    sports_event = load_excel_data("data/sport.xlsx", "Sheet1", ['cnt', 'domestic_case', 'imported_case', 'death', 'date', 'organization', 'league', 'attendance'])
    crud.insert_sports_event(db, sports_event)

    # MovieScreeningData 데이터 삽입
    movie_screening_data = load_excel_data("data/kobis_data.xlsx", "kobis_data", ['date', 'screen_cnt', 'total_sales', 'audience'])
    crud.insert_movie_screening_data(db, movie_screening_data)

    # 데이터베이스 커밋
    db.commit()

    # 데이터베이스 연결 닫기
    db.close()

if __name__ == "__main__":
    save_data_to_db()