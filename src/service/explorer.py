from src.data import explorer as data
from src.model.explorer import Explorer



def list() -> list[Explorer]:
    return data.list()


def get(name: str) -> Explorer:
    return data.get(name)


def create(explore: Explorer) -> Explorer:
    return data.create(explore)


def modify(explore: Explorer) -> Explorer:
    return data.modify(explore)


def replace(explore: Explorer) -> Explorer:
    return data.replace(explore)


def delete(name: str) -> bool:
    return data.delete(name)
