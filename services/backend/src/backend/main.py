from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.backend.config import settings

# Create FastAPI app
app = FastAPI()

# Adjust the CORS to accept from the front end
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.front_end_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return "Hello, World!"
