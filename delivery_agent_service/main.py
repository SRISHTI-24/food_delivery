from fastapi import FastAPI
from delivery_agent_service.api.endpoints import router as resturant_router
from delivery_agent_service.api.endpoints import router as delivery_router
from delivery_agent_service.database.connection import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"msg": "Delivery_agent Service working"}

app.include_router(delivery_router, prefix="/delivery")