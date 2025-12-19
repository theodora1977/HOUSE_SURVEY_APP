from pydantic import BaseModel, EmailStr
from app.models import HouseType, BathroomType, ToiletType, ParkingSpaceType

class HouseResponse(BaseModel):
    id: int
    state: str
    town: str
    price: float
    house_type: HouseType
    bedrooms: int
    bathrooms: BathroomType
    toilets: ToiletType
    parking_space: ParkingSpaceType
    description: str | None = None

    class Config:
        from_attributes = True

# Schemas for Authentication
class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    is_active: bool

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str | None = None
class HouseCreate(BaseModel):
    state: str
    town: str
    price: float
    house_type: HouseType
    bedrooms: int
    bathrooms: BathroomType
    toilets: ToiletType
    parking_space: ParkingSpaceType
    description: str | None = None
    class Config:
        from_attributes = True

class HousePredictionInput(BaseModel):
    state: str
    town: str
    house_type: HouseType
    bedrooms: int
    bathrooms: BathroomType
    toilets: ToiletType
    parking_space: ParkingSpaceType
