import pygame as pg
from settings import *
from loadImage import *

class Player(pg.sprite.Sprite):
	def __init__(self, game, xSpawn, ySpawn, number):
		self.groups = game.allSprites
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		self.number = number
		self.image = PLAYER_IMAGE
		self.rect = self.image.get_rect()
		self.rect.topleft = (xSpawn, ySpawn)

