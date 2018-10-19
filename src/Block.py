import pygame as pg
from settings import *
from loadImage import *

class Block(pg.sprite.Sprite):
	def __init__(self, game, xSpawn, ySpawn):
		self.groups = game.allSprites
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		self.image = BLOCK_IMAGE
		self.rect = self.image.get_rect()
		self.rect.topleft = (xSpawn, ySpawn)
