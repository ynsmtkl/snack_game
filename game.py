import pygame
import random
import time
from sys import exit
from enum import Enum


pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
WIDTH = 360
HEIGHT = 630

SCENE_WIDTH = 300
SCENE_HEIGHT = 300


class Direction(Enum):
    TOP = 1
    RIGHT = 2
    BOTTOM = 3
    LEFT = 4


WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
WINDOW.fill(BLACK)

SCENE = pygame.Rect(30, 30, SCENE_WIDTH, SCENE_HEIGHT)
SCENE2 = pygame.Rect(32, 32, SCENE_WIDTH-4, SCENE_HEIGHT-4)

clock = pygame.time.Clock()

Rects = []

Snack_Head = pygame.Rect(150, 150, 10, 10)
Rects.append(Snack_Head)

game = True
Player_moving = False
Last_direction = None


def moving():
    global Last_direction
    global game

    WINDOW.fill(BLACK)
    if Last_direction == Direction.LEFT:
        Rects[0].x -= 11
    elif Last_direction == Direction.RIGHT:
        Rects[0].x += 11
    elif Last_direction == Direction.TOP:
        Rects[0].y -= 11
    elif Last_direction == Direction.BOTTOM:
        Rects[0].y += 11

    for i in range(len(Rects)-1, 0, -1):
        Rects[i].x = Rects[i-1].x
        Rects[i].y = Rects[i-1].y

        if i != 1 and i != 0 and Rects[0].colliderect(Rects[i]):
            game = False

    if Rects[0].x < 32 or Rects[0].y < 32 or Rects[0].x > SCENE_WIDTH + 28 - Rects[0].w or Rects[0].y > SCENE_HEIGHT + 28 - Rects[0].h:
        game = False




def keys_setup():
    global Last_direction

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        if Last_direction != Direction.LEFT:
            Last_direction = Direction.RIGHT
    elif keys[pygame.K_LEFT]:
        if Last_direction != Direction.RIGHT:
            Last_direction = Direction.LEFT
    elif keys[pygame.K_DOWN]:
        if Last_direction != Direction.TOP:
            Last_direction = Direction.BOTTOM
    elif keys[pygame.K_UP]:
        if Last_direction != Direction.BOTTOM:
            Last_direction = Direction.TOP


def updateFood():
    return pygame.Rect(random.randrange(33, SCENE_WIDTH-4), random.randrange(33, SCENE_HEIGHT-4), 10, 10)


def change_rect_coin():
    return pygame.Rect(random.randrange(33, SCENE_WIDTH - 4), random.randrange(33, SCENE_HEIGHT - 4), 10, 10)


game_over = pygame.Rect(WIDTH/2, HEIGHT/2, 50, 50)
FOOD = updateFood()

font_style = pygame.font.SysFont('comicsansms', 25)

# COIN = change_rect_coin()

SCORE = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if not game and event.key == pygame.K_SPACE:
                Rects = []
                Snack_Head.x = 50
                Snack_Head.y = 50
                Snack_Head.width = 10

                Rects.append(Snack_Head)

                updateFood()
                Last_direction = None

                WINDOW.fill(BLACK)
                game = True

    if game:
        keys_setup()
        moving()

        pygame.draw.rect(WINDOW, WHITE, SCENE)

        pygame.draw.rect(WINDOW, BLACK, SCENE2)

        Removed = False
        for R in Rects:
            if R.colliderect(FOOD):
                FOOD = updateFood()
                SCORE = SCORE + 1

                LAST_RECT = Rects[-1]

                NEW_RECT = pygame.Rect(LAST_RECT.x, LAST_RECT.y, 10, 10)
                Rects.append(NEW_RECT)

        # score_text = font_style.render(SCORE, True, WHITE)
        # WINDOW.blit(score_text, WIDTH/2, 3*HEIGHT/4)
            # if R.colliderect(COIN) and not Removed:
            #     Rects.pop()
            #     Removed = True

        # pygame.draw.rect(WINDOW, WHITE, RECT1)
        for Rec in Rects:
            pygame.draw.rect(WINDOW, WHITE, Rec)

        pygame.draw.rect(WINDOW, BLUE, FOOD)

        # if SCORE != 0 and SCORE % 5 == 0:
        #     pygame.draw.rect(WINDOW, ORANGE, COIN)
    else:
        pygame.draw.rect(WINDOW, BLUE, game_over)

    clock.tick(15)
    pygame.display.update()