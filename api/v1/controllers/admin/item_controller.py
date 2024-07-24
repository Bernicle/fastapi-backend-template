from fastapi import APIRouter, Depends, HTTPException, status

from api.v1.middlewares.auth.authentication import get_current_user
from api.v1.schemas.admin.user_schema import User
from api.v1.services.admin.item_service import ItemService, get_item_service

from api.v1.schemas.admin.item_schema import Item as item_schema, CreateItem as item_create_schema, UpdateItem as item_update_schema
from api.v1.schemas.Invalid_id_schema import InvalidIDResponse
from config.database  import get_db

router = APIRouter()

@router.get("/", response_model=list[item_schema])
async def get_items(item_service : ItemService = Depends(get_item_service)):
    # ... (Retrieve items from database)
    return await item_service.get_all_item()

@router.get("/{item_id}", response_model=item_schema, responses={400: {"description": "Item not found", "model": InvalidIDResponse}})
async def get_item_by_id(item_id: int, item_service : ItemService = Depends(get_item_service), current_user : User = Depends(get_current_user)):
    # ... (Retrieve item by ID from database)
    item = item_service.get_item(item_id=item_id)
    if not item:
        raise HTTPException(status_code=400, detail=f"The item with provided ID was not exist. Try different ID.")
    
    return item

@router.post("/", response_model=item_schema, status_code=status.HTTP_201_CREATED)
async def create_item(item: item_create_schema, item_service : ItemService = Depends(get_item_service), current_user : User = Depends(get_current_user)):
    # Create a new Item instance using Pydantic data
    new_item = await item_service.create_item(item=item)
    return new_item

@router.put("/{item_id}", response_model=item_schema, responses={404: {"model": InvalidIDResponse}})
async def update_item(item_id: int, item_data: item_update_schema, item_service : ItemService = Depends(get_item_service)):
    # Retrieve the item by ID
    item = item_service.update_item(item_id=item_id, item_data=item_data)
    return item

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT, responses={404: {"model": InvalidIDResponse}})
async def delete_item(item_id: int, item_service : ItemService = Depends(get_item_service)):
    item_service.delete_item(item_id=item_id)
    # Return no content (204) on successful deletion
    return None