from sqladmin import ModelView
from models.user import User
from models.category import Category
from models.models_base import Phone, Accessory, Headphone


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.email, User.is_active, User.role]
    name = "User"
    name_plural = "Users"
    icon = "fa-solid fa-user"

class CategoryAdmin(ModelView, model=Category):
    column_list = [Category.id, Category.name]
    name = "Category"
    name_plural = "Categories"
    icon = "fa-solid fa-layer-group"


class PhoneAdmin(ModelView, model=Phone):
    column_list = [Phone.id , Phone.name, Phone.description, Phone.price, Phone.category_id]
    name = "Phone"
    name_plural = "Phones"
    icon = "fa-solid fa-mobile"


class HeadphoneAdmin(ModelView, model=Headphone):
    column_list = [Headphone.id, Headphone.name, Headphone.price, Headphone.brand, Headphone.description]
    name = "Headphones"
    name_plural = "Headphones"


class AccessoryAdmin(ModelView, model=Accessory):
    column_list = [Accessory.id, Accessory.name, Accessory.brand, Accessory.price]





