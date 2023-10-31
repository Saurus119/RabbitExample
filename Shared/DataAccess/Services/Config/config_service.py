from typing import Union
from abc import ABC, abstractmethod
from Shared.DataAccess.Config import db_session

class DBService(ABC):

    def __init__(self) -> None:
        self.db = db_session

    @abstractmethod
    def get(self, filter: object):
        pass

    @abstractmethod
    def create(self, data: object):
        pass

    @abstractmethod
    def update(self, id: int, data: object):
        pass

    @abstractmethod
    def delete(self, id: int):
        pass