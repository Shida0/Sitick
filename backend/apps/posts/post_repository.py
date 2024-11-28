from models import Post
from models import Comment
from utils import SQLRepository

class PostRepository(SQLRepository):
    def __init__(self):
        super().__init__(
            model=Post,
        )        
