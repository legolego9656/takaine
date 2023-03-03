import pygame
import pgzrun
from pgzero.builtins import Actor, animate, keyboard
import random
import time

WIDTH = 1000
HEIGHT = 600
score = 0
game_over = False

pacman = Actor("pacman")
pacman.pos = 100, 200

dot = Actor("enemy")
dot.pos = 500, 500

dot2 = Actor("enemy")
dot2.pos = 500, 500

dot3 = Actor("enemy")
dot3.pos = 500, 500


def draw():
    global score, game_over
    screen.fill("white")
    dot.draw()
    pacman.draw()
    screen.draw.text("Score: " + str(score), color="black", topleft=(10, 10))

    direction = random.randint(1, 4)
    dot_direction = random.randint(1, 4)
    dot2_direction = random.randint(1, 4)
    dot3_direction = random.randint(1, 4)

    length = random.randint(1000, 4000)  # 一歩をやる回数


    speed = 0.2  # 一歩の距離
    n = 20  # nを10と仮定
    # -----------------------------------------------------------------
    for i in range(length):
        if not i % n:
            if direction == 1:
                dot.x = max(dot.x - speed, 0)
            elif direction == 2:
                dot.x = min(dot.x + speed, WIDTH - 1)
            elif direction == 3:
                dot.y = max(dot.y - speed, 0)
            elif direction == 4:
                dot.y = min(dot.y + speed, HEIGHT - 1)

            if dot2_direction == 1:
                dot2.x = max(dot2.x - speed, 0)
            elif dot2_direction == 2:
                dot2.x = min(dot2.x + speed, WIDTH - 1)
            elif dot2_direction == 3:
                dot2.y = max(dot2.y - speed, 0)
            elif dot2_direction == 4:
                dot2.y = min(dot2.y + speed, HEIGHT - 1)

            if dot3_direction == 1:
                dot3.x = max(dot3.x - speed, 0)
            elif dot3_direction == 2:
                dot3.x = min(dot3.x + speed, WIDTH - 1)
            elif dot3_direction == 3:
                dot3.y = max(dot3.y - speed, 0)
            elif dot3_direction == 4:
                dot3.y = min(dot3.y + speed, HEIGHT - 1)

    # -----------------------------------------------------------------

    if game_over:
        screen.fill("black")
        screen.draw.text("Your Score Is " + str(score) + " Congrats!!", topleft=(10, 10), fontsize=60)

    if score >= 500:
        dot2.draw()
    if score >= 750:
        dot3.draw()






def update():
    global score, dot, game_over
    pacman_speed = 5

    if keyboard.left:
        pacman.x = max(pacman.x - pacman_speed, 0)

    elif keyboard.right:
        pacman.x = min(pacman.x + pacman_speed, WIDTH - pacman.width)

    elif keyboard.up:
        pacman.y = max(pacman.y - pacman_speed, 0)

    elif keyboard.down:
        pacman.y = min(pacman.y + pacman_speed, HEIGHT - pacman.height)

    touch = pacman.colliderect(dot) or pacman.colliderect(dot2) or pacman.colliderect(dot3)

    if not game_over:
        score += 1

        if touch:
            game_over = True

    if touch:
        game_over = True


pgzrun.go()
