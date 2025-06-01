# delivery_agent_service/schemas.py
from pydantic import BaseModel
from enum import Enum

class OrderStatusEnum(str, Enum):
    pending = "pending"
    accepted = "accepted"
    rejected = "rejected"
    picked_up = "picked_up"
    delivered = "delivered"

class StatusUpdate(BaseModel):
    order_id: int
    status: OrderStatusEnum
