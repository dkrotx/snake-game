from ui import FieldDrawer
import curses.textpad

class CursesDrawer(FieldDrawer):
    def __init__(self, scr):
        self.scr = scr

    def initField(self, width, height):
        #curses.textpad.rectangle(self.scr, 0,0, height+2, width+2)
        self.wnd = curses.newwin(height+2, width+2, 0, 0)

    def drawSnake(self, snake):
        self.wnd.addch(snake.body[0][1]+1, snake.body[0][0]+1, 's')
        for x, y in snake.body[1:]:
            self.wnd.addch(y+1, x+1, 'S')

    def drawFood(self, x, y):
        self.wnd.addch(y+1, x+1, 'F')

    def clear(self):
        self.wnd.clear()

    def redraw(self):
        self.wnd.border()
        self.wnd.refresh()
