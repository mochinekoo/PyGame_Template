from Manager.ObjectManager import ObjectManager
from Scene.BaseScene import BaseScene
from Scene.RootScene import RootScene

class SceneManager:

    instance = None # インスタンス
    sceneMap: dict[str, BaseScene] = {
        "RootScene": RootScene()
    }
    currentScene: BaseScene = None

    def __init__(self):
        self.changeScene("RootScene")

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
            ObjectManager.getInstance().clearAllObject()
            self.currentScene = scene
            self.currentScene.init()

