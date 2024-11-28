from services import Service
from models.comment import Comment
from .comment_schema import Comment_schema
from .comment_repository import CommentRepository


class CommentService(Service):
    def __init__(self):
        super().__init__(
            CommentRepository(), 
            Comment_schema,
            Comment
        )

        