from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import joblib
import pandas as pd
import os

from app import models, schema, security
from app.database import get_db

router = APIRouter(prefix="/houses", tags=["Houses"])

@router.get("/states", response_model=List[str]) # Removed the local get_current_user
def get_all_states(db: Session = Depends(get_db), current_user: schema.UserResponse = Depends(security.get_current_user)):
    """
    Returns a list of all unique states where houses are available.
    Requires authentication.
    """
    states = db.query(models.House.state).distinct().all()
    return [state[0] for state in states]

@router.get("/states/{state_name}/towns", response_model=List[str]) # Removed the local get_current_user
def get_towns_in_state(state_name: str, db: Session = Depends(get_db), current_user: schema.UserResponse = Depends(security.get_current_user)):
    """
    Given a state, returns a list of all unique towns within that state.
    Requires authentication.
    """
    towns = db.query(models.House.town).filter(models.House.state.ilike(state_name)).distinct().all()
    if not towns:
        raise HTTPException(status_code=404, detail="State not found or no towns available")
    return [town[0] for town in towns]

@router.get("/towns/{town_name}/houses", response_model=List[schema.HouseResponse]) # Removed the local get_current_user
def get_houses_in_town(town_name: str, db: Session = Depends(get_db), current_user: schema.UserResponse = Depends(security.get_current_user)):
    """
    Given a town, returns a list of all available houses.
    The price shown is the specific price for each house listing.
    Requires authentication.
    """
    houses = db.query(models.House).filter(models.House.town.ilike(town_name)).all()
    if not houses:
        raise HTTPException(status_code=404, detail="Town not found or no houses available")
    return houses

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

@router.post("/predict")
def predict_price(input_data: schema.HousePredictionInput, current_user: schema.UserResponse = Depends(security.get_current_user)):
    """
    Predicts the house price based on features provided by the user.
    """
    model_path = "house_price_model.pkl"
    
    if not os.path.exists(model_path):
        return {"predicted_price": 0.0, "message": "Model not trained yet. Please run app/train_model.py"}

    # Load the model
    model = joblib.load(model_path)

    # Convert input data to a DataFrame (must match the training columns exactly)
    input_df = pd.DataFrame([input_data.dict()])
    
    # Make prediction
    prediction = model.predict(input_df)
    
    # Return the result (prediction is an array, we take the first item)
    return {"predicted_price": round(prediction[0], 2)}

@router.get("/{house_id}", response_model=schema.HouseResponse) # Removed the local get_current_user
def get_house_by_id(house_id: int, db: Session = Depends(get_db), current_user: schema.UserResponse = Depends(security.get_current_user)):
    """
    Retrieves the full details for a single house by its ID.
    This would be the "view details" page for a property.
    Requires authentication.
    """
    house = db.query(models.House).filter(models.House.id == house_id).first()
    if not house:
        raise HTTPException(status_code=404, detail=f"House with id {house_id} not found")
    return house