import pygame.draw

from Object.TestObject import TestObject
from Scene.BaseScene import BaseScene
from abc import ABC, abstractmethod

class RootScene(BaseScene):

    testObj: TestObject = None

    def __init__(self):
        super().__init__("RootScene")

    def init(self):
        self.testObj = TestObject()
        self.testObj.init()

    def update(self):
        self.sceneCounter += 1
        self.testObj.update()

    def draw(self):
        self.testObj.draw()

    def release(self):
        pass