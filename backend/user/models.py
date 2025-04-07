from pydantic import BaseModel, Field, ValidationError, validator
from typing import Annotated, List, TypeAlias
from uuid import UUID
from uuid import uuid4

# Type alias for EntryId
EntryId: TypeAlias = Annotated[str, UUID.hex]

# Mixins
class MixinId(BaseModel):
    id: EntryId = Field(default_factory=lambda: EntryId(uuid4()))

# User Models
class _UserBaseModel(BaseModel):
    phone: str = Field(..., pattern=r'^\+?1?\d{9,15}$')  # Phone number validation
    password: str
    name: str
    surname: str
    registered_event_ids: List[int] = Field(default_factory=list)

    @validator('password')
    def validate_password(cls, v):
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters long')
        return v

    @validator('phone')
    def validate_phone(cls, v):
        if not v:
            raise ValueError('Phone number is required')
        return v

    @validator('name', 'surname')
    def validate_name_and_surname(cls, v):
        if not v.isalpha():
            raise ValueError('Name and surname must contain only letters')
        return v

class UserModel(_UserBaseModel, MixinId):
    pass