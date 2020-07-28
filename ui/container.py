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
        file = open("map/1.map", "r", encoding="utf-8")
        # row = 0
        # for line in file:
        #     print(line)
        #     row +=1

        for row, line in enumerate(file):
            # 去掉换行符
            texts = line.strip()
            for column, text in enumerate(texts):
                # print("row:{}, column:{}, text:{}".format(row, column, text))
                x = column * BLOCK
                y = row * BLOCK
                if text == "砖":
                    self.views.append(WaLL(surface=self.surface, x=x, y=y))
                if text == "铁":
                    self.views.append(Steel(surface=self.surface, x=x, y=y))
                if text == "水":
                    self.views.append(Water(surface=self.surface, x=x, y=y))
                if text == "草":
                    self.views.append(Grass(surface=self.surface, x=x, y=y))
                if text == "主":
                    self.player = PlayerTank(surface=self.surface, x=x, y=y)
                    self.views.append(self.player)

        file.close()

    def __sort(self, view):
        return view.get_order() if isinstance(view, Order) else 0

    def graphic(self):
        """渲染"""
        # 清屏
        self.surface.fill((0x00, 0x00, 0x00))
        # 对列表进行排序， 排序的标准
        # self.views.sort(key=lambda view: view.get_order() if isinstance(view, Order) else 0)
        self.views.sort(key=self.__sort)
        # self.views = sorted(self.views,key=self.__sort)
        print(len(self.views))
        # 判断物体是否需要回收
        for view in list(self.views):
            if isinstance(view, Destroy) and view.is_destroyed():
                self.views.remove(view)

        # 遍历列表，让所有的元素显示
        for view in self.views:
            view.display()
        # 判断墙和坦克是否发生碰撞
        # 判断 可移动的物体 是否和 可阻挡移动的物体 发生了碰撞

        # for view in self.views:
        #     if isinstance(view, WaLL):
        #         # 墙
        #         if self.player.is_blocked(view):
        #             # 墙 和坦克碰撞
        #             break

        # for block in self.views:
        #     # 找出所有课阻塞移动的物体
        #     if isinstance(block, Block):
        #         for move in self.views:
        #             if isinstance(move, Move):
        #                 if move.is_blocked(block):
        #                     # 移动的物体被阻塞的物体挡住了
        #                     break

        # 移动和阻塞的碰撞检测
        for move in self.views:
            if isinstance(move, Move):
                for block in self.views:
                    # 找出所有课阻塞移动的物体
                    if isinstance(block, Block):
                        if move.is_blocked(block):
                            # 移动的物体被阻塞的物体挡住了
                            break

        # 具备自动移动的物体， 让他自己移动
        for auoMove in self.views:
            if isinstance(auoMove, AutoMove):
                auoMove.move()

        # 子弹和砖墙的碰撞
        for bullet in self.views:
            if isinstance(bullet, Bullet):
                for wall in self.views:
                    if isinstance(wall, WaLL) and bullet.is_blocked(wall):
                        # 判断子弹和墙是否发生碰撞

                        # 根据子弹的杀伤力和墙的生命值
                        # 杀伤力
                        power = bullet.get_attack_power()
                        # 生命值
                        hp = wall.get_hp()

                        # 子弹杀伤力会减弱
                        bullet.receive_attack(hp)
                        # 墙的生命值也会减弱
                        wall.receive_beaten(power)

                        break

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
        if keys[K_RETURN]:
            # 发射子弹
            # self.views.append(self.player.fire())
            self._add_view(self.player.fire())

    def _add_view(self, view):
        if isinstance(view, Display):
            self.views.append(view)


class InfoContainer:
    def __init__(self, surface):
        self.surface = surface

    def graphic(self):
        """渲染"""
        self.surface.fill((0x00, 0x00, 0xff))
