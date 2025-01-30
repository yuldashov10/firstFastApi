from fastapi import FastAPI, Depends


from core.utils import user_dep
from fake_data import get_creatures
from models import Creature

app = FastAPI()


@app.get("/creatures")
def get_creatures_list() -> list[Creature]:
    """Возвращает список существ."""
    return get_creatures(count=5)


@app.get("/user")
def get_user(user: dict = Depends(user_dep)) -> dict[str, str | bool]:
    return user


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("web_app:app", reload=True)
