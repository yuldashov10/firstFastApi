from fastapi import FastAPI

from src.web import explorer, creature

app = FastAPI()

app.include_router(explorer.router)
app.include_router(creature.router)


@app.get("/")
def index() -> str:
    return "Hello!"

@app.get("/echo/{thing}")
def echo(thing: str) -> str:
    return f"echoing {thing}"


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", reload=True)
