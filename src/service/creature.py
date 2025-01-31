from src.fake.creature import FakeCreatureData
from src.model.creature import Creature

data = FakeCreatureData()


def list() -> list[Creature]:
    return data.list()


def get(name: str) -> Creature:
    return data.get(name)


def create(creature: Creature) -> Creature:
    return data.create(creature)


def modify(creature: Creature) -> Creature:
    return data.modify(creature)


def replace(creature: Creature) -> Creature:
    return data.replace(creature)


def delete(name: str) -> None:
    return data.delete(name)
