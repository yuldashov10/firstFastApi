from fastapi import APIRouter

from src.model.explorer import Explorer
from src.fake.explorer import FakeExplorerData

service = FakeExplorerData()

router = APIRouter(prefix="/explorer")


@router.get("/")
def list() -> list[Explorer]:
    return service.list()


@router.get("/{name}")
def get(name: str) -> Explorer:
    return service.get(name)


@router.post("/")
def create(explore: Explorer) -> Explorer:
    return service.create(explore)


@router.patch("/")
def modify(explore: Explorer) -> Explorer:
    return service.modify(explore)


@router.put("/")
def replace(explore: Explorer) -> Explorer:
    return service.replace(explore)


@router.delete("/{name}")
def delete(name: str) -> None:
    return service.delete(name)
