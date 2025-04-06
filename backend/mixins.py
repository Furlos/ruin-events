from datetime import datetime
from uuid import uuid4

from pydantic import BaseModel, Field

from src.types import EntryId


class MixinId(BaseModel):
    id: EntryId = Field(default_factory=lambda: EntryId(uuid4()))


class MixinStartEndTime(BaseModel):
    start_at: datetime
    end_at: datetime
