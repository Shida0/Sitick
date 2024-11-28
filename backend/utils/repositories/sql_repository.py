from typing import Any
from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncEngine

from .abc_repository import ABCRepository
from utils.engine import engine


class SQLRepository(ABCRepository):
    def __init__(self, model):
        self.session_factory = async_sessionmaker(bind=engine)
        self.model = model
    
    async def create(self, **kwargs) -> Any:
        """create one object and add it to the database"""
        async with self.session_factory() as session:
            new_obj = self.model(**kwargs)
            session.add(new_obj)
            await session.commit()
            await session.refresh(new_obj)
            return new_obj
        
    async def get_all(self) -> list:
        """get all objects from the database"""
        async with self.session_factory() as session:
            objs = await session.execute(select(self.model))
            return objs.scalars().all()
        
    async def get(self, obj_id: int) -> Any:
        """get one object from the database by its id"""
        async with self.session_factory() as session:
            obj = await session.execute(select(self.model).where(self.model.id == obj_id))
            return obj.scalars().first()        
        
    async def update(self, obj_id: int, **kwargs) -> Any:
        """update one object in the database by its id"""
        async with self.session_factory() as session:
            await session.execute(update(self.model).where(self.model.id == obj_id).values(**kwargs))
            await session.commit()
            return await self.get(obj_id)
        
    async def delete(self, obj_id: int) -> bool|str:
        """delete one object from the database by its id"""
        async with self.session_factory() as session:

            obj = await self.get(obj_id)
            if obj is None:
                return False
            
            await session.execute(delete(self.model).where(self.model.id == obj_id))
            await session.commit()                                
            
            return True    
         