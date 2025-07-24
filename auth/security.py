from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
JWT_SECRET = 'supersecret'
JWT_ALGORITHM = 'HS256'

#ХЕШИРОВАНИЕ ПАРОЛЯ ЕБАНОГО
def hash_password(password:str) -> str:
    return pwd_context.hash(password)

#ПРОВЕРКА ПАРОЛЯ ЕБАНОГО
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data:dict, expires_delta: int = 30):
    to_encode = data.copy()
    expire = datetime.utcnow()+timedelta(minutes=expires_delta)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, JWT_SECRET, algorithm=JWT_ALGORITHM)