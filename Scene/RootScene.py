import pygame.draw

from Manager.ObjectManager import ObjectManager
from Object.TestObject import TestObject
from Scene.BaseScene import BaseScene
from abc import ABC, abstractmethod

class RootScene(BaseScene):

    def __init__(self):
        super().__init__("RootScene")

    def init(self):
        ObjectManager.getInstance().addObject(TestObject())

    def update(self):
        self.sceneCounter += 1

    def draw(self):
        pass

    def release(self):
        pass