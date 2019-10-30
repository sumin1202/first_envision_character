import random
import json
import os

from pico2d import *

import game_framework
import title_state

name = "MainState"

Back_Width, Back_Height = 1400, 780
character = None
background = None
green_s = None
blue_s = None
block = None
font = None

check = 0
color = 0

class Background:
    def __init__(self):
        self.x, self.y = 700, 390
        self.x1, self.x2 = 2100, 3500
        self.image = load_image('b1.png')

    def update(self):
        self.x -= 10
        self.x1 -= 10
        self.x2 -= 10

    def draw(self):
        self.image.draw(self.x, self.y)
        self.image.draw(self.x1, self.y)
        self.image.draw(self.x2, self.y)

class Character:
    def __init__(self):
        global check, color
        self.frame = 0
        self.cx, self.cy = 270, 190
        self.image = load_image('run_Pink_Slime.png')
        self.dir = 1

    def update(self):
        global check, color
        self.frame = (self.frame + 1) % 4

    def draw(self):
        global check, color
        self.image.clip_draw(self.frame * 100, 0, 105, 110, self.cx, self.cy)
        delay(0.1)

class Green_Slime:
    def __init__(self):
        global check, color
        self.frame = 0
        self.cx, self.cy = 270, 185
        self.image = load_image('green.png')
        self.dir = 1

    def update(self):
        global check, color
        self.frame = (self.frame + 1) % 4

    def draw(self):
        global check, color
        self.image.clip_draw(self.frame * 100, 0, 105, 110, self.cx, self.cy)
        delay(0.1)

class Blue_Slime:
    def __init__(self):
        global check, color
        self.frame = 0
        self.cx, self.cy = 270, 185
        self.image = load_image('blue.png')
        self.dir = 1

    def update(self):
        global check, color
        self.frame = (self.frame + 1) % 4

    def draw(self):
        global check, color
        self.image.clip_draw(self.frame * 100, 0, 105, 110, self.cx, self.cy)
        delay(0.1)

class Block:
    def __init__(self):
        self.bx, self.by = 1000, 100
        self.bx2, self.by2 = 1600, 370
        self.image = load_image('bb.png')

    def update(self):
        self.bx -= 10
        self.bx2 -= 10
        pass

    def draw(self):
        self.image.draw(self.bx, self.by)
        self.image.draw(self.bx2, self.by2)

def enter():
    global character, background, attack_ch, block, green_s, blue_s
    character = Character()
    background = Background()
    blue_s = Blue_Slime()
    green_s = Green_Slime()
    block = Block()
    pass


def exit():
    global character, background, green_s, blue_s
    del(character)
    del(green_s)
    del(blue_s)
    del(block)
    del(background)
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
        elif event.type == SDL_KEYDOWN and event.key == SDLK_q:
            if color == 2:
                color = -1
            color += 1

    pass

def update():
    global check, color
    character.update()
    green_s.update()
    blue_s.update()
    block.update()
    background.update()
    pass


def draw():
    global check, color
    clear_canvas()
    background.draw()
    block.draw()
    if check == 0:
        # pink
        if color == 0:
            character.draw()
        # green
        elif color == 1:
            green_s.draw()
        # blue
        elif color == 2:
            blue_s.draw()
    update_canvas()
    pass