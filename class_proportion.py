from pico2d import*
import random

class Background:
    def __init__(self):
        self.x, self.y = 700, 390
        self.x1, self.x2, self.x3, self.x4, self.x5, self.x6, self.x7 = 2100, 3500, 4900, 5600, 6300, 7000, 7700
        self.image = load_image('b1.png')
        self.image2 = load_image('b3.png')

    def update(self):
        num = 10
        self.x -= num
        self.x1 -= num
        self.x2 -= num
        self.x3 -= num
        self.x4 -= num
        self.x5 -= num
        self.x6 -= num
        self.x7 -= num

    def draw(self):

        self.image.draw(self.x, self.y)
        self.image.draw(self.x1, self.y)
        self.image.draw(self.x2, self.y)
        self.image.draw(self.x3, self.y)
        self.image2.draw(self.x4, self.y)

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
        self.bx, self.by = 770, 0
        self.bx2, self.bx3 = 1800, 3400
        self.image = load_image('b_block.png')
        self.image2 = load_image('p_block.png')
        self.image3 = load_image('b_blcok.png')

    def update(self):
        self.bx -= 10
        self.bx2 -= 10
        self.bx3 -= 10
        pass

    def draw(self):
        self.image.draw(self.bx, self.by)
        self.image.draw(self.bx2, self.by)
        self.image.draw(self.bx3, self.by)

class GBlock:
    def __init__(self):
        self.bx, self.by = 1300, 0
        self.bx2 = 2100
        self.bx3 = 2600
        self.bx4, self. by4 = 3300, 2350
        self.image = load_image('g_block.png')

    def update(self):
        r1_y = random.randint(5, 8)
        self.bx -= 10
        self.bx2 -= 10
        self.bx3 -= 10
        self.bx4 -= 10

        self.by4 -= r1_y
        pass

    def draw(self):
        self.image.draw(self.bx, self.by)
        self.image.draw(self.bx2, self.by)
        self.image.draw(self.bx3, self.by)
        self.image.draw(self.bx4, self.by4)

# 이거 나중에 정리해야함
class DownBlock:
    def __init__(self):
        self.bx, self.by = 1000, 700
        self.bx2, self.by2 = 1600, 800
        self.bx3, self.by3 = 2450, 1800
        self.bx4, self.by4 = 2800, 2000
        self.bx5, self.by0 = 3000, 0
        self.bx6 = 3700
        self.image = load_image('p_block.png')
        self.image2 = load_image('g_block.png')
        self.image3 = load_image('b_block.png')

    def update(self):
        r1_y = random.randint(5, 8)
        r2_y = random.randint(3, 5)
        self.bx -= 10
        self.bx2 -= 10
        self.bx3 -= 10
        self.bx4 -= 10
        self.bx5 -= 10
        self.bx6 -= 10

        self.by -= r1_y
        self.by2 -= r2_y
        self.by3 -= r1_y
        self.by4 -= r1_y

    def draw(self):
        self.image.draw(self.bx, self.by)
        self.image2.draw(self.bx2, self.by2)
        self.image.draw(self.bx3, self.by3)
        self.image.draw(self.bx4, self.by4)
        self.image.draw(self.bx5, self.by0)
        self.image.draw(self.bx6, self.by0)

class HP:
    def __init__(self):
        self.x, self.y = 1150, 720
        self.image = load_image('hp.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)