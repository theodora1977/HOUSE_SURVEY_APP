from pydantic import BaseModel, EmailStr

# --- House Prediction Input ---
class HousePredictionInput(BaseModel):
    bedrooms: int
    bathrooms: int
    toilets: int
    parking_space: int

# --- Response from Prediction ---
class HousePredictionResponse(BaseModel):
    predicted_price: float

# --- User Schemas ---
class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    is_active: bool

    class Config:
        from_attributes = True

# --- Token Schemas ---
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str | None = None
