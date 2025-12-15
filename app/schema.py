from pydantic import BaseModel

class HouseResponse(BaseModel):
    id: int
    location: str
    price: str
    house_type: str
    bedrooms: int | None = None
    bathrooms: int | None = None
    description: str | None = None

    class Config:
        orm_mode = True
class HouseCreate(BaseModel):
    location: str
    price:str
    house_type: str
    bedrooms: int | None = None
    bathrooms: int | None = None
    description: str | None = None
    class Config:
        orm_mode = True
