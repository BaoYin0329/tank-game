import pygame
from ui.locals import *
from ui.action import *


class PlayerTank(Display, Move):

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
        self.speed = 1
        # 错误的方向
        self.bad_direction = Direction.NONE
        # width , height
        self.width = self.images[0].get_width()
        self.height = self.images[0].get_height()


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
        # 如果是错误的方向就不移动了
        if direction == self.bad_direction:
            return

        if self.direction != direction:
            # 1. 只是转方向
            # 改变方向
            self.direction = direction
        else:
            # 方向相同
            if direction == Direction.UP:
                self.y -= self.speed
                if self.y < 0:
                    self.y = 0
            elif direction == Direction.DOWN:
                self.y += self.speed
                if self.y > GAME_HEIGHT - self.height:
                    self.y = GAME_HEIGHT - self.height
            elif direction == Direction.LEFT:
                self.x -= self.speed
                if self.x < 0:
                    self.x = 0
            elif direction == Direction.RIGHT:
                self.x += self.speed
                if self.x > GAME_WIDTH - self.width:
                    self.x = GAME_WIDTH - self.width

    def fire(self):
        # TODO:
        pass
    def is_blocked(self, wall):
        # 判断坦克和墙碰撞

        # 判断坦克下一步的矩形和现在的墙是否碰撞
        next_x = self.x
        next_y = self.y

        if self.direction == Direction.UP:
            next_y -= self.speed
        elif self.direction == Direction.DOWN:
            next_y += self.speed
        elif self.direction == Direction.LEFT:
            next_x -= self.speed
        elif self.direction == Direction.RIGHT:
            next_x += self.speed

        # 矩形和矩形的碰撞， 当前矩形
        rect_self = pygame.Rect(next_x, next_y, self.width, self.height)
        rect_wall = pygame.Rect(wall.x, wall.y, wall.width, wall.height)

        collide = pygame.Rect.colliderect(rect_self, rect_wall)
        if collide:
            # 碰撞了,当前的方向是错误的方向
            self.bad_direction = self.direction
            return True
        else:
            # 没有错误方向
            self.bad_direction = Direction.NONE
            return False


class WaLL(Display, Block):
    """砖墙"""

    def __init__(self, **kwargs):
        self.x = kwargs["x"]
        self.y = kwargs["y"]
        self.image = pygame.image.load("img/walls.gif")
        self.surface = kwargs["surface"]
        self.width = self.image.get_width()
        self.height = self.image.get_height()


    def display(self):
        self.surface.blit(self.image, (self.x, self.y))

    def destroy(self):
        pass


class Steel(Display, Block):
    """铁墙"""

    def __init__(self, **kwargs):
        self.x = kwargs["x"]
        self.y = kwargs["y"]
        self.image = pygame.image.load("img/steels.gif")
        self.surface = kwargs["surface"]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def display(self):
        self.surface.blit(self.image, (self.x, self.y))

class Water(Display):
    """水"""

    def __init__(self, **kwargs):
        self.x = kwargs["x"]
        self.y = kwargs["y"]
        self.image = pygame.image.load("img/water.gif")
        self.surface = kwargs["surface"]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def display(self):
        self.surface.blit(self.image, (self.x, self.y))

class Grass(Display, Order):
    """丛林"""

    def __init__(self, **kwargs):
        self.x = kwargs["x"]
        self.y = kwargs["y"]
        self.image = pygame.image.load("img/grass.png")
        self.surface = kwargs["surface"]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def display(self):
        self.surface.blit(self.image, (self.x, self.y))

    def get_order(self):
        return 100