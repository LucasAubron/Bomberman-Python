import pygame as pg
from settings import *
from loadImage import *

class Explosion(pg.sprite.Sprite):
	def __init__(self, game, centerx, centery, reach, dir):
		self.groups = game.allSprites
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		self.reach = reach
		self.posx = centerx
		self.posy = centery
		self.timeOfBirth = pg.time.get_ticks()
		if dir == 'x':
			self.image = EXPLOSION_X
			self.rect = self.image.get_rect()
			self.rect.x = centerx
			self.rect.y = centery
		elif dir == 'y':
			self.image = EXPLOSION_Y
			self.rect = self.image.get_rect()
			self.rect.x = centerx
			self.rect.y = centery
		elif dir == "center":
			self.image = EXPLOSION
			self.rect = self.image.get_rect()
			self.rect.x = centerx
			self.rect.y = centery
			for i in range (1, reach + 1):
				if [self.posx + (i * TILESIZE), self.posy] not in self.game.IBlockPos:
					pg.sprite.spritecollide(Explosion(self.game, self.posx + (i * TILESIZE), self.posy, 0,'x'), self.game.destructibleAndDontBlockExplosion, True)
					hit = pg.sprite.spritecollide(Explosion(self.game, self.posx + (i * TILESIZE), self.posy, 0,'x'), self.game.destructible, False)
					if hit:
						hit[0].getDestroyed()
						break
					hit = pg.sprite.spritecollide(Explosion(self.game, self.posx + (i * TILESIZE), self.posy, 0,'x'), self.game.bombs, False)
					if hit:
						hit[0].explode(True)
				else:
					break
			for i in range (1, reach + 1):
				if [self.posx + (-i * TILESIZE), self.posy] not in self.game.IBlockPos:
					pg.sprite.spritecollide(Explosion(self.game, self.posx + (-i * TILESIZE), self.posy, 0,'x'), self.game.destructibleAndDontBlockExplosion, True)
					hit = pg.sprite.spritecollide(Explosion(self.game, self.posx + (-i * TILESIZE), self.posy, 0,'x'), self.game.destructible, False)
					if hit:
						hit[0].getDestroyed()
						break
					hit = pg.sprite.spritecollide(Explosion(self.game, self.posx + (-i * TILESIZE), self.posy, 0,'x'), self.game.bombs, False)
					if hit:
						hit[0].explode(True)
				else:
					break
			for j in range (1, reach + 1):
				if [self.posx, self.posy + (j * TILESIZE)] not in self.game.IBlockPos:
					pg.sprite.spritecollide(Explosion(self.game, self.posx, self.posy + (j * TILESIZE), 0,'y'), self.game.destructibleAndDontBlockExplosion, True)
					hit = pg.sprite.spritecollide(Explosion(self.game, self.posx, self.posy + (j * TILESIZE), 0,'y'), self.game.destructible, False)
					if hit:
						hit[0].getDestroyed()
						break
					hit = pg.sprite.spritecollide(Explosion(self.game, self.posx, self.posy + (j * TILESIZE), 0,'y'), self.game.bombs, False)
					if hit:
						hit[0].explode(True)
				else:
					break
			for j in range (1, reach + 1):
				if [self.posx, self.posy + (-j * TILESIZE)] not in self.game.IBlockPos:
					pg.sprite.spritecollide(Explosion(self.game, self.posx, self.posy + (-j * TILESIZE), 0,'y'), self.game.destructibleAndDontBlockExplosion, True)
					hit = pg.sprite.spritecollide(Explosion(self.game, self.posx, self.posy + (-j * TILESIZE), 0,'y'), self.game.destructible, False)
					if hit:
						hit[0].getDestroyed()
						break
					hit = pg.sprite.spritecollide(Explosion(self.game, self.posx, self.posy + (-j * TILESIZE), 0,'y'), self.game.bombs, False)
					if hit:
						hit[0].explode(True)
				else:
					break

	def update(self):
		now = pg.time.get_ticks()
		if now - self.timeOfBirth > EXPLOSION_CLOCK:
			self.kill()



