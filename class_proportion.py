from pico2d import*

class Background:
    def __init__(self):
        self.x, self.y = 700, 390
        self.x1, self.x2 = 2100, 3500
        self.image = load_image('b4.png')

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

class Block:
    def __init__(self):
        self.bx, self.by = 1000, 100
        self.bx2, self.by2 = 1600, 370
        self.image = load_image('p_block.png')

    def update(self):
        self.bx -= 10
        self.bx2 -= 10
        pass

    def draw(self):
        self.image.draw(self.bx, self.by)
        self.image.draw(self.bx2, self.by2)