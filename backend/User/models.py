from pydantic import BaseModel, Field
from typing import List
from ..mixins import MixinId

class _UserBaseModel(BaseModel):
    phone: str
    password: str
    name: str
    surname: str
    registered_event_ids: List[int] = Field(default_factory=list)

class UserModel(_UserBaseModel):
    id: MixinId
