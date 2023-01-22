import pygame
from enum import Enum
from sys import exit

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


class Game:
    def __init__(self):
        snack = []
        Win = pygame.display.set_mode((WIDTH, HEIGHT))
        Win.fill(BLACK)

    def updateUi(self):
        pass
