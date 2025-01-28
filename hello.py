import asyncio

from fastapi import FastAPI

app = FastAPI()


@app.get("/hi")
async def say_hello() -> str:
    await asyncio.sleep(1)
    return f"Hello!"


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("hello:app", reload=True)
