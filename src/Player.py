import pygame as pg
from settings import *
from loadImage import *

class Player(pg.sprite.Sprite):
	def __init__(self, game, xSpawn, ySpawn):
		self.groups = game.allSprites, game.players
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		self.image = PLAYER_IMAGE
		self.rect = self.image.get_rect()
		self.x, self.y = xSpawn * TILESIZE, ySpawn * TILESIZE
		self.vx, self.vy = 0, 0
		self.size = self.rect.width
		self.dropBomb = False
		self.bomb = 1
		self.bombPower = 1

	def update(self):
		self.getKeys()
		self.move()
		self.updatePosition('x')
		self.collideWithWalls('x')
		self.updatePosition('y')
		self.collideWithWalls('y')
		self.collideWithBorder()
		self.setSpeedToZero("both")
		self.attack()

	def move(self):
		self.x += self.vx * self.game.dt
		self.y += self.vy * self.game.dt

	def collideWithWalls(self, dir):
		hits = pg.sprite.spritecollide(self, self.game.blocks, False)
		if dir == 'x':
			if hits:
				if self.vx > 0:
					self.x = hits[0].rect.left - self.size
				elif self.vx < 0:
					self.x = hits[0].rect.right
			self.updatePosition('x')
		if dir == 'y':
			if hits:
				if self.vy > 0:
					self.y = hits[0].rect.top - self.size
				elif self.vy < 0:
					self.y = hits[0].rect.bottom
			self.updatePosition('y')

	def setSpeedToZero(self, dir):
		if dir =='x':
			self.vx = 0
		elif dir =='y':
			self.vy = 0
		elif dir == 'both':
			self.vx, self.vy = 0, 0

	def collideWithBorder(self):
		if self.x > DISPLAY_SIZE - self.size:
			self.x = DISPLAY_SIZE - self.size
		if self.x < 0:
			self.x = 0
		if self.y > DISPLAY_SIZE - self.size:
			self.y = DISPLAY_SIZE - self.size
		if self.y < 0:
			self.y = 0
		self.updatePosition("both")

	def updatePosition(self, dir):
		if dir == 'x':
			self.rect.x = self.x
		elif dir == 'y':
			self.rect.y = self.y
		elif dir =="both":
			self.rect.x, self.rect.y = self.x, self.y

	def attack(self):
		pass

	def getKeys(self):
		keys = pg.key.get_pressed()
		if keys[pg.K_w]:
			self.vy = -PLAYER_SPEED
		if keys[pg.K_a]:
			self.vx = -PLAYER_SPEED
		if keys[pg.K_s]:
			self.vy = PLAYER_SPEED
		if keys[pg.K_d]:
			self.vx = PLAYER_SPEED
		if self.vx != 0 and self.vy != 0:
			self.vx *= 0.7071
			self.vy *= 0.7071
		if keys[pg.K_SPACE]:
			self.dropBomb = True



