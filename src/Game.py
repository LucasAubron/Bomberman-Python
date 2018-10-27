import pygame as pg
import Settings
import LoadImages
import importlib
from Player import Player
from IBlock import IBlock
from Block import Block
from Bomb import Bomb
from Explosion import Explosion
from PowerUp import PowerUp
from Map import Map
import random


class Game:
	def __init__(self):
		pg.init()
		pg.mixer.init()
		self.running = True
		self.numberOfPlayers = input("Nombre de joueurs :")
		self.screen = pg.display.set_mode([Settings.DISPLAY_SIZE, Settings.DISPLAY_SIZE])
		pg.display.set_caption(Settings.TITLE)
		self.screen.fill(Settings.BG_COLOR)
		self.clock = pg.time.Clock()
		self.map = None
		pg.key.set_repeat(30,100)
		self.new()

	def new(self):
		self.allSprites = pg.sprite.Group()
		self.blocks = pg.sprite.Group()
		self.players = pg.sprite.Group()
		self.bombs = pg.sprite.Group()
		self.items = pg.sprite.Group()
		self.destructible = pg.sprite.Group()
		self.destructibleAndDontBlockExplosion = pg.sprite.Group()
		self.powerUp = pg.sprite.Group()
		self.bombPos = []
		self.IBlockPos = []
		self.image = LoadImages.BG_IMAGE
		self.tileSize = Settings.TILESIZE
		self.loadData()
		self.loadMap()
		self.run()

	def run(self):
		while self.running:
			self.dt = self.clock.tick(Settings.FPS) / 100
			self.events()
			self.update()
			self.draw()

	def events(self):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				quit()
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_ESCAPE:
					pg.quit()
					quit()

	def update(self):
		self.allSprites.update()
		self.end()

	def draw(self):
		self.screen.blit(LoadImages.BG_IMAGE, (0, 0))
		#self.drawGrid()
		self.allSprites.draw(self.screen)
		self.players.draw(self.screen)
		pg.display.flip()

	def drawGrid(self):
		for x in range(0, Settings.DISPLAY_SIZE, Settings.TILESIZE):
			pg.draw.line(self.screen, Settings.GRID_COLOR, (x,0),(x, Settings.DISPLAY_SIZE))
		for y in range(0, Settings.DISPLAY_SIZE, Settings.TILESIZE):
			pg.draw.line(self.screen, Settings.GRID_COLOR, (0,y),(Settings.DISPLAY_SIZE, y))

	def loadData(self):
		biggerMapPlanList = ["../Maps/24x24Maps/map1.txt","../Maps/24x24Maps/map2.txt"]
		smallerMapPlanList = ["../Maps/16x16Maps/map1.txt"]
		if Settings.mapIsBig:
			self.mapPlan = random.choice(biggerMapPlanList)
		else:
			self.mapPlan = random.choice(smallerMapPlanList)
		self.map = Map(self, self.mapPlan)

	def loadMap(self):
		# create new players, they have each a unique spawn location (first two parameters) and ID
		for i in range (int(self.numberOfPlayers)):
			if i == 0:
				self.player1 = Player(self, 0, 0, 1)
			elif i == 1:
				self.player2 = Player(self, 23, 23, 2)
			elif i == 2:
				self.player3 = Player(self, 23, 0, 3)
			elif i == 3:
				self.player4 = Player(self, 0, 23, 4)
		#load map with destructible blocks and inderstructible blocks
		for row, tiles in enumerate(self.map.data):
			for col, tile in enumerate(tiles):
				if tile == "I":
					IBlock(self, col, row)
				if tile == "B":
					Block(self, col, row)

	def end(self):
		if len(self.players) <= 1:
			self.refreshData()
			self.new()

	def refreshData(self):
		#When a new game is launched, the size of the map should be able to change so all map can spawn even if they don't have the same size as the first one
		#So we reload settings so the Settings.TILESIZE can change (or not), if so then we reload LoadImages in each of the existing classes that have an image
		#To do that we need to create one object of each and cal their refresh image, pretty ugly but can't find an other way arround
		importlib.reload(Settings)
		trashplayer = Player(self, 0, 0, 1) #Player is created alone because it needs a name in order to call him for the creation of a bomb
		allKindOfSprites = [trashplayer, Bomb(trashplayer, self, 0, 0), Explosion(self, 0, 0, 0, ""), Block(self, 0, 0), IBlock(self, 0, 0), PowerUp(self, 0, 0)]
		for object in allKindOfSprites:
			object.refreshData()
