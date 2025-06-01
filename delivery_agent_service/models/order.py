# delivery_agent_service/models.py
from sqlalchemy import Column, Integer, String, Enum
from delivery_agent_service.database.connection import Base
import enum

class OrderStatusEnum(str, enum.Enum):
    pending = "pending"
    accepted = "accepted"
    picked_up = "picked_up"
    delivered = "delivered"

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    delivery_agent_id = Column(Integer)
    status = Column(Enum(OrderStatusEnum), default="pending")
