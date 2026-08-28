from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Sign Language API")

class LandmarkData(BaseModel):
    landmarks: list[float]

@app.post("/predict")
def predict_sign(data: LandmarkData):
    # TODO: Додати інтеграцію з MediaPipe та RandomForest
    return {"status": "success", "gesture": "dactyl_A"}