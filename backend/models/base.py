from datetime import datetime
from sqlalchemy.types import TIMESTAMP
from sqlalchemy import func
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped

class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now(), type_=TIMESTAMP(timezone=True))