from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from api.v1.models.admin.permission_model import Permission  # Assuming User model is in a 'models' folder
from api.v1.schemas.admin.permission_schema import CreatePermission 
from config.database import get_db  # Assuming a function to get database session

class PermissionService:
    def __init__(self, db : Session) -> None:
        self.db = db

    async def get_all(self) -> list[Permission]:
        # Implement logic for fetching all item
        return self.db.query(Permission).all()
    
    async def create(self, permission: CreatePermission) -> Permission:
        # Implement logic for item creation (validation, saving to database)
        new_permission = Permission(**permission.model_dump())  # Unpack the Pydantic data
        self.db.add(new_permission)
        self.db.commit()
        self.db.refresh(new_permission)  # Refresh the object to include the newly generated ID
        return new_permission

    
    def get_by_user_id(self, user_id: int) -> list[Permission]:
        # Implement logic for fetching a specific item by ID
        return self.db.query(Permission).filter(Permission.user_id  == user_id).all()

    def get(self, permission_id: int) -> Permission:
        # Implement logic for fetching a specific item by ID
        return self.db.query(Permission).filter(Permission.id  == permission_id).first()

    def update(self, permission_id: int, permission_data: Permission) -> Permission:
        # Implement logic for updating item data
        
        permission = self.db.query(Permission).filter(Permission.id == permission_id).first()
        if not permission:
            raise HTTPException(status_code=404, detail="Permission not found")

        # Update the item's permission_datas with the provided data
        for field, value in permission_data.model_dump(exclude_unset=True).items():
            setattr(permission, field, value)  # Update specific attributes as needed
        
        self.db.commit()
        self.db.refresh(permission)  # Refresh for updated values
        return permission


    def delete(self, permission_id: int):
        # Implement logic for deleting a item
        # Retrieve the item by ID
        permission = self.db.query(Permission).filter(Permission.id == permission_id).first()
        if not permission:
            raise HTTPException(status_code=404, detail="Permission not found")

        # Delete the item from the database
        self.db.delete(permission)
        self.db.commit()

# Dependency for injecting the database session
def get_permission_service(db: Session = Depends(get_db)):
    yield PermissionService(db)
