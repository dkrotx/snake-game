from abc import ABCMeta, abstractmethod


class FieldDrawer(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def initField(self, width, height):
        pass

    @abstractmethod
    def drawSnake(self, snake):
        pass

    @abstractmethod
    def drawFood(self, x, y):
        pass

    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def redraw(self):
        pass
