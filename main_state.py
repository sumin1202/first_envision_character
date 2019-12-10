import random
import json
import os

from pico2d import *
import game_framework
import title_state
import game_world

from slime import Slime, G_Slime, B_Slime
from grass import Grass
from fallingblock import BLOCK, G_BLOCK, B_BLOCK

from background import FixedBackground as Background

name = "MainState"

slime = None
s2 = None
s3 = None
g_slime = None
b_slime = None
grass = None
blocks = None
g_blocks = None
b_blocks = None

check = ((1030, 700), (1600, 900), (2100, 1200), (2600, 1400), (3200, 1800), (3500, 1900),
         (4100, 2100))
check2 = ((750, -10), (1800, -10), (2750, -10), (3400, -10), (4100, -10))
check3 = ((1300, -10), (2100, -10), (2350, -10), (3100, -10), (3800, -10))

def collide(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


def enter():
    global slime, s2, s3
    slime = Slime()
    s2 = G_Slime()
    s3 = B_Slime()
    game_world.add_object(slime, 1)

    global grass
    grass = Grass()
    game_world.add_object(grass, 0)

    # fill here for balls
    global blocks
    blocks = [BLOCK() for i in range(100)]
    for i in range(7):
        blocks[i].pos(check[i])
    game_world.add_objects(blocks, 1)

    global g_blocks
    g_blocks = [G_BLOCK() for i in range(100)]
    for i in range(5):
        g_blocks[i].pos(check2[i])
    game_world.add_objects(g_blocks, 1)

    global b_blocks
    b_blocks = [B_BLOCK() for i in range(100)]
    for i in range(5):
        b_blocks[i].pos(check3[i])
    game_world.add_objects(b_blocks, 1)

    global background
    background = Background()
    game_world.add_object(background, 0)


def exit():
    game_world.clear()


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
            game_framework.quit()
        else:
            slime.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()

    # collision check 슬라임 색깔과 블럭색깔
    global slime, blocks, g_blocks, b_blocks
    for b1 in blocks:
        if collide(slime, b1):
            print(slime.color, b1.b_color)
            if slime.color == b1.b_color:
                blocks.remove(b1)
                game_world.remove_object(b1)
            elif slime.color != b1.b_color:
                game_framework.change_state(title_state)

    for b2 in g_blocks:
       if collide(slime, b2):
           print(slime.color, b2.b_color)
           if slime.color == b2.b_color:
                pass
           else:
                game_framework.change_state(title_state)

   # for b3 in b_blocks:
      #  if collide(slime, b3):
      #      if slime.color == b3.b_color:
      #          pass
        #    else:
         #       game_framework.change_state(title_state)

    # for ball in blocks:
    # if collide(grass, ball):
    # ball.stop()

    if collide(grass, slime):
        slime.y = 180


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()
