import pygame as pg
import settings
import LoadImages
from Explosion import Explosion
import importlib

class Bomb(pg.sprite.Sprite):
	def __init__(self, player, game, bombx, bomby):
		self.groups = game.allSprites, game.bombs
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		self.player = player
		self.image = LoadImages.BOMB_IMAGE
		self.rect = self.image.get_rect()
		self.bombx = bombx
		self.bomby = bomby
		self.power = player.bombPower
		self.rect.topleft = (bombx * settings.TILESIZE, bomby * settings.TILESIZE)
		self.game.bombPos.append([bombx, bomby])
		self.timeOfBirth = pg.time.get_ticks()
		self.canBecomeABlock = True #In order to prevent invisible blocks caused by destroyed bomb

	def update(self):
		self.becomeBlock()
		self.explode(False)

	def becomeBlock(self):
		if self.canBecomeABlock and not pg.sprite.spritecollide(self, self.game.players, False):
			self.add(self.game.blocks)
			self.canBecomeABlock = False
	
	def explode(self, triggeredByAnotherBomb):
		now = pg.time.get_ticks()
		if now - self.timeOfBirth > settings.BOMB_CLOCK or triggeredByAnotherBomb:
			try:
				self.game.bombPos.remove([self.bombx, self.bomby])
			except:
				pass
			self.game.bombs.remove(self)
			self.player.bomb += 1
			self.kill()	
			Explosion(self.game, self.bombx*settings.TILESIZE, self.bomby*settings.TILESIZE, self.power, "center")

	def refreshData(self):
		importlib.reload(settings)
		importlib.reload(LoadImages)
