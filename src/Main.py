import pygame as pg
import settings
from Game import Game

class Main:
	def __init__(self, isATest):
		game = Game(isATest) #boolean test
		pg.quit()
		quit()

m = Main(settings.isATest)