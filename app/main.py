from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from app.model import predict
from app.schemas import PredictionResponse

app = FastAPI(title="Breast Cancer Detection API")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def home():
    with open("templates/index.html") as f:
        return f.read()

@app.post("/predict", response_model=PredictionResponse)
async def run_prediction(file: UploadFile = File(...)):
    image_bytes = await file.read()
    result = predict(image_bytes)
    return result

@app.get("/health")
def health():
    return {"status": "ok"}