from pathlib import Path
from typing import Generator

from fastapi import FastAPI, Request, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from starlette import status

from src.web import explorer, creature, user
import logging

from opentelemetry import trace
from opentelemetry import metrics

BASE_DIR: str = str(Path(__file__).resolve().parent)

tracer = trace.get_tracer("firstFastApi.tracer")
meter = metrics.get_meter("firstFastApi.meter")

roll_counter = meter.create_counter(
    "dice.rolls",
    description="The number of rolls by roll value",
)

app = FastAPI()
app.include_router(explorer.router)
app.include_router(creature.router)
app.include_router(user.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://ui.cryptids.com", ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory=f"{BASE_DIR}/static", html=True), name="free")

logging.basicConfig(level=logging.INFO, encoding="UTF-8")
logger = logging.getLogger(__name__)


@app.get("/")
def index() -> str:
    return "Hello!"


@app.post("/upload_small")
async def upload_small_file(small_file: bytes = File()) -> str:
    return f"File size: {len(small_file)} bytes"


@app.post("/upload_big")
async def upload_big_file(big_file: UploadFile) -> str:
    return f"File size: {big_file.size} bytes, name: {big_file.filename}"


@app.get("/download_small/{name}")
async def download_small_file(name: str) -> FileResponse:
    return FileResponse(name)


def read_file(path: str) -> Generator:
    with open(path, mode="rb") as file:
        yield file.read()


@app.get("/download_big/{name}")
async def download_big_file(name: str) -> StreamingResponse:
    return StreamingResponse(
        content=read_file(name),
        status_code=status.HTTP_200_OK
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", reload=True)
