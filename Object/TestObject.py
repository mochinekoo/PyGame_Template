import pygame.draw
from pygame import Rect
from pygame.constants import K_RIGHT, K_LEFT
from pygame.math import Vector2

from Object.BaseObject import BaseObject
from Scene.BaseScene import BaseScene
from abc import ABC, abstractmethod

class TestObject(BaseObject):

    def __init__(self):
        super().__init__("TestObject")
        global location, vector
        location = Vector2(100, 50)
        vector = Vector2(1, 0)

    def init(self):
        pass

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            location.x -= 1
        if keys[K_RIGHT]:
            location.x += 1


    def draw(self):
        screen = pygame.display.get_surface()
        pygame.draw.rect(screen,(255,0,0), pygame.Rect(location.x, location.y, 100, 100))

    def release(self):
        pass