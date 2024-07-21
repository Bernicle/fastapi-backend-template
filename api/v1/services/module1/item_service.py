from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from api.v1.models.module1.item_model import Item  # Assuming User model is in a 'models' folder
from api.v1.schemas.module1.item_schema import CreateItem as item_create_schema 
from config.database import get_db  # Assuming a function to get database session

class ItemService:
    def __init__(self, db : Session) -> None:
        self.db = db

    async def get_all_item(self):
        # Implement logic for fetching all item
        return self.db.query(Item).all()
    
    async def create_item(self, item: item_create_schema):
        # Implement logic for item creation (validation, saving to database)
        new_item = Item(**item.model_dump())  # Unpack the Pydantic data
        self.db.add(new_item)
        self.db.commit()
        self.db.refresh(new_item)  # Refresh the object to include the newly generated ID
        return new_item

    def get_item(self, item_id: int):
        # Implement logic for fetching a specific item by ID
        return self.db.query(Item).filter(Item.id  == item_id).first()

    def update_item(self, item_id: int, item_data: Item):
        # Implement logic for updating item data
        
        item = self.db.query(Item).filter(Item.id == item_id).first()
        if not item:
            raise HTTPException(status_code=404, detail="Item not found")

        # Update the item's attributes with the provided data
        for field, value in item_data.model_dump(exclude_unset=True).items():
            setattr(item, field, value)  # Update specific attributes as needed
        
        self.db.commit()
        self.db.refresh(item)  # Refresh for updated values
        return item


    def delete_item(self, item_id: int):
        # Implement logic for deleting a item
        # Retrieve the item by ID
        item = self.db.query(Item).filter(Item.id == item_id).first()
        if not item:
            raise HTTPException(status_code=404, detail="Item not found")

        # Delete the item from the database
        self.db.delete(item)
        self.db.commit()
        


# Dependency for injecting the database session
def get_item_service(db: Session = Depends(get_db)):
    yield ItemService(db)
