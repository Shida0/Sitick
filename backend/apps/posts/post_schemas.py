from datetime import datetime
from pydantic import BaseModel, ConfigDict
from pytz import UTC

class Post_schema_in(BaseModel):
    title: str
    content: str

class Post_schema(Post_schema_in):
    id: int
    
    created_at: datetime = datetime.now(UTC)
    
    model_config = ConfigDict(from_attributes=True)