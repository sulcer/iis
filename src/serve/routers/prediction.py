from fastapi import APIRouter

router = APIRouter(
    prefix="/prediction",
    tags=["Prediction"],
    responses={404: {"description": "Not found"}},
)


@router.post("/predict")
def predict(data):
    return data
