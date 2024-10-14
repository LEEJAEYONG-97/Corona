# 이 파일은 디렉토리를 패키지로 인식하게 해주는 역할을 합니다.
# 특별한 코드가 필요하지 않으며, 빈 파일로 두거나, 패키지의 초기화 동작을 정의할 수 있습니다.

# __init__.py 파일은 빈 파일로 남겨두거나, 라우터 파일들을 모듈로 임포트하는 역할을 할 수 있습니다.

from .covid_data import router as covid_data_router
from .sports_data import router as sports_data_router
