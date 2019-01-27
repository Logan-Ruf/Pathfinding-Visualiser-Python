import pygame, sys, time, numpy, random
from pygame.locals import *

class Tile():
    #This Class handles tile position and color
    #each indiviual tile is an object of this class
    def __init__(self, DISPLAYSURF, size = 20, pos = (0, 0), color = (200,200,200)):
        self.size = size
        self.color = color
        self.pos = pos
        self.posx = pos[0]
        self.posy = pos[1]
        self.DISPLAYSURF = DISPLAYSURF

    #call pygame draw rectangle function
    def draw(self):
        pygame.draw.rect(self.DISPLAYSURF, self.color, (self.posx,self.posy,self.size,self.size))

    #set new color
    def newColor(self, color):
        self.color = color
        self.draw()

    def reset(self):
        self.newColor((200,200,200))
        self.draw()
