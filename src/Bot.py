import pygame as pg
import random
import settings
import LoadImages
from Player import Player
from Bomb import Bomb
from PowerUp import PowerUp
import importlib

class Bot(Player):
	def getKeys(self):
		now = pg.time.get_ticks()
		if abs(self.lastSavedPos[0] - self.x) >= settings.TILESIZE or abs(self.lastSavedPos[1] - self.y) >= settings.TILESIZE or (now-self.lastBotUpdate) > settings.TIME_BOT_WAIT:
			self.centerSquare(now)
			matrice = self.getInfo()
			mode = self.choseMode(matrice)
			squareToGo = self.choseSquareToGoTo(matrice, mode)
			#self.choice = self.choseAction(squareToGo[0], squareToGo[1]) #squareToGo = [where to go, do the bot want to place a bomb once he arrives]
			self.choice = random.randint(0, 10000)
		if 0 <= self.choice < 2500:
			self.vy = -settings.PLAYER_SPEED
		if 2500 <= self.choice < 5000:
			self.vx = -settings.PLAYER_SPEED
		if 5000 <= self.choice < 7500:
			self.vy = settings.PLAYER_SPEED
		if 7500 <= self.choice < 10000:
			self.vx = settings.PLAYER_SPEED
		if self.vx != 0 and self.vy != 0:
			self.vx *= 0.7071
			self.vy *= 0.7071
		if 10000 <= self.choice <= 12500:
			self.dropBomb = True
	#Player's movement speed is calculated in pixel/ms so if the tile size rise but the screen size doesn't, we need to make sure the player moves faster so his tile/ms speed stays the same
		if settings.TILESIZE == 60: self.vx, self.vy = self.vx * 1.5, self.vy * 1.5

	#the bot analyse his surrounding, returns a two dimensionnal array
	def getInfo(self):
		matrice = [[0,0]]
		return matrice

	#Depending on what the bot knows, he choses a strategy for the next few sec: defensiv (run away from bombs), aggresiv (rush unto enemies and place bomb near them), loot (destroy blocks and pick up powerUp)
	def choseMode(self, matrice):
		mode = "aggresiv"
		return mode

	#Once we know what is the gameplan, we need to chose a square to go to and if we want to place a bomb there or not
	def choseSquareToGoTo(self, matrice, mode):
		square =[0,0]
		return square

	#We have an objectiv, we need to find the best path and place a bomb or not once we arrive
	def choseAction(self, square, placeABomb):
		action = "left"
		return action

	#to make sure the bot is always centered in a square
	def centerSquare(self, now):
		self.lastBotUpdate = now
		self.lastSavedPos[0] = self.x
		self.lastSavedPos[1] = self.y
		self.updatePosition("both")
		self.x = int((self.rect.center[0] // settings.TILESIZE) * settings.TILESIZE) + 10 # +10 and +3 because the bot is not perfectly centered (because the player image is smaller than 40x40 and is placed at the topleft corner)
		self.y = int((self.rect.center[1] // settings.TILESIZE) * settings.TILESIZE) + 3

	def refreshData(self):
		importlib.reload(settings)		