from fastapi import APIRouter, Depends, HTTPException

from apps.comments.comment_schema import Comment_schema, Comment_schema_in

from .comment_service import CommentService

crouter = APIRouter(
    prefix="/comments",
    tags=["comments"],
)

comment_service = CommentService()

@crouter.post("/add")
async def add(comment: Comment_schema_in) -> Comment_schema:
    try:
        return await comment_service.create(**comment.model_dump())
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@crouter.put("/update")
async def update(id: int, content: str) -> Comment_schema:
    return await comment_service.update(id, content=content)

@crouter.delete("/delete")
async def delete(id: int) -> bool:
    return await comment_service.delete(id)
