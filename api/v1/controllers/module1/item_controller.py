from fastapi import APIRouter, Depends, HTTPException, status
import pytest
from sqlalchemy.orm import Session

from api.v1.middlewares.auth.authentication import get_current_user
from api.v1.schemas.module1.user_schema import User
from api.v1.services.module1.item_service import ItemService, get_item_service

from ...models.module1.item_model import Item
from ...schemas.module1.item_schema import Item as item_schema, CreateItem as item_create_schema, UpdateItem as item_update_schema
from ...schemas.Invalid_id_schema import InvalidIDResponse
from config.database  import get_db

router = APIRouter()

@router.get("/", response_model=list[item_schema])
async def get_items(item_service : ItemService = Depends(get_item_service)):
    # ... (Retrieve items from database)
    return await item_service.get_all_item()

@router.get("/{item_id}", response_model=item_schema, responses={400: {"description": "Item not found", "model": InvalidIDResponse}})
async def get_item_by_id(item_id: int, db: Session = Depends(get_db), current_user : User = Depends(get_current_user)):
    # ... (Retrieve item by ID from database)
    item = db.query(Item).filter(Item.id  == item_id).first()
    if not item:
        raise HTTPException(status_code=400, detail=f"The item with provided ID was not exist. Try different ID.")
    
    return item

@router.post("/", response_model=item_schema, status_code=status.HTTP_201_CREATED)
async def create_item(item: item_create_schema, db: Session = Depends(get_db), current_user : User = Depends(get_current_user)):
    # Create a new Item instance using Pydantic data
    new_item = Item(**item.model_dump())  # Unpack the Pydantic data
    db.add(new_item)
    db.commit()
    db.refresh(new_item)  # Refresh the object to include the newly generated ID

    return new_item

@router.put("/{item_id}", response_model=item_schema, responses={404: {"model": InvalidIDResponse}})
async def update_item(item_id: int, item_data: item_update_schema, db: Session = Depends(get_db)):
    # Retrieve the item by ID
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    # Update the item's attributes with the provided data
    for field, value in item_data.model_dump(exclude_unset=True).items():
        setattr(item, field, value)  # Update specific attributes as needed
    
    db.commit()
    db.refresh(item)  # Refresh for updated values

    return item

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT, responses={404: {"model": InvalidIDResponse}})
async def delete_item(item_id: int, db: Session = Depends(get_db)):
    # Retrieve the item by ID
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    # Delete the item from the database
    db.delete(item)
    db.commit()

    # Return no content (204) on successful deletion
    return None