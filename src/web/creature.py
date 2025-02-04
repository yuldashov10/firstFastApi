from fastapi import APIRouter, Response
import plotly.express as px

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


@router.get("/test")
def test():
    df = px.data.iris()
    fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
    fig_bytes = fig.to_image(format="png")

    return Response(content=fig_bytes, media_type="image/png")
