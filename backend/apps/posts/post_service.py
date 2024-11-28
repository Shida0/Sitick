from apps.comments.comment_schema import Comment_schema, Comment_schema_in
from models import Post
from .post_repository import PostRepository
from services import Service
from .post_schemas import Post_schema


class PostService(Service):
    def __init__(self):
        super().__init__(
            repository=PostRepository(),
            schema=Post_schema,
            model=Post,
        )
    
    async def get_all_comments(self, id: int) -> list[Comment_schema]:
        post = await self.repository.get(id)
        print(post.comments[0])
        if post:
            return [Comment_schema.model_validate(comment) for comment in post.comments]
        raise ValueError("Post not found")