from datetime import timedelta

from decouple import config
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from starlette import status

from core.exceptions import ObjectDoesNotExist, DuplicateRecordError
from src.model.user import User

if config("CRYPTID_UNIT_TEST", cast=str):
    from src.fake.user import FakeUserData

    service = FakeUserData()
else:
    from src.service import user as service

ACCESS_TOKEN_EXPIRE_MINUTES: int = config(
    "ACCESS_TOKEN_EXPIRE_MINUTES",
    default=15,
    cast=int
)

router = APIRouter(prefix="/user")

oauth2_dep = OAuth2PasswordBearer(tokenUrl="token")


def unauthenticated():
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Bearer"},
    )


@router.post("/token")
async def create_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """Получение имени пользователя и пароля из формы OAuth, возврат токена доступа"""
    user = service.auth_user(form_data.username, form_data.password)

    if not user:
        unauthenticated()

    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = service.create_access_token(
        data={"sub": user.username},
        expires=expires,
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/token")
def get_access_token(token: str = Depends(oauth2_dep)) -> dict:
    """Возврат текущего токена"""
    return {"token": token}


@router.get("")
@router.get("/")
def list() -> list[User]:
    return service.list()


@router.get("/{username}")
@router.get("/{username}/")
def get(username: str) -> User:
    try:
        return service.get(username)
    except ObjectDoesNotExist as err:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=err.msg
        )


@router.post("", status_code=status.HTTP_201_CREATED)
@router.post("/", status_code=status.HTTP_201_CREATED)
def create(user: User) -> User:
    try:
        return service.create(user)
    except DuplicateRecordError as err:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=err.msg
        )


@router.patch("/")
def modify(username: str, user: User) -> User:
    try:
        return service.modify(username, user)
    except DuplicateRecordError as err:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=err.msg
        )


@router.delete("/{username}", status_code=status.HTTP_204_NO_CONTENT)
@router.delete("/{username}/", status_code=status.HTTP_204_NO_CONTENT)
def delete(username: str) -> None:
    try:
        return service.delete(username)
    except ObjectDoesNotExist as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=err.msg)
