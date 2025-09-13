from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.routes.configs import router as configs_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Place for startup/shutdown hooks if needed
    yield


app = FastAPI(title="Config Files Server", version="0.1.0", lifespan=lifespan)

app.include_router(configs_router)


@app.get("/healthz")
async def health() -> dict[str, str]:
    return {"status": "ok"}
