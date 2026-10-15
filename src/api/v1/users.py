from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse
from services.user_check import check_user
from database.sessions import get_db

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/{id}")
async def get_user(id: int, session: AsyncSession = Depends(get_db)):
    get_user = await check_user(session, id)

    if get_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="user not found"
        )

    return JSONResponse({"user": get_user.dict(), "id": id})


