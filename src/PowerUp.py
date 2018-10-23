import pygame as pg
from settings import *
from loadImage import *
import random

class PowerUp(pg.sprite.Sprite):
	def __init__(self, game, xSpawn, ySpawn):
		self.groups = game.allSprites, game.destructibleAndDontBlockExplosion, game.powerUp
		pg.sprite.Sprite.__init__(self, self.groups)
		imageList = [POWERUP_NUMBER_BOMB, POWERUP_POWER_BOMB]
		self.image = random.choice(imageList)
		self.rect = self.image.get_rect()
		self.rect.topleft = (xSpawn, ySpawn)

	def isTaken(self, player):
		if self.image == POWERUP_NUMBER_BOMB:
			player.bomb += 1
		else:
			player.bombPower +=1