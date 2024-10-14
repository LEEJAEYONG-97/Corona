from sqlalchemy.orm import Session
from app import models
from sqlalchemy import func

# CovidData 삽입
def insert_covid_data(db: Session, data):
    for _, row in data.iterrows():
        existing_data = db.query(models.CovidData).filter(models.CovidData.date == row['date']).first()
        if not existing_data:
            covid_data = models.CovidData(
                date=row['date'],
                cnt=row['cnt'],
                domestic_case=row['domestic_case'],
                imported_case=row['imported_case'],
                death=row['death']
            )
            db.add(covid_data)
    db.commit()

# CovidGenderData 삽입
def insert_covid_gender_data(db: Session, data):
    for _, row in data.iterrows():
        existing_data = db.query(models.CovidGenderData).filter(models.CovidGenderData.date == row['date']).first()
        if not existing_data:
            covid_gender_data = models.CovidGenderData(
                date=row['date'],
                male=row['male'],
                female=row['female']
            )
            db.add(covid_gender_data)
    db.commit()

# CovidYearOccurrence 삽입
def insert_covid_year_occurrence(db: Session, data):
    for _, row in data.iterrows():
        existing_data = db.query(models.CovidYearOccurrence).filter(models.CovidYearOccurrence.date == row['date']).first()
        if not existing_data:
            covid_year_occurrence = models.CovidYearOccurrence(
                date=row['date'],
                cnt=row['cnt'],
                age_0_9=row['0_9'],
                age_10_19=row['10_19'],
                age_20_29=row['20_29'],
                age_30_39=row['30_39'],
                age_40_49=row['40_49'],
                age_50_59=row['50_59'],
                age_60_69=row['60_69'],
                age_70_79=row['70_79'],
                age_80_plus=row['80_']
            )
            db.add(covid_year_occurrence)
    db.commit()

# CovidYearDeath 삽입
def insert_covid_year_death(db: Session, data):
    for _, row in data.iterrows():
        existing_data = db.query(models.CovidYearDeath).filter(models.CovidYearDeath.year == row['year']).first()
        if not existing_data:
            covid_year_death = models.CovidYearDeath(
                year=row['year'],
                cnt=row['cnt'],
                age_0_9=row['0_9'],
                age_10_19=row['10_19'],
                age_20_29=row['20_29'],
                age_30_39=row['30_39'],
                age_40_49=row['40_49'],
                age_50_59=row['50_59'],
                age_60_69=row['60_69'],
                age_70_79=row['70_79'],
                age_80_plus=row['80_']
            )
            db.add(covid_year_death)
    db.commit()

# CovidCityOccurrence 삽입
def insert_covid_city_occurrence(db: Session, data):
    for _, row in data.iterrows():
        existing_data = db.query(models.CovidCityOccurrence).filter(models.CovidCityOccurrence.date == row['date']).first()
        if not existing_data:
            covid_city_occurrence = models.CovidCityOccurrence(
                date=row['date'],
                cnt=row['cnt'],
                seoul=row['seoul'],
                busan=row['busan'],
                daegu=row['daegu'],
                incheon=row['incheon'],
                gwangju=row['gwangju'],
                daejeon=row['daejeon'],
                ulsan=row['ulsan'],
                sejong=row['sejong'],
                gyeonggi=row['gyeonggi'],
                gangwon=row['gangwon'],
                chungbuk=row['chungbuk'],
                chungnam=row['chungnam'],
                jeonbuk=row['jeonbuk'],
                jeonnam=row['jeonnam'],
                gyeongbuk=row['gyeongbuk'],
                gyeongnam=row['gyeongnam'],
                jeju=row['jeju'],
                quarantine=row['quarantine']
            )
            db.add(covid_city_occurrence)
    db.commit()

# CovidCityDeath 삽입
def insert_covid_city_death(db: Session, data):
    for _, row in data.iterrows():
        existing_data = db.query(models.CovidCityDeath).filter(models.CovidCityDeath.date == row['date']).first()
        if not existing_data:
            covid_city_death = models.CovidCityDeath(
                date=row['date'],
                cnt=row['cnt'],
                seoul=row['seoul'],
                busan=row['busan'],
                daegu=row['daegu'],
                incheon=row['incheon'],
                gwangju=row['gwangju'],
                daejeon=row['daejeon'],
                ulsan=row['ulsan'],
                sejong=row['sejong'],
                gyeonggi=row['gyeonggi'],
                gangwon=row['gangwon'],
                chungbuk=row['chungbuk'],
                chungnam=row['chungnam'],
                jeonbuk=row['jeonbuk'],
                jeonnam=row['jeonnam'],
                gyeongbuk=row['gyeongbuk'],
                gyeongnam=row['gyeongnam'],
                jeju=row['jeju'],
                quarantine=row['quarantine']
            )
            db.add(covid_city_death)
    db.commit()

# CovidCityTotal 삽입
def insert_covid_city_total(db: Session, data):
    for _, row in data.iterrows():
        existing_data = db.query(models.CovidCityTotal).filter(models.CovidCityTotal.city == row['city']).first()
        if not existing_data:
            covid_city_total = models.CovidCityTotal(
                city=row['city'],
                si_gun_gu=row['si_gun_gu'],
                total_cnt=row['total_cnt'],
                total_death=row['total_death'],
                occurrence_rate=row['occurrence_rate'],
                death_rate=row['death_rate']
            )
            db.add(covid_city_total)
    db.commit()

# SportsEvent 삽입
def insert_sports_event(db: Session, data):
    for _, row in data.iterrows():
        existing_data = db.query(models.SportsEvent).filter(models.SportsEvent.date == row['date']).first()
        if not existing_data:
            sports_event = models.SportsEvent(
                cnt=row['cnt'],
                domestic_case=row['domestic_case'],
                imported_case=row['imported_case'],
                death=row['death'],
                date=row['date'],
                organization=row['organization'],
                league=row['league'],
                attendance=row['attendance']
            )
            db.add(sports_event)
    db.commit()

# MovieScreeningData 삽입
def insert_movie_screening_data(db: Session, data):
    for _, row in data.iterrows():
        existing_data = db.query(models.MovieScreeningData).filter(models.MovieScreeningData.date == row['date']).first()
        if not existing_data:
            movie_screening_data = models.MovieScreeningData(
                date=row['date'],
                screen_cnt=row['screen_cnt'],
                total_sales=row['total_sales'],
                audience=row['audience']
            )
            db.add(movie_screening_data)
    db.commit()

# 누적 확진자 수와 사망자 수를 가져오는 함수
def get_total_covid_cases_and_deaths(db: Session):
    total_cases = db.query(func.sum(models.CovidData.cnt)).scalar()
    total_deaths = db.query(func.sum(models.CovidData.death)).scalar()
    return total_cases, total_deaths

# 일자별 확진자 및 사망자 수를 가져오는 함수
def get_daily_cases_and_deaths(db: Session):
    return db.query(models.CovidData).order_by(models.CovidData.date).all()
