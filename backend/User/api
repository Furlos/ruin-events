from datetime import datetime
from uuid import uuid4
from pydantic import BaseModel, Field, ValidationError
from typing import Annotated, List, TypeAlias
from uuid import UUID
import pymongo
from fastapi import FastAPI, HTTPException

# Type alias for EntryId
EntryId: TypeAlias = Annotated[str, UUID.hex]

# Mixins
class MixinId(BaseModel):
    id: EntryId = Field(default_factory=lambda: EntryId(uuid4()))

class MixinStartEndTime(BaseModel):
    start_at: datetime
    end_at: datetime

# User Models
class _UserBaseModel(BaseModel):
    phone: str
    password: str
    name: str
    surname: str
    registered_event_ids: List[int] = Field(default_factory=list)

class UserModel(_UserBaseModel, MixinId):
    pass

# Set up the database connection
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
user_collection = db["user"]
event_collection = db["event"]

# CRUD operations
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

# FastAPI application
app = FastAPI()

@app.post("/users/")
def create_user_endpoint(user_data: _UserBaseModel):
    try:
        user = UserModel(**user_data.dict())
        user_collection.insert_one(user.dict())
        return {"status": "success", "message": "User created successfully"}
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.put("/users/{user_id}")
def update_user_endpoint(user_id: str, update_data: dict):
    try:
        user = user_collection.find_one({"id": user_id})
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        for key, value in update_data.items():
            user[key] = value

        UserModel(**user)  # Validate updated user model
        user_collection.update_one({"id": user_id}, {"$set": update_data})
        return {"status": "success", "message": "User updated successfully"}
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/users/{user_id}/events/")
def get_events_endpoint(user_id: str):
    user = user_collection.find_one({"id": user_id})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    event_ids = user.get("registered_event_ids", [])
    events = event_collection.find({"id": {"$in": event_ids}})
    return {"status": "success", "events": list(events)}

@app.delete("/users/{user_id}")
def delete_user_endpoint(user_id: str):
    user = user_collection.find_one({"id": user_id})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user_collection.delete_one({"id": user_id})
    return {"status": "success", "message": "User deleted successfully"}
