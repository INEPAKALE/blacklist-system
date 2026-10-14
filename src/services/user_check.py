from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from database.models.users import Users


async def check_user(session: AsyncSession, id: int) -> Users | None:
    result = await session.execute(select(Users).where(Users.id == id))
    return result.scalar_one_or_none()
