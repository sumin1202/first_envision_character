from pico2d import *

Back_Width, Back_Height = 1400, 780

open_canvas(Back_Width, Back_Height)

Slime_P = load_image('run_Pink_Slime.png')
Slime_G = load_image('Green_Slime.png')
Slime_B = load_image('Blue_Slime.png')
BackG = load_image('vv.png')
grass = load_image('grass.png')
block = load_image('bb.png')

running = True

frame = 0
while running:
    clear_canvas()
    BackG.draw(Back_Width // 2, Back_Height // 2)
    Slime_P.clip_draw(frame * 137, 0, 130, 130, 250, 200)
    grass.draw(0, 100)
    block.draw(800, 100)
    frame = (frame + 1) % 4
    update_canvas()
    delay(0.1)
    get_events()

close_canvas()