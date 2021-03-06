import pygame
from ui.locals import *
from ui.action import *
import time

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
        # 时间延时
        self.__fire_start = 0
        self.__fire_delay = 0.5


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
                # if self.y < 0:
                #     self.y = 0
            elif direction == Direction.DOWN:
                self.y += self.speed
                # if self.y > GAME_HEIGHT - self.height:
                #     self.y = GAME_HEIGHT - self.height
            elif direction == Direction.LEFT:
                self.x -= self.speed
                # if self.x < 0:
                #     self.x = 0
            elif direction == Direction.RIGHT:
                self.x += self.speed
                # if self.x > GAME_WIDTH - self.width:
                #     self.x = GAME_WIDTH - self.width

    def fire(self):
        now = time.time()

        if now -self.__fire_start < self.__fire_delay:
            return None
        self.__fire_start = now

        print("fire")
        # 创建子弹
        x = 0
        y = 0
        if self.direction == Direction.UP:
            x = self.x + self.width / 2
            y = self.y
        elif self.direction == Direction.DOWN:
            x = self.x + self.width / 2
            y = self.y +self.height
        elif self.direction == Direction.LEFT:
            x = self.x
            y = self.y + self.width / 2
        elif self.direction == Direction.RIGHT:
            x = self.x + self.height
            y = self.y + self.width / 2

        return Bullet(x=x,y=y,direction=self.direction,surface=self.surface)

    def is_blocked(self, wall):
        # 判断坦克和墙碰撞

        # 判断坦克下一步的矩形和现在的墙是否碰撞
        next_x = self.x
        next_y = self.y

        if self.direction == Direction.UP:
            next_y -= self.speed
            if next_y < 0:
                self.bad_direction = self.direction
                return True
        elif self.direction == Direction.DOWN:
            next_y += self.speed
            if next_y > GAME_HEIGHT - self.height:
                self.bad_direction = self.direction
                return True
        elif self.direction == Direction.LEFT:
            next_x -= self.speed
            if next_x < 0:
                self.bad_direction = self.direction
                return True
        elif self.direction == Direction.RIGHT:
            next_x += self.speed
            if next_x > GAME_WIDTH - self.width:
                self.bad_direction = self.direction
                return True

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


class WaLL(Display, Block, Destroy):
    """砖墙"""



    def __init__(self, **kwargs):
        self.x = kwargs["x"]
        self.y = kwargs["y"]
        self.image = pygame.image.load("img/walls.gif")
        self.surface = kwargs["surface"]
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        # 生命值
        self.hp = 2


    def display(self):
        self.surface.blit(self.image, (self.x, self.y))

    def destroy(self):
        pass

    def get_hp(self):
        return self.hp

    def receive_beaten(self, power):
        """power 打我者的杀伤力"""
        self.hp -= power

    def is_destroyed(self):
        return self.hp <= 0


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

class Bullet(Display, AutoMove, Destroy):



    def __init__(self, **kwargs):

        self.image = pygame.image.load("img/tankmissile.gif")
        self.surface = kwargs["surface"]
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.direction = kwargs["direction"]
        self.speed = 5
        # x,y
        self.x = kwargs["x"] - self.width / 2
        self.y = kwargs["y"] - self.height / 2
        # 是否回收的状态
        self.__is_destroyed = False
        # 杀伤力
        self.power = 1



    def display(self):
        self.surface.blit(self.image, (self.x, self.y))

    def move(self):
        # 方向相同
        if self.direction == Direction.UP:
            self.y -= self.speed
            if self.y < 0:
                # 出屏幕了， 回收
                self.__is_destroyed = True
        elif self.direction == Direction.DOWN:
            self.y += self.speed
            if self.y > GAME_HEIGHT - self.height:
                # 出屏幕了， 回收
                self.__is_destroyed = True
        elif self.direction == Direction.LEFT:
            self.x -= self.speed
            if self.x < 0:
                # 出屏幕了， 回收
                self.__is_destroyed = True

        elif self.direction == Direction.RIGHT:
            self.x += self.speed
            if self.x > GAME_WIDTH - self.width:
                # 出屏幕了， 回收
                self.__is_destroyed = True

    def is_blocked(self, block):
        # 矩形和矩形的碰撞， 当前矩形
        rect_self = pygame.Rect(self.x, self.y, self.width, self.height)
        rect_wall = pygame.Rect(block.x, block.y, block.width, block.height)

        return pygame.Rect.colliderect(rect_self, rect_wall)


    def is_destroyed(self):
        if self.power <= 0:
            return True

        return self.__is_destroyed

    def get_attack_power(self):
        return self.power

    def receive_attack(self, hp):
        """hp 被打者的生命值"""
        self.power -= hp

