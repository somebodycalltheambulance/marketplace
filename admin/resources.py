from sqladmin import ModelView
from models.user import User


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.username, User.email]
    form_columns = [User.username, User.email, User.hashed_password]

    