from sqlalchemy.orm import Session
from models.phone import Phone
from schemas.phones import PhoneCreate

def create_phone(db: Session, phone_data: PhoneCreate) -> Phone:
    phone = Phone(**phone_data.dict())
    db.add(phone)
    db.commit()
    db.refresh(phone)
    return phone

def get_all_phones(db: Session):
    return db.query(Phone).all()

def delete_phone(db:Session, phone_id: int):
    phone = db.query(Phone).filter(Phone.id==phone_id).first()
    if not phone:
        return None
    db.delete(phone)
    db.commit()
    return phone
