# C
import pygame

COLOR_MENU = (50, 25, 0)
COLOR_MENU_OP = (250, 250, 230)
COLOR_MENU_SELECT = (0, 255, 255)

# E

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'Level1Bg7': 999,
    'Level1Bg8': 999,
    'Level2Bg0': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Level2Bg3': 999,
    'Level2Bg4': 999,
    'Player1': 300,
    'Player1Shot': 1,
    'Player2': 300,
    'Player2Shot': 1,
    'Enemy1': 50,
    'Enemy1Shot': 1,
    'Enemy2': 60,
    'Enemy2Shot': 1,
}

ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 1,
    'Level1Bg3': 2,
    'Level1Bg4': 3,
    'Level1Bg5': 4,
    'Level1Bg6': 5,
    'Level1Bg7': 6,
    'Level1Bg8': 7,
    'Player1': 6,
    'Player2': 6,
    'Enemy1': 3,
    'Enemy2' : 2

}

EVENT_ENEMY = pygame.USEREVENT +1

# M
MENU_OPTION = (' Novo Jogo - 1 Jogador ',
               ' Novo Jogo - 2 Jogador - Cooperativo ',
               ' Novo Jogo - 2 Jogador - Competitivo ',
               'Classificação',
               'Sair'
               )
# p
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL,
                    'Player2': pygame.K_LCTRL}
#
SPAW_TIME = 2000
# W
WIN_WIDTH = 1000
WIN_HEIGHT = 561
