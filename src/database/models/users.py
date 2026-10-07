from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean
from base import Base


class users(Base):
    __tablename__ = "Users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(254), unique=True)
    password_hash: Mapped[str] = mapped_column(String(255))
    is_active: Mapped[bool] = mapped_column(Boolean, default=False)
    login: Mapped[str] = mapped_column(String(30), unique=True)
