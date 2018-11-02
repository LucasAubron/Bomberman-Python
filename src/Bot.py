import pygame as pg
from Player import Player
import random
from Settings import *
import LoadImages
from Bomb import Bomb
from PowerUp import PowerUp
import importlib

class Bot(Player):
	def getKeys(self):
		choice = random.randint(1,10005)
		if 0 <= choice < 2500:
			self.vy = -PLAYER_SPEED
		if 2500 <= choice < 5000:
			self.vx = -PLAYER_SPEED
		if 5000 <= choice < 7500:
			self.vy = PLAYER_SPEED
		if 7500 <= choice < 10000:
			self.vx = PLAYER_SPEED
		if self.vx != 0 and self.vy != 0:
			self.vx *= 0.7071
			self.vy *= 0.7071
		if 10000 <= choice <= 10005:
			self.dropBomb = True
	#Player's movement speed is calculated in pixel/ms so if the tile rise but the screen size doesn't, we need to make sure the player moves faster so his tile/ms speed stays the same
		if self.game.tileSize == 60: self.vx, self.vy = self.vx * 1.5, self.vy * 1.5