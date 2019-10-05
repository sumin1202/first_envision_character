from pico2d import *

Back_Width, Back_Height = 960, 540

open_canvas(Back_Width, Back_Height)

Slime_P = load_image('run_Pink_Slime.png')
Slime_G = load_image('Green_Slime.png')
Slime_B = load_image('Blue_Slime.png')
BackG = load_image('background.png')

running = True

frame = 0
while running:
    clear_canvas()
    BackG.draw(Back_Width // 2, Back_Height // 2)
    Slime_P.clip_draw(frame * 100, 0, 100, 100, 200, 200)
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.02)
    get_events()

close_canvas()

