from pygame.locals import *
from ui.container import *
from ui.locals import *
import pygame

# 0代表start页面 1代表game页面
__current = 1


def getCurrent():
    return __current


def setCurrent(value):
    global __current
    __current = value


class StartPage:
    def __init__(self, surface):
        self.surface = surface

    def graphic(self):
        """渲染"""
        self.surface.fill((0xff, 0x00, 0x00))

    def keydown(self, key):
        """按下事件"""
        print(key)
        if key == K_RETURN:
            # 显示game
            setCurrent(1)

    def keypress(self, key):
        """长按事件"""
        pass


class GamePage:
    def __init__(self, surface):
        self.surface = surface
        self.gameSurface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        self.infoSurface = pygame.Surface((INFO_WIDTH, INFO_HEIGHT))

        # 游戏区
        self.gameContainer = GameContainer(self.gameSurface)
        # 信息区
        self.infoContainer = InfoContainer(self.infoSurface)


    def graphic(self):
        """渲染"""
        self.surface.fill((0x77, 0x77, 0x77))

        # 渲染游戏区
        self.surface.blit(self.gameSurface,(WINDOW_PADDING,WINDOW_PADDING))
        self.gameContainer.graphic()

        # 渲染信息区
        self.surface.blit(self.infoSurface, (2 * WINDOW_PADDING + GAME_WIDTH, WINDOW_PADDING))
        self.infoContainer.graphic()

    def keydown(self, key):
        """按下事件"""
        self.gameContainer.keydown(key)

    def keypress(self, keys):
        """长按事件"""
        self.gameContainer.keypress(keys)
