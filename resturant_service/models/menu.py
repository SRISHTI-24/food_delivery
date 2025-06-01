from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from resturant_service.database.connection import Base

class MenuItem(Base):
    __tablename__ = "menu_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    available = Column(Boolean, default=True)
    resturant_id = Column(Integer, ForeignKey("resturants.id"))

    resturant = relationship("Resturant", back_populates="menu_items")
