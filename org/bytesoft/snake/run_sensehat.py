#!/usr/bin/python3
import time
from sensehat_ui import SenseHatDrawer
from sense_hat import SenseHat, ACTION_RELEASED
from engine import Engine

def main(sense):
    engine = Engine(SenseHatDrawer(sense), 8, 8)

    def pushed_up(event):
        if event.action != ACTION_RELEASED:
            engine.turn_up()
    
    def pushed_down(event):
        if event.action != ACTION_RELEASED:
            engine.turn_down()

    def pushed_left(event):
        if event.action != ACTION_RELEASED:
            engine.turn_left()

    def pushed_right(event):
        if event.action != ACTION_RELEASED:
            engine.turn_right()

    sense.stick.direction_up = pushed_up
    sense.stick.direction_down = pushed_down
    sense.stick.direction_left = pushed_left
    sense.stick.direction_right = pushed_right

    engine.start()
    while not engine.is_finished():
        time.sleep(1)

    score = engine.score()
    engine.join()

    sense.show_message(str(score))
    print("Final score: %d" % score)


while True:
    main(SenseHat())
