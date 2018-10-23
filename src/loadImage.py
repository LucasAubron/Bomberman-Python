import pygame as pg
from settings import *

#Player
PLAYER_IMAGE = pg.image.load('../Images/PlayerImage/Player.png')
P1 = pg.image.load('../Images/PlayerImage/PlayerFront/PlayerFront (1).png')
P2 = pg.image.load('../Images/PlayerImage/PlayerFront/PlayerFront (2).png')
P3 = pg.image.load('../Images/PlayerImage/PlayerFront/PlayerFront (3).png')
P4 = pg.image.load('../Images/PlayerImage/PlayerFront/PlayerFront (4).png')
P5 = pg.image.load('../Images/PlayerImage/PlayerBack/PlayerBack (1).png')
P6 = pg.image.load('../Images/PlayerImage/PlayerBack/PlayerBack (2).png')
P7 = pg.image.load('../Images/PlayerImage/PlayerBack/PlayerBack (3).png')
P8 = pg.image.load('../Images/PlayerImage/PlayerBack/PlayerBack (4).png')
P9 = pg.image.load('../Images/PlayerImage/PlayerRight/PlayerRight (1).png')
P10 = pg.image.load('../Images/PlayerImage/PlayerRight/PlayerRight (2).png')
P11 = pg.image.load('../Images/PlayerImage/PlayerRight/PlayerRight (3).png')
P12 = pg.image.load('../Images/PlayerImage/PlayerRight/PlayerRight (4).png')
P13 = pg.image.load('../Images/PlayerImage/PlayerLeft/PlayerLeft (1).png')
P14 = pg.image.load('../Images/PlayerImage/PlayerLeft/PlayerLeft (2).png')
P15 = pg.image.load('../Images/PlayerImage/PlayerLeft/PlayerLeft (3).png')
P16 = pg.image.load('../Images/PlayerImage/PlayerLeft/PlayerLeft (4).png')

PLAYER_FRONT = [P1, P2, P3, P4]
PLAYER_BACK = [P5, P6, P7, P8]
PLAYER_RIGHT = [P9, P10, P11, P12]
PLAYER_LEFT = [P13, P14, P15, P16]


#Bomb and explosion
BOMB_IMAGE = pg.image.load('../Images/BombImage/Bomb.png')
BG_IMAGE = pg.image.load('../Images/BackgroundImage/Background.png')
EXPLOSION_Y = pg.image.load('../Images/ExplosionImage/Explosiony.png')
EXPLOSION_X = pg.image.load('../Images/ExplosionImage/Explosionx.png')
EXPLOSION = pg.image.load('../Images/ExplosionImage/Explosion.png')

#Power Up
POWERUP_NUMBER_BOMB = pg.image.load('../Images/PowerUpImage/BombNumber.png')
POWERUP_POWER_BOMB = pg.image.load('../Images/PowerUpImage/BombPower.png')

#Block
BLOCK_IMAGE = pg.image.load('../Images/BlockImage/Block.png')
IBLOCK_IMAGE = pg.image.load('../Images/BlockImage/IBlock.png')