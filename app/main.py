from fastapi import FastAPI
from app import models, schema
from app.database import engine
from app.routers import houses, auth

app = FastAPI()

# Include the routers from other files
app.include_router(houses.router)
app.include_router(auth.router)

@app.get("/")
def read_root():
    return {"message": "House Survey API is running"}