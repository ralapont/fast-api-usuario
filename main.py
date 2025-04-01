from fastapi import FastAPI
from fastapi.logger import logger as fastapi_logger
import logging

from app.v1.router.user_router import router as user_router
from app.v1.router.profesor_router import router as profesor_router
from app.v1.router.clase_router import router as clase_router

app = FastAPI()

logging.getLogger(__name__)

app.include_router(user_router)
app.include_router(profesor_router)
app.include_router(clase_router)

@app.get("/")
async def root():
    fastapi_logger.info("Uvicorn is alive")
    return {"Uvicorn": "I'm alive"}