from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from schemas.phones import PhoneCreate, PhoneRead
from repositories.phone import create_phone, get_all_phones, delete_phone
from dependencies.roles import require_admin
from models.user import User

router = APIRouter(prefix="/phones")

@router.post("/", response_model=PhoneRead)
def create(phone_data: PhoneCreate, db: Session = Depends(get_db),
           user: User = Depends(require_admin)): #ПРоверка require admin чтобы телефоны мог добавлять только администратор
    return create_phone(db, phone_data)

@router.get("/", response_model=list[PhoneRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_phones(db)

@router.delete("/{phone_id}", response_model=PhoneRead)
def delete_phone_route(
    phone_id: int,
    db: Session = 
    Depends(get_db),
    user: User = Depends(require_admin) #ТОЛЬКО АДМИН УДАЛЯЕТ 
):
    deleted = delete_phone(db, phone_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Phone not found")
    return deleted

