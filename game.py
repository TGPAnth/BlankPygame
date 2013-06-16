# -*- coding: utf-8 -*-
import pygame, sys, copy,math,time
from pprint import pprint
from field import Map
from window import Window
from pygame.locals import *
pygame.init()

MLOG = 0

class Game(object):

	def __init__(self):
		self.WD = 640
		self.HG = 480
		self.mousex,self.mousey = 0,0
		self.GameMap = Map(self.WD,self.HG)
		self.MainWindow = Window(self.WD,self.HG)
		self.mousexy = pygame.mouse.get_pos()
		self.fpsClock = pygame.time.Clock()
		
	def mouse_button_up(self,GameMap):
		pass

	def main_loop(self):
		while 1:			
			# TODO:
			self.MainWindow.update(self.GameMap)

			self.user_action()

			pygame.display.update()
			self.fpsClock.tick(30)

	def user_action(self):
		for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()

				elif event.type == MOUSEBUTTONDOWN:
					# mouse_button_up()
					self.mousexy = pygame.mouse.get_pos()
					# 1 - LB 2 - MB 3 - RB 4 - SU 5 - SD
					pass
					
				elif event.type == MOUSEMOTION:
					self.mousexy = pygame.mouse.get_pos()

				elif event.type == MOUSEBUTTONUP:
					self.mousexy = pygame.mouse.get_pos()
					if event.button == 1:
						self.mouse_button_up()

				elif event.type == KEYDOWN:
					if event.key == K_SPACE:
						pass

				elif event.type == KEYUP:
					if event.key == K_SPACE:
						pass

if __name__=="__main__":
	mainGame = Game()
	mainGame.main_loop()
