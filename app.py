from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from src.web import explorer, creature, user
import logging

from opentelemetry import trace
from opentelemetry import metrics

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

logging.basicConfig(level=logging.INFO, encoding="UTF-8")
logger = logging.getLogger(__name__)


@app.get("/")
def index() -> str:
    return "Hello!"


@app.get("/echo/{thing}")
def echo(thing: str) -> str:
    return f"echoing {thing}"


@app.get("/test_cors")
def test_cors(request: Request):
    print(request)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", reload=True)
