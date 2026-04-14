from fastapi import FastAPI
from app.api.v1.router import api_router
from contextlib import asynccontextmanager
from sqlmodel import SQLModel
from app.core.database import engine
from app.models import *

@asynccontextmanager
async def lifespan(app:FastAPI):
    SQLModel.metadata.create_all(engine)
    print("Tables created")

    yield
    print('App shutingdown')

app=FastAPI(lifespan=lifespan)
app.include_router(api_router)