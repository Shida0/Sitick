from typing import Any

from models import Comment
from utils import SQLRepository
from apps.posts.post_repository import PostRepository

class CommentRepository(SQLRepository):
    def __init__(self):
        super().__init__(Comment)
    
    async def create(self, **kwargs) -> Any:
        post_id = kwargs.get("post_id")
        
        if await PostRepository().get(post_id) is None:
            raise ValueError("Post not found")  
        
        return await super().create(**kwargs)
    