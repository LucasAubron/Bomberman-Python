import pygame as pg
from settings import *

#Images are set for a 40 by 40 tiles game, which allow to display a 24x24 tiles map, howewer smaller map only contain 16x16 tiles but keep the same screen size, which mean the tile need to be expanded to 60 by 60

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

EXPLY1 = pg.image.load('../Images/ExplosionImage/Explosiony (1).png')
EXPLY2 = pg.image.load('../Images/ExplosionImage/Explosiony (2).png')
EXPLY3 = pg.image.load('../Images/ExplosionImage/Explosiony (3).png')
EXPLX1 = pg.image.load('../Images/ExplosionImage/Explosionx (1).png')
EXPLX2 = pg.image.load('../Images/ExplosionImage/Explosionx (2).png')
EXPLX3 = pg.image.load('../Images/ExplosionImage/Explosionx (3).png')
EXPL1 = pg.image.load('../Images/ExplosionImage/Explosion (1).png')
EXPL2 = pg.image.load('../Images/ExplosionImage/Explosion (2).png')
EXPL3 = pg.image.load('../Images/ExplosionImage/Explosion (3).png')

EXPLX = [EXPLX1, EXPLX2, EXPLX3]
EXPLY = [EXPLY1, EXPLY2, EXPLY3]
EXPL = [EXPL1, EXPL2, EXPL3]

#Power Up
POWERUP_NUMBER_BOMB = pg.image.load('../Images/PowerUpImage/BombNumber.png')
POWERUP_POWER_BOMB = pg.image.load('../Images/PowerUpImage/BombPower.png')
POWERUP_ROLLER = pg.image.load('../Images/PowerUpImage/Roller.png')

#Block
BLOCK_IMAGE = pg.image.load('../Images/BlockImage/Block.png')
IBLOCK_IMAGE = pg.image.load('../Images/BlockImage/IBlock.png')

#---------------------------------------------------------------------------------------------
#Images get rescaled by 150% if the TILESIZE happens to be 60 and not 40
#Player images are smaller to facilitate his movements on the map, his original size is 31x34 pixels
if not mapIsBig:
	PLAYER_IMAGE = pg.transform.scale(PLAYER_IMAGE, (46,51))
	P1 = pg.transform.scale(P1, (46,51))
	P2 = pg.transform.scale(P2, (46,51))
	P3 = pg.transform.scale(P3, (46,51))
	P4 = pg.transform.scale(P4, (46,51))
	P5 = pg.transform.scale(P5, (46,51))
	P6 = pg.transform.scale(P6, (46,51))
	P7 = pg.transform.scale(P7, (46,51))
	P8 = pg.transform.scale(P8, (46,51))
	P9 = pg.transform.scale(P9, (46,51))
	P10 = pg.transform.scale(P10, (46, 51))
	P11 = pg.transform.scale(P11, (46, 51))
	P12 = pg.transform.scale(P12, (46, 51))
	P13 = pg.transform.scale(P13, (46, 51))
	P14 = pg.transform.scale(P14, (46, 51))
	P15 = pg.transform.scale(P15, (46, 51))
	P16 = pg.transform.scale(P16, (46, 51))

	PLAYER_FRONT = [P1, P2, P3, P4]
	PLAYER_BACK = [P5, P6, P7, P8]
	PLAYER_RIGHT = [P9, P10, P11, P12]
	PLAYER_LEFT = [P13, P14, P15, P16]


	#Bomb and explosion
	BOMB_IMAGE = pg.transform.scale(BOMB_IMAGE, (60, 60))

	EXPLY1 = pg.transform.scale(EXPLY1, (60, 60))
	EXPLY2 = pg.transform.scale(EXPLY2, (60, 60))
	EXPLY3 = pg.transform.scale(EXPLY3, (60, 60))
	EXPLX1 = pg.transform.scale(EXPLX1, (60, 60))
	EXPLX2 = pg.transform.scale(EXPLX2, (60, 60))
	EXPLX3 = pg.transform.scale(EXPLX3, (60, 60))
	EXPL1 = pg.transform.scale(EXPL1, (60, 60))
	EXPL2 = pg.transform.scale(EXPL2, (60, 60))
	EXPL3 = pg.transform.scale(EXPL3, (60, 60))

	EXPLX = [EXPLX1, EXPLX2, EXPLX3]
	EXPLY = [EXPLY1, EXPLY2, EXPLY3]
	EXPL = [EXPL1, EXPL2, EXPL3]

	#Power Up
	POWERUP_NUMBER_BOMB = pg.transform.scale(POWERUP_NUMBER_BOMB, (60, 60))
	POWERUP_POWER_BOMB = pg.transform.scale(POWERUP_POWER_BOMB, (60, 60))
	POWERUP_ROLLER = pg.transform.scale(POWERUP_ROLLER, (60, 60))

	#Block
	BLOCK_IMAGE = pg.transform.scale(BLOCK_IMAGE, (60, 60))
	IBLOCK_IMAGE = pg.transform.scale(IBLOCK_IMAGE, (60, 60))
