from typing_extensions import Annotated
from pydantic import BaseModel, StringConstraints, ConfigDict

class UserBase(BaseModel):
    username: str
    first_name: str
    middle_name: str | None = None
    last_name: str
    extension_name : str | None = None
    address: str | None = None
    mobile_number : Annotated[str, StringConstraints(strip_whitespace=True, to_upper=True, pattern=r"^(09|\+639)\d{9}$")]

class CreateUser(UserBase):
    password:str
    pass

class User(UserBase):
    model_config = ConfigDict(from_attributes = True)
    id: int

class UpdateUser(UserBase):
    first_name : str | None = None
    last_name : str | None = None
    username : str | None = None
    mobile_number : Annotated[str, StringConstraints(strip_whitespace=True, to_upper=True, pattern=r"^(09|\+639)\d{9}$")] | None = None

    pass