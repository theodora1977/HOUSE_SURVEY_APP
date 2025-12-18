from fastapi import FastAPI
from app.database import engine, Base
from app.routers import houses, auth


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Nigerian Housing API")

# Include routers
app.include_router(auth.router)
app.include_router(houses.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Nigerian Housing API"}
