from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean, ForeignKey, Date, Interval
from base import Base
from datetime import date, timedelta
from users import Users

manager: Mapped["Users"] = relationship(back_populates="users")


class BlockedUsers(Base):
    __tablename__ = "blacklist"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"), primary_key=True, unique=True
    )
    username: Mapped[str] = mapped_column(ForeignKey("users.username"), String(50))
    user: Mapped["Users"] = relationship(back_populates="block")
    blocked_at: Mapped[date] = mapped_column(Date, index=True)
    reason: Mapped[str | None] = mapped_column(String(250))
    blocking_time: Mapped[timedelta] = mapped_column(
        Interval, default=timedelta(days=7)
    )
