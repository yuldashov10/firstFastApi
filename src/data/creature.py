from core.exceptions import ObjectDoesNotExist, DuplicateRecordError
from src.model.creature import Creature
from .init_db import cur, IntegrityError


def init_table() -> None:
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS creature(
            name TEXT PRIMARY KEY,
            description TEXT,
            country TEXT,
            area TEXT,
            aka TEXT
        )
        """
    )


init_table()


def row_to_model(row: tuple) -> Creature:
    name, description, country, area, aka = row
    return Creature(
        name=name,
        description=description,
        country=country,
        area=area,
        aka=aka
    )


def model_to_dict(creature: Creature) -> dict:
    return creature.model_dump()


def list() -> list[Creature]:
    query = "SELECT * FROM creature"
    cur.execute(query)

    return [row_to_model(row) for row in cur.fetchall()]


def get(name: str) -> Creature:
    query: str = (
        "SELECT * FROM creature WHERE name=:name"
    )

    cur.execute(query, {"name": name})
    creature = cur.fetchone()

    if not creature:
        raise ObjectDoesNotExist(f"Creature '{name}' not found")
    return row_to_model(creature)


def create(creature: Creature) -> Creature:
    query: str = (
        "INSERT INTO creature(name, description, country, area, aka)"
        "VALUES (:name, :description, :country, :area, :aka)"
    )

    try:
        cur.execute(query, model_to_dict(creature))
    except IntegrityError:
        raise DuplicateRecordError(
            f"Creature '{creature.name}' already exists"
        )
    return get(creature.name)


def modify(name: str, creature: Creature) -> Creature:
    if not (name and creature):
        return None

    query = (
        """
        UPDATE creature
        SET country=:country,
            name=:name,
            description=:description,
            area=:area,
            aka=:aka
        WHERE name=:name_orig
    """
    )
    params = model_to_dict(creature)

    params["name_orig"] = creature.name
    cur.execute(query, params)

    if cur.rowcount != 1:
        raise ObjectDoesNotExist(f"Creature '{name}' not found")
    return get(creature.name)


def replace(creature: Creature) -> Creature:
    return creature


def delete(name: str) -> bool | None:
    if not name:
        return False

    query: str = "DELETE FROM creature WHERE name = :name"
    cur.execute(query, {"name": name})

    if cur.rowcount != 1:
        raise ObjectDoesNotExist(f"Explorer '{name}' not found")

    return None
