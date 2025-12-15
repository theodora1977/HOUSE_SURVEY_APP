import csv
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.models import Base, House
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")  # Example: postgresql://user:pass@localhost:5432/housing_db

# Create database engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

# Path to CSV
CSV_FILE = "data/nigerian_houses.csv"

# Helper functions for numeric conversion
def parse_float(value):
    try:
        return float(value)
    except:
        return None

def parse_int(value):
    try:
        return int(value)
    except:
        return None

# Seed database
with open(CSV_FILE, newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    count = 0
    for row in reader:
        house = House(
            location=row.get("location", "").strip(),
            price=parse_float(row.get("price", 0)),
            house_type=row.get("house_type", "Unknown").strip(),
            bedrooms=parse_int(row.get("bedrooms", 0)),
            bathrooms=parse_int(row.get("bathrooms", 0)),
            description=row.get("description", "").strip()
        )
        db.add(house)
        count += 1
    db.commit()

print(f"Seeded {count} houses into the database.")
db.close()
