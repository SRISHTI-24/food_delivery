from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from user_service.database.connection import get_db
from user_service.schemas.user_schemas import ResturantOut, OrderCreate, OrderResponse, RatingCreate
from user_service.crud.resturant_crud import get_available_resturants, get_available_resturants
from user_service.crud.order_crud import create_order
from user_service.crud.rating_crud import submit_rating
from user_service.schemas.user_schemas import ResturantOut

router = APIRouter()

@router.get("/resturants/available", response_model=list[ResturantOut])
def list_available_resturants(hour: int = Query(..., ge=0, le=23), db: Session = Depends(get_db)):
    result = get_available_resturants(db, hour)
    if not result:
        raise HTTPException(status_code=404, detail="No restaurants available")
    return result

@router.post("/orders", response_model=OrderResponse)
def place_order(order: OrderCreate, db: Session = Depends(get_db)):
    new_order = create_order(db, order)
    return {"order_id": new_order.id, "status": new_order.status}

@router.post("/ratings")
def rate_order(rating: RatingCreate, db: Session = Depends(get_db)):
    return submit_rating(db, rating)
