# Initialize the Database First Before anything else.
from config.database import get_db, initialize_setup, engine, Base
initialize_setup()

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import sys, os
sys.path.insert(1,os.path.dirname(os.path.abspath(__file__)))

from api.v1.routers.main_route import router as v1_router

app = FastAPI()

app.include_router(v1_router, dependencies=[Depends(get_db)])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
