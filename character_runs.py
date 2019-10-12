from pico2d import *

Back_Width, Back_Height = 1400, 780

open_canvas(Back_Width, Back_Height)

Slime_P = load_image('run_Pink_Slime.png')
Slime_G = load_image('Green_Slime.png')
Slime_B = load_image('Blue_Slime.png')
jump_P = load_image('jump_Pink_Slime.png')
BackG = load_image('vv.png')
block = load_image('bb.png')

running = True
frame = 0

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            jump_P.clip_draw(frame * 100, 0, 110, 110, 300, 300)


while running:
    clear_canvas()
    BackG.draw(Back_Width // 2, Back_Height // 2)
    Slime_P.clip_draw(frame * 100, 0, 110, 110, 300, 300)
    frame = (frame + 1) % 4
    update_canvas()
    delay(0.1)
    get_events()

close_canvas()