import pygame as pg
from settings import *
from loadImage import *
from PowerUp import PowerUp
import random

class Block(pg.sprite.Sprite):
	def __init__(self, game, xSpawn, ySpawn):
		self.groups = game.allSprites, game.blocks, game.destructible
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		self.image = BLOCK_IMAGE
		self.rect = self.image.get_rect()
		self.x = xSpawn * TILESIZE
		self.y = ySpawn * TILESIZE
		self.rect.topleft = (self.x , self.y)

	def getDestroyed(self):
		self.kill()
		if random.randint(0,1):
			PowerUp(self.game, self.x, self.y)

