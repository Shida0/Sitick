from tokenize import Comment
from fastapi import APIRouter
from fastapi.exceptions import HTTPException

from apps.comments.comment_schema import Comment_schema

from .post_service import PostService
from .post_schemas import Post_schema, Post_schema_in

router = APIRouter(
    prefix="/posts",
    tags=["posts"],
)

post_service = PostService()

# get all posts
@router.get("/")
async def get_all_posts() -> list[Post_schema]:
    return await post_service.get_all()

# get post by id
@router.get("/{post_id}")
async def get_post(post_id: int) -> Post_schema|None:
    res = await post_service.get(post_id)
    print(res)
    if res is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return res

#get all comments
@router.get("/{post_id}/comments")
async def get_all_comments(post_id: int) -> list[Comment_schema]:
    try:
        return await post_service.get_all_comments(post_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

# create post
@router.post("/")
async def create_post(post: Post_schema_in) -> Post_schema:
    print(post)
    res = await post_service.create(**post.model_dump())
    if res is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return res
    
# update post
@router.put("/{post_id}")
async def update_post(post_id: int, post: Post_schema_in) -> Post_schema|None:
    res = await post_service.update(post_id, **post.model_dump())
    if res is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return res

# delete post
@router.delete("/{post_id}")
async def delete_post(post_id: int) -> bool|str:
    res = await post_service.delete(post_id)
    if not res:
        raise HTTPException(status_code=404, detail="Post not found")
    return res
