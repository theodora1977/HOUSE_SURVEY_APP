import csv
import os
from app.database import SessionLocal, engine
from app.models import Base, House, HouseType, BathroomType, ToiletType, ParkingSpaceType

# Database setup using the configuration from app.database
db = SessionLocal()

Base.metadata.create_all(bind=engine)

# Path to CSV
CSV_FILE = "data/house_data.csv"

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
        # We use .get() with defaults to avoid errors if columns are missing in CSV
        house = House(
            state=row.get("state", "").strip(),
            town=row.get("town", "").strip(),
            # Ensure these match your Enum values exactly (e.g., "Duplex")
            house_type=row.get("house_type", "Duplex").strip(),
            bedrooms=parse_int(row.get("bedrooms", 0)),
            # For Enums, we pass the string value (e.g., "1", "2", "5+")
            bathrooms=row.get("bathrooms", "1").strip(),
            toilets=row.get("toilets", "1").strip(),
            parking_space=row.get("parking_space", "1").strip(),
            price=parse_float(row.get("price", 0))
        )
        db.add(house)
        count += 1
    db.commit()

print(f"Seeded {count} houses into the database.")
db.close()
