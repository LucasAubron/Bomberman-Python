import pygame as pg
import Settings
from Game import Game

class Main:
	def __init__(self, isATest):
		game = Game(isATest) #boolean test
		pg.quit()
		quit()

m = Main(Settings.isATest)