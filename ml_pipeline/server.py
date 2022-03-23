import os
from pathlib import Path
import pickle

from fastapi import FastAPI
import pandas as pd
from pydantic import BaseModel


MODEL_PATH = os.environ.get('MODEL_PATH', '.')

app = FastAPI()

loaded = False
_model = None


class Vector(BaseModel):
    fixed_acidity: float
    volatile_acidity: float
    citric_acid: float
    residual_sugar: float
    chlorides: float
    free_sulfur_dioxide: float
    total_sulfur_dioxide: float
    density: float
    ph: float
    sulphates: float
    alcohol: float

    def convert(self):
        return pd.DataFrame(
            self.dict().values(),
            index=pd.Index(
                [
                    'fixed acidity',
                    'volatile acidity',
                    'citric acid',
                    'residual sugar',
                    'chlorides',
                    'free sulfur dioxide',
                    'total sulfur dioxide',
                    'density',
                    'pH',
                    'sulphates',
                    'alcohol',
                ]
            )
        )


def model():
    global loaded
    global _model
    if loaded:
        return _model
    else:
        models = sorted([m for m in Path(MODEL_PATH).iterdir()], reverse=True)
        with open(models[0], 'rb') as file:
            file.seek(0)
            model = pickle.load(file)
        loaded = True
        _model = model
        return model


@app.post("/predict")
async def predict(data: Vector):
    vector = data.convert().transpose()
    result = model().predict(vector)
    return {'prediction': round(result[0])}
