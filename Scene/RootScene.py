import pygame.draw

from Scene.BaseScene import BaseScene
from abc import ABC, abstractmethod

class RootScene(BaseScene):

    def __init__(self):
        super().__init__("RootScene")

    def init(self):
        pass

    def update(self):
        self.sceneCounter += 1

    def draw(self):
        screen = pygame.display.get_surface()
        pygame.draw.rect(screen,(255,0,0),(100,100,180,150),5)

    def release(self):
        pass