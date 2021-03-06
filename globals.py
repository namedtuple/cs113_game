class Imports:
    # python standard library modules
    import datetime
    import os
    import random
    import sys
    from collections import namedtuple
    from collections import defaultdict

    # psutil  (download here:  http://www.lfd.uci.edu/~gohlke/pythonlibs/#psutil)
    try:
        import psutil
        psutil_found = True
    except ImportError:
        psutil_found = False

    locals_dict = dict(locals().items())
    for k, v in locals_dict.items():
        sys.modules[__name__].__dict__[k] = v


class PygameLocalsImports:
    from pygame.locals import HAT_CENTERED
    from pygame.locals import HAT_DOWN
    from pygame.locals import HAT_LEFT
    from pygame.locals import HAT_LEFTDOWN
    from pygame.locals import HAT_LEFTUP
    from pygame.locals import HAT_RIGHT
    from pygame.locals import HAT_RIGHTDOWN
    from pygame.locals import HAT_RIGHTUP
    from pygame.locals import HAT_UP
    from pygame.locals import JOYAXISMOTION
    from pygame.locals import JOYBALLMOTION
    from pygame.locals import JOYBUTTONDOWN
    from pygame.locals import JOYBUTTONUP
    from pygame.locals import JOYHATMOTION
    from pygame.locals import KEYDOWN
    from pygame.locals import KEYUP
    from pygame.locals import KMOD_ALT
    from pygame.locals import KMOD_CAPS
    from pygame.locals import KMOD_CTRL
    from pygame.locals import KMOD_LALT
    from pygame.locals import KMOD_LCTRL
    from pygame.locals import KMOD_LMETA
    from pygame.locals import KMOD_LSHIFT
    from pygame.locals import KMOD_META
    from pygame.locals import KMOD_MODE
    from pygame.locals import KMOD_NONE
    from pygame.locals import KMOD_NUM
    from pygame.locals import KMOD_RALT
    from pygame.locals import KMOD_RCTRL
    from pygame.locals import KMOD_RMETA
    from pygame.locals import KMOD_RSHIFT
    from pygame.locals import KMOD_SHIFT
    from pygame.locals import K_0
    from pygame.locals import K_1
    from pygame.locals import K_2
    from pygame.locals import K_3
    from pygame.locals import K_4
    from pygame.locals import K_5
    from pygame.locals import K_6
    from pygame.locals import K_7
    from pygame.locals import K_8
    from pygame.locals import K_9
    from pygame.locals import K_AMPERSAND
    from pygame.locals import K_ASTERISK
    from pygame.locals import K_AT
    from pygame.locals import K_BACKQUOTE
    from pygame.locals import K_BACKSLASH
    from pygame.locals import K_BACKSPACE
    from pygame.locals import K_BREAK
    from pygame.locals import K_CAPSLOCK
    from pygame.locals import K_CARET
    from pygame.locals import K_CLEAR
    from pygame.locals import K_COLON
    from pygame.locals import K_COMMA
    from pygame.locals import K_DELETE
    from pygame.locals import K_DOLLAR
    from pygame.locals import K_DOWN
    from pygame.locals import K_END
    from pygame.locals import K_EQUALS
    from pygame.locals import K_ESCAPE
    from pygame.locals import K_EURO
    from pygame.locals import K_EXCLAIM
    from pygame.locals import K_F1
    from pygame.locals import K_F10
    from pygame.locals import K_F11
    from pygame.locals import K_F12
    from pygame.locals import K_F13
    from pygame.locals import K_F14
    from pygame.locals import K_F15
    from pygame.locals import K_F2
    from pygame.locals import K_F3
    from pygame.locals import K_F4
    from pygame.locals import K_F5
    from pygame.locals import K_F6
    from pygame.locals import K_F7
    from pygame.locals import K_F8
    from pygame.locals import K_F9
    from pygame.locals import K_FIRST
    from pygame.locals import K_GREATER
    from pygame.locals import K_HASH
    from pygame.locals import K_HELP
    from pygame.locals import K_HOME
    from pygame.locals import K_INSERT
    from pygame.locals import K_KP0
    from pygame.locals import K_KP1
    from pygame.locals import K_KP2
    from pygame.locals import K_KP3
    from pygame.locals import K_KP4
    from pygame.locals import K_KP5
    from pygame.locals import K_KP6
    from pygame.locals import K_KP7
    from pygame.locals import K_KP8
    from pygame.locals import K_KP9
    from pygame.locals import K_KP_DIVIDE
    from pygame.locals import K_KP_ENTER
    from pygame.locals import K_KP_EQUALS
    from pygame.locals import K_KP_MINUS
    from pygame.locals import K_KP_MULTIPLY
    from pygame.locals import K_KP_PERIOD
    from pygame.locals import K_KP_PLUS
    from pygame.locals import K_LALT
    from pygame.locals import K_LAST
    from pygame.locals import K_LCTRL
    from pygame.locals import K_LEFT
    from pygame.locals import K_LEFTBRACKET
    from pygame.locals import K_LEFTPAREN
    from pygame.locals import K_LESS
    from pygame.locals import K_LMETA
    from pygame.locals import K_LSHIFT
    from pygame.locals import K_LSUPER
    from pygame.locals import K_MENU
    from pygame.locals import K_MINUS
    from pygame.locals import K_MODE
    from pygame.locals import K_NUMLOCK
    from pygame.locals import K_PAGEDOWN
    from pygame.locals import K_PAGEUP
    from pygame.locals import K_PAUSE
    from pygame.locals import K_PERIOD
    from pygame.locals import K_PLUS
    from pygame.locals import K_POWER
    from pygame.locals import K_PRINT
    from pygame.locals import K_QUESTION
    from pygame.locals import K_QUOTE
    from pygame.locals import K_QUOTEDBL
    from pygame.locals import K_RALT
    from pygame.locals import K_RCTRL
    from pygame.locals import K_RETURN
    from pygame.locals import K_RIGHT
    from pygame.locals import K_RIGHTBRACKET
    from pygame.locals import K_RIGHTPAREN
    from pygame.locals import K_RMETA
    from pygame.locals import K_RSHIFT
    from pygame.locals import K_RSUPER
    from pygame.locals import K_SCROLLOCK
    from pygame.locals import K_SEMICOLON
    from pygame.locals import K_SLASH
    from pygame.locals import K_SPACE
    from pygame.locals import K_SYSREQ
    from pygame.locals import K_TAB
    from pygame.locals import K_UNDERSCORE
    from pygame.locals import K_UNKNOWN
    from pygame.locals import K_UP
    from pygame.locals import K_a
    from pygame.locals import K_b
    from pygame.locals import K_c
    from pygame.locals import K_d
    from pygame.locals import K_e
    from pygame.locals import K_f
    from pygame.locals import K_g
    from pygame.locals import K_h
    from pygame.locals import K_i
    from pygame.locals import K_j
    from pygame.locals import K_k
    from pygame.locals import K_l
    from pygame.locals import K_m
    from pygame.locals import K_n
    from pygame.locals import K_o
    from pygame.locals import K_p
    from pygame.locals import K_q
    from pygame.locals import K_r
    from pygame.locals import K_s
    from pygame.locals import K_t
    from pygame.locals import K_u
    from pygame.locals import K_v
    from pygame.locals import K_w
    from pygame.locals import K_x
    from pygame.locals import K_y
    from pygame.locals import K_z
    from pygame.locals import MOUSEBUTTONDOWN
    from pygame.locals import MOUSEBUTTONUP
    from pygame.locals import MOUSEMOTION
    from pygame.locals import NOEVENT
    from pygame.locals import NUMEVENTS
    from pygame.locals import QUIT
    from pygame.locals import RESIZABLE
    from pygame.locals import SRCALPHA
    from pygame.locals import SRCCOLORKEY
    from pygame.locals import SWSURFACE
    from pygame.locals import USEREVENT
    from pygame.locals import VIDEOEXPOSE
    from pygame.locals import VIDEORESIZE
    from pygame.locals import color
    from pygame.locals import Color
    from pygame.locals import Rect

    locals_dict = dict(locals().items())
    for k, v in locals_dict.items():
        sys.modules[__name__].__dict__[k] = v


