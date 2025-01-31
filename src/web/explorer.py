from typing import Optional
from fastapi import APIRouter, HTTPException

from core.exceptions import DuplicateRecordError, ObjectDoesNotExist
from src.model.explorer import Explorer
from src.service import explorer as service

router = APIRouter(prefix="/explorer")


@router.get("")
@router.get("/")
def list() -> list[Explorer]:
    return service.list()


@router.get("/{name}")
@router.get("/{name}/")
def get(name: str) -> Explorer:
    try:
        return service.get(name)
    except ObjectDoesNotExist as err:
        raise HTTPException(status_code=404, detail=err.msg)


@router.post("", status_code=201)
@router.post("/", status_code=201)
def create(explore: Explorer) -> Explorer:
    try:
        return service.create(explore)
    except DuplicateRecordError as err:
        raise HTTPException(status_code=404, detail=err.msg)


@router.patch("/")
def modify(explore: Explorer) -> Explorer:
    try:
        return service.modify(explore)
    except DuplicateRecordError as err:
        raise HTTPException(status_code=404, detail=err.msg)


@router.delete("/{name}", status_code=204)
@router.delete("/{name}/", status_code=204)
def delete(name: str) -> None:
    try:
        service.delete(name)
    except ObjectDoesNotExist as err:
        raise HTTPException(status_code=404, detail=err.msg)
