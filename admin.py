import uvicorn
from fastapi import FastAPI
from fastapi_admin.app import app as admin_app
from fastapi_admin.providers.login import UsernamePasswordProvider
from fastapi_admin.resources import Model
from fastapi_admin import Site
from starlette.requests import Request
from starlette.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncEngine

from core.config import settings
from db.session import engine, async_session_maker
from models.user import User
from models.phone import Phone


settings = settings()

app = FastAPI()

templates = Jinja2Templates(directory="templates")

login_provider = UsernamePasswordProvider(
    admin_model=User,
    login_logo_url="",
)


class UserResource(Model):
    label = "Пользователи"
    model = User


class ProductResource(Model):
    label = "Товары"
    model = Phone


@app.on_event("startup")
async def startup():
    await admin_app.configure(
        logo_url="",
        template_folders=["templates"],
        providers=[login_provider],
        admin_path="/admin",
        engine=engine,
        session_maker=async_session_maker,
        resources=[
            UserResource,
            ProductResource,
        ],
        site=Site(
            name="Techly admin",
        ),
    )
    app.mount("/admin", reload=True)
