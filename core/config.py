from pydantic_settings import BaseSettings
from typing import ClassVar

class Settings(BaseSettings):
    DATABASE_URL: ClassVar[str]
    JWT_SECRET: ClassVar[str]= "supersecretkey"
    JWT_ALGORITHM: ClassVar[str] = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: ClassVar[int] = 30
    ADMIN_PATH: ClassVar[str] = "/admin" 

    class Config:
        env_file = ".env"
        case_sensitive = True
        extra = "allow"

settings = Settings()