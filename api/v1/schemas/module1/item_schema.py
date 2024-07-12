from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str
    description: str | None = None
    price: float

class CreateItem(ItemBase):
    pass

class Item(ItemBase):
    id: int
    class Config:
        orm_mode = True

class UpdateItem(ItemBase):
    name : str | None = None
    price: float | None = None
    pass