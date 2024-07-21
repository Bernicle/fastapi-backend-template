from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from api.v1.models.module1.item_model import Item  # Assuming User model is in a 'models' folder
from api.v1.schemas.module1.item_schema import CreateItem as item_create_schema 
from config.database import get_db  # Assuming a function to get database session

class ItemService:
    def __init__(self, db : Session) -> None:
        self.db = db

    async def get_all_item(self):
        # Implement logic for user creation (validation, password hashing, saving to database)
        # ...
        return self.db.query(Item).all()
    
    async def create_item(self, item_user: item_create_schema):
        # Implement logic for user creation (validation, password hashing, saving to database)
        # ...
        pass

    def get_item(self, item_id: int):
        # Implement logic for fetching a specific user by ID
        # ...
        pass

    def update_item(self, user_id: int, item_data: Item):
        # Implement logic for updating user data
        # ...
        pass

    def delete_item(self, item_id: int):
        # Implement logic for deleting a user
        # ...
        pass

# Dependency for injecting the database session
def get_item_service(db: Session = Depends(get_db)):
    yield ItemService(db)
