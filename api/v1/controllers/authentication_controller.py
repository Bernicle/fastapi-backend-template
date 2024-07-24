from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta
import os

from api.v1.models.admin.user_model import User
from api.v1.schemas.admin.user_schema import User as user_schema
from api.v1.schemas.Invalid_id_schema import InvalidIDResponse
from api.v1.schemas.authentication_schema import LoginResponse
from config.database  import get_db
from helper.security import create_access_token

from helper.security import hash_password, verify_password

router = APIRouter()

# ... (Optional database connection logic)


@router.post("/login", response_model=LoginResponse, responses={400: {"description": "Failed to Login", "model": InvalidIDResponse}})
async def login(login_detail: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    
    user_found = db.query(User).filter(User.username == login_detail.username).first()
    
    if (user_found is None):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Failed to Login"
        )
    
    if (not verify_password(login_detail.password, user_found.hash_password)):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Failed to Login"
        )
    setting = {
        "SECRET_KEY":os.getenv("SECRET_KEY"),
        "ALGORITHM": os.getenv("ALGORITHM")
    }
    user_detail = user_schema(**user_found.__dict__).model_dump()
    access_token = create_access_token({
            "id": user_found.id
        },
        expires_delta=timedelta(minutes=15), SECRET_SETTING=setting)
    return {
        "user": user_found.__dict__, 
        "access_token": access_token,
        "token_type":"bearer"
    }
