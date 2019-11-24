from pico2d import *

import class_proportion
import title_state
import game_framework

name = "MainState"

Back_Width, Back_Height = 1400, 780
background = None

pink_s = None
green_s = None
blue_s = None

jp = None
jg = None
jb = None

block = None
downb = None
font = None

next = None
hp = None

check = 0
color = 0

def enter():
    global background, block, pink_s, green_s, blue_s, jp, jg, jb, downb, hp
    pink_s = class_proportion.Character()
    background = class_proportion.Background()
    blue_s = class_proportion.Blue_Slime()
    green_s = class_proportion.Green_Slime()
    jp = class_proportion.Jump_p()
    jg = class_proportion.Jump_g()
    jb = class_proportion.Jump_b()
    block = class_proportion.Block()
    downb = class_proportion.DownBlock()
    hp = class_proportion.HP()
    pass


def exit():
    global pink_s, background, green_s, blue_s, jp, jg, jb, downb, hp
    del(pink_s)
    del(green_s)
    del(blue_s)
    del(jp)
    del(jg)
    del(jb)
    del(block)
    del(background)
    del(downb)
    del(hp)
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    global check, color
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        # change color
        elif event.type == SDL_KEYDOWN and event.key == SDLK_q:
            if color == 2:
                color = -1
            color += 1
        # jump character
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            check = 1
            pass
    pass

def update():
    global check, color
    pink_s.update()
    green_s.update()
    blue_s.update()
    block.update()
    background.update()
    downb.update()
    hp.update()
    pass


def draw():
    global check, color
    clear_canvas()
    background.draw()
    #block.draw()
    downb.draw()
    hp.draw()
    # just running
    if check == 0:
        # pink
        if color == 0:
            pink_s.draw()
        # green
        elif color == 1:
            green_s.draw()
        # blue
        elif color == 2:
            blue_s.draw()
    # jump character
    elif check == 1:
        # pink
        if color == 0:
            jp.draw()
            check = 0
        # green
        elif color == 1:
            jg.draw()
            check = 0
        # blue
        elif color == 2:
            jb.draw()
            check = 0
    update_canvas()
    pass