from pydantic import BaseModel, Field
from typing import List
from ..mixins import MixinId, MixinStartEndTime

class _EventBaseModel(BaseModel, MixinStartEndTime):
    name: str
    description: str
    location: str
    price: int

class EventModel(_EventBaseModel):
    id: MixinId
