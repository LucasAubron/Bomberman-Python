import pygame as pg
import settings
import LoadImages
import random
import importlib

class PowerUp(pg.sprite.Sprite):
	def __init__(self, game, xSpawn, ySpawn):
		self.groups = game.allSprites, game.destructibleAndDontBlockExplosion, game.powerUp
		pg.sprite.Sprite.__init__(self, self.groups)
		randomVar = random.randint(1,100)
		if randomVar > 100 - settings.CHANCE_TO_LOOT_NOTHING:
			self.kill()
		else:
			if 0 < randomVar <= settings.CHANCE_ROLLER:
				self.image = LoadImages.POWERUP_ROLLER
			elif settings.CHANCE_ROLLER < randomVar <= settings.CHANCE_ROLLER + settings.CHANCE_POWERBOMB:
				self.image = LoadImages.POWERUP_NUMBER_BOMB
			elif settings.CHANCE_ROLLER + settings.CHANCE_POWERBOMB < randomVar <= settings.CHANCE_ROLLER + settings.CHANCE_POWERBOMB + settings.CHANCE_BOMB_NUMBER: 
				self.image = LoadImages.POWERUP_POWER_BOMB
			self.rect = self.image.get_rect()
			self.rect.topleft = (xSpawn, ySpawn)

	def isTaken(self, player):
		if self.image == LoadImages.POWERUP_NUMBER_BOMB:
			if player.bomb < player.maxBomb:
				player.bomb += 1
		elif self.image == LoadImages.POWERUP_POWER_BOMB:
			if player.bombPower < player.maxBombPower:
				player.bombPower +=1
		elif self.image == LoadImages.POWERUP_ROLLER:
			if player.roller < player.maxRoller:
				player.roller += 1

	def refreshData(self):
		importlib.reload(settings)
		importlib.reload(LoadImages)
		