from pydantic import BaseModel, Field
from typing import Literal, Optional


class BaseProductCreate(BaseModel):
    name: str
    brand: Optional[str]
    price: float
    category_id: int
    description: Optional[str]


class PhoneCreate(BaseProductCreate):
    type: Literal["phone"] = "phone"
    ram: Optional[int] = Field(None, description="Оперативная память")
    storage: Optional[int] = Field(None, description="Обьем памяти в ГБ")
    color: Optional[str] = Field(None, description="Цвет устройства")



class HeadphoneCreate(BaseProductCreate):
    type: Literal["headphone"] = "headphone"


class AccessoryCreate(BaseProductCreate):
    type: Literal["accessory"] = "accessory"
    # Например: accessory_type: str


ProductCreateUnion = PhoneCreate | HeadphoneCreate | AccessoryCreate
