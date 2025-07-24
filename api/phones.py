from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from db.session import get_async_session
from schemas.phones import PhoneCreate, PhoneRead
from repositories.phone import create_phone, get_all_phones, delete_phone
from dependencies.roles import require_admin
from models.user import User

router = APIRouter(prefix="/phones")

@router.post("/", response_model=PhoneRead)
async def create(
    phone_data: PhoneCreate,
    db: AsyncSession = Depends(get_async_session),
    user: User = Depends(require_admin)
):
    return await create_phone(db, phone_data)

@router.get("/", response_model=list[PhoneRead])
async def read_all(db: AsyncSession = Depends(get_async_session)):
    return await get_all_phones(db)

@router.delete("/{phone_id}", response_model=PhoneRead)
async def delete_phone_route(
    phone_id: int,
    db: AsyncSession = Depends(get_async_session),
    user: User = Depends(require_admin)
):
    deleted = await delete_phone(db, phone_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Phone not found")
    return deleted
