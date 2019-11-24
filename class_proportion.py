from pico2d import*
import random

class Background:
    def __init__(self):
        self.x, self.y = 700, 390
        self.x1, self.x2, self.x3 = 2100, 3500, 4900
        self.image = load_image('b1.png')

    def update(self):
        self.x -= 10
        self.x1 -= 10
        self.x2 -= 10
        self.x3 -= 10

    def draw(self):

        self.image.draw(self.x, self.y)
        self.image.draw(self.x1, self.y)
        self.image.draw(self.x2, self.y)
        self.image.draw(self.x3, self.y)

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

class Jump_p:
    def __init__(self):
        global check, color
        self.frame = 0
        self.cx, self.cy = 270, 260
        self.image = load_image('neum.png')
        self.dir = 1

    def draw(self):
        global check, color
        self.image.draw(self.cx, self.cy)
        delay(0.1)

class Jump_g:
    def __init__(self):
        global check, color
        self.frame = 0
        self.cx, self.cy = 270, 260
        self.image = load_image('neumg.png')
        self.dir = 1

    def draw(self):
        global check, color
        self.image.draw(self.cx, self.cy)
        delay(0.1)

class Jump_b:
    def __init__(self):
        global check, color
        self.frame = 0
        self.cx, self.cy = 270, 260
        self.image = load_image('neumb.png')
        self.dir = 1

    def draw(self):
        global check, color
        self.image.draw(self.cx, self.cy)
        delay(0.1)

class Color:
    def __init__(self):
        self.x, self.y = 120, 720
        self.image = load_image('color.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

class nextStage:
    def __init__(self):
        self.x, self.y = 700, 300
        self.image = load_image('next.png')

    def draw(self):
        self.image.draw(self.x, self.y)

# stage 1
class Block:
    def __init__(self):
        self.bx, self.by = 770, 50
        self.bx2, self.by2 = 1800, 370
        self.image = load_image('b_block.png')

    def update(self):
        self.bx -= 10
        self.bx2 -= 10
        pass

    def draw(self):
        self.image.draw(self.bx, self.by)
        self.image.draw(self.bx2, self.by2)

class GBlock:
    def __init__(self):
        self.bx, self.by = 1200, 50
        self.bx2, self.by2 = 2100, 370
        self.image = load_image('g_block.png')

    def update(self):
        self.bx -= 10
        self.bx2 -= 10
        pass

    def draw(self):
        self.image.draw(self.bx, self.by)
        self.image.draw(self.bx2, self.by2)

class DownBlock:
    def __init__(self):
        self.bx, self.by = 1000, 700
        self.bx2, self.by2 = 1600, 800
        self.image = load_image('p_block.png')

    def update(self):
        r1_y = random.randint(5, 8)
        r2_y = random.randint(3, 5)
        self.bx -= 10
        self.bx2 -= 10
        self.by -= r1_y
        self.by2 -= r2_y


    def draw(self):
        self.image.draw(self.bx, self.by)
        self.image.draw(self.bx2, self.by2)

class HP:
    def __init__(self):
        self.x, self.y = 1150, 720
        self.image = load_image('hp.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)