from fastapi import FastAPI
from api.phones import router as phones_router
from api.categories import router as category_router
from api import auth
from api.authenticate import auth_router


app = FastAPI(title="MARKETPLACE")

#ПОДКЛЮЧАЕМ РОУТЫ СЮДА
app.include_router(auth.router, prefix="", tags=["Auth"])
app.include_router(auth_router, tags = ["Auth"])
app.include_router(phones_router, tags = ["Phones"])
app.include_router(category_router, tags = ["Categories"])
