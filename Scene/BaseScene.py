from abc import ABC, abstractmethod

class BaseScene(ABC):

    sceneName: str = None

    def __init__(self, sceneName: str):
        self.sceneName = sceneName
        self.sceneCounter = 0

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