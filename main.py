from fastapi import FastAPI
from api.phones import router as phones_router
from api.categories import router as category_router
from api import auth
from api.authenticate import auth_router
from sqladmin import Admin
from db.session import engine
from admin.resources import UserAdmin
from admin.admin_views import PhoneAdmin, UserAdmin, CategoryAdmin, HeadphoneAdmin, AccessoryAdmin
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
from starlette.responses import RedirectResponse
from core.config import settings

class AdminAuth(AuthenticationBackend):
    def __init__(self, secret_key: str):
        super().__init__(secret_key=secret_key)

    async def login(self, request: Request) -> bool:
        form = await request.form()
        if form.get("username") == "admin" and form.get("password") == "secret":
            request.session.update({"token": "authenticated"})
            return True
        return False

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request):
        return request.session.get("token") == "authenticated"


app = FastAPI(title="MARKETPLACE")

#ПОДКЛЮЧАЕМ РОУТЫ СЮДА
app.include_router(auth.router, prefix="", tags=["Auth"])
app.include_router(auth_router, tags = ["Auth"])
app.include_router(phones_router, tags = ["Phones"])
app.include_router(category_router, tags = ["Categories"])


auth_backend = AdminAuth(secret_key=settings.JWT_SECRET)
admin = Admin(app, engine, authentication_backend=auth_backend)
admin.add_view(UserAdmin)
admin.add_view(CategoryAdmin)
admin.add_view(PhoneAdmin)
admin.add_view(HeadphoneAdmin)
admin.add_view(AccessoryAdmin)
