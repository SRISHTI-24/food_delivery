from fastapi import FastAPI
from resturant_service.api.endpoints import router as order_router
from resturant_service.api.endpoints import router as resturant_router
from resturant_service.database.connection import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"msg": "Resturant Service working"}

app.include_router(resturant_router, prefix="/resturants")