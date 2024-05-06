import joblib
from fastapi import APIRouter

router = APIRouter(
    prefix="/prediction",
    tags=["Prediction"],
    responses={404: {"description": "Not found"}},
)


@router.post("/predict")
def predict(data):
    model = joblib.load("models/model.joblib")
    prediction = model.predict(data)

    return prediction
