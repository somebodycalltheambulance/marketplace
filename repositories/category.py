from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models.category import Category
from schemas.category import CategoryCreate

async def create_category(db: AsyncSession, category_data: CategoryCreate) -> Category:
    category = Category(**category_data.dict())
    db.add(category)
    await db.commit()
    await db.refresh(category)
    return category

# Асинхронное получение всех категорий
async def get_all_categories(db: AsyncSession):
    result = await db.execute(select(Category))
    return result.scalars().all()