class PygameImports:
    import pygame

    from pygame import Surface
    from pygame.time import Clock
    from pygame.mixer import Sound
    from pygame.event import Event
    from pygame.joystick import Joystick
    from pygame.font import Font
    from pygame.font import SysFont

    from pygame.draw import circle as draw_circle
    from pygame.draw import polygon as draw_polygon
    from pygame.draw import rect as draw_rect

    from pygame.event import get as get_events
    from pygame.event import post as post_event

    from pygame.image import load as image_load
    from pygame.transform import flip as image_flip
    from pygame.transform import rotate as image_rotate
    from pygame.transform import scale as image_scale

    locals_dict = dict(locals().items())
    for k, v in locals_dict.items():
        sys.modules[__name__].__dict__[k] = v


class Setup:
    if os.environ['COMPUTERNAME'] == 'BRIAN-DESKTOP':
        os.environ['SDL_VIDEO_WINDOW_POS'] = '{},{}'.format(1920, 230)
    if os.environ['COMPUTERNAME'] in ('MAX-LT', 'BRIAN-LAPTOP'):
        os.environ['SDL_VIDEO_WINDOW_POS'] = '{},{}'.format(50, 30)

    pygame.init()
    pygame.display.set_caption('Famished Tournament')


def add_to_module_namespace(locals_dict):
    for k, v in locals_dict.items():
        globals()[k] = v


