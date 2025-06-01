import json
from user_service.models import Order

def create_order(db, order_data):
    items_json = json.dumps([item.dict() for item in order_data.items])
    new_order = Order(
        user_id=order_data.user_id,
        resturant_id=order_data.resturant_id,
        items=items_json,
        address=order_data.delivery_address,
        status="pending"
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order
