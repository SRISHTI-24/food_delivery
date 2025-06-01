from enum import Enum
from typing import List
from pydantic import BaseModel

from resturant_service.schemas.menu_schema import MenuItemOut


class ResturantCreate(BaseModel):
    name: str
    open_hour: int
    close_hour: int
    is_open: bool


class ResturantOut(BaseModel):
    name: str
    is_online: bool
    menu_items: List[MenuItemOut]

    class Config:
        orm_mode = True

class OrderOut(BaseModel):
    id: int
    user_id: int
    resturant_id: int
    items: str
    address: str
    status: str

    class Config:
        from_attributes = True 

class OrderStatusEnum(str, Enum):
    pending = "pending"
    accepted = "accepted"
    rejected = "rejected"
    picked_up = "picked_up"
    delivered = "delivered"

class StatusUpdate(BaseModel):
    status: str