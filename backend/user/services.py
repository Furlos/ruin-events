from pydantic import ValidationError
from User.models import UserModel
from db import get_db

db = get_db()
user_collection = db["user"]
event_collection = db["event"]

class UserService:
    def __init__(self, db):
        self.user_collection = db["user"]

    def create_user(self, user_data: dict):
        try:
            user = UserModel(**user_data)
            self.user_collection.insert_one(user.dict())
            # Retrieve the newly created user to verify
            return self.search_by_phone(user.phone)
        except ValidationError as e:
            return {"status": "error", "message": str(e)}

    def update_user(self, user_id: str, update_data: dict):
        try:
            user = self.user_collection.find_one({"id": user_id})
            if not user:
                return {"status": "error", "message": "User not found"}

            for key, value in update_data.items():
                user[key] = value

            UserModel(**user)  # Validate updated user model
            self.user_collection.update_one({"id": user_id}, {"$set": update_data})
            return {"status": "success", "message": "User updated successfully"}
        except ValidationError as e:
            return {"status": "error", "message": str(e)}

    def delete_user(self, user_id: str):
        user = self.user_collection.find_one({"id": user_id})
        if not user:
            return {"status": "error", "message": "User not found"}

        self.user_collection.delete_one({"id": user_id})
        return {"status": "success", "message": "User deleted successfully"}

    def get_events(self, user_id: str):
        user = self.user_collection.find_one({"id": user_id})
        if not user:
            return {"status": "error", "message": "User not found"}

        event_ids = user.get("registered_event_ids", [])
        events = event_collection.find({"id": {"$in": event_ids}})
        return {"status": "success", "events": list(events)}

    def search_by_phone(self, phone: str):
        user = self.user_collection.find_one({"phone": phone})
        if not user:
            return {"status": "error", "message": "User not found"}
        return {"status": "success", "user": user}