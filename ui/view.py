import pygame
from ui.locals import *
from ui.action import *


class PlayerTank(Display):

    def __init__(self, **kwargs):
        self.x = kwargs["x"]
        self.y = kwargs["y"]
        self.images = [
            pygame.image.load("img/p1tankU.gif"),
            pygame.image.load("img/p1tankD.gif"),
            pygame.image.load("img/p1tankL.gif"),
            pygame.image.load("img/p1tankR.gif")
        ]
        self.direction = Direction.UP
        # surface
        self.surface = kwargs["surface"]
        # speed
        self.speed = 5

    def display(self):
        image = None

        if self.direction == Direction.UP:
            image = self.images[0]
        elif self.direction == Direction.DOWN:
            image = self.images[1]
        elif self.direction == Direction.LEFT:
            image = self.images[2]
        elif self.direction == Direction.RIGHT:
            image = self.images[3]

        self.surface.blit(image, (self.x, self.y))

    def move(self, direction):
        """移动"""
        # 如果当前的方向和要去走的方向是不同的
        # 1. 只是转方向
        # 2. 转方向+移动

        if self.direction != direction:
            # 1. 只是转方向
            # 改变方向
            self.direction = direction
        else:
            # 方向相同
            if direction == Direction.UP:
                self.y -= self.speed
            elif direction == Direction.DOWN:
                self.y += self.speed
            elif direction == Direction.LEFT:
                self.x -= self.speed
            elif direction == Direction.RIGHT:
                self.x += self.speed

    def fire(self):
        # TODO:
        pass


class wall(Display):
    """砖墙"""

    def __init__(self, **kwargs):
        self.x = kwargs["x"]
        self.y = kwargs["y"]
        self.image = pygame.image.load("img/walls.gif")
        self.surface = kwargs["surface"]

    def display(self):
        self.surface.blit(self.image, (self.x, self.y))

    def destroy(self):
        pass


class Steel(Display):
    """铁墙"""

    def __init__(self, **kwargs):
        self.x = kwargs["x"]
        self.y = kwargs["y"]
        self.image = pygame.image.load("img/steels.gif")
        self.surface = kwargs["surface"]

    def display(self):
        self.surface.blit(self.image, (self.x, self.y))
