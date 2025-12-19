import enum
from sqlalchemy import Column, Integer, String, Float, Boolean, Enum
from app.database import Base

class HouseType(str, enum.Enum):
    DUPLEX = "Duplex"
    DETACHED_DUPLEX = "Detached Duplex"
    SEMI_DETACHED_DUPLEX = "Semi-Detached Duplex"
    MODERN_DETACHED = "Modern Detached"
    BUNGALOW = "Bungalow"
    APARTMENT = "Apartment"
    TERRACE = "Terrace"
    PENTHOUSE = "Penthouse"

class BathroomType(str, enum.Enum):
    ONE = "1"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE_PLUS = "5+"

class ToiletType(str, enum.Enum):
    ONE = "1"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE_PLUS = "5+"

class ParkingSpaceType(str, enum.Enum):
    ONE = "1"
    TWO = "2"
    THREE = "3"
    FOUR_PLUS = "4+"

class House(Base):
    __tablename__ = "houses"

    id = Column(Integer, primary_key=True, index=True)
    state = Column(String, index=True, nullable=False)
    town = Column(String, index=True, nullable=False)
    price = Column(Float, index=True, nullable=False)
    house_type = Column(Enum(HouseType), index=True, nullable=False)
    bedrooms = Column(Integer, nullable=False)
    bathrooms = Column(Enum(BathroomType), nullable=False)
    toilets = Column(Enum(ToiletType), nullable=False)
    parking_space = Column(Enum(ParkingSpaceType), nullable=False)
    description = Column(String, nullable=True)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