class Constants:
    SCREEN = pygame.display.set_mode((1280, 600))
    WINDOW = SCREEN.get_rect()
    CLOCK = pygame.time.Clock()
    FPS = 30
    NEXT_PAGE = '_start'

    # Music
    SONGS = ['data/songs/pneumatic_driller.mp3', 'data/songs/euglena_zielona.mp3',
             'data/songs/drilldance.mp3', 'data/songs/running_emu.mp3', 'data/songs/wooboodoo.mp3',
             'data/songs/accident.mp3']

    SOUNDS = {}

    # Monster Types and Globals
    ALL = 'ALL'
    WEAK = 'WEAK'
    MEDIUM = 'MEDIUM'
    ULTIMATE = 'ULTIMATE'
    CHASING = 'CHASING'
    IDLE = 'IDLE'
    ULTIMATE_SPAWN_RATE = 5000
    WEAK_EXP_VALUE = 10
    MEDIUM_EXP_VALUE = 25
    ULTIMATE_EXP_VALUE = 50

    # Player exp level-up thresholds
    #                   1  2   3    4    5    6    7    8    9    10
    LEVEL_THRESHOLDS = [0, 50, 100, 150, 200, 250, 300, 350, 400, 450]

    # Player States (for animation)
    STAND = 'STAND'
    LWALK = 'LWALK'
    RWALK = 'RWALK'
    JUMP = 'JUMP'
    FALL = 'FALL'
    WIN = 'WIN'
    DEATH = 'DEATH'
    RESET = 'RESET'
    ATTACK = 'ATTACK'  # Rest is attacks
    ONEHAND = 'ONEHAND'
    TWOHAND = 'TWOHAND'
    CAST1 = 'CAST1'
    CAST2 = 'CAST2'
    CAST3 = 'CAST3'
    THROW = 'THROW'
    MACHGUN = 'MACHGUN'
    BREATH = 'BREATH'
    POKE = 'POKE'
    BULLET = 'BULLET'
    DASH = 'DASH'
    RUN = 'RUN'

    # Player Attack State Info Table [index, max value]
    PL_ATTACK_TABLE = {'ONEHAND': [28, 3],
                       'TWOHAND': [32, 3],
                       'CAST1': [36, 2],
                       'CAST2': [39, 3],
                       'CAST3': [43, 0],
                       'THROW': [44, 3],
                       'MACHGUN': [48, 1],
                       'BREATH': [50, 2],
                       'POKE': [53, 3],
                       'BULLET': [57, 3],
                       'DASH': [7, 0],
                       'RUN': [8, 15]}

    # Inputs
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'
    MELEE = 'MELEE'
    RANGE = 'RANGED'
    FIELD = 'FIELD'

    # Conditions
    STUN = 'STUN'
    SLOW = 'SLOW'
    SNARE = 'SNARE'
    DOT = 'DOT'
    SILENCE = 'SILENCE'
    WOUNDED = 'WOUNDED'
    WEAKENED = 'WEAKENED'
    SPEED = 'SPEED'
    SHIELD = 'SHIELD'
    INVIGORATED = 'INVIGORATED'
    EMPOWERED = 'EMPOWERED'
    BUFFS = [SPEED, SHIELD, INVIGORATED, EMPOWERED]
    DEBUFFS = [STUN, SLOW, SNARE, DOT, SILENCE, WOUNDED, WEAKENED]

    # Buttons
    ATTACKBUTTON = 'attack_id'
    SKILL1BUTTON = 'skill1_id'
    SKILL2BUTTON = 'skill2_id'
    SKILL3BUTTON = 'skill3_id'
    ULTBUTTON = 'ult_id'

    # Scrolling texts
    ST_DMG = 'ST_DMG'
    ST_HP = 'ST_HP'
    ST_ENERGY = 'ST_ENERGY'
    ST_LEVEL_UP = 'ST_LEVEL_UP'

    # Events
    TIME_TICK_EVENT = USEREVENT + 0
    PLAYER1_LOCK_EVENT = USEREVENT + 1
    PLAYER2_LOCK_EVENT = USEREVENT + 2
    PLAYER1_PICKUP_EVENT = USEREVENT + 3
    PLAYER2_PICKUP_EVENT = USEREVENT + 4
    REGENERATION_EVENT = USEREVENT + 5
    MONSTER_SPAWN_EVENT = USEREVENT + 6
    SONG_END_EVENT = USEREVENT + 7
    MORE_RAIN_EVENT = USEREVENT + 8

    add_to_module_namespace(locals())


# noinspection PyMethodParameters
class Functions:

    def all_in(items_want_inside, container_being_checked):
        for thing in items_want_inside:
            if thing not in container_being_checked:
                return False
        return True

    def all_isinstance(items_checking, instance_wanted):
        for thing in items_checking:
            if isinstance(thing, instance_wanted) is False:
                return False
        return True

    def font_position_center(rect, font, text):
        x = (rect.width - font.size(text)[0]) // 2
        y = (rect.height - font.size(text)[1]) // 2
        return rect.left + x, rect.top + y

    def out_of_arena_fix(player):
        """Global to handle players from reaching out of arena."""
        global SELECTED_ARENA  # set in GameLoop._setup_arena of main.py
        play_area = SELECTED_ARENA.play_area_rect
        fixed = False  # Can be used for out-of-bounds checking since it returns true
        if player.left < play_area.left:
            player.left = play_area.left
            fixed = True
        if player.bottom > play_area.bottom:
            player.bottom = play_area.bottom
            fixed = True
        if player.right > play_area.right:
            player.right = play_area.right
            fixed = True
        return fixed

    def handle_damage(target, value, time):
        if value != 0:
            target.hit_points -= value
            target.shield_trigger(value)
            if target.hit_points < 0:
                target.hit_points = 0
            if time >= 0:
                target.st_buffer.append((ST_DMG, value, time + 2000))
            else:
                target.st_buffer.append((ST_DMG, value, time))

    def handle_hp_gain(target, value, time):
        if value != 0:
            if target.hit_points > 0:
                target.hit_points += value
            if target.hit_points > target.hit_points_max:
                target.hit_points = target.hit_points_max
            if time >= 0:
                target.st_buffer.append((ST_HP, value, time + 2000))
            else:
                target.st_buffer.append((ST_HP, value, time))

    def handle_energy(target, value, time):
        if value != 0:
            target.energy += value
            if time >= 0:
                target.st_buffer.append((ST_ENERGY, value, time + 2000))
            else:
                target.st_buffer.append((ST_ENERGY, value, time))

    def condition_string(cond, value):
        st = cond + ': '
        left = 0 + int(value / 1000)
        right = 0 + int((value % 1000) / 100)
        st += str(left)
        st += '.'
        st += str(right)
        return st

    def force_add_particle_to_player(particle, player):
        if isinstance(particle, list):
            if player.new_particle is None:
                player.new_particle = particle
            elif isinstance(player.new_particle, list):
                player.new_particle += particle
            else:
                player.new_particle = [player.new_particle] + particle

        else:
            if player.new_particle is None:
                player.new_particle = particle
            elif isinstance(player.new_particle, list):
                player.new_particle.append(particle)
            else:
                player.new_particle = [player.new_particle, particle]

    # noinspection PyPep8Naming
    def EXIT_GAME():
        pygame.quit()
        sys.exit()

    add_to_module_namespace(locals())


