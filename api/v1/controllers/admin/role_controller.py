from fastapi import APIRouter, Depends, HTTPException, status

from api.v1.middlewares.auth.authentication import get_current_user
from api.v1.schemas.admin.user_schema import User
from api.v1.services.admin.role_service import RoleService, get_role_service

from api.v1.schemas.admin.role_schema import Role as role_schema, CreateRole as role_create_schema, UpdateRole as role_update_schema
from api.v1.schemas.Invalid_id_schema import InvalidIDResponse
from config.database  import get_db

router = APIRouter()

@router.get("/", response_model=list[role_schema])
async def get_role(role_service : RoleService = Depends(get_role_service)):
    # ... (Retrieve items from database)
    return await role_service.get_all()

@router.get("/{role_id}", response_model=role_schema, responses={400: {"description": "Role not found", "model": InvalidIDResponse}})
async def get_role_by_id(role_id: int, role_service : RoleService = Depends(get_role_service), current_user : User = Depends(get_current_user)):
    # ... (Retrieve item by ID from database)
    role = role_service.get(role_id=role_id)
    if not role:
        raise HTTPException(status_code=400, detail=f"The role with provided ID was not exist. Try different ID.")
    
    return role

@router.post("/", response_model=role_schema, status_code=status.HTTP_201_CREATED)
async def create_item(role: role_create_schema, role_service : RoleService = Depends(get_role_service), current_user : User = Depends(get_current_user)):
    # Create a new Item instance using Pydantic data
    new_role = await role_service.create(role=role)
    return new_role

@router.put("/{role_id}", response_model=role_schema, responses={404: {"model": InvalidIDResponse}})
async def update_item(role_id: int, role_data: role_update_schema, role_service : RoleService = Depends(get_role_service)):
    # Retrieve the item by ID
    role = role_service.update(role_id=role_id, role_data=role_data)
    return role

@router.delete("/{role_id}", status_code=status.HTTP_204_NO_CONTENT, responses={404: {"model": InvalidIDResponse}})
async def delete_item(role_id: int, role_service : RoleService = Depends(get_role_service)):
    role_service.delete(role_id=role_id)
    # Return no content (204) on successful deletion
    return None