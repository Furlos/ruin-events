from fastapi import APIRouter, HTTPException, Query
from .models import _UserBaseModel
from .services import UserService

router = APIRouter()

@router.post("/users/")
def create_user_endpoint(user_data: _UserBaseModel):
    result = UserService().create_user(user_data.dict())
    if result["status"] == "error":
        raise HTTPException(status_code=400, detail=result["message"])
    return result

@router.put("/users/{user_id}")
def update_user_endpoint(user_id: str, update_data: dict):
    result = UserService().update_user(user_id, update_data)
    if result["status"] == "error":
        if result["message"] == "User not found":
            raise HTTPException(status_code=404, detail=result["message"])
        raise HTTPException(status_code=400, detail=result["message"])
    return result

@router.get("/users/{user_id}/events/")
def get_events_endpoint(user_id: str):
    result = UserService().get_events(user_id)
    if result["status"] == "error":
        if result["message"] == "User not found":
            raise HTTPException(status_code=404, detail=result["message"])
    return result

@router.get("/users/search/")
def search_user_by_phone(phone: str = Query(..., pattern=r'^\+?1?\d{9,15}$')):
    result = UserService().search_by_phone(phone)
    if result["status"] == "error":
        raise HTTPException(status_code=404, detail=result["message"])
    return result

@router.delete("/users/{user_id}")
def delete_user_endpoint(user_id: str):
    result = UserService().delete_user(user_id)
    if result["status"] == "error":
        if result["message"] == "User not found":
            raise HTTPException(status_code=404, detail=result["message"])
    return result