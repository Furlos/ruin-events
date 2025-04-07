import pymongo
from pydantic import ValidationError
from Events.models import EventModel
from db import get_db

db = get_db()
user_collection = db["user"]
event_collection = db["event"]

class EventService:
    def __init__(self, db):
        self.event_collection = db["event"]

    def get_events(self, user_id: str):
        user = user_collection.find_one({"id": user_id})
        if not user:
            return {"status": "error", "message": "User not found"}

        event_ids = user.get("registered_event_ids", [])
        events = self.event_collection.find({"id": {"$in": event_ids}})
        return {"status": "success", "events": list(events)}

    def sort_events_by_price(self):
        events = self.event_collection.find().sort("price", pymongo.ASCENDING)
        return {"status": "success", "events": list(events)}

    def sort_events_by_datetime(self):
        events = self.event_collection.find().sort("start_at", pymongo.ASCENDING)
        return {"status": "success", "events": list(events)}

    def update_event(self, event_id: str, update_data: dict):
        try:
            event = self.event_collection.find_one({"id": event_id})
            if not event:
                return {"status": "error", "message": "Event not found"}

            for key, value in update_data.items():
                event[key] = value

            EventModel(**event)  # Validate updated event model
            self.event_collection.update_one({"id": event_id}, {"$set": update_data})
            return {"status": "success", "message": "Event updated successfully"}
        except ValidationError as e:
            return {"status": "error", "message": str(e)}

    def delete_event(self, event_id: str):
        event = self.event_collection.find_one({"id": event_id})
        if not event:
            return {"status": "error", "message": "Event not found"}

        self.event_collection.delete_one({"id": event_id})
        return {"status": "success", "message": "Event deleted successfully"}