class Colors:
    BLACK = Color(0, 0, 0)
    DGREY = Color(64, 64, 64)
    GREY = Color(100, 100, 100)
    WHITE = Color(255, 255, 255)
    BROWN = Color(139, 69, 19)
    RED = Color(255, 0, 0)
    DKRED = Color(128, 0, 0)
    DKGREEN = Color(0, 128, 0)
    GREEN = Color(0, 255, 0)
    BLUE = Color(0, 0, 255)
    LLBLUE = Color(0, 0, 128)
    LBLUE = Color(0, 128, 255)
    CYAN = Color(80, 191, 201)
    DKCYAN = Color(20, 118, 128)
    SKYBLUE = Color(128, 223, 223)
    YELLOW = Color(255, 255, 0)
    DKYELLOW = Color(153, 153, 0)
    DKDKYELLOW = Color(128, 128, 0)
    PURPLE = Color(255, 0, 255)
    DKPURPLE = Color(153, 0, 153)
    ORANGE = Color(255, 153, 0)
    DKORANGE = Color(153, 92, 0)
    TRANSPARENT = Color(235, 0, 255)
    add_to_module_namespace(locals())


class Audio:
    def __init__(self):
        try:
            pygame.mixer.init(44100)
            self.audio_device_found = True
        except pygame.error:
            self.audio_device_found = False
        self.menu_song = self.curr_song = 'data/songs/404error.mp3'
        self.music_on = self.sound_on = False

    def restart_music(self):
        if self.audio_device_found:
            self.turn_off_music()
            self.turn_on_music()

    def turn_on_music(self):
        if self.audio_device_found:
            self.music_on = True
            self.curr_song = self.menu_song
            pygame.mixer.music.load(self.curr_song)
            pygame.mixer.music.play(-1)
            print('music turned on', end='    ')
            print(self)

    def turn_off_music(self):
        if self.audio_device_found:
            self.music_on = False
            pygame.mixer.music.stop()
            print('music turned off')

    def turn_on_effects(self):
        if self.audio_device_found:
            self.sound_on = True
            print('sound effects turned on')

    def turn_off_effects(self):
        if self.audio_device_found:
            self.sound_on = False
            print('sound effects turned off')

    def play_next_random_song(self):
        if self.audio_device_found:
            self.curr_song = random.choice([s for s in SONGS if s != self.curr_song])
            pygame.mixer.music.load(self.curr_song)
            pygame.mixer.music.play()
            pygame.mixer.music.set_endevent(SONG_END_EVENT)
            print(self)

    def __str__(self):
        t = datetime.datetime.now().strftime('%H:%M:%S')
        return 'new song: "{}"    started at: {}'.format(self.curr_song.replace('data/songs/', '').replace('.mp3', ''), t)
AUDIO = Audio()


