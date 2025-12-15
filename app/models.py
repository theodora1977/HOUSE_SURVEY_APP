from sqlalchemy import Column, Integer, String, Float
from .database import Base

class House(Base):
    __tablename__ = "houses"

    id = Column(Integer, primary_key=True, index=True)
    location = Column(String, index=True, nullable=False)
    price = Column(String, index=True, nullable=False)
    house_type = Column(String, index=True, nullable=False)
    bedrooms = Column(Integer, nullable=True)
    bathrooms = Column(Integer, nullable=True)
    description = Column(String, nullable=True)



