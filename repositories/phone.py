from sqlalchemy.orm import Session
from models.models_base import Phone
from schemas.phones import PhoneCreate
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


# Создание телефона
async def create_phone(db: AsyncSession, phone_data: PhoneCreate) -> Phone:
    phone = Phone(**phone_data.dict())
    db.add(phone)
    await db.commit()
    await db.refresh(phone)
    return phone

# Получение всех телефонов
async def get_all_phones(db: AsyncSession):
    result = await db.execute(select(Phone))
    return result.scalars().all()

# Удаление телефона
async def delete_phone(db: AsyncSession, phone_id: int):
    result = await db.execute(select(Phone).where(Phone.id == phone_id))
    phone = result.scalars().first()
    if not phone:
        return None
    await db.delete(phone)
    await db.commit()
    return phone