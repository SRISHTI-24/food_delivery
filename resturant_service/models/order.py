import enum
from typing import List
from pydantic import BaseModel
from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from resturant_service.database.connection import Base


class AvailabilityStatus(enum.Enum):
    ONLINE = "online"
    OFFLINE = "offline"
    
class Resturant(Base):
    __tablename__ = "resturants"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    open_hour = Column(Integer)  # 0-23
    close_hour = Column(Integer)  # 0-23
    rating = Column(Float, default=0.0)
    is_online = Column(Boolean, default=True)

    menu_items = relationship("MenuItem", back_populates="resturant")
    orders = relationship("Order", back_populates="resturant")


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    resturant_id = Column(Integer, ForeignKey("resturants.id"))
    delivery_agent_id = Column(Integer, ForeignKey("delivery_agents.id"))
    items = Column(String)
    address = Column(String)
    status = Column(String, default="pending")  # new field for status

    resturant = relationship("Resturant", back_populates="orders")
    delivery_agent = relationship("DeliveryAgent", back_populates="orders")

class DeliveryAgent(Base):
    __tablename__ = "delivery_agents"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    is_available = Column(Boolean, default=True)

    orders = relationship("Order", back_populates="delivery_agent")