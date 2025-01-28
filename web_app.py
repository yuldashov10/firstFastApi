from fastapi import FastAPI

from fake_data import get_creatures
from models import Creature

app = FastAPI()


@app.get("/creatures")
def get_creatures_list() -> list[Creature]:
    """Возвращает список существ."""
    return get_creatures(count=5)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("web_app:app", reload=True)
