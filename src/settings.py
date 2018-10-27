import pygame as pg
import random

#screen seetings
DISPLAY_SIZE = 960
FPS = 60
TITLE = "Bomberman"

#COLORS
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
GREY = (30,30,30)

#GRID
BIG_TILESIZE = 60
SMALL_TILESIZE = 40
TILESIZE = random.choice([BIG_TILESIZE, SMALL_TILESIZE])
mapIsBig = True if TILESIZE == 40 else False
GRID_COLOR = GREY
BG_COLOR = WHITE
TILE_ON_LINE = DISPLAY_SIZE/TILESIZE

#GAME MOTOR----------------------------------------------------------------------------------

#Player

PLAYER_SPEED = 14
ANIMATION_TIME_TO_WAIT = 100
MAX_BOMB_POWER = 12
MAX_BOMB = 8
MAX_ROLLER = 4
ROLLER_SPEED = 0.8 if mapIsBig else 0.6

#BOMB
BOMB_CLOCK = 2500
EXPLOSION_CLOCK = 150

#Loot
CHANCE_ROLLER = 5
CHANCE_POWERBOMB = 15
CHANCE_BOMB_NUMBER = 25
CHANCE_TO_LOOT_NOTHING = 100 - CHANCE_POWERBOMB - CHANCE_ROLLER - CHANCE_BOMB_NUMBER

#-------------------------------------------------------------------------------------------