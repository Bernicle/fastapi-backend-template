from pydantic import BaseModel, ConfigDict

class RoleBase(BaseModel):
    name: str
    description: str | None = None
    price: float

class CreateRole(RoleBase):
    pass

class Role(RoleBase):
    model_config = ConfigDict(from_attributes = True)
    id: int

class UpdateRole(RoleBase):
    name : str | None = None
    pass