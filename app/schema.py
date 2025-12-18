from pydantic import BaseModel, EmailStr

class HouseResponse(BaseModel):
    id: int
    state: str
    town: str
    price: float
    house_type: str
    bedrooms: int | None = None
    bathrooms: int | None = None
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
    house_type: str
    bedrooms: int | None = None
    bathrooms: int | None = None
    description: str | None = None
    class Config:
        from_attributes = True
