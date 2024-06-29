from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str
    description: str | None = None

class CreateItem(ItemBase):
    pass

class Item(ItemBase):
    id: int
    class Config:
        orm_mode = True