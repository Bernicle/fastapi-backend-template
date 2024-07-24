from pydantic import BaseModel
from api.v1.schemas.admin.user_schema import User as user_schema

class LoginResponse(BaseModel):
    user: user_schema
    access_token: str
    token_type: str
