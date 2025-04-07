from fastapi import APIRouter, HTTPException
from Events.services import EventService

router = APIRouter()

@router.get("/events/sort/price")
def sort_events_by_price_endpoint():
    result = EventService().sort_events_by_price()
    if result["status"] == "error":
        raise HTTPException(status_code=400, detail=result["message"])
    return result

@router.get("/events/sort/datetime")
def sort_events_by_datetime_endpoint():
    result = EventService().sort_events_by_datetime()
    if result["status"] == "error":
        raise HTTPException(status_code=400, detail=result["message"])
    return result

@router.put("/events/{event_id}")
def update_event_endpoint(event_id: str, update_data: dict):
    result = EventService().update_event(event_id, update_data)
    if result["status"] == "error":
        if result["message"] == "Event not found":
            raise HTTPException(status_code=404, detail=result["message"])
        raise HTTPException(status_code=400, detail=result["message"])
    return result

@router.delete("/events/{event_id}")
def delete_event_endpoint(event_id: str):
    result = EventService().delete_event(event_id)
    if result["status"] == "error":
        if result["message"] == "Event not found":
            raise HTTPException(status_code=404, detail=result["message"])
    return result