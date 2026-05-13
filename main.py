import sys

import pygame
from pygame.math import Vector2

from Manager.SceneManager import SceneManager

class Main:

    instance = None
    keyFlag = False
    screen = None

    def __init__(self):
        pass

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    @staticmethod
    def getInstance():
        if Main.instance is None:
            Main.instance = Main()
        return Main.instance

    def initGame(self):
        global keyFlag
        # 初期化
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("テストゲームだよ")
        self.screen.fill((0, 255, 0))
        self.runGame()

    def runGame(self):
        clock = pygame.time.Clock()
        # ゲーム
        while True:
            clock.tick(60)
            self.screen.fill((0, 255, 0))
            self.update()
            self.draw()
            pygame.display.flip()

    def draw(self):
        currentScene = SceneManager.getInstance().getCurrentScene()
        if currentScene is not None:
            currentScene.draw()

    def update(self):
        currentScene = SceneManager.getInstance().getCurrentScene()
        if currentScene is not None:
            currentScene.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

if __name__ == '__main__':
    mainInstance = Main.getInstance()
    mainInstance.initGame()