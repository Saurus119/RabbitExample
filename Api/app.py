from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from Api.before_start import lifespan
from Api.routes import register_routes

app = FastAPI(lifespan=lifespan, root_path="/api")
api_router = APIRouter()

registered_router = register_routes(api_router)

app.include_router(registered_router)

# Set up CORS
origins = [
    "http://localhost",  # Add the URLs of your React application here
    "http://localhost:3000",
    "https://yourdeployedreactapp.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
