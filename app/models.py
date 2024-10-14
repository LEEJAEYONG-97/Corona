from sqlalchemy import Column, BigInteger, Integer, String, Float, Date
from app.database import Base

# CovidData 테이블 정의
class CovidData(Base):
    __tablename__ = 'covid_data'

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False)
    cnt = Column(Integer, nullable=False)
    domestic_case = Column(Integer, nullable=False)
    imported_case = Column(Integer, nullable=False)
    death = Column(Integer, nullable=False)

# CovidGenderData 테이블 정의
class CovidGenderData(Base):
    __tablename__ = 'covid_gender_data'

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False)
    male = Column(Integer, nullable=False)
    female = Column(Integer, nullable=False)

# CovidYearOccurrence 테이블 정의
class CovidYearOccurrence(Base):
    __tablename__ = 'covid_year_occurrence'

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False)
    cnt = Column(Integer, nullable=False)
    age_0_9 = Column(Integer, nullable=False)
    age_10_19 = Column(Integer, nullable=False)
    age_20_29 = Column(Integer, nullable=False)
    age_30_39 = Column(Integer, nullable=False)
    age_40_49 = Column(Integer, nullable=False)
    age_50_59 = Column(Integer, nullable=False)
    age_60_69 = Column(Integer, nullable=False)
    age_70_79 = Column(Integer, nullable=False)
    age_80_plus = Column(Integer, nullable=False)

# CovidYearDeath 테이블 정의
class CovidYearDeath(Base):
    __tablename__ = 'covid_year_death'

    id = Column(Integer, primary_key=True, index=True)
    year = Column(Integer, nullable=False)
    cnt = Column(Integer, nullable=False)
    age_0_9 = Column(Integer, nullable=False)
    age_10_19 = Column(Integer, nullable=False)
    age_20_29 = Column(Integer, nullable=False)
    age_30_39 = Column(Integer, nullable=False)
    age_40_49 = Column(Integer, nullable=False)
    age_50_59 = Column(Integer, nullable=False)
    age_60_69 = Column(Integer, nullable=False)
    age_70_79 = Column(Integer, nullable=False)
    age_80_plus = Column(Integer, nullable=False)

# CovidCityOccurrence 테이블 정의
class CovidCityOccurrence(Base):
    __tablename__ = 'covid_city_occurrence'

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False)
    cnt = Column(Integer, nullable=False)
    seoul = Column(Integer, nullable=False)
    busan = Column(Integer, nullable=False)
    daegu = Column(Integer, nullable=False)
    incheon = Column(Integer, nullable=False)
    gwangju = Column(Integer, nullable=False)
    daejeon = Column(Integer, nullable=False)
    ulsan = Column(Integer, nullable=False)
    sejong = Column(Integer, nullable=False)
    gyeonggi = Column(Integer, nullable=False)
    gangwon = Column(Integer, nullable=False)
    chungbuk = Column(Integer, nullable=False)
    chungnam = Column(Integer, nullable=False)
    jeonbuk = Column(Integer, nullable=False)
    jeonnam = Column(Integer, nullable=False)
    gyeongbuk = Column(Integer, nullable=False)
    gyeongnam = Column(Integer, nullable=False)
    jeju = Column(Integer, nullable=False)
    quarantine = Column(Integer, nullable=False)

# CovidCityDeath 테이블 정의
class CovidCityDeath(Base):
    __tablename__ = 'covid_city_death'

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False)
    cnt = Column(Integer, nullable=False)
    seoul = Column(Integer, nullable=False)
    busan = Column(Integer, nullable=False)
    daegu = Column(Integer, nullable=False)
    incheon = Column(Integer, nullable=False)
    gwangju = Column(Integer, nullable=False)
    daejeon = Column(Integer, nullable=False)
    ulsan = Column(Integer, nullable=False)
    sejong = Column(Integer, nullable=False)
    gyeonggi = Column(Integer, nullable=False)
    gangwon = Column(Integer, nullable=False)
    chungbuk = Column(Integer, nullable=False)
    chungnam = Column(Integer, nullable=False)
    jeonbuk = Column(Integer, nullable=False)
    jeonnam = Column(Integer, nullable=False)
    gyeongbuk = Column(Integer, nullable=False)
    gyeongnam = Column(Integer, nullable=False)
    jeju = Column(Integer, nullable=False)
    quarantine = Column(Integer, nullable=False)

# CovidCityTotal 테이블 정의
class CovidCityTotal(Base):
    __tablename__ = 'covid_city_total'

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String(100), nullable=False)  # VARCHAR 길이 지정
    si_gun_gu = Column(String(100), nullable=False)  # VARCHAR 길이 지정
    total_cnt = Column(Integer, nullable=False)
    total_death = Column(Integer, nullable=False)
    occurrence_rate = Column(Float, nullable=False)
    death_rate = Column(Float, nullable=False)

# SportsEvent 테이블 정의
class SportsEvent(Base):
    __tablename__ = 'sports_event'

    id = Column(Integer, primary_key=True, index=True)
    cnt = Column(Integer, nullable=False)
    domestic_case = Column(Integer, nullable=False)
    imported_case = Column(Integer, nullable=False)
    death = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
    organization = Column(String(100), nullable=False)  # VARCHAR 길이 지정
    league = Column(String(100), nullable=False)  # VARCHAR 길이 지정
    attendance = Column(Integer, nullable=False)

class MovieScreeningData(Base):
    __tablename__ = 'movie_screening_data'
    
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    screen_cnt = Column(Integer)
    total_sales = Column(BigInteger)  # 기존 Integer에서 BigInteger로 수정
    audience = Column(BigInteger)  # 관객 수도 큰 값이 있을 수 있으므로 BigInteger로 수정