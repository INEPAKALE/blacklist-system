from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession
from database.models.users import Users


async def del_user(session: AsyncSession, id: int) -> Users | None:
    result = await session.execute(delete(Users).where(Users.id == id))
    return result.scalar_one_or_none()
