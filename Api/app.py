from fastapi import FastAPI, APIRouter

from Api.before_start import lifespan
from Api.routes import register_routes

app = FastAPI(lifespan=lifespan)
api_router = APIRouter()

registered_router = register_routes(api_router)

app.include_router(registered_router)
