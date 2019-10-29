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
font = None

#Character Event


class Background:
    def __init__(self):
        self.x, self.y = 700, 390
        self.x1, self.y1 = 2100, 390
        self.image = load_image('b1.png')

    def update(self):
        self.x -= 2
        self.x1 -= 2

    def draw(self):
        self.image.draw(self.x, self.y)
        self.image.draw(self.x1, self.y1)

class Character:
    def __init__(self):
        self.frame = 0
        self.image = load_image('run_Pink_Slime.png')
        self.dir = 1

    def update(self):
        self.frame = (self.frame + 1) % 4

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 110, 110, 270, 190)
        delay(0.1)

class Attack_Character:
    def __init__(self):
        self.frame = 0
        self.image2 = load_image('jump_Pink_Slime')

def enter():
    global character, background
    character = Character()
    background = Background()
    pass


def exit():
    global character, background
    del(character)
    del(background)
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            pass
    pass


def update():
    character.update()
    background.update()
    pass


def draw():
    clear_canvas()
    background.draw()
    character.draw()
    update_canvas()
    pass