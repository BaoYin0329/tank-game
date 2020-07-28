from abc import *

# abstract class
from abc import ABC

"""
1. 导入模块
2. 类中metaclass=ABCMeta
3. @abstractmethod修饰方法
"""
class Display(metaclass=ABCMeta):
    """
    抽象类：规范显示行为
    """
    @abstractmethod
    def display(self):
        """显示"""
        pass

class Move(metaclass=ABCMeta):
    """移动的规范"""
    @abstractmethod
    def move(self, direction):
        pass
    @abstractmethod
    def is_blocked(self, block):
        pass

class Block(metaclass=ABCMeta):
    """阻塞的规范"""
    pass

class Order(metaclass=ABCMeta):
    """排序显示"""
    @abstractmethod
    def get_order(self):
        pass

class AutoMove(Move, ABC):
    """自动移动"""
    pass

class Destroy(metaclass=ABCMeta):
    """回收的规范"""

    @abstractmethod
    def is_destroyed(self):
        pass

