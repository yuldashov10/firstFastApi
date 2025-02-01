from core.exceptions import DuplicateRecordError, ObjectDoesNotExist
from src.model.explorer import Explorer
from .init_db import cur, IntegrityError


def init_table() -> None:
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS explorer(
            name TEXT PRIMARY KEY,
            country TEXT,
            description TEXT
        )
        """
    )


init_table()


def row_to_model(row: tuple) -> Explorer:
    name, country, description = row
    return Explorer(
        name=name,
        country=country,
        description=description
    )


def model_to_dict(explorer: Explorer) -> dict:
    return explorer.model_dump()


def list() -> list[Explorer]:
    query = "SELECT * FROM explorer"
    cur.execute(query)

    return [row_to_model(row) for row in cur.fetchall()]


def get(name: str) -> Explorer:
    query: str = (
        "SELECT * FROM explorer WHERE name=:name"
    )

    cur.execute(query, {"name": name})
    explorer = cur.fetchone()

    if not explorer:
        raise ObjectDoesNotExist(f"Explorer '{name}' not found")
    return row_to_model(explorer)


def create(explorer: Explorer) -> Explorer | None:
    if not explorer:
        return None

    query: str = (
        "INSERT INTO explorer(name, country, description)"
        "VALUES (:name, :description, :country)"
    )

    try:
        cur.execute(query, model_to_dict(explorer))
    except IntegrityError:
        raise DuplicateRecordError(
            f"Explorer '{explorer.name}' already exists"
        )

    return get(explorer.name)


def modify(name: str, explorer: Explorer) -> Explorer | None:
    if not (name and explorer):
        return None

    query = (
        """
        UPDATE explorer
        SET name=:name,
            country=:country,
            description=:description
        WHERE name=:name_orig
    """
    )
    params = model_to_dict(explorer)

    params["name_orig"] = explorer.name
    cur.execute(query, params)

    if cur.rowcount != 1:
        raise ObjectDoesNotExist(f"Explorer '{name}' not found")
    return get(explorer.name)


def replace(explorer: Explorer) -> Explorer:
    return explorer


def delete(name: str) -> bool | None:
    if not name:
        return False

    query: str = "DELETE FROM explorer WHERE name = :name"
    cur.execute(query, {"name": name})

    if cur.rowcount != 1:
        raise ObjectDoesNotExist(f"Explorer '{name}' not found")

    return None
