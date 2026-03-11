from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pickle
import pandas as pd
import numpy as np
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = pickle.load(open("artifacts/car_price_model.pkl","rb"))

# serve frontend
app.mount("/static", StaticFiles(directory="../frontend"), name="static")

@app.get("/")
def serve_frontend():
    return FileResponse("../frontend/index.html")

@app.post("/predict")
def predict(data: dict):

    km_per_year = data["km_driven"] / data["car_age"]

    input_df = pd.DataFrame([{
        "brand": data["brand"],
        "fuel": data["fuel"],
        "seller_type": data["seller_type"],
        "transmission": data["transmission"],
        "owner": data["owner"],
        "km_driven": data["km_driven"],
        "car_age": data["car_age"],
        "km_per_year": km_per_year
    }])

    pred = model.predict(input_df)

    price = int(np.exp(pred)[0])

    return {"predicted_price": price}