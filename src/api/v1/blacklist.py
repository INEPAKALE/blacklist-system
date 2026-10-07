from fastapi import  APIRouter, HTTPException, status, Depends
from database.schemas.schema import UserBase
from services.blacklist import ServiceCheck
from sqlalchemy import select




router = APIRouter(prefix="/blacklist", tags=["blacklist"]) 








@router.get("/{name}", status_code=status.HTTP_200_OK, response_model=list[UserBase])
async def get_name(name: str, service = Depends(ServiceCheck)): 
    service()
    if not name:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User {name} not found",
        )
    return name


