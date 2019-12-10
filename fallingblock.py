import random
from pico2d import *
import game_world
import game_framework

b_color = 0

class FallingBlock:
    def __init__(self):
        self.x, self.y, self.fall_speed = random.randint(0, 1600 - 1), 60, 0
        FallingBlock.image = load_image('p_block.png')
        self.dir = 1

    def get_bb(self):
        # fill here
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        self.image.draw(self.x, self.y)
        # fill here for draw
        draw_rectangle(*self.get_bb())

    def update(self):
        self.y -= self.fall_speed * game_framework.frame_time
        pass

    #fill here for def stop
    def stop(self):
        self.fall_speed = 0

    def after_collide(self):

        self.x += self.dir * game_framework.frame_time * self.speed
        #self.x = clamp(100, self.x, 1600 - 100)
        pass

# fill here
class BLOCK:
    MIN_FALL_SPEED = 3
    MAX_FALL_SPEED = 5

    image = None
    b_color = 0
    def __init__(self):
        global b_color

        BLOCK.image = load_image('p_block.png')


        self.x, self.y = -100, 0
        self.fall_speed = random.randint(BLOCK.MIN_FALL_SPEED, BLOCK.MAX_FALL_SPEED)

    def update(self):
        global b_color
        num = 10
        self.x -= num
        self.y -= self.fall_speed
        pass

    def pos(self, check):
        self.x = check[0]
        self.y = check[1]

    def get_bb(self):
        global b_color
        return self.x - 70, self.y - 160, self.x + 70, self.y + 150

    def draw(self):
        global b_color
        if self.b_color == 0:
            self.image.draw(self.x, self.y)
        else:
            self.image2.draw(self.x, self.y)

        # fill here for draw
       # draw_rectangle(*self.get_bb())

class G_BLOCK:
    image = None
    b_color = 1

    def __init__(self):
        global b_color
        G_BLOCK.image = load_image('g_block.png')

        self.x, self.y = -100, 0

    def update(self):
        global b_color
        num = 10
        self.x -= num
        pass

    def pos(self, check):
        self.x = check[0]
        self.y = check[1]

    def get_bb(self):
        global cnt
        return self.x - 70, self.y - 160, self.x + 70, self.y + 150

    def draw(self):
        global cnt
        if self.b_color == 1:
            self.image.draw(self.x, self.y)
        # fill here for draw
        #draw_rectangle(*self.get_bb())

class B_BLOCK:
    image = None
    b_color = 2

    def __init__(self):
        global b_color
        B_BLOCK.image = load_image('b_block.png')

        self.x, self.y = -100, 0

    def update(self):
        global b_color
        num = 10
        self.x -= num
        pass

    def pos(self, check):
        self.x = check[0]
        self.y = check[1]

    def get_bb(self):
        global cnt
        return self.x - 70, self.y - 160, self.x + 70, self.y + 150

    def draw(self):
        global cnt
        if self.b_color == 2:
            self.image.draw(self.x, self.y)
        # fill here for draw
       # draw_rectangle(*self.get_bb())
