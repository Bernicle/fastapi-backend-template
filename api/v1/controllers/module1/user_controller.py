from bcrypt import hashpw, gensalt

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ...models.module1.user_model import User
from ...schemas.module1.user_schema import User as user_schema, CreateUser as user_create_schema, UpdateUser as user_update_schema
from ...schemas.Invalid_id_schema import InvalidIDResponse
from .....config.database  import get_db

router = APIRouter()

def hash_password(password):
   password_bytes = password.encode('utf-8')
   hashed_bytes = hashpw(password_bytes, gensalt())
   return hashed_bytes.decode('utf-8')


@router.get("/", response_model=list[user_schema])
async def get_users(db: Session = Depends(get_db)):
    # ... (Retrieve items from database)
    return db.query(User).all()

@router.get("/{user_id}", response_model=user_schema, responses={400: {"description": "User not found", "model": InvalidIDResponse}})
async def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    # ... (Retrieve item by ID from database)
    item = db.query(User).filter(User.id  == user_id).first()
    if not item:
        raise HTTPException(status_code=400, detail=f"The user for the provided ID was not exist. Try different ID.")
    
    return item

@router.post("/", response_model=user_schema, status_code=status.HTTP_201_CREATED)
async def create_user(item: user_create_schema, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.username == item.username or User.mobile_number == item.mobile_number).first()
    
    if existing_user:
        raise HTTPException(
            status=status.HTTP_400_BAD_REQUEST,
            detail="Username or mobile number already exists"
        )
    
    salted_password = hash_password(item.password)
    user_dict = item.dict()
    del user_dict['password']
    # Create a new Item instance using Pydantic data
    new_user = User(**user_dict)  # Unpack the Pydantic data
    new_user.hash_password = salted_password
    db.add(new_user)
    db.commit()
    db.refresh(new_user)  # Refresh the object to include the newly generated ID

    return new_user

@router.put("/{user_id}", response_model=user_schema, responses={404: {"model": InvalidIDResponse}})
async def update_user(user_id: int, user_data: user_update_schema, db: Session = Depends(get_db)):
    # Retrieve the item by ID
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Item not found")

    # Update the item's attributes with the provided data
    for field, value in user_data.dict(exclude_unset=True).items():
        setattr(user, field, value)  # Update specific attributes as needed
    
    db.commit()
    db.refresh(user)  # Refresh for updated values

    return user

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT, responses={404: {"model": InvalidIDResponse}})
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    # Retrieve the item by ID
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User Id not found")

    # Delete the item from the database
    db.delete(user)
    db.commit()

    # Return no content (204) on successful deletion
    return None