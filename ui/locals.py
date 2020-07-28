from enum import Enum


# 游戏区域
BLOCK = 60
GAME_WIDTH = 13 * BLOCK
GAME_HEIGHT = 13 * BLOCK

# 信息区域
INFO_WIDTH = 4 * BLOCK
INFO_HEIGHT = GAME_HEIGHT

# 窗体相关
WINDOW_PADDING = 8
WINDOW_WIDTH = 3 * WINDOW_PADDING + GAME_WIDTH + INFO_WIDTH
WINDOW_HEIGHT = 2 * WINDOW_PADDING + GAME_HEIGHT

class Direction(Enum):
    NONE = -1
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3