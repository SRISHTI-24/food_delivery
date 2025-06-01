import random
from fastapi import HTTPException
from sqlalchemy.orm import Session
from resturant_service.models import order
from resturant_service.models.order import DeliveryAgent, Order, Resturant

def assign_delivery_agent(order: Order,db: Session) -> int:
    agent = db.query(DeliveryAgent).filter(DeliveryAgent.is_available == True).first()
    if not agent:
        raise HTTPException(status_code=503, detail="No delivery agents available")

    order.delivery_agent_id = agent.id
    agent.is_available = False  # mark agent as unavailable
    db.commit()

def get_pending_orders(db: Session):
    return db.query(Order).filter(Order.status == "pending").all()

def update_order_status(db: Session, order_id: int, new_status: str):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        return None
    order.status = new_status
    db.commit()
    db.refresh(order)
    return order

def update_restaurant_status(db: Session, resturant_id: int, is_online: bool):
    rest = db.query(Resturant).filter(Resturant.id == resturant_id).first()
    if not rest:
        return None
    rest.is_online = is_online
    db.commit()
    db.refresh(rest)
    return rest

