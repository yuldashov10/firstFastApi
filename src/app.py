from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index() -> str:
    return "Hello!"

@app.get("/echo/{thing}")
def echo(thing: str) -> str:
    return f"echoing {thing}"


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("app:app", reload=True)
