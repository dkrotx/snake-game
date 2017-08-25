from ui import FieldDrawer
from sense_hat import SenseHat

class SenseHatDrawer(FieldDrawer):
    COLOR_SNAKE_HEAD = [255, 255, 255]
    COLOR_SNAKE_BODY = [150, 150, 150]
    COLOR_FOOD = [0, 200, 0]

    def __init__(self, sense):
        self.sense = sense

    def _set_pixel(self, x, y, color):
        self.pixels[y * self.width + x] = color

    def initField(self, width, height):
        self.width = width
        self.height = height
        self.clear()
        self.redraw()

    def drawSnake(self, snake):
        hx, hy = snake.body[0]
        self._set_pixel(hx, hy, self.COLOR_SNAKE_HEAD)

        for x, y in snake.body[1:]:
            self._set_pixel(x, y, self.COLOR_SNAKE_BODY)

    def drawFood(self, x, y):
        self._set_pixel(x, y, self.COLOR_FOOD)

    def clear(self):
        self.pixels = [[0,0,0] for i in range(self.width * self.height)]

    def redraw(self):
        self.sense.set_pixels(self.pixels)
