from pydantic import BaseModel, ConfigDict

class PermissionBase(BaseModel):
    user_id: int
    role_id: int
    module: float
    submodule: str
    permissions: str

class CreatePermission(PermissionBase):
    pass

class Permission(PermissionBase):
    model_config = ConfigDict(from_attributes = True)
    id: int

class UpdatePermission(PermissionBase):
    pass