from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..models.module1.user_model import User
from ..schemas.module1.user_schema import Login as login_schema, User as user_schema
from ..schemas.Invalid_id_schema import InvalidIDResponse
from config.database  import get_db

from helper.security import hash_password, verify_password

router = APIRouter()

# ... (Optional database connection logic)


@router.post("/login", response_model=user_schema, responses={400: {"description": "Failed to Login", "model": InvalidIDResponse}})
async def login(login_detail: login_schema, db: Session = Depends(get_db)):
    
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

    return user_found
