from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from api.v1.models.admin.role_model import Role  # Assuming User model is in a 'models' folder
from api.v1.schemas.admin.role_schema import CreateRole as role_create_schema 
from config.database import get_db  # Assuming a function to get database session

class RoleService:
    def __init__(self, db : Session) -> None:
        self.db = db

    async def get_all(self):
        # Implement logic for fetching all item
        return self.db.query(Role).all()
    
    async def create(self, role: role_create_schema):
        # Implement logic for item creation (validation, saving to database)
        new_role = Role(**role.model_dump())  # Unpack the Pydantic data
        self.db.add(new_role)
        self.db.commit()
        self.db.refresh(new_role)  # Refresh the object to include the newly generated ID
        return new_role

    def get(self, role_id: int):
        # Implement logic for fetching a specific item by ID
        return self.db.query(Role).filter(Role.id  == role_id).first()

    def update(self, item_id: int, role_data: Role):
        # Implement logic for updating item data
        
        role = self.db.query(Role).filter(Role.id == item_id).first()
        if not role:
            raise HTTPException(status_code=404, detail="Role not found")

        # Update the item's attributes with the provided data
        for field, value in role_data.model_dump(exclude_unset=True).items():
            setattr(role, field, value)  # Update specific attributes as needed
        
        self.db.commit()
        self.db.refresh(role)  # Refresh for updated values
        return role


    def delete(self, role_id: int):
        # Implement logic for deleting a item
        # Retrieve the item by ID
        role = self.db.query(Role).filter(Role.id == role_id).first()
        if not role:
            raise HTTPException(status_code=404, detail="Role not found")

        # Delete the item from the database
        self.db.delete(role)
        self.db.commit()

# Dependency for injecting the database session
def get_role_service(db: Session = Depends(get_db)):
    yield RoleService(db)
