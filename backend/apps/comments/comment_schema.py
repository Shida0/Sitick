from pytz import UTC
from datetime import datetime
from pydantic import BaseModel, ConfigDict

class Comment_schema_in(BaseModel):
    content: str
    post_id: int

class Comment_schema(Comment_schema_in):
    id: int
    
    created_at: datetime = datetime.now(UTC)
    
    model_config = ConfigDict(from_attributes=True)