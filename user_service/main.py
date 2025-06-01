from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from user_service.api.endpoints import router as user_router
from user_service.database.connection import Base, engine
from fastapi.middleware.cors import CORSMiddleware
import os

# Create tables
from user_service.models import Base
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Allow frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Register API routes first
app.include_router(user_router, prefix="/api/user", tags=["User Service"])

# ✅ Then mount frontend folder
frontend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "frontend"))
app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend")

@app.get("/")
def read_root():
    return {"msg": "User Service working"}
