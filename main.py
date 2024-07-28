import sys, os
from dotenv import load_dotenv
from jwt.exceptions import ExpiredSignatureError

sys.path.insert(1,os.path.dirname(os.path.abspath(__file__)))
# Initialize the Database First Before anything else.
from config.database import get_db, initialize_setup
initialize_setup()

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from api.v1.controllers.exception.handler.expire_signature_handler import expire_signature_handler
from api.v1.routers.main_route import router as v1_router

load_dotenv()

app = FastAPI()

origins = os.getenv("CORS_ORIGIN")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(v1_router, dependencies=[Depends(get_db)])
app.add_exception_handler(ExpiredSignatureError, expire_signature_handler)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
