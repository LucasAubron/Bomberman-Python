import pygame as pg
from Settings import *
import LoadImages
import importlib

class IBlock(pg.sprite.Sprite):
	def __init__(self, game, xSpawn, ySpawn):
		self.groups = game.allSprites, game.blocks
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		self.image = LoadImages.IBLOCK_IMAGE
		self.rect = self.image.get_rect()
		self.x = xSpawn * game.tileSize
		self.y = ySpawn * game.tileSize
		self.rect.topleft = (self.x, self.y)
		self.game.IBlockPos.append([self.x, self.y])

	def refreshData(self):
		importlib.reload(LoadImages)

