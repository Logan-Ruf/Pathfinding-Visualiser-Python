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


    def toggleWall(self):
        #checks to see if the block is currently a wall
        #if currently a start or end store that in VAR oldWall
        oldWall = None
        if(self.isWall == True):
            self.reset()
            return None
            #stop if you are toggling off the wall status
        elif(self.isStart == True):
            self.reset()
            oldWall = 'start'
        elif(self.isEnd == True):
            self.reset()
            oldWall = 'end'
        #set to being a wall
        self.isWall = True
        self.newColor((200, 0, 0))
        #return nome of oldWall if there was any
        return oldWall

#setTYPE methods reset tile first then set attributes to be the right type

    def setStart(self):
        self.reset()
        self.isStart = True
        self.newColor((0, 255, 0))

    def setEnd(self):
        self.reset()
        self.isEnd = True
        self.newColor((0, 0, 255))
