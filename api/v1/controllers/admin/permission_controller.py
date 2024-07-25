from fastapi import APIRouter, Depends, HTTPException, status

from api.v1.middlewares.auth.authentication import get_current_user
from api.v1.schemas.admin.permission_schema import Permission
from api.v1.services.admin.permission_service import PermissionService, get_permission_service

from api.v1.schemas.admin.permission_schema import Permission as permission_schema, CreatePermission as permission_create_schema, UpdatePermission as permission_update_schema
from api.v1.schemas.Invalid_id_schema import InvalidIDResponse
from config.database  import get_db

router = APIRouter()

@router.get("/", response_model=list[permission_schema])
async def get_permission(user_id:int | None=None, permision_service : PermissionService = Depends(get_permission_service)):
    # ... (Retrieve items from database)
    permissions = None
    if not user_id:
        permissions = await permision_service.get_all()
    else:
        permissions = await permision_service.get_by_user_id(user_id=user_id)
    return permissions

@router.get("/{permisione_id}", response_model=permission_schema, responses={400: {"description": "Permision not found", "model": InvalidIDResponse}})
async def get_permission_by_id(permision_id: int, permision_service : PermissionService = Depends(get_permission_service), current_user : Permission = Depends(get_current_user)):
    # ... (Retrieve item by ID from database)
    permision = permision_service.get(permision_id=permision_id)
    if not permision:
        raise HTTPException(status_code=400, detail=f"The permision with provided ID was not exist. Try different ID.")
    
    return permision

@router.post("/", response_model=permission_schema, status_code=status.HTTP_201_CREATED)
async def create_permission(permission: permission_create_schema, permission_service : PermissionService = Depends(get_permission_service), current_user : Permission = Depends(get_current_user)):
    # Create a new Item instance using Pydantic data
    new_permission = await permission_service.create(permission=permission)
    return new_permission

@router.put("/{permission_id}", response_model=permission_schema, responses={404: {"model": InvalidIDResponse}})
async def update_permission(permission_id: int, permission_data: permission_update_schema, permission_service : PermissionService = Depends(get_permission_service)):
    # Retrieve the item by ID
    permission = permission_service.update(permission_id=permission_id, permission_data=permission_data)
    return permission

@router.delete("/{permission_id}", status_code=status.HTTP_204_NO_CONTENT, responses={404: {"model": InvalidIDResponse}})
async def delete_permission(permission_id: int, permission_service : PermissionService = Depends(get_permission_service)):
    permission_service.delete(permission_id=permission_id)
    # Return no content (204) on successful deletion
    return None