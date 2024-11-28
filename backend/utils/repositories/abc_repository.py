from abc import ABCMeta, abstractmethod
from typing import Any
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncEngine

class ABCRepository(metaclass=ABCMeta):
    @abstractmethod
    async def __init__(self, model):
        pass
    
    @abstractmethod
    async def create(self, **kwargs) -> Any:
        pass
    
    @abstractmethod
    async def get_all(self) -> list:
        pass
    
    @abstractmethod
    async def get(self, obj_id: int) -> Any:
        pass
    
    @abstractmethod
    async def update(self, obj_id: int, **kwargs) -> Any:
        pass
    
    @abstractmethod
    async def delete(self, obj_id: int) -> bool|str:
        pass