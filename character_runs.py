from pico2d import *
open_canvas()

Slime_P = load_image('run_Pink_Slime.png')
Slime_G = load_image('Green_Slime.png')
Slime_B = load_image('Blue_Slime.png')

isDone = True

x = 0
frame = 0
while True:
    clear_canvas()
    while True:
        Slime_P.draw_now(100, 90)
        update_canvas()
    delay(0.01)
    get_events()

close_canvas()

