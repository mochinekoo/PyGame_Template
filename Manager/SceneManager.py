from Scene.BaseScene import BaseScene
from Scene.RootScene import RootScene

class SceneManager:

    instance = None # インスタンス
    sceneMap: dict[str, BaseScene] = {
        "RootScene": RootScene()
    }
    currentScene: BaseScene = sceneMap["RootScene"]

    def __init__(self):
        pass

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    @staticmethod
    def getInstance():
        if SceneManager.instance is None:
            SceneManager.instance = SceneManager()
        return SceneManager.instance

    def getCurrentScene(self):
        return self.currentScene

    def changeScene(self, sceneName: str):
        scene = self.sceneMap.get(sceneName)
        if scene is not None:
            self.currentScene = scene

