from ui import FieldDrawer
import time
from snake import Snake, direction
import threading
import random

class Food:
    def __init__(self, x, y):
        self.coord = (x, y)
        self.creation_time = time.time()


class Engine(threading.Thread):
    def __init__(self, drawer, field_w, field_h):
        super().__init__()
        assert isinstance(drawer, FieldDrawer)
        self.field_w = field_w
        self.field_h = field_h
        self.drawer = drawer
        self.drawer.initField(field_w, field_h)
        self.snake = Snake(3, 3, field_w, field_h)
        self.dir = direction.DOWN
        self._quit = False
        self.food = None
        self.finished = False

    def is_finished(self):
        return self.finished

    def make_food(self):
        while True:
            x, y = random.randint(0, self.field_w-1), random.randint(0, self.field_h-1)
            if not self.snake.is_collide_with(x, y):
                return Food(x, y)

    def _set_direction_checked(self, dir):
        if self.snake.check_move_safe(dir):
            self.dir = dir

    def turn_left(self):
        self._set_direction_checked(direction.LEFT)

    def turn_right(self):
        self._set_direction_checked(direction.RIGHT)

    def turn_up(self):
        self._set_direction_checked(direction.UP)

    def turn_down(self):
        self._set_direction_checked(direction.DOWN)

    def _step(self):
        self.snake.move(self.dir)
        if self.food and self.snake.head() == self.food.coord:
            self.snake.return_tail()
            self.food = None

        if self.snake.is_collided():
            self.finished = True

        if not self.food:
            self.food = self.make_food()

    def _redraw_scene(self):
        self.drawer.clear()
        self.drawer.drawFood(*self.food.coord)
        self.drawer.drawSnake(self.snake)
        self.drawer.redraw()

    def run(self):
        while not self._quit:
            time.sleep(0.3)
            self._step()
            if self.finished:
                return
            self._redraw_scene()

    def quit(self):
        self._quit = True
