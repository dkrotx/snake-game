from enum import Enum, unique


@unique
class direction(Enum):
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4


class Snake:
    def __init__(self, x, y, field_w, field_h):
        self.body = [(x, y)]
        self.field_w = field_w
        self.field_h = field_h
        self.saved_tail = None

    def __len__(self):
        return len(self.body)

    def _move_coord(self, coord, dir):
        x, y = coord

        if dir == direction.LEFT:
            x -= 1
            if x < 0:
                x = self.field_w - 1
        elif dir == direction.RIGHT:
            x += 1
            if x >= self.field_w:
                x = 0
        elif dir == direction.UP:
            y -= 1
            if y < 0:
                y = self.field_h - 1
        elif dir == direction.DOWN:
            y += 1
            if y >= self.field_h:
                y = 0

        return x,y

    def return_tail(self):
        if self.saved_tail:
            self.body.append(self.saved_tail)
            self.saved_tail = None

    def head(self):
        return self.body[0]

    def move(self, dir):
        assert isinstance(dir, direction)
        # moving is like setting head to new position and removing tail
        self.saved_tail = self.body[-1]
        self.body = [self._move_coord(self.body[0], dir)] + self.body[:-1]
        return self.is_collided()

    def check_move_safe(self, dir):
        if len(self.body) > 1:
            return not self.is_collide_with(*self._move_coord(self.body[0], dir))
        return True

    def is_collided(self):
        return self.body[0] in self.body[1:]

    def is_collide_with(self, x, y):
        return (x, y) in self.body
