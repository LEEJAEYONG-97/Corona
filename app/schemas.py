from pydantic import BaseModel
from datetime import date

# CovidData 스키마
class CovidDataBase(BaseModel):
    date: date
    cnt: int
    domestic_case: int
    imported_case: int
    death: int

class CovidDataCreate(CovidDataBase):
    pass

class CovidData(CovidDataBase):
    id: int

    class Config:
        orm_mode = True

# CovidGenderData 스키마
class CovidGenderDataBase(BaseModel):
    date: date
    male: int
    female: int

class CovidGenderDataCreate(CovidGenderDataBase):
    pass

class CovidGenderData(CovidGenderDataBase):
    id: int

    class Config:
        orm_mode = True

# CovidYearOccurrence 스키마
class CovidYearOccurrenceBase(BaseModel):
    date: date
    cnt: int
    age_0_9: int
    age_10_19: int
    age_20_29: int
    age_30_39: int
    age_40_49: int
    age_50_59: int
    age_60_69: int
    age_70_79: int
    age_80_plus: int

class CovidYearOccurrenceCreate(CovidYearOccurrenceBase):
    pass

class CovidYearOccurrence(CovidYearOccurrenceBase):
    id: int

    class Config:
        orm_mode = True

# CovidYearDeath 스키마
class CovidYearDeathBase(BaseModel):
    year: int
    cnt: int
    age_0_9: int
    age_10_19: int
    age_20_29: int
    age_30_39: int
    age_40_49: int
    age_50_59: int
    age_60_69: int
    age_70_79: int
    age_80_plus: int

class CovidYearDeathCreate(CovidYearDeathBase):
    pass

class CovidYearDeath(CovidYearDeathBase):
    id: int

    class Config:
        orm_mode = True

# CovidCityOccurrence 스키마
class CovidCityOccurrenceBase(BaseModel):
    date: date
    cnt: int
    seoul: int
    busan: int
    daegu: int
    incheon: int
    gwangju: int
    daejeon: int
    ulsan: int
    sejong: int
    gyeonggi: int
    gangwon: int
    chungbuk: int
    chungnam: int
    jeonbuk: int
    jeonnam: int
    gyeongbuk: int
    gyeongnam: int
    jeju: int
    quarantine: int

class CovidCityOccurrenceCreate(CovidCityOccurrenceBase):
    pass

class CovidCityOccurrence(CovidCityOccurrenceBase):
    id: int

    class Config:
        orm_mode = True

# CovidCityDeath 스키마
class CovidCityDeathBase(BaseModel):
    date: date
    cnt: int
    seoul: int
    busan: int
    daegu: int
    incheon: int
    gwangju: int
    daejeon: int
    ulsan: int
    sejong: int
    gyeonggi: int
    gangwon: int
    chungbuk: int
    chungnam: int
    jeonbuk: int
    jeonnam: int
    gyeongbuk: int
    gyeongnam: int
    jeju: int
    quarantine: int

class CovidCityDeathCreate(CovidCityDeathBase):
    pass

class CovidCityDeath(CovidCityDeathBase):
    id: int

    class Config:
        orm_mode = True

# CovidCityTotal 스키마 (도시별 토탈 데이터)
class CovidCityTotalBase(BaseModel):
    city: str
    si_gun_gu: str
    total_cnt: int
    total_death: int
    occurrence_rate: float
    death_rate: float

class CovidCityTotalCreate(CovidCityTotalBase):
    pass

class CovidCityTotal(CovidCityTotalBase):
    id: int

    class Config:
        orm_mode = True

# SportsEvent 스키마
class SportsEventBase(BaseModel):
    cnt: int
    domestic_case: int
    imported_case: int
    death: int
    date: date
    organization: str
    league: str
    attendance: float

class SportsEventCreate(SportsEventBase):
    pass

class SportsEvent(SportsEventBase):
    id: int

    class Config:
        orm_mode = True

# MovieScreeningData 스키마
class MovieScreeningDataBase(BaseModel):
    date: date
    screen_cnt: int
    total_sales: int
    audience: int

class MovieScreeningDataCreate(MovieScreeningDataBase):
    pass

class MovieScreeningData(MovieScreeningDataBase):
    id: int

    class Config:
        orm_mode = True