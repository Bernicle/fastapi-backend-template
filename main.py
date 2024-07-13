import sys, os
sys.path.insert(1,os.path.dirname(os.path.abspath(__file__)))

# Initialize the Database First Before anything else.
from config.database import get_db, initialize_setup, engine, Base
initialize_setup()

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from api.v1.routers.main_route import router as v1_router

app = FastAPI()

origins = [
    "*", #Comment this before uploading to server
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(v1_router, dependencies=[Depends(get_db)])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
