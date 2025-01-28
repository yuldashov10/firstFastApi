from fastapi import Body, FastAPI

app = FastAPI()


@app.get("/hi")
def say_hello(
        name: str = Body(embed=True),
        age: int = Body(embed=True)
) -> str:
    return f"Hello, {name}! I'm {age} years old."


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("hello:app", reload=True)
