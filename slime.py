import game_framework
from pico2d import *
from fallingblock import FallingBlock, BLOCK

import game_world

color = 0

# Boy Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SLEEP_TIMER, SPACE = range(6)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE
}


class IdleState:
    @staticmethod
    def enter(boy, event):
        global color
        if event == RIGHT_DOWN:
            boy.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            boy.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            boy.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            boy.velocity += RUN_SPEED_PPS

        boy.timer = 1000

    @staticmethod
    def exit(boy, event):
        if event == SPACE and boy.is_jump == False:
            boy.jump()
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 4
        boy.timer -= 1
        if boy.timer == 0:
            boy.add_event(SLEEP_TIMER)

    @staticmethod
    def draw(boy):
        global color
        if boy.dir == 1:
            boy.image.clip_draw(int(boy.frame) * 100, 100, 100, 100, boy.x, boy.y)
            delay(0.1)
        else:
            if boy.checkColor == 0:
                boy.image.clip_draw(int(boy.frame) * 100, 0, 100, 100, boy.x, boy.y)
            elif boy.checkColor == 1:
                boy.image2.clip_draw(int(boy.frame) * 100, 0, 100, 100, boy.x, boy.y)
            elif boy.checkColor == 2:
                boy.image3.clip_draw(int(boy.frame) * 100, 0, 100, 100, boy.x, boy.y)
            delay(0.08)


next_state_table = {
    IdleState: {SPACE: IdleState}
}


class Slime:
    def __init__(self):
        global color
        self.x, self.y = 270, 185
        # Boy is only once created, so instance image loading is fine
        self.image = load_image('run_Pink_Slime.png')
        self.image2 = load_image('green.png')
        self.image3 = load_image('blue.png')

        self.font = load_font('ENCR10B.TTF', 16)
        self.dir = 0
        self.velocity = 0
        self.frame = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

        self.is_jump = False
        self.x1, self.y1, self.x2, self.y2, self.x3, self.y3 = 0, 0, 0, 0, 0, 0
        self.is_collide_brick = False
        self.color = 0
        self.v = 0

        self.checkColor = 0

    def handle_event(self, event):
        global color
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
            # change color
        elif event.type == SDL_KEYDOWN and event.key == SDLK_q:
            if self.checkColor == 2:
                self.checkColor = -1
            self.checkColor += 1

    def get_bb(self):
        # fill here
        return self.x - 40, self.y - 50, self.x + 40, self.y + 35


    def add_event(self, event):
        global color
        self.event_que.insert(0, event)

    def jump(self):
        global color
        self.is_jump = True
        self.x1 = self.x
        self.y1 = self.y
        self.x2 = self.x
        self.y2 = self.y + 180
        self.x3 = self.x
        self.y3 = 185

    def update(self):
        global color
        self.cur_state.do(self)

        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

        if self.is_jump:
            self.y = (2 * self.v ** 2 - 3 * self.v + 1) * self.y1 + (-4 * self.v ** 2 + 4 * self.v) * self.y2 + (
                    2 * self.v ** 2 - self.v) * self.y3
            self.v += game_framework.frame_time

            if self.v >= 1:
                self.v = 0
                self.is_jump = False

        if not self.is_collide_brick:
            self.y -= game_framework.frame_time * 200

    def draw(self):
        global color
        self.cur_state.draw(self)
        #self.font.draw(self.x - 60, self.y + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))
        # fill here
        #draw_rectangle(*self.get_bb())

