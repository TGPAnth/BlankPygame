# -*- coding: utf-8 -*-

import pygame, sys, math, copy
from pygame.locals import *
pygame.init()

class Map(object):
	"""docstring for Map"""
	def __init__(self,wd,hg):
		super(Map, self).__init__()
		self.height = 10
		self.width = 10
		self.Scale = 32 #""" TODO: """# Расчитывать ДИНАМИЧЕСКИ!!!
		self.wd = wd
		self.hg = hg
		self.Surface = pygame.Surface((wd,hg))
		self.bkgnd_color = (255,255,255)
	
	def redraw(self):
		self.Surface = pygame.Surface((self.wd,self.hg))
		self.Surface.fill(self.bkgnd_color)
		# if self.Draw_Coord: self.redraw_coord()
		# for i in self.polygons_array:
		# 	self.redraw_poly(i)
		# for i in self.finish_array:
		# 	self.redraw_poly(i)
		return self.Surface
