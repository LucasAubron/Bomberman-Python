import pygame as pg
from settings import *
from loadImage import *

class Bomb:
	def __init__(self, player, game, bombx, bomby):
		self.groups = game.allSprites, game.bombs
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		self.image = BLOCK_IMAGE
		self.rect = self.image.get_rect()