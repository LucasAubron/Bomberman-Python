import pygame as pg
from settings import *
from loadImage import *
from Explosion import Explosion

class Bomb(pg.sprite.Sprite):
	def __init__(self, player, game, bombx, bomby):
		self.groups = game.allSprites, game.bombs
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		self.player = player
		self.image = BOMB_IMAGE
		self.rect = self.image.get_rect()
		self.bombx = bombx
		self.bomby = bomby
		self.power = player.bombPower
		self.rect.topleft = (bombx * TILESIZE, bomby * TILESIZE)
		self.game.bombPos.append([bombx, bomby])
		self.timeOfBirth = pg.time.get_ticks()

	def update(self):
		self.becomeBlock()
		self.explode(False)

	def becomeBlock(self):
		if not pg.sprite.spritecollide(self, self.game.players, False):
			self.add(self.game.blocks)
	
	def explode(self, triggeredByAnotherBomb):
		now = pg.time.get_ticks()
		if now - self.timeOfBirth > BOMB_CLOCK or triggeredByAnotherBomb:
			self.game.bombPos.remove([self.bombx, self.bomby])
			self.player.bomb += 1
			self.kill()	
			Explosion(self.game, self.bombx*TILESIZE, self.bomby*TILESIZE, self.power, "center")
			