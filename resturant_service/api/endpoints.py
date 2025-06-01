import json
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from resturant_service.crud import order_crud, menu_crud
from resturant_service.database.connection import get_db
from resturant_service.models.order import DeliveryAgent, Resturant
from resturant_service.schemas.order_schema import OrderOut, StatusUpdate
from resturant_service.crud.order_crud import assign_delivery_agent, get_pending_orders
from resturant_service.models.order import Order
from user_service.schemas.user_schemas import OrderCreate
from resturant_service.schemas import menu_schema, order_schema

router = APIRouter()

# View pending orders
@router.get("/orders/pending", response_model=list[order_schema.OrderOut])
def get_pending_orders(db: Session = Depends(get_db)):
    return order_crud.get_pending_orders(db)

# Accept or reject order

@router.get("/available")
def get_available_resturants(hour: int = Query(..., ge=0, le=23), db: Session = Depends(get_db)):
    resturants = db.query(Resturant).filter(
        Resturant.open_hour <= hour,
        Resturant.close_hour >= hour,
        Resturant.is_online == True
    ).all()
    
    if not resturants:
        raise HTTPException(status_code=404, detail="No resturants available at this hour.")
    
    return resturants

@router.post("/")
def place_order(order: OrderCreate, db: Session = Depends(get_db)):
    # Convert items list to JSON string
    items_json = json.dumps([item.dict() for item in order.items])

    new_order = Order(
        user_id=order.user_id,
        restaurant_id=order.restaurant_id,
        items=items_json,
        address=order.address,
        status="pending"
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return {"message": "Order placed", "order_id": new_order.id}

@router.get("/pending", response_model=list[OrderOut])
def list_pending_orders(db: Session = Depends(get_db)):
    return get_pending_orders(db)


#accept
@router.post("/orders/{order_id}/accept")
def accept_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    order.status = "accepted"
    
    # Assign delivery agent (pseudo logic or microservice call)
    try:
        assign_delivery_agent(order, db)
    except HTTPException as e:
        order.status = "pending"  # roll back to pending if no agent
        db.commit()
        raise e
    
    db.commit()
    return {"message": f"Order accepted and assigned to delivery agent {order.delivery_agent_id}"}



# reject
@router.post("/orders/{order_id}/reject")
def reject_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    order.status = "rejected"
    db.commit()
    return {"message": "Order rejected"}

#update status by delivery agent
@router.put("/orders/{order_id}/status", response_model=OrderOut)
def update_order_status(order_id: int, status_update: StatusUpdate, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    
    order.status = status_update.status
    db.commit()
    db.refresh(order)
    return order

# free delivery agent
def release_delivery_agent(agent_id: int, db: Session):
    agent = db.query(DeliveryAgent).filter(DeliveryAgent.id == agent_id).first()
    if agent:
        agent.is_available = True
        db.commit()

# CRUD for menu items
@router.post("/menu", response_model=menu_schema.MenuItemOut)
def create_menu_item(item: menu_schema.MenuItemCreate, db: Session = Depends(get_db)):
    return menu_crud.create_menu_item(db, item)

@router.get("/menu/{resturant_id}", response_model=list[menu_schema.MenuItemOut])
def get_menu_by_resturant(resturant_id: int, db: Session = Depends(get_db)):
    return menu_crud.get_menu_by_resturant(db, resturant_id)

@router.put("/menu/{resturant_id}/{item_id}", response_model=menu_schema.MenuItemOut)
def update_menu_item(item_id: int, item_update: menu_schema.MenuItemUpdate, db: Session = Depends(get_db)):
    updated = menu_crud.update_menu_item(db, item_id, item_update)
    if not updated:
        raise HTTPException(status_code=404, detail="Menu item not found")
    return updated

@router.delete("/menu/{item_id}")
def delete_menu_item(item_id: int, db: Session = Depends(get_db)):
    if not menu_crud.delete_menu_item(db, item_id):
        raise HTTPException(status_code=404, detail="Menu item not found")
    return {"message": "Menu item deleted successfully"}




