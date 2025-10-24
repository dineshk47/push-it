import logging
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from app.db.init_db import get_mongo_db
from app.api import api_router
load_dotenv()


app = FastAPI(
    title="My API",
    description="This is a Fast API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
log_level = os.getenv("LOG_LEVEL", "INFO") 
logger = logging.getLogger()
logger.setLevel(log_level.upper())

@app.middleware("http")
async def log_requests(request, call_next):
    logger.info(f"Incoming request: {request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"Response status: {response.status_code}")
    return response 

@app.middleware("http")
async def db_session_middleware(request, call_next):
    request.state.mongo_db, mongo_client = get_mongo_db()
    response = await call_next(request)
    return response

app.include_router(api_router)