import re
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

class Comment(Base):
    __tablename__ = "comments"
    content: Mapped[str] = mapped_column(nullable=False)
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id", ondelete="CASCADE"), nullable=False)
    
    post: Mapped["Post"] = relationship(back_populates="comments") # type: ignore

    def __repr__(self) -> str:
        return f"Comment(content={self.content}, post_id={self.post_id}, id={self.id}, date_created={self.created_at})"