import pygame as pg
import random
import Settings
import LoadImages
from Player import Player
from Bomb import Bomb
from PowerUp import PowerUp
import importlib

class Bot(Player):
	def getKeys(self):
		now = pg.time.get_ticks()
		if abs(self.lastSavedPos[0] - self.x) >= Settings.TILESIZE or abs(self.lastSavedPos[1] - self.y) >= Settings.TILESIZE or (now-self.lastBotUpdate) > Settings.TIME_BOT_WAIT:
			self.refresh(now)
			if self.choice == -1:
				self.choice = 1000
				#self.choice = random.randint(1,10005)
			else:
				self.choice =-1
		if 0 <= self.choice < 2500:
			self.vy = -Settings.PLAYER_SPEED
		if 2500 <= self.choice < 5000:
			self.vx = -Settings.PLAYER_SPEED
		if 5000 <= self.choice < 7500:
			self.vy = Settings.PLAYER_SPEED
		if 7500 <= self.choice < 10000:
			self.vx = Settings.PLAYER_SPEED
		if self.vx != 0 and self.vy != 0:
			self.vx *= 0.7071
			self.vy *= 0.7071
		if 10000 <= self.choice <= 10005:
			self.dropBomb = True
	#Player's movement speed is calculated in pixel/ms so if the tile rise but the screen size doesn't, we need to make sure the player moves faster so his tile/ms speed stays the same
		if Settings.TILESIZE == 60: self.vx, self.vy = self.vx * 1.5, self.vy * 1.5

	def refresh(self, now):
		self.lastBotUpdate = now
		self.lastSavedPos[0], self.lastSavedPos[1] = self.x, self.y
		self.rect.x, self.rect.y = (self.rect.center[0]//Settings.TILESIZE) * Settings.TILESIZE, (self.rect.center[1]//Settings.TILESIZE) * Settings.TILESIZE
		self.updatePosition("both")

	def refreshData(self):
		importlib.reload(Settings)		