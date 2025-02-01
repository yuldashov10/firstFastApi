from core.exceptions import DuplicateRecordError, ObjectDoesNotExist
from src.model.user import User
from .init_db import cur, IntegrityError


def init_tables() -> None:
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS user(
            username TEXT PRIMARY KEY,
            password_hash TEXT
        )
        """
    )
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS ex_user(
            username TEXT PRIMARY KEY,
            password_hash TEXT
        )
        """
    )


init_tables()


def row_to_model(row: tuple) -> User:
    username, password_hash = row
    return User(username=username, password_hash=password_hash)


def model_to_dict(user: User) -> dict:
    return user.model_dump()


def list() -> list[User]:
    query = "SELECT * FROM user"
    cur.execute(query)

    return [row_to_model(row) for row in cur.fetchall()]


def get(username: str) -> User:
    query: str = (
        "SELECT * FROM user WHERE username=:username"
    )

    cur.execute(query, {"username": username})
    user = cur.fetchone()

    if not user:
        raise ObjectDoesNotExist(f"User '{username}' not found")
    return row_to_model(user)


def create(user: User, table: str = "user") -> User:
    query: str = (
        f"INSERT INTO {table}(username, password_hash)"
        "VALUES (:username, :password_hash)"
    )

    try:
        cur.execute(query, model_to_dict(user))
    except IntegrityError:
        raise DuplicateRecordError(
            f"{table}: User '{user.username}' already exists"
        )
    return get(user.username)


def modify(username: str, user: User) -> User:
    query = (
        """
        UPDATE user
        SET username=:username,
            password_hash=:password_hash
        WHERE username=:name_orig
    """
    )
    params = model_to_dict(user)

    params["name_orig"] = user.username
    cur.execute(query, params)

    if cur.rowcount != 1:
        raise ObjectDoesNotExist(f"User '{username}' not found")
    return get(user.username)


def replace(user: User) -> User:
    return user


def delete(username: str) -> bool | None:
    user: User = get(username)
    if not username:
        return False

    query: str = "DELETE FROM user WHERE username = :username"
    cur.execute(query, {"username": username})

    if cur.rowcount != 1:
        raise ObjectDoesNotExist(f"User '{username}' not found")

    create(user, table="ex_user")
