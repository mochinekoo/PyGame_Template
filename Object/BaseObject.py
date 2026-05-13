from abc import ABC, abstractmethod

class BaseObject(ABC):

    objectName: str = None

    def __init__(self, objectName: str):
        self.objectName = objectName

    @abstractmethod
    def init(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def release(self):
        pass