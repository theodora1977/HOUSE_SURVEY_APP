from fastapi import FastAPI
from app.database import engine, Base
from app.routers import houses


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Nigerian Housing API")


app.include_router(houses.router, prefix="/houses", tags=["houses"])

@app.get("/")
def root():
    return {"message": "Welcome to the Nigerian Housing API"}
