import game_framework
import start_state
import pico2d

pico2d.open_canvas(1400, 780)
game_framework.run(start_state)
pico2d.close_canvas()