from pydantic import BaseModel, ConfigDict

class ItemBase(BaseModel):
    name: str
    description: str | None = None
    price: float

class CreateItem(ItemBase):
    pass

class Item(ItemBase):
    model_config = ConfigDict(from_attributes = True)
    id: int

class UpdateItem(ItemBase):
    name : str | None = None
    price: float | None = None
    pass