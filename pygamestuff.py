'''
virtualenv

activate your virtual env

pip install gamepy
This is a test

install atom package "script"

install atom package platformio-ide-terminal
'''

#import dependencies
import pygame, sys, time, numpy, random

import sort_tile
from pygame.locals import *




#variables
TILESIZE = 40
MAPWIDTH = 20
MAPHEIGHT = 20

#initialize pygame
pygame.init()
#initialize canvas
DISPLAYSURF = pygame.display.set_mode((TILESIZE*MAPWIDTH, TILESIZE*MAPHEIGHT), pygame.RESIZABLE)

class Tile(pygame.sprite.Sprite):
    #This Class handles tile position and color
    #each indiviual tile is an object of this class
    def __init__(self, size = 20, pos = (0, 0), color = (200,200,200)):
        self.size = size
        self.color = color
        self.posx = pos[0]
        self.posy = pos[1]

    #call pygame draw rectangle function
    def draw(self):
        pygame.draw.rect(DISPLAYSURF, self.color, (self.posx,self.posy,self.size,self.size))

    #set new color
    def newColor(self, color):
        self.color = color
        self.draw()


class Grid:
    #This call will be called to draw the tiles
    def __init__(self, xLen = 10, yLen = 10, tileSize = 20):
        #array that holds tile objects
        self.classesArray =[]
        #how many tiles in each coordinate directions and size of tiles
        self.xLen = xLen
        self.yLen = yLen
        self.tileSize = tileSize
        self.draw(self.xLen, self.yLen, self.tileSize)

    #this creates all tile objects and draws them
    def draw(self, xLen = 10, yLen = 10, tileSize = 20):
        self.classesArray = []
        #draw a black screen to get rid of old tiles
        DISPLAYSURF.fill((0,0,0))
        #set variables
        self.xLen = xLen
        self.yLen = yLen
        self.tileSize = tileSize
        #nested for loop to create 2d array to old tile objects
        for x in range(xLen):
            self.classesArray.append([])
            for y in range(yLen):
                #create tile object and draw it
                tile = Tile(tileSize-1,(x*tileSize, y*tileSize))
                tile.draw()
                #add object pointer to array
                self.classesArray[x].append(tile)
        #return self.classesArray

#creates a random rgb color
def randomColor():
    rgbColor = (((random.randrange(255)),(random.randrange(255)),(random.randrange(255))))
    return rgbColor

#takes in grid coordinate and changed that tile to a random color
def randomTileColor(pos):
    grid.classesArray[pos[0]][pos[1]].newColor(randomColor())

#gets mouse position and turns into a grid coordinate based on the tile size
def mouseToTile():
    pos = pygame.mouse.get_pos()
    xCor = int(pos[0] / TILESIZE)
    yCor = int(pos[1] / TILESIZE)
    tile = (xCor, yCor)
    return tile

#create grid for the first time with variables at the top of the file
grid = Grid(MAPWIDTH, MAPHEIGHT, TILESIZE)

#main loop
while True:
    #use this loop to handle pygame events and input
    for event in pygame.event.get():
        if(event.type != MOUSEMOTION):
            #use this to understand pygame events
            #print(event)
            pass
        #when you click the mouse button get the mouse position and set the tile
        #underneath it to a random color
        if event.type == MOUSEBUTTONDOWN:
            randomTileColor(mouseToTile())
        #shutdown when you hit the X button
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            quit()

    #redraw or refresh the display
    pygame.display.update()
