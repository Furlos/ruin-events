from datetime import datetime
from uuid import uuid4
from pydantic import BaseModel, Field
from typing import Annotated, TypeAlias
from uuid import UUID

# Type alias for EntryId
EntryId: TypeAlias = Annotated[str, UUID.hex]

# Mixins
class MixinId(BaseModel):
    id: EntryId = Field(default_factory=lambda: EntryId(uuid4()))

class MixinStartEndTime:
    start_at: datetime
    end_at: datetime

# Event Models
class _EventBaseModel(BaseModel, MixinStartEndTime):
    name: str
    description: str
    location: str
    price: int

class EventModel(_EventBaseModel, MixinId):
    pass