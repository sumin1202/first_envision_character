from pico2d import*

# character Event
ATTACK_SLIME, JUMP_SLIME, CHANGE_SLIME, SLEEP_TIMER = range(4)

key_event_table = {
    (SDLK_DOWN, SDLK_q): CHANGE_SLIME,
    (SDL_KEYDOWN, SDLK_SPACE): JUMP_SLIME
}

# IDLE 에서 Timer_out 되었을 때
class SleepState:
    @staticmethod
    def enter(chararcter, event):
        chararcter.frame = 0

    @staticmethod
    def exit(character, event):
        pass

    @staticmethod
    def do(character):
        character.frame = (character.frame + 1) % 4
        character.cx, character.cy = 270, 190

    @staticmethod
    def draw(character):
        if character.dir == 1:
            character.image.clip_draw(character.frame * 100, 0, 105, 110, character.cx, character.cy)

# 아무것도 안하고 있는 상태
class IdleState:
    @staticmethod
    def enter(character, event):
        pass

    @staticmethod
    def exit(character, event):
        pass

    @staticmethod
    def do(character):
        character.frame = (character.frame + 1) % 4
        character.timer -= 1

    @staticmethod
    def draw(character):
        if character.dir == 1:
            character.image.clip_draw(character.frame * 100, 0, 105, 110, character.cx, character.cy)


class RunState:
    # staticmethod 란 정적메소드와 비슷한 것, 인스턴스 없이 호출이 가능(cls 를 넘겨주지 않아도 됨)
    @staticmethod
    def enter(character, event):
        if event == JUMP_SLIME:
            pass

    @staticmethod
    def exit(character, event):
        pass

    @staticmethod
    def do(character):
        character.frame = (character.frame + 1) % 4

    @staticmethod
    def draw(chararcter):
        pass

next_state_table = {
    IdleState: {SLEEP_TIMER: SleepState}
}

class SLIME:
    def __init__(self):
        self.x, self.y = 270, 190
        self.image = load_image('run_Pink_Slime.png')
        self.dir = 1
        self.frame = 0
        self.timer = 0

    def update_state(self):
        pass

    def add_event(self, event):
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def handle_event(self, event):
        pass
    