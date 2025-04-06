from pydantic import ValidationError
from models import UserModel
from backend.db import user_collection, event_collection

def create_user(user_data: dict):
    try:
        user = UserModel(**user_data)
        user_collection.insert_one(user.dict())
        return {"status": "success", "message": "User created successfully"}
    except ValidationError as e:
        return {"status": "error", "message": str(e)}

def update_user(user_id: str, update_data: dict):
    try:
        user = user_collection.find_one({"id": user_id})
        if not user:
            return {"status": "error", "message": "User not found"}

        for key, value in update_data.items():
            user[key] = value

        UserModel(**user)  # Validate updated user model
        user_collection.update_one({"id": user_id}, {"$set": update_data})
        return {"status": "success", "message": "User updated successfully"}
    except ValidationError as e:
        return {"status": "error", "message": str(e)}

def get_events(user_id: str):
    user = user_collection.find_one({"id": user_id})
    if not user:
        return {"status": "error", "message": "User not found"}

    event_ids = user.get("registered_event_ids", [])
    events = event_collection.find({"id": {"$in": event_ids}})
    return {"status": "success", "events": list(events)}

def delete_user(user_id: str):
    user = user_collection.find_one({"id": user_id})
    if not user:
        return {"status": "error", "message": "User not found"}

    user_collection.delete_one({"id": user_id})
    return {"status": "success", "message": "User deleted successfully"}