class Input:
    def __init__(self, player_id=1):
        self.gp_input = defaultdict(bool)
        self.kb_input = defaultdict(bool)
        self.player_id = player_id
        self.DEBUG_MODE_ON = False
        self.PAUSE_MODE_ON = False
        self.P1_ININITE_HEALTH_ENERGY_ON = False
        self.P2_ININITE_HEALTH_ENERGY_ON = False
        self.num_joys = pygame.joystick.get_count()

        if self.num_joys == 2:  # p1 = gamepad0 or keyboard, p2 = gamepad1
            self.joy_num = player_id - 1
            self.gamepad = pygame.joystick.Joystick(self.joy_num)
            self.gamepad.init()
            self.gamepad_found = True
            print('p{} uses "{}"'.format(str(self.player_id), self.gamepad.get_name()))
            self.__setup_gamepad_buttons__()

        elif self.num_joys == 1:  # p1 = keyboard, p2 = gamepad0
            if player_id == 1:
                self.gamepad_found = False
                print('p{} uses keyboard'.format(str(self.player_id)))
            elif player_id == 2:
                self.joy_num = 0
                self.gamepad = pygame.joystick.Joystick(self.joy_num)
                self.gamepad.init()
                self.gamepad_found = True
                print('p{} uses "{}"'.format(str(self.player_id), self.gamepad.get_name()))
                self.__setup_gamepad_buttons__()

        elif self.num_joys == 0:  # p1 = keyboard, p2 = cannot play
            if player_id == 1:
                self.gamepad_found = False
                print('p{} uses keyboard'.format(str(self.player_id)))
            elif player_id == 2:
                self.gamepad_found = False
                print('p{} cannot play!'.format(str(self.player_id)))

    def __setup_gamepad_buttons__(self):
        input_nt = namedtuple('input_nt', 'kind, number, value1, value2')

        #  L2                                  R2
        #     L1                            R1
        #         U                      Y
        #       L   R   SELCT  START   X   B
        #         D                      A

        if self.gamepad.get_name() == 'Gioteck PS3 Wired Controller':  # Max's gamepad
            self.GP_INPUTS_DICT = {
                'GP_LEFT': input_nt(kind='hat', number=0, value1=-1, value2=0),
                'GP_RIGHT': input_nt(kind='hat', number=0, value1=1, value2=0),
                'GP_UP': input_nt(kind='hat', number=0, value1=1, value2=-1),
                'GP_DOWN': input_nt(kind='hat', number=0, value1=-1, value2=+1),
                'GP_A': input_nt(kind='button', number=2, value1=None, value2=None),
                'GP_B': input_nt(kind='button', number=1, value1=None, value2=None),
                'GP_X': input_nt(kind='button', number=3, value1=None, value2=None),
                'GP_Y': input_nt(kind='button', number=0, value1=None, value2=None),
                'GP_R1': input_nt(kind='button', number=5, value1=None, value2=None),
                'GP_R2': input_nt(kind='button', number=7, value1=None, value2=None),
                'GP_L1': input_nt(kind='button', number=4, value1=None, value2=None),
                'GP_L2': input_nt(kind='button', number=6, value1=None, value2=None),
                'GP_START': input_nt(kind='button', number=9, value1=None, value2=None),
                'GP_SELECT': input_nt(kind='button', number=8, value1=None, value2=None)}

        elif self.gamepad.get_name() in ('Logitech Cordless RumblePad 2', 'Logitech Cordless RumblePad 2 USB'):  # Brian's gamepad if switched to "D"
            self.GP_INPUTS_DICT = {
                'GP_LEFT': input_nt(kind='hat', number=0, value1=-1, value2=0),
                'GP_RIGHT': input_nt(kind='hat', number=0, value1=+1, value2=0),
                'GP_UP': input_nt(kind='hat', number=0, value1=0, value2=+1),
                'GP_DOWN': input_nt(kind='hat', number=0, value1=0, value2=-1),
                'GP_A': input_nt(kind='button', number=1, value1=None, value2=None),
                'GP_B': input_nt(kind='button', number=2, value1=None, value2=None),
                'GP_X': input_nt(kind='button', number=0, value1=None, value2=None),
                'GP_Y': input_nt(kind='button', number=3, value1=None, value2=None),
                'GP_R1': input_nt(kind='button', number=5, value1=None, value2=None),
                'GP_R2': input_nt(kind='button', number=7, value1=None, value2=None),
                'GP_L1': input_nt(kind='button', number=4, value1=None, value2=None),
                'GP_L2': input_nt(kind='button', number=6, value1=None, value2=None),
                'GP_START': input_nt(kind='button', number=9, value1=None, value2=None),
                'GP_SELECT': input_nt(kind='button', number=8, value1=None, value2=None)}

        elif self.gamepad.get_name() in ('Wireless Gamepad F710 (Controller)', 'Controller (XBOX 360 For Windows)'):  # Brian's gamepad if switched to "X"
            self.GP_INPUTS_DICT = {
                'GP_LEFT': input_nt(kind='hat', number=0, value1=-1, value2=0),
                'GP_RIGHT': input_nt(kind='hat', number=0, value1=+1, value2=0),
                'GP_UP': input_nt(kind='hat', number=0, value1=0, value2=+1),
                'GP_DOWN': input_nt(kind='hat', number=0, value1=0, value2=-1),
                'GP_A': input_nt(kind='button', number=0, value1=None, value2=None),
                'GP_B': input_nt(kind='button', number=1, value1=None, value2=None),
                'GP_X': input_nt(kind='button', number=2, value1=None, value2=None),
                'GP_Y': input_nt(kind='button', number=3, value1=None, value2=None),
                'GP_R1': input_nt(kind='button', number=5, value1=None, value2=None),
                'GP_R2': input_nt(kind='axis', number=2, value1=-1, value2=None),
                'GP_L1': input_nt(kind='button', number=4, value1=None, value2=None),
                'GP_L2': input_nt(kind='axis', number=2, value1=+1, value2=None),
                'GP_START': input_nt(kind='button', number=7, value1=None, value2=None),
                'GP_SELECT': input_nt(kind='button', number=6, value1=None, value2=None)}

    def refresh(self):
        self._reset_all_event_flags()
        if self.player_id == 1:
            self._get_keyboard_pressed()
            self._get_keyboard_events()
        self._get_gamepad_pressed_and_events()
        self._combine_all_pressed()
        self._combine_all_events()
        if self.player_id == 1:
            self._handle_mouse_visibility()
        # self._debug()

    def _get_keyboard_pressed(self):
        sucky_kb_input = pygame.key.get_pressed()
        self.kb_input['KB_LEFT'] = sucky_kb_input[K_LEFT]
        self.kb_input['KB_RIGHT'] = sucky_kb_input[K_RIGHT]
        self.kb_input['KB_UP'] = sucky_kb_input[K_UP]
        self.kb_input['KB_DOWN'] = sucky_kb_input[K_DOWN]

        self.kb_input['KB_SPACE'] = sucky_kb_input[K_SPACE]
        self.kb_input['KB_s'] = sucky_kb_input[K_s]
        self.kb_input['KB_a'] = sucky_kb_input[K_a]
        self.kb_input['KB_d'] = sucky_kb_input[K_d]
        self.kb_input['KB_f'] = sucky_kb_input[K_f]
        self.kb_input['KB_g'] = sucky_kb_input[K_g]
        self.kb_input['KB_q'] = sucky_kb_input[K_q]

        self.kb_input['KB_RETURN'] = sucky_kb_input[K_RETURN]
        self.kb_input['KB_ESCAPE'] = sucky_kb_input[K_ESCAPE]
        self.kb_input['KB_r'] = sucky_kb_input[K_r]
        self.kb_input['KB_k'] = sucky_kb_input[K_k]
        self.kb_input['KB_BACKQUOTE'] = sucky_kb_input[K_BACKQUOTE]
        self.kb_input['KB_F12'] = sucky_kb_input[K_F12]

    def _get_keyboard_events(self):
        keydown_events = [e for e in pygame.event.get(KEYDOWN)]
        for e in keydown_events:
            if e.key == K_LEFT:         self.kb_input['KB_LEFT_EVENT'] = True
            if e.key == K_RIGHT:        self.kb_input['KB_RIGHT_EVENT'] = True
            if e.key == K_UP:           self.kb_input['KB_UP_EVENT'] = True
            if e.key == K_DOWN:         self.kb_input['KB_DOWN_EVENT'] = True

            if e.key == K_SPACE:        self.kb_input['KB_SPACE_EVENT'] = True

            if e.key == K_RETURN:       self.kb_input['KB_RETURN_EVENT'] = True
            if e.key == K_ESCAPE:       self.kb_input['KB_ESCAPE_EVENT'] = True

            if e.key == K_r:            self.kb_input['KB_r_EVENT'] = True
            if e.key == K_k:            self.kb_input['KB_k_EVENT'] = True
            if e.key == K_F12:          self.kb_input['KB_F12_EVENT'] = True
            if e.key == K_BACKQUOTE:    self.kb_input['KB_BACKQUOTE_EVENT'] = True

            if e.key == K_F1:           self.kb_input['KB_F1_EVENT'] = True
            if e.key == K_F2:           self.kb_input['KB_F2_EVENT'] = True
            if e.key == K_F3:           self.kb_input['KB_F3_EVENT'] = True
            if e.key == K_F4:           self.kb_input['KB_F4_EVENT'] = True
            if e.key == K_F5:           self.kb_input['KB_F5_EVENT'] = True

            if e.key == K_F6:           self.kb_input['KB_F6_EVENT'] = True
            if e.key == K_F7:           self.kb_input['KB_F7_EVENT'] = True
            if e.key == K_F8:           self.kb_input['KB_F8_EVENT'] = True
            if e.key == K_F9:           self.kb_input['KB_F9_EVENT'] = True
            if e.key == K_F10:          self.kb_input['KB_F10_EVENT'] = True

            if e.key == K_1:            self.kb_input['KB_1_EVENT'] = True
            if e.key == K_2:            self.kb_input['KB_2_EVENT'] = True

    def _get_gamepad_pressed_and_events(self):
        if self.gamepad_found:
            if (self.num_joys == 2 and self.player_id == 1) or \
                    (self.num_joys == 1 and self.player_id == 2):
                # These three lists are placed in the namespace of the Input
                # class so that both instances of Input may access them
                Input.joy_button_events = [e for e in pygame.event.get(JOYBUTTONDOWN)]
                Input.joy_axis_events = [e for e in pygame.event.get(JOYAXISMOTION)]
                Input.joy_hat_events = [e for e in pygame.event.get(JOYHATMOTION)]

            joy_button_events = list(filter(lambda x: x.joy == self.joy_num, Input.joy_button_events))
            joy_axis_events = list(filter(lambda x: x.joy == self.joy_num, Input.joy_axis_events))
            joy_hat_events = list(filter(lambda x: x.joy == self.joy_num, Input.joy_hat_events))

            for name, info in self.GP_INPUTS_DICT.items():  # these are all the inputs that we care about
                if info.kind == 'button':
                    self.gp_input[name] = self.gamepad.get_button(info.number)
                    if info.number in [e.button for e in joy_button_events]:
                        self.gp_input[name + '_EVENT'] = True
                        # print('button', name + '_EVENT', self.gp_input[name + '_EVENT'])

                elif info.kind == 'axis':
                    self.gp_input[name] = round(self.gamepad.get_axis(info.number)) == info.value1
                    if (info.number, info.value1) in [(e.axis, e.value) for e in joy_axis_events]:
                        self.gp_input[name + '_EVENT'] = True
                        # print('axis  ', name + '_EVENT', self.gp_input[name + '_EVENT'])

                elif info.kind == 'hat':
                    self.gp_input[name] = self.gamepad.get_hat(info.number) == (info.value1, info.value2)
                    if (info.number, (info.value1, info.value2)) in [(e.hat, e.value) for e in joy_hat_events]:
                        self.gp_input[name + '_EVENT'] = True
                        # print('hat   ', name + '_EVENT', self.gp_input[name + '_EVENT'])

    def _combine_all_pressed(self):
        self.LEFT = self.kb_input['KB_LEFT'] or self.gp_input['GP_LEFT']
        self.RIGHT = self.kb_input['KB_RIGHT'] or self.gp_input['GP_RIGHT']
        self.UP = self.kb_input['KB_UP'] or self.gp_input['GP_UP']
        self.DOWN = self.kb_input['KB_DOWN'] or self.gp_input['GP_DOWN']
        self.JUMP = self.kb_input['KB_SPACE'] or self.gp_input['GP_A']
        self.ATTACK = self.kb_input['KB_a'] or self.gp_input['GP_X']
        self.SKILL1 = self.kb_input['KB_s'] or self.gp_input['GP_B']
        self.SKILL2 = self.kb_input['KB_d'] or self.gp_input['GP_Y']
        self.SKILL3 = self.kb_input['KB_f'] or self.gp_input['GP_R1']
        self.ULT = self.kb_input['KB_g'] or self.gp_input['GP_R2']
        self.DROP_SKILL = self.kb_input['KB_q'] or self.gp_input['GP_L1'] or self.gp_input['GP_L2']

    def _combine_all_events(self):
        self.LEFT_EVENT = self.gp_input['GP_LEFT_EVENT'] or self.kb_input['KB_LEFT_EVENT']
        self.RIGHT_EVENT = self.gp_input['GP_RIGHT_EVENT'] or self.kb_input['KB_RIGHT_EVENT']
        self.UP_EVENT = self.gp_input['GP_UP_EVENT'] or self.kb_input['KB_UP_EVENT']
        self.DOWN_EVENT = self.gp_input['GP_DOWN_EVENT'] or self.kb_input['KB_DOWN_EVENT']

        self.CONFIRM = self.gp_input['GP_A_EVENT'] or self.gp_input['GP_START_EVENT'] or self.kb_input['KB_RETURN_EVENT']
        self.CANCEL = self.gp_input['GP_B_EVENT'] or self.gp_input['GP_SELECT_EVENT'] or self.kb_input['KB_ESCAPE_EVENT']

        self.RESPAWN_CHEAT = self.kb_input['KB_r_EVENT']
        self.KILLALL_CHEAT = self.kb_input['KB_k_EVENT']
        self.QUICK_START = self.kb_input['KB_F12_EVENT']

        # need to save whether this was on or off for the next call to refresh
        self.PAUSE_MODE_TOGGLED = self.gp_input['GP_START_EVENT'] or self.kb_input['KB_RETURN_EVENT'] or self.kb_input['KB_ESCAPE_EVENT']
        if self.PAUSE_MODE_TOGGLED:
            self.PAUSE_MODE_ON = not self.PAUSE_MODE_ON

        # need to save whether this was on or off for the next call to refresh
        self.DEBUG_MODE_TOGGLED = self.kb_input['KB_BACKQUOTE_EVENT']
        if self.DEBUG_MODE_TOGGLED and not self.PAUSE_MODE_ON:  # only "really" toggle debug mode if not paused
            self.DEBUG_MODE_ON = not self.DEBUG_MODE_ON

        self.NEW_P1_RED_SKILL_CHEAT = self.kb_input['KB_F1_EVENT']
        self.NEW_P1_BLUE1_SKILL_CHEAT = self.kb_input['KB_F2_EVENT']
        self.NEW_P1_BLUE2_SKILL_CHEAT = self.kb_input['KB_F3_EVENT']
        self.NEW_P1_BLUE3_SKILL_CHEAT = self.kb_input['KB_F4_EVENT']
        self.NEW_P1_YELLOW_SKILL_CHEAT = self.kb_input['KB_F5_EVENT']

        self.NEW_P2_RED_SKILL_CHEAT = self.kb_input['KB_F6_EVENT']
        self.NEW_P2_BLUE1_SKILL_CHEAT = self.kb_input['KB_F7_EVENT']
        self.NEW_P2_BLUE2_SKILL_CHEAT = self.kb_input['KB_F8_EVENT']
        self.NEW_P2_BLUE3_SKILL_CHEAT = self.kb_input['KB_F9_EVENT']
        self.NEW_P2_YELLOW_SKILL_CHEAT = self.kb_input['KB_F10_EVENT']

        self.P1_INFINITE_HEALTH_ENERGY = self.kb_input['KB_1_EVENT']
        if self.P1_INFINITE_HEALTH_ENERGY and not self.PAUSE_MODE_ON:
            self.P1_ININITE_HEALTH_ENERGY_ON = not self.P1_ININITE_HEALTH_ENERGY_ON

        self.P2_INFINITE_HEALTH_ENERGY = self.kb_input['KB_2_EVENT']
        if self.P2_INFINITE_HEALTH_ENERGY and not self.PAUSE_MODE_ON:
            self.P2_ININITE_HEALTH_ENERGY_ON = not self.P2_ININITE_HEALTH_ENERGY_ON

    def _reset_all_event_flags(self):
        for k in self.kb_input.keys():
            self.kb_input[k] = False
        for k in self.gp_input.keys():
            self.gp_input[k] = False

    def _handle_mouse_visibility(self):
        if NEXT_PAGE not in ('GameLoop()', 'GL.CURR_GAME'):
            pass
        elif self.DEBUG_MODE_ON and NEXT_PAGE in ('GameLoop()', 'GL.CURR_GAME'):
            pygame.mouse.set_visible(False)
        else:
            pygame.mouse.set_visible(True)

    def _debug(self):
        for k in self.kb_input.keys():
            if self.kb_input[k]:
                print(k)
        for k in self.gp_input.keys():
            if self.gp_input[k]:
                print(k)

