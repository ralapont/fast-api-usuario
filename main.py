from fastapi import FastAPI
from fastapi.logger import logger as fastapi_logger
import logging

from app.v1.router.user_router import router as user_router
from app.v1.router.profesor_router import router as profesor_router
from app.v1.router.clase_router import router as clase_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:4200"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.getLogger(__name__)

app.include_router(user_router)
app.include_router(profesor_router)
app.include_router(clase_router)

@app.options("/")
async def root():
    fastapi_logger.info("Uvicorn is alive")
    return {"Uvicorn": "I'm alive"}