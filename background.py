from pico2d import *
import title_state
import game_framework
import fallingblock

class FixedBackground:

    def __init__(self):
        self.x, self.y = 700, 390
        self.x1, self.x2, self.x3 = 2100, 3500, 4900
        self.image = load_image('b1.png')

        self.image3 = load_image('color.png')
        self.cx, self.cy = 170, 640

    def draw(self):
        # background
        self.image.draw(self.x, self.y)
        self.image.draw(self.x1, self.y)
        self.image.draw(self.x2, self.y)
        self.image.draw(self.x3, self.y)

        # color_bar
        self.image3.draw(self.cx, self.cy)
        pass


    def update(self):
        num = 10
        if self.x3 < 700:
            game_framework.change_state(title_state)
        self.x -= num
        self.x1 -= num
        self.x2 -= num
        self.x3 -= num
        pass

    def handle_event(self, event):
        pass

