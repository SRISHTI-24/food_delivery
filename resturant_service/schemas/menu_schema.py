from pydantic import BaseModel
from typing import Optional

class MenuItemCreate(BaseModel):
    name: str
    price: float
    resturant_id: int

class MenuItemUpdate(BaseModel):
    name: Optional[str]
    price: Optional[float]
    available: Optional[bool]

class MenuItemOut(BaseModel):
    id: int
    name: str
    price: float
    available: bool
    resturant_id: int  # This must be included

    class Config:
        orm_mode = True
