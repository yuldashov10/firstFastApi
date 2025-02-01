import os
from datetime import datetime, timedelta

from decouple import config
from jose import jwt, JWTError
from passlib.context import CryptContext

from src.model.user import User

if config("CRYPTID_UNIT_TEST", cast=str):
    from src.fake.user import FakeUserData

    data = FakeUserData()
else:
    from src.data import user as data

SECRET_KEY = config("SECRET_KEY", cast=str)
ALGORITHM = config("ALGORITHM", cast=str)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain: str, hash: str) -> bool:
    """Хеширование строки <plain> и сравнение с записью <hash> из базы данных."""
    return pwd_context.verify(plain, hash)


def get_hash(plain: str) -> str:
    """Возврат xeш строки <plain>."""
    return pwd_context.hash(plain)


def get_jwt_username(token: str) -> str | None:
    """Возврат имени пользователя из JWT -доступа ctoken>."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if not (username := payload.get("sub")):
            return None
    except JWTError:
        return None

    return username


def lookup_user(username: str) -> User | None:
    """Возврат совпадающего пользователя из базы данных для строки <name>."""
    return data.get(username) or None


def get_current_user(token: str) -> User | None:
    """Декодирование токена <token> доступа OAuth и возврат объекта User."""
    if not (username := get_jwt_username(token)):
        return None
    return lookup_user(username) or None


def auth_user(name: str, plain: str) -> User | None:
    """Аутентификация пользователя <name> и cplain> пароль."""
    if not (user := lookup_user(name)):
        return None

    if not verify_password(plain, user.hash):
        return None

    return user


def create_access_token(data: dict, expires: timedelta | None = None) -> str:
    """Возвращение токена доступа JWT"""
    src: dict = data.copy()
    now: datetime = datetime.utcnow()

    if not expires:
        expires = timedelta(minutes=15)

    src.update({"exp": now + expires})

    return jwt.encode(src, SECRET_KEY, algorithm=ALGORITHM)


def list() -> list[User]:
    return data.list()


def get(username: str) -> User:
    return data.get(username)


def create(user: User) -> User:
    return data.create(user)


def modify(username: str, user: User) -> User:
    return data.modify(username, user)


def replace(user: User) -> User:
    return data.replace(user)


def delete(username: str) -> bool:
    return data.delete(username)
