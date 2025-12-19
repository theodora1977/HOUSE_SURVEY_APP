from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import joblib
import pandas as pd
import os

from app import schema, security
from app.database import get_db
from app import models

router = APIRouter(prefix="/houses", tags=["Houses"])

# --- Load AI model once ---
MODEL_PATH = "house_price_model.pkl"
model = None

if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
    print("Prediction model loaded successfully.")

# --- Prediction Endpoint ---
@router.post("/predict")
def predict_price(
    input_data: schema.HousePredictionInput,
    current_user: schema.UserResponse = Depends(security.get_current_user)
):
    """
    Predicts house price based on user input:
    bedrooms, bathrooms, toilets, parking space.
    """
    if model is None:
        return {"predicted_price": 0.0, "message": "Model not trained yet."}

    # Convert input to DataFrame (model expects same columns as training)
    input_df = pd.DataFrame([input_data.dict()])
    prediction = model.predict(input_df)
    return {"predicted_price": round(prediction[0], 2)}

@router.get("/options/house-types", response_model=List[str])
def get_house_types(current_user: schema.UserResponse = Depends(security.get_current_user)):
    """Returns available house types for the dropdown."""
    return [t.value for t in models.HouseType]

@router.get("/options/bathroom-types", response_model=List[str])
def get_bathroom_types(current_user: schema.UserResponse = Depends(security.get_current_user)):
    """Returns available bathroom options for the dropdown."""
    return [t.value for t in models.BathroomType]

@router.get("/options/toilet-types", response_model=List[str])
def get_toilet_types(current_user: schema.UserResponse = Depends(security.get_current_user)):
    """Returns available toilet options for the dropdown."""
    return [t.value for t in models.ToiletType]

@router.get("/options/parking-space-types", response_model=List[str])
def get_parking_space_types(current_user: schema.UserResponse = Depends(security.get_current_user)):
    """Returns available parking space options for the dropdown."""
    return [t.value for t in models.ParkingSpaceType]
