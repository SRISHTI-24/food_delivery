from pydantic import BaseModel
from typing import List, Optional

class ResturantOut(BaseModel):
    id: int
    name: str
    rating: float
    is_open: bool

    class Config:
        orm_mode = True

class OrderItem(BaseModel):
    item_id: int
    name: str
    quantity: int

class OrderCreate(BaseModel):
    user_id: int
    resturant_id: int
    items: List[OrderItem]
    delivery_address: str

class OrderResponse(BaseModel):
    order_id: int
    status: str

class RatingCreate(BaseModel):
    order_id: int
    resturant_rating: int
    agent_rating: Optional[int] = None
    comments: Optional[str] = ""
