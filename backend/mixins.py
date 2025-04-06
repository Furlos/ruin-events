from datetime import datetime
from uuid import uuid4

from pydantic import BaseModel, Field

from typing import Annotated, TypeAlias
from uuid import UUID


EntryId: TypeAlias = Annotated[str, UUID.hex]

class MixinId(BaseModel):
    id: EntryId = Field(default_factory=lambda: EntryId(uuid4()))


class MixinStartEndTime(BaseModel):
    start_at: datetime
    end_at: datetime
