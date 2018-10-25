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
#Player's movement speed is calculated in pixel/ms so if the tile size change but the screen size doesn't, we need to make sure the player moves faster (for smaller map)
PLAYER_SPEED = 15 if mapIsBig else 23
ANIMATION_TIME_TO_WAIT = 100
MAX_BOMB_POWER = 12 if mapIsBig else 8
MAX_BOMB = 12 if mapIsBig else 8
MAX_ROLLER = 4 if mapIsBig else 3
ROLLER_SPEED = 0.8

#BOMB
BOMB_CLOCK = 2500
EXPLOSION_CLOCK = 150

#Loot
CHANCE_ROLLER = 5
CHANCE_POWERBOMB = 15
CHANCE_BOMB_NUMBER = 15
CHANCE_TO_LOOT_NOTHING = 100 - CHANCE_POWERBOMB - CHANCE_ROLLER - CHANCE_BOMB_NUMBER

#-------------------------------------------------------------------------------------------