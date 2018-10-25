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
		self.lastUpdate = pg.time.get_ticks()
		self.currentFrame = 0
		if dir == 'x':
			self.image = EXPLX1
			self.rect = self.image.get_rect()
			self.rect.x = centerx
			self.rect.y = centery
		elif dir == 'y':
			self.image = EXPLY1
			self.rect = self.image.get_rect()
			self.rect.x = centerx
			self.rect.y = centery
		elif dir == "center":
			self.image = EXPL1
			self.rect = self.image.get_rect()
			self.rect.x = centerx
			self.rect.y = centery
			#the center explosion should kill players, it's not needed to check if it collide with other type of sprite since a bomb can only be placed on an empty spaces
			pg.sprite.spritecollide(self, self.game.players, True)
			#four for to let explosion spread and collide in the 4 directions
			for i in range (1, reach + 1):
				#check if the explosion can spread to the next tile, in other word, check if the next tile is already occupied by an indestructible block or not
				if [self.posx + (i * TILESIZE), self.posy] not in self.game.IBlockPos:
					#check collide between explosion and desructible sprites that don't stop the explosion (items and players) and destroy them immediatly
					pg.sprite.spritecollide(Explosion(self.game, self.posx + (i * TILESIZE), self.posy, 0,'x'), self.game.destructibleAndDontBlockExplosion, True)
					#check collide between explosion and destructible sprites that stop the explosion (destructible blocks) and stop the explosion in this direction, doesn't kill immediatly the  sprite, a getDestroyed method is called instead so the blocks can drop item
					hit = pg.sprite.spritecollide(Explosion(self.game, self.posx + (i * TILESIZE), self.posy, 0,'x'), self.game.destructible, False)
					if hit:
						hit[0].getDestroyed()
						break
					#check collide between explosion and bombs
					hit = pg.sprite.spritecollide(Explosion(self.game, self.posx + (i * TILESIZE), self.posy, 0,'x'), self.game.bombs, False)
					#make bomb hit explode, triggering a chain reaction
					if hit:
						hit[0].explode(True)
				#if the next tile is an indestructible block, stop immediatly the spreading of the explosion in that direction
				else:
					break
			#And repeat 3 times ...
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
		self.animate()
		self.die()

	def die(self):
		now = pg.time.get_ticks()
		if now - self.timeOfBirth > EXPLOSION_CLOCK:
			self.kill()

	def animate(self):
		now = pg.time.get_ticks()
		if now - self.lastUpdate > EXPLOSION_CLOCK/3:
			self.lastUpdate = now
			self.currentFrame += 1
			try:
				if self.image in EXPLX:
					self.image = EXPLX[self.currentFrame]
				elif self.image in EXPLY:
					self.image = EXPLY[self.currentFrame]
				elif self.image in EXPL:
					self.image = EXPL[self.currentFrame]
			except:
				pass