import sys

import pygame
from pygame.math import Vector2

keyFlag = False
location = Vector2(100, 50)
vector = Vector2(1, 0)

def initGame():
    global keyFlag
    # 初期化
    pygame.init()
    global screen
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("テストゲームだよ")
    screen.fill((0, 255, 0))
    runGame()

def runGame():
    clock = pygame.time.Clock()
    # ゲーム
    while True:
        clock.tick(60)
        screen.fill((0, 255, 0))
        update()
        draw()
        pygame.display.flip()

def draw():
    pass

def update():
    global keyFlag

    keys = pygame.key.get_pressed()

    if keys[pygame.K_0]:
        keyFlag = True
    if keys[pygame.K_d]:
        location.x += vector.x
    if keys[pygame.K_a]:
        location.x -= vector.x
    if keys[pygame.K_w]:
        location.y -= vector.x
    if keys[pygame.K_s]:
        location.y += vector.x

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_0:
                keyFlag = False

if __name__ == '__main__':
    initGame()