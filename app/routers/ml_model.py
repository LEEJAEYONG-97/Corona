from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
import pandas as pd
import joblib  # joblib을 사용하여 스케일러 로드
from tensorflow.keras.models import load_model
from fastapi.responses import JSONResponse  # JSON 응답을 위해 추가

router = APIRouter()

# 템플릿 디렉토리 설정
templates = Jinja2Templates(directory="app/templates")

# 모델 및 스케일러 로드
model = load_model("app/model/lstm_model.keras")

# joblib으로 스케일러 로드
scaler_X = joblib.load('app/model/scaler_X.pkl')
scaler_y = joblib.load('app/model/scaler_y.pkl')

# 예측을 위한 전처리 함수
def preprocess_data(date, cnt, domestic_case, imported_case, death, organization):
    # 데이터프레임 생성
    data = pd.DataFrame([{
        'date': date,
        'cnt': cnt,
        'domestic_case': domestic_case,
        'imported_case': imported_case,
        'death': death,
        'organization': organization
    }])

    # 날짜 데이터 전처리
    data['date'] = pd.to_datetime(data['date'])
    data.set_index('date', inplace=True)

    # 협회를 더미 변수로 변환
    dummy_columns = ['organization_KBL', 'organization_KBO', 'organization_KLEAGUE', 'organization_KOVO', 'organization_WKBL']
    data = pd.get_dummies(data, columns=['organization'])

    # 모든 더미 컬럼이 있는지 확인하고 없으면 0으로 채움
    for col in dummy_columns:
        if col not in data.columns:
            data[col] = 0

    # 필요한 입력 피처
    input_features = ['cnt', 'domestic_case', 'imported_case', 'death'] + dummy_columns
    data = data[input_features]

    # 데이터 정규화
    data_scaled = scaler_X.transform(data)
    return data_scaled

# 예측 함수
def make_prediction(input_data):
    # 입력 데이터 전처리 및 예측
    SEQ_LENGTH = 1  # 시퀀스 길이
    input_data_scaled = input_data.reshape(1, SEQ_LENGTH, -1)

    # 모델을 통한 예측
    prediction_scaled = model.predict(input_data_scaled)

    # 예측값을 다시 스케일링 해제
    prediction = scaler_y.inverse_transform(prediction_scaled)

    return prediction.flatten().tolist()  # 리스트 형태로 반환

# model 사업 예측을 보여주는 페이지
@router.get("/predict-model/")
def predict_model_page(request: Request):
    # 입력 폼을 렌더링하는 GET 요청 처리
    return templates.TemplateResponse("ml_model.html", {"request": request})

# 예측 처리
@router.post("/predict-model/")
def predict_model_result(request: Request,
                         date: str = Form(...),
                         cnt: int = Form(...),
                         domestic_case: int = Form(...),
                         imported_case: int = Form(...),
                         death: int = Form(...),
                         organization: str = Form(...)):
    # POST 요청 처리, 입력 데이터를 받아 예측 로직 실행
    
    # 입력 데이터 전처리
    input_data = preprocess_data(date, cnt, domestic_case, imported_case, death, organization)

    # 예측 함수 호출
    prediction = make_prediction(input_data)

     # 예측 결과 로그 확인
    print("예측 값:", prediction)

    # 예측 결과를 JSON 형식으로 반환 (float로 변환된 값)
    return JSONResponse(content={"prediction": prediction})