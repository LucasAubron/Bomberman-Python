import pygame as pg
from settings import *
from Player import Player
from IBlock import IBlock
from Block import Block
from Map import Map

class Game:
	def __init__(self):
		pg.init()
		pg.mixer.init()
		self.running = True
		self.numberOfPlayers = input("Nombre de joueurs :")
		self.screen = pg.display.set_mode([DISPLAY_SIZE, DISPLAY_SIZE])
		pg.display.set_caption(TITLE)
		self.screen.fill(BG_COLOR)
		self.clock = pg.time.Clock()
		self.map = None
		self.loadData()
		self.new()

	def new(self):
		self.allSprites = pg.sprite.Group()
		self.loadMap()
		self.run()

	def run(self):
		while self.running:
			self.clock.tick(FPS)
			self.events()
			self.update()
			self.draw()

	def events(self):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				quit()

	def update(self):
		self.allSprites.update()

	def draw(self):
		self.screen.fill(BG_COLOR)
		for sprite in self.allSprites:
			self.screen.blit(sprite.image, sprite.rect)
		self.drawGrid()
		pg.display.flip()

	def drawGrid(self):
		for x in range(0, DISPLAY_SIZE, TILESIZE):
			pg.draw.line(self.screen, GRID_COLOR, (x,0),(x, DISPLAY_SIZE))
		for y in range(0, DISPLAY_SIZE, TILESIZE):
			pg.draw.line(self.screen, GRID_COLOR, (0,y),(DISPLAY_SIZE, y))

	def loadData(self):
		self.map = Map("map1.txt")

	def loadMap(self):
		# create new players, they have each a unique spawn location (first two parameters) and ID
		for i in range (int(self.numberOfPlayers)):
			if i == 0:
				player1 = Player(self, 3*TILESIZE,3*TILESIZE,1)
			elif i == 1:
				player2 = Player(self, 20*TILESIZE,20*TILESIZE,2)
			elif i == 2:
				player3 = Player(self, 20*TILESIZE,3*TILESIZE,3)
			elif i == 3:
				player4 = Player(self, 3*TILESIZE,20*TILESIZE,4)
		#load map with destructible blocks and inderstructible blocks
		for row, tiles in enumerate(self.map.data):
			for col, tile in enumerate(tiles):
				if tile == "I":
					IBlock(self, col * TILESIZE, row * TILESIZE)
				if tile == "B":
					Block(self, col * TILESIZE, row * TILESIZE)