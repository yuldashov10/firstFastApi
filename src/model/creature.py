from pydantic import BaseModel

__all__ = [
    "Creature",
]


class Creature(BaseModel):
    name: str
    country: str
    area: str
    description: str
    aka: str


if __name__ == "__main__":
    thing = Creature(
        name="Luntik",
        country="RU",
        area="1234567S89",
        description="Some text",
        aka="Лунтик",
    )

    print(f"Имя {thing.name}")
