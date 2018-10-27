import pygame as pg
from Settings import *
import LoadImages
from PowerUp import PowerUp
import importlib
import random

class Block(pg.sprite.Sprite):
	def __init__(self, game, xSpawn, ySpawn):
		self.groups = game.allSprites, game.blocks, game.destructible
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		self.image = LoadImages.BLOCK_IMAGE
		self.rect = self.image.get_rect()
		self.x = xSpawn * game.tileSize
		self.y = ySpawn * game.tileSize
		self.rect.topleft = (self.x , self.y)

	def getDestroyed(self):
		self.kill()
		PowerUp(self.game, self.x, self.y)

	def refreshData(self):
		importlib.reload(LoadImages)

