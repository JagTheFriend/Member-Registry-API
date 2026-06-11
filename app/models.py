from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date
import uuid


class MemberBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, description="Member's full name")
    email: EmailStr = Field(..., description="Member's email address")
    phone: Optional[str] = Field(None, pattern=r"^\+?1?\d{10,15}$", description="Contact phone number")
    membership_date: date = Field(..., description="Date of membership registration")
    active: bool = Field(default=True, description="Whether the member is currently active")


class MemberCreate(MemberBase):
    pass


class MemberUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    email: Optional[EmailStr] = None
    phone: Optional[str] = Field(None, pattern=r"^\+?1?\d{10,15}$")
    membership_date: Optional[date] = None
    active: Optional[bool] = None


class Member(MemberBase):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), description="Unique member identifier")

    model_config = {"from_attributes": True}


class MemberResponse(Member):
    pass
