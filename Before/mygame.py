import pico2d

from Before import start_state
from Before import game_framework

pico2d.open_canvas(1400, 780)
game_framework.run(start_state)
pico2d.close_canvas()