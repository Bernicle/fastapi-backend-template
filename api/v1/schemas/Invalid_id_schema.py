from pydantic import BaseModel

class InvalidIDResponse(BaseModel):
    detail: str
