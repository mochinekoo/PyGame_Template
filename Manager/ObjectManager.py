from Object.BaseObject import BaseObject


class ObjectManager:

    instance = None
    objectList: list[BaseObject] = []

    def __init__(self):
        pass

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    @staticmethod
    def getInstance():
        if ObjectManager.instance is None:
            ObjectManager.instance = ObjectManager()
        return ObjectManager.instance

    def initAllObject(self):
        for obj in self.objectList:
            if obj is not None:
                pass
            obj.init()

    def updateAllObject(self):
        for obj in self.objectList:
            if obj is not None:
                obj.update()

    def drawAllObject(self):
        for obj in self.objectList:
            if obj is not None:
                obj.draw()

    def addObject(self, obj: BaseObject):
        self.objectList.append(obj)
        obj.init()

    def removeObject(self, findObj: BaseObject):
        for obj in self.objectList:
            if obj == findObj:
                self.objectList.remove(obj)
                break

    def getAllObject(self):
        return self.objectList

    def clearAllObject(self):
        self.objectList.clear()