from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship
from user_service.database.connection import Base

class Resturant(Base):
    __tablename__ = "resturant"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    open_hour = Column(Integer)
    close_hour = Column(Integer)
    rating = Column(Float)
    is_open = Column(Boolean, default=False)

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    resturant_id = Column(Integer, ForeignKey("resturant.id"))
    items = Column(String)  # JSON string
    address = Column(String, nullable=False)
    status = Column(String, default="pending")
    resturant = relationship("Resturant", backref="orders")

class Rating(Base):
    __tablename__ = "ratings"
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer)
    resturant_rating = Column(Integer)
    agent_rating = Column(Integer)
    comments = Column(String)
