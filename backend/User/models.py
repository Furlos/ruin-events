from pydantic import BaseModel, Field
from typing import List

class User(BaseModel):
    id: int
    phone: str
    password: str
    name: str
    surname: str
    registered_event_ids: List[int] = Field(default_factory=list)