INPUT1 = Input(player_id=1)
INPUT2 = Input(player_id=2)


class ArenaInfos:
    arena_nt = namedtuple('arena_nt', 'left_wall_x, right_wall_x, floor_y, platforms, max_monsters, possible_monsters, background, p1_spawn, p2_spawn')
    terrain_nt = namedtuple('terrain_nt', 'left, top, width, height, color, hits_to_destroy, spawn_point')

    arena1 = arena_nt(
        left_wall_x=65, right_wall_x=1215, floor_y=475,
        platforms=[
            terrain_nt(0, 270, 300, 60, DKGREEN, -1, False),
            terrain_nt(850, 270, 300, 60, DKGREEN, -1, False),
            terrain_nt(545, 150, 60, 230, DKGREEN, -1, False),
            terrain_nt(140, 100, 150, 20, DKGREEN, -1, False),
            terrain_nt(860, 100, 150, 20, DKGREEN, -1, False),
            terrain_nt(30, 240, 40, 20, WHITE, 5, False),
            terrain_nt(1145, 465, -5, 5, None, -1, True),
            terrain_nt(15, 465, -5, 5, None, -1, True), ],
        max_monsters=3, possible_monsters=(WEAK, MEDIUM),
        background=None, p1_spawn=(135, 150), p2_spawn=(985, 150))

    arena2 = arena_nt(
        left_wall_x=65, right_wall_x=1215, floor_y=475,
        platforms=[
            terrain_nt(50, 100, 50, 300, DKGREEN, -1, False),
            terrain_nt(240, 40, 50, 300, DKGREEN, -1, False),
            terrain_nt(500, 135, 100, 25, DKGREEN, -1, False),
            terrain_nt(725, 255, 175, 25, DKGREEN, -1, False),
            terrain_nt(1050, 375, 100, 25, DKGREEN, -1, False),
            terrain_nt(400, 434, 300, 41, DKGREEN, -1, False),
            terrain_nt(485, 394, 300, 41, DKGREEN, -1, False),
            terrain_nt(970, 65, 80, 10, DKGREEN, -1, False),
            terrain_nt(150, 465, -5, 5, None, -1, True),
            terrain_nt(930, 465, -5, 5, None, -1, True), ],
        max_monsters=3, possible_monsters=(WEAK, MEDIUM),  # ALL
        background=None, p1_spawn=(135, 150), p2_spawn=(985, 150))

    arena3 = arena_nt(
        left_wall_x=65, right_wall_x=1215, floor_y=458,
        platforms=[
            terrain_nt(401, 80, 112, 37, None, -1, False),
            terrain_nt(557, 80, 112, 37, None, -1, False),
            terrain_nt(85, 140, 228, 40, None, -1, False),
            terrain_nt(85, 180, 40, 142, None, -1, False),
            terrain_nt(85, 322, 95, 40, None, -1, False),
            terrain_nt(332, 241, 220, 40, None, -1, False),
            terrain_nt(595, 319, 417, 40, None, -1, False),
            terrain_nt(972, 156, 40, 163, None, -1, False),
            terrain_nt(785, 120, 227, 40, None, -1, False),
            terrain_nt(150, 465, -5, 5, None, -1, True),
            terrain_nt(930, 465, -5, 5, None, -1, True), ],
        max_monsters=3, possible_monsters=(WEAK, MEDIUM),  # ALL
        background='data/backgrounds/arena_vines.png', p1_spawn=(75, 50), p2_spawn=(992, 50))

    arena4 = arena_nt(
        left_wall_x=65, right_wall_x=1215, floor_y=458,
        platforms=[
            terrain_nt(546, 51, 229, 37, None, -1, False),
            terrain_nt(0, 114, 110, 37, None, -1, False),
            terrain_nt(338, 114, 112, 37, None, -1, False),
            terrain_nt(823, 152, 229, 37, None, -1, False),
            terrain_nt(594, 164, 18, 194, None, -1, False),
            terrain_nt(702, 181, 18, 194, None, -1, False),
            terrain_nt(134, 190, 113, 37, None, -1, False),
            terrain_nt(268, 286, 229, 37, None, -1, False),
            terrain_nt(802, 316, 348, 37, None, -1, False),
            terrain_nt(72, 351, 112, 37, None, -1, False),
            terrain_nt(150, 450, -5, 5, None, -1, True),
            terrain_nt(930, 450, -5, 5, None, -1, True), ],
        max_monsters=3, possible_monsters=(WEAK, MEDIUM),  # ALL
        background='data/backgrounds/arena_human.png', p1_spawn=(75, 50), p2_spawn=(992, 50))

    arena5 = arena_nt(
        left_wall_x=65, right_wall_x=1215, floor_y=458,
        platforms=[
            terrain_nt(59, 70, 40, 298, None, -1, False),
            terrain_nt(236, 44, 40, 298, None, -1, False),
            terrain_nt(498, 119, 112, 37, None, -1, False),
            terrain_nt(953, 47, 112, 37, None, -1, False),
            terrain_nt(1031, 335, 112, 37, None, -1, False),
            terrain_nt(673, 208, 229, 37, None, -1, False),
            terrain_nt(496, 348, 263, 56, None, -1, False),
            terrain_nt(381, 402, 350, 56, None, -1, False),
            terrain_nt(150, 450, -5, 5, None, -1, True),
            terrain_nt(930, 450, -5, 5, None, -1, True), ],
        max_monsters=3, possible_monsters=(WEAK, MEDIUM),  # ALL
        background='data/backgrounds/arena_android.png', p1_spawn=(75, 50), p2_spawn=(985, 150))

    add_to_module_namespace(locals())


