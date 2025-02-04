from fastapi import APIRouter

from src.model.creature import Creature

from src.service import creature as service

router = APIRouter(prefix="/creature")


@router.get("/")
def list() -> list[Creature]:
    return service.list()


@router.get("/{name}")
def get(name: str) -> Creature:
    return service.get(name)


@router.post("/")
def create(creature: Creature) -> Creature:
    return service.create(creature)


@router.patch("/")
def modify(creature: Creature) -> Creature:
    return service.modify(creature)


@router.delete("/{name}")
def delete(name: str) -> None:
    return service.delete(name)
