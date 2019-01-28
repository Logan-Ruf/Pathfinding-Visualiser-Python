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
        self.isStart = False
        self.isEnd = False
        self.isWall = False
        self.DISPLAYSURF = DISPLAYSURF

    #call pygame draw rectangle function
    def draw(self):
        pygame.draw.rect(self.DISPLAYSURF, self.color, (self.posx,self.posy,self.size,self.size))

    #set new color
    def newColor(self, color):
        self.color = color
        self.draw()

    def reset(self):
        self.isStart = False
        self.isEnd = False
        self.isWall = False
        self.newColor((200,200,200))
        self.draw()

    def setWall(self):
        self.reset()
        self.isWall = True
        self.newColor((255, 100, 100))

    def setStart(self):
        self.reset()
        self.isStart = True
        self.newColor((0, 255, 0))

    def setEnd(self):
        self.reset()
        self.isEnd = True
        self.newColor((0, 0, 255))
