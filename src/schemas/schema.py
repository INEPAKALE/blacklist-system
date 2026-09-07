from pydantic import BaseModel, Field, EmailStr
from datetime import date, timedelta



class UserLogin(BaseModel):
    login: str = Field(..., min_length=3, max_length=16)
    password: str = Field(..., min_length=12, max_length=30)

class UserBase(BaseModel):
    username: str = Field(..., min_length=2, max_length=50)
    email: EmailStr


class UserCreate(UserBase):
    password: str = Field(..., min_length=12, max_length=30)

class UserResponse(UserBase):
    id: int
    is_active: bool

class BlacklistedUser(UserBase):
    Id: int
    blocked_at: date
    Reason: str | None = Field(max_length=250)
    Blocking_time: timedelta = Field(..., description="Duration for which the user is blocked", examples=["5 years"])