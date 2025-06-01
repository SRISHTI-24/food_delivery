from sqlalchemy.orm import Session
from resturant_service.models.menu import MenuItem
from resturant_service.schemas.menu_schema import MenuItemCreate, MenuItemUpdate

def create_menu_item(db: Session, item: MenuItemCreate):
    new_item = MenuItem(**item.dict())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

def get_menu_by_resturant(db: Session, resturant_id: int):
    return db.query(MenuItem).filter(MenuItem.resturant_id == resturant_id).all()

def update_menu_item(db: Session, item_id: int, item_update: MenuItemUpdate):
    item = db.query(MenuItem).filter(MenuItem.id == item_id).first()
    if not item:
        return None
    for key, value in item_update.dict(exclude_unset=True).items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item

def delete_menu_item(db: Session, item_id: int):
    item = db.query(MenuItem).filter(MenuItem.id == item_id).first()
    if not item:
        return None
    db.delete(item)
    db.commit()
    return item
