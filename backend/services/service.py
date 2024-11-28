from typing import Any
from utils import ABCRepository
from sqlalchemy.ext.asyncio import AsyncEngine
from pydantic import BaseModel

class Service:
    def __init__(self, repository: ABCRepository, schema: BaseModel, model):
        self.repository = repository
        self.schema = schema
    
    async def create(self, **kwargs) -> BaseModel:
        print(kwargs)
        obj = await self.repository.create(**kwargs)
        return self.schema.model_validate(obj)
    
    async def get(self, obj_id: int) -> BaseModel:
        obj = await self.repository.get(obj_id)
        if obj is None:
            return None
        return self.schema.model_validate(obj)
    
    async def get_all(self) -> list[BaseModel]:
        objs = await self.repository.get_all()
        return [self.schema.model_validate(obj) for obj in objs]
    
    async def update(self, obj_id: int, **kwargs) -> BaseModel:
        obj = await self.repository.update(obj_id, **kwargs)
        if obj is None:
            return None
        return self.schema.model_validate(obj)
    
    async def delete(self, obj_id: int) -> bool|str:
        return await self.repository.delete(obj_id)