import pygame as pg
import Settings
import LoadImages
from Bomb import Bomb
from PowerUp import PowerUp
import importlib

class Player(pg.sprite.Sprite):
	def __init__(self, game, xSpawn, ySpawn, id):
		self.groups = game.allSprites, game.players, game.destructibleAndDontBlockExplosion
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		self.image = LoadImages.PLAYER_IMAGE
		self.rect = self.image.get_rect()
		self.x, self.y = xSpawn * Settings.TILESIZE, ySpawn * Settings.TILESIZE
		self.vx, self.vy = 0, 0
		self.id = id 
		self.dropBomb = False
		self.bomb = 1
		self.bombPower = 1
		self.roller = 0
		self.maxBombPower = Settings.MAX_BOMB_POWER
		self.maxBomb = Settings.MAX_BOMB
		self.maxRoller = Settings.MAX_ROLLER
		self.choice = 1000 #for bots
		self.lastSavedPos = [self.x, self.y] #for bots
		self.lastBotUpdate = 0 #for bots
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
		if self.vx !=0:
			self.x += self.vx * (self.game.dt + (Settings.ROLLER_SPEED * self.roller / abs(self.vx)))
		if self.vy !=0:
			self.y += self.vy * (self.game.dt + (Settings.ROLLER_SPEED * self.roller / abs(self.vy)))

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

	def collideWithBorder(self):
		if self.x > Settings.DISPLAY_SIZE - self.rect.width:
			self.x = Settings.DISPLAY_SIZE - self.rect.width
		if self.x < 0:
			self.x = 0
		if self.y > Settings.DISPLAY_SIZE - self.rect.height:
			self.y = Settings.DISPLAY_SIZE - self.rect.height
		if self.y < 0:
			self.y = 0
		self.updatePosition("both")		

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

	def updatePosition(self, dir):
		if dir == 'x':
			self.rect.x = self.x
		elif dir == 'y':
			self.rect.y = self.y
		elif dir =="both":
			self.rect.x, self.rect.y = self.x, self.y

	def attack(self):
		bombx, bomby = self.rect.center[0]//Settings.TILESIZE, self.rect.center[1]//Settings.TILESIZE
		if self.dropBomb and self.bomb>0 and [bombx, bomby] not in self.game.bombPos:
			Bomb(self, self.game, bombx, bomby)
			self.bomb -= 1
		self.dropBomb = False

	def animate(self):
		now = pg.time.get_ticks()
		if now - self.lastUpdate > Settings.ANIMATION_TIME_TO_WAIT:
			self.lastUpdate = now
			if self.vx > 0:
				self.currentFrame = (self.currentFrame + 1) % len(LoadImages.PLAYER_RIGHT)
				self.image = LoadImages.PLAYER_RIGHT[self.currentFrame]
				self.lastDirection = (1, 0)
			elif self.vx < 0:
				self.currentFrame = (self.currentFrame + 1) % len(LoadImages.PLAYER_LEFT)
				self.image = LoadImages.PLAYER_LEFT[self.currentFrame]
				self.lastDirection = (-1, 0)
			elif self.vy > 0:
				self.currentFrame = (self.currentFrame + 1) % len(LoadImages.PLAYER_FRONT)
				self.image = LoadImages.PLAYER_FRONT[self.currentFrame]
				self.lastDirection = (0, 1)
			elif self.vy < 0:
				self.currentFrame = (self.currentFrame + 1) % len(LoadImages.PLAYER_BACK)
				self.image = LoadImages.PLAYER_BACK[self.currentFrame]
				self.lastDirection = (0, -1)
			else:
				if self.lastDirection == (1, 0):
					self.image = LoadImages.PLAYER_RIGHT[0]
				elif self.lastDirection == (-1, 0):
					self.image = LoadImages.PLAYER_LEFT[0]
				elif self.lastDirection == (0, 1):
					self.image = LoadImages.PLAYER_FRONT[0]
				elif self.lastDirection == (0, -1):
					self.image = LoadImages.PLAYER_BACK[0]

	def getKeys(self):
		keys = pg.key.get_pressed()
		if self.id == 1:
			if keys[pg.K_w]:
				self.vy = -Settings.PLAYER_SPEED
			if keys[pg.K_a]:
				self.vx = -Settings.PLAYER_SPEED
			if keys[pg.K_s]:
				self.vy = Settings.PLAYER_SPEED
			if keys[pg.K_d]:
				self.vx = Settings.PLAYER_SPEED
			if self.vx != 0 and self.vy != 0:
				self.vx *= 0.7071
				self.vy *= 0.7071
			if keys[pg.K_SPACE]:
				self.dropBomb = True
		'''		
		if self.id == 2:
			if keys[pg.K_UP]:
				self.vy = -Settings.PLAYER_SPEED
			if keys[pg.K_LEFT]:
				self.vx = -Settings.PLAYER_SPEED
			if keys[pg.K_DOWN]:
				self.vy = Settings.PLAYER_SPEED
			if keys[pg.K_RIGHT]:
				self.vx = Settings.PLAYER_SPEED
			if self.vx != 0 and self.vy != 0:
				self.vx *= 0.7071
				self.vy *= 0.7071
			if keys[pg.K_KP_ENTER]:
				self.dropBomb = True
		'''		
		#Player's movement speed is calculated in pixel/ms so if the tile rise but the screen size doesn't, we need to make sure the player moves faster so his tile/ms speed stays the same
		if Settings.TILESIZE == 60: self.vx, self.vy = self.vx * 1.5, self.vy * 1.5

	def refreshData(self):
		importlib.reload(Settings)
		importlib.reload(LoadImages)
