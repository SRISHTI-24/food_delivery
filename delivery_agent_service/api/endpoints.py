# delivery_agent_service/api/endpoints.py
from fastapi import APIRouter, Body, HTTPException
import requests
from delivery_agent_service.schemas import StatusUpdate as Deliver_status_update

router = APIRouter()

@router.put("/update-status")
def update_delivery_status(payload: Deliver_status_update):
    try:
        response = requests.put(
            f"http://localhost:8000/resturants/orders/{payload.order_id}/status",
            json={"status": payload.status}
        )
        response.raise_for_status()
        return {"message": "Status updated"}
    except Exception as e:
        print("ERROR:", str(e), response.text)
        raise HTTPException(status_code=500, detail="Order not found, Failed to update status")