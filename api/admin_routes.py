from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from db.session import get_async_session
from schemas.product_create import ProductCreateUnion
from models.models_base import Phone, Headphone, Accessory
from dependencies.auth import get_current_admin_user  # зависит от твоей реализации

router = APIRouter(prefix="/admin/products", tags=["Admin Products"])

@router.post("/", status_code=201)
async def create_product(
    product: ProductCreateUnion,
    session: AsyncSession = Depends(get_async_session),
    user=Depends(get_current_admin_user)
):
    if not user.is_superuser:
        raise HTTPException(status_code=403, detail="Not authorized")

    if product.type == "phone":
        db_obj = Phone(**product.dict(exclude={"type"}))
    elif product.type == "headphone":
        db_obj = Headphone(**product.dict(exclude={"type"}))
    elif product.type == "accessory":
        db_obj = Accessory(**product.dict(exclude={"type"}))
    else:
        raise HTTPException(status_code=400, detail="Invalid product type")

    session.add(db_obj)
    await session.commit()
    await session.refresh(db_obj)
    return {"id": db_obj.id, "message": "Product created successfully"}
