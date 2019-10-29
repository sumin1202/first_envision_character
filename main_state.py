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
attack_ch = None
block = None
font = None

check = 0

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
        global check
        self.frame = 0
        self.cx, self.cy = 270, 190
        self.image = load_image('run_Pink_Slime.png')
        self.dir = 1

    def update(self):
        global check
        self.frame = (self.frame + 1) % 4

    def draw(self):
        global check
        self.image.clip_draw(self.frame * 100, 0, 105, 110, self.cx, self.cy)
        delay(0.1)

class Attack_Slime:
    def __init__(self):
        self.frame = 0
        self.cx, self.cy = 270, 190
        self.image = load_image('neum.png')
        self.dir = 1

    def update(self):
        self.frame = (self.frame + 1) % 4

    def draw(self):
        self.image.draw(self.cx, self.cy)
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
    global character, background, attack_ch, block
    character = Character()
    attack_ch = Attack_Slime()
    background = Background()
    block = Block()
    pass


def exit():
    global character, background, attack_ch
    del(attack_ch)
    del(character)
    del(block)
    del(background)
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    global check
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            check = 1
    pass

def update():
    global check
    character.update()
    attack_ch.update()
    block.update()
    background.update()
    pass


def draw():
    global check
    clear_canvas()
    background.draw()
    block.draw()
    if check == 1:
        attack_ch.draw()
        check = 0
    else:
        character.draw()
    update_canvas()
    pass