class MonsterInfos:
    monster_info_nt = namedtuple('monster_info_nt', 'kind, w, h, dx, dy, hp, chase, idle, exp_value, dmg')
    MONSTER_TABLE = {
        WEAK: monster_info_nt(WEAK, 30, 40, 2, 10, 50, 5000, 5000, WEAK_EXP_VALUE, 3),
        MEDIUM: monster_info_nt(MEDIUM, 50, 60, 3, 12, 100, 7000, 5000, MEDIUM_EXP_VALUE, 5),
        ULTIMATE: monster_info_nt(ULTIMATE, 80, 80, 4, 13, 150, 10000, 5000, ULTIMATE_EXP_VALUE, 8)}

    add_to_module_namespace(locals())

def draw_mouse_debug():
    if INPUT1.DEBUG_MODE_ON:
        pygame.mouse.set_visible(False)
        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.circle(SCREEN, WHITE, mouse_pos, 2, 0)
        pygame.draw.circle(SCREEN, BLACK, mouse_pos, 2, 1)
        real_pos_mouse_font = pygame.font.SysFont('consolas', 12).render(str(mouse_pos), True, DKYELLOW)
        SCREEN.blit(real_pos_mouse_font, (mouse_pos[0] + 3, mouse_pos[1] + 10))
    else:
        pygame.mouse.set_visible(True)
