from ui.view import *
from pygame.locals import *

class GameContainer:
    """

    """

    # 1. 可以通过列表去管理所有的显示元素
    # 2.

    def __init__(self, surface):
        self.surface = surface
        self.views = []

        # 通过读文件来加载元素
        file = open("map/0.map", "r", encoding="utf-8")
        row = 0

        # for line in file:
        #     print(line)
        #     row +=1

        for row, line in enumerate(file):
            texts = line.strip()
            for column, text in enumerate(texts):
                print("row:{}, column:{}, text:{}".format(row, column, text))
                x = column * BLOCK
                y = row * BLOCK
                if text == "砖":
                    self.views.append(wall(surface=self.surface, x=x, y=y))
                if text == "铁":
                    self.views.append(Steel(surface=self.surface, x=x, y=y))
                if text == "主":
                    self.player = PlayerTank(surface=self.surface, x=x, y=y)
                    self.views.append(self.player)


        file.close()

        # # 玩家坦克
        # self.player = PlayerTank(surface=self.surface)
        # self.views.append(self.player)
        #
        # # 砖墙
        # self.wall = wall(surface=self.surface, x=200, y=200)
        # self.views.append(self.wall)
        # # 砖墙2
        # self.wall2 = wall(surface=self.surface, x=300, y=300)
        # self.views.append(self.wall2)
        #
        # # 铁墙
        # self.steel = Steel(surface=self.surface, x=400, y=400)
        # self.views.append(self.steel)

    def graphic(self):
        """渲染"""
        # 清屏
        self.surface.fill((0x00, 0x00, 0x00))

        # 遍历列表，让所有的元素显示
        for view in self.views:
            view.display()

    def keydown(self, key):
        """按下事件"""
        pass

    def keypress(self, keys):
        """长按事件"""
        if keys[K_a]:
            # 向左移动
            self.player.move(Direction.LEFT)
        if keys[K_d]:
            self.player.move(Direction.RIGHT)
        if keys[K_w]:
            self.player.move(Direction.UP)
        if keys[K_s]:
            self.player.move(Direction.DOWN)


class InfoContainer:
    def __init__(self, surface):
        self.surface = surface

    def graphic(self):
        """渲染"""
        self.surface.fill((0x00, 0x00, 0xff))
