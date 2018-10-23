import pygame as pg
from settings import *
from loadImage import *
from Bomb import Bomb
from PowerUp import PowerUp

class Player(pg.sprite.Sprite):
	def __init__(self, game, xSpawn, ySpawn, id):
		self.groups = game.allSprites, game.players, game.destructibleAndDontBlockExplosion
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		self.image = PLAYER_IMAGE
		self.rect = self.image.get_rect()
		self.x, self.y = xSpawn * TILESIZE, ySpawn * TILESIZE
		self.vx, self.vy = 0, 0
		self.id = id 
		self.dropBomb = False
		self.bomb = 1
		self.bombPower = 1
		self.lastUpdate = 0
		self.lastDirection = (0, 0)
		self.currentFrame = 0

	def update(self):
		self.getKeys()
		self.move()
		self.updatePosition('x')
		self.collideWithWalls('x')
		self.updatePosition('y')
		self.collideWithWalls('y')
		self.collideWithBorder()
		self.attack()
		self.getPowerUp()
		self.animate()
		self.setSpeedToZero("both")
		
	def move(self):
		self.x += self.vx * self.game.dt
		self.y += self.vy * self.game.dt

	def collideWithWalls(self, dir):
		hits = pg.sprite.spritecollide(self, self.game.blocks, False)
		if dir == 'x':
			if hits:
				if self.vx > 0:
					self.x = hits[0].rect.left - self.rect.width
				elif self.vx < 0:
					self.x = hits[0].rect.right
			self.updatePosition('x')
		if dir == 'y':
			if hits:
				if self.vy > 0:
					self.y = hits[0].rect.top - self.rect.height
				elif self.vy < 0:
					self.y = hits[0].rect.bottom
			self.updatePosition('y')

	def getPowerUp(self):
		hits = pg.sprite.spritecollide(self, self.game.powerUp, True)
		for powerUp in hits:
			powerUp.isTaken(self)

	def setSpeedToZero(self, dir):
		if dir =='x':
			self.vx = 0
		elif dir =='y':
			self.vy = 0
		elif dir == 'both':
			self.vx, self.vy = 0, 0

	def collideWithBorder(self):
		if self.x > DISPLAY_SIZE - self.rect.width:
			self.x = DISPLAY_SIZE - self.rect.width
		if self.x < 0:
			self.x = 0
		if self.y > DISPLAY_SIZE - self.rect.height:
			self.y = DISPLAY_SIZE - self.rect.height
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
		bombx, bomby = self.rect.center[0]//TILESIZE, self.rect.center[1]//TILESIZE
		if self.dropBomb and self.bomb>0 and [bombx, bomby] not in self.game.bombPos:
			Bomb(self, self.game, bombx, bomby)
			self.bomb -= 1
		self.dropBomb = False

	def animate(self):
		now = pg.time.get_ticks()
		if now - self.lastUpdate > ANIMATION_TIME_TO_WAIT:
			self.lastUpdate = now
			if self.vx > 0:
				self.currentFrame = (self.currentFrame + 1) % len(PLAYER_RIGHT)
				self.image = PLAYER_RIGHT[self.currentFrame]
				self.lastDirection = (1, 0)
			elif self.vx < 0:
				self.currentFrame = (self.currentFrame + 1) % len(PLAYER_LEFT)
				self.image = PLAYER_LEFT[self.currentFrame]
				self.lastDirection = (-1, 0)
			elif self.vy > 0:
				self.currentFrame = (self.currentFrame + 1) % len(PLAYER_FRONT)
				self.image = PLAYER_FRONT[self.currentFrame]
				self.lastDirection = (0, 1)
			elif self.vy < 0:
				self.currentFrame = (self.currentFrame + 1) % len(PLAYER_BACK)
				self.image = PLAYER_BACK[self.currentFrame]
				self.lastDirection = (0, -1)
			else:
				if self.lastDirection == (1,0):
					self.image = PLAYER_RIGHT[0]
				elif self.lastDirection == (-1,0):
					self.image = PLAYER_LEFT[0]
				elif self.lastDirection == (0, 1):
					self.image = PLAYER_FRONT[0]
				elif self.lastDirection == (0, -1):
					self.image = PLAYER_BACK[0]

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