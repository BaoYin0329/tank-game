from abc import *

# abstract class
"""
1. 导入模块
2. 类中metaclass=ABCMeta
3. @abstractclassmethod修饰方法
"""
class Display(metaclass=ABCMeta):
    """
    抽象类：规范显示行为
    """
    @abstractclassmethod
    def display(self):
        """显示"""
        pass