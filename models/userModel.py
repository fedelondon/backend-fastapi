from pydantic import BaseModel, Field
import uuid


class User(BaseModel):
    id: str = Field(default=uuid.uuid4, alias="_id")
    name: str
    lastname: str
    identification: int