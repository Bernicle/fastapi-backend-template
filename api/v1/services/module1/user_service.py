from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from api.v1.models.module1.user_model import User  # Assuming User model is in a 'models' folder
from api.v1.schemas.module1.user_schema import CreateUser as user_create_schema 
from config.database import get_db
from helper.security import hash_password  # Assuming a function to get database session

class UserService:
    def __init__(self, db : Session) -> None:
        self.db = db

    async def get_all_user(self):
        # Implement logic for fetching all user
        return self.db.query(User).all()
    
    async def create_user(self, user: user_create_schema):
        # Implement logic for user creation (validation, password hashing, saving to database)
        existing_user = self.db.query(User).filter(User.username == user.username or User.mobile_number == user.mobile_number).first()
        
        if existing_user:
            raise HTTPException(
                status_code=400,
                detail="Username or mobile number already exists"
            )
        
        salted_password = hash_password(user.password)
        user_dict = user.model_dump()
        del user_dict['password']
        # Create a new Item instance using Pydantic data
        new_user = User(**user_dict)  # Unpack the Pydantic data
        new_user.hash_password = salted_password
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)  # Refresh the object to include the newly generated ID
        return new_user
    
    
    def are_keys_taken(self, mobile_number: str, username : str):
        # Implement logic for fetching a specific user by ID
        return self.db.query(User).filter(User.mobile_number  == mobile_number or User.username == username).first()


    async def get_user(self, user_id: int):
        # Implement logic for fetching a specific user by ID
        return self.db.query(User).filter(User.id  == user_id).first()

    async def update_user(self, user_id: int, user_data: User):
        # Implement logic for updating user data
        # Retrieve the item by ID
        user = self.db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="Item not found")

        # Update the item's attributes with the provided data
        for field, value in user_data.model_dump(exclude_unset=True).items():
            setattr(user, field, value)  # Update specific attributes as needed
        
        self.db.commit()
        self.db.refresh(user)  # Refresh for updated values
        return user
    
    async def reset_password(self, user_id: int, new_password: str):
        # Implement logic for user creation (validation, password hashing, saving to database)
        existing_user = await self.get_user(user_id=user_id)
        
        if existing_user:
            raise HTTPException(
                status_code=400,
                detail="Username or mobile number already exists"
            )
        
        salted_password = hash_password(new_password)
        
        setattr(existing_user, "hash_password", salted_password)
        self.db.commit()
        self.db.refresh(existing_user)  # Refresh the object to include the newly generated ID

    async def delete_user(self, user_id: int):
        # Implement logic for deleting a user
        user = self.db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User Id not found")

        # Delete the item from the database
        self.db.delete(user)
        self.db.commit()

# Dependency for injecting the database session
def get_user_service(db: Session = Depends(get_db)):
    yield UserService(db)
