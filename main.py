from fastapi import FastAPI
from config.database import Base, engine
from config.routers import router

# Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)
