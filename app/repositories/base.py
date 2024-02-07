from abc import ABC, abstractmethod

class BaseRepository(ABC):
    @abstractmethod
    def create():
        pass

    @abstractmethod
    def update():
        pass

    @abstractmethod
    def remove():
        pass

    @abstractmethod
    def get_by_id(id: str):
        pass
    
    @abstractmethod
    def get_all():
        pass