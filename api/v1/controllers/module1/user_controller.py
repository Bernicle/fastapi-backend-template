from bcrypt import hashpw, gensalt

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from api.v1.models.module1.user_model import User
from api.v1.schemas.module1.user_schema import User as user_schema, CreateUser as user_create_schema, UpdateUser as user_update_schema
from api.v1.schemas.Invalid_id_schema import InvalidIDResponse
from api.v1.services.module1.user_service import UserService, get_user_service
from config.database  import get_db

router = APIRouter()

@router.get("/", response_model=list[user_schema])
async def get_users(user_service : UserService = Depends(get_user_service)):
    # ... (Retrieve items from database)
    return await user_service.get_all_user()

@router.get("/{user_id}", response_model=user_schema, responses={400: {"description": "User not found", "model": InvalidIDResponse}})
async def get_user_by_id(user_id: int, user_service : UserService = Depends(get_user_service)):
    # ... (Retrieve item by ID from database)
    item = await user_service.get_user(user_id=user_id)
    if not item:
        raise HTTPException(status_code=400, detail=f"The user for the provided ID was not exist. Try different ID.")
    return item

@router.post("/", response_model=user_schema, status_code=status.HTTP_201_CREATED)
async def create_user(user: user_create_schema, user_service : UserService = Depends(get_user_service)):
    new_user = await user_service.create_user(user)
    return new_user

@router.put("/{user_id}", response_model=user_schema, responses={404: {"model": InvalidIDResponse}})
async def update_user(user_id: int, user_data: user_update_schema, user_service : UserService = Depends(get_user_service)):
    user = await user_service.update_user(user_id= user_id, user_data=user_data)
    return user

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT, responses={404: {"model": InvalidIDResponse}})
async def delete_user(user_id: int, user_service : UserService = Depends(get_user_service)):
    # Retrieve the item by ID
    await user_service.delete_user(user_id=user_id)
    # Return no content (204) on successful deletion
    return None