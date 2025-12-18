from sqlalchemy import Column, Integer, String, Float, Boolean
from app.database import Base

class House(Base):
    __tablename__ = "houses"

    id = Column(Integer, primary_key=True, index=True)
    state = Column(String, index=True, nullable=False)
    town = Column(String, index=True, nullable=False)
    price = Column(Float, index=True, nullable=False)
    house_type = Column(String, index=True, nullable=False)
    bedrooms = Column(Integer, nullable=True)
    bathrooms = Column(Integer, nullable=True)
    description = Column(String, nullable=True)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
