from pydantic import BaseModel, Field, EmailStr
from datetime import date, timedelta


class UserLogin(BaseModel):
    login: str = Field(..., min_length=3, max_length=16)
    password: str = Field(..., min_length=12, max_length=255)


class UserBase(BaseModel):
    username: str = Field(..., min_length=2, max_length=50)
    email: EmailStr = Field(..., max_length=2, max_length=254)


class UserCreate(UserBase):
    password: str = Field(..., min_length=12, max_length=30)


class UserResponse(UserBase):
    id: int
    is_active: bool


class BlacklistedUser(UserBase):
    id: int
    blocked_at: date
    reason: str | None = Field(max_length=250)
    blocking_time: timedelta = Field(
        ..., description="Duration for which the user is blocked", examples=["5 years"]
    )
