from datetime import datetime
from sqlalchemy import TIMESTAMP, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from .base import Base

class Post(Base):
    __tablename__ = "posts"
    title: Mapped[str] = mapped_column(unique=True)
    content: Mapped[str]
    
    comments: Mapped[list["Comment"]] = relationship(back_populates="post", lazy="selectin") # type: ignore