import uuid
from pydantic import BaseModel, Field
from datetime import datetime


class Message(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, alias="_id")
    text: str = Field(...)
    timestamp: datetime = Field(default_factory= datetime.now)

    class Config:
        json_schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "text": "Hello",
                "timestamp": "20230108"
            }
        }
