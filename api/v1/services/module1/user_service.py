from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from api.v1.models.module1.user_model import User  # Assuming User model is in a 'models' folder
from api.v1.schemas.module1.user_schema import CreateUser as user_create_schema 
from config.database import get_db  # Assuming a function to get database session

class UserService:
    def __init__(self, db : Session) -> None:
        self.db = db

    async def get_all_user(self):
        # Implement logic for user creation (validation, password hashing, saving to database)
        # ...
        return self.db.query(User).all()
    
    async def create_user(self, new_user: user_create_schema):
        # Implement logic for user creation (validation, password hashing, saving to database)
        # ...
        pass

    def get_user(self, user_id: int):
        # Implement logic for fetching a specific user by ID
        # ...
        pass

    def update_user(self, user_id: int, user_data: User):
        # Implement logic for updating user data
        # ...
        pass

    def delete_user(self, user_id: int):
        # Implement logic for deleting a user
        # ...
        pass

# Dependency for injecting the database session
def get_user_service(db: Session = Depends(get_db)):
    yield UserService(db)
