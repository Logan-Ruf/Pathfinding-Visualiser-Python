import pygame, time
#import classes.tile, classes.grid, classes.pathfinder3
from classes.tile import *
from classes.grid import *
from classes.pathfinder3 import *

#global parameters
TILESIZE = 20
MAPWIDTH = 20
MAPHEIGHT = 20

#initialize pygame
pygame.init()

#create grid for the first time with variables at the top of the file
grid = Grid(MAPWIDTH, MAPHEIGHT, TILESIZE)
mapMaker = MapMaker(grid)
pathFinder = PathFinder2D(grid.tiles)

hasRun = False
#main loop
while True:
    #use this loop to handle pygame events and input
    for event in pygame.event.get():
        if(event.type != MOUSEMOTION):
            #use this to understand pygame events
            #print(event)
            pass
        #when you click the mouse button get the mouse position and set the tile
        #underneath it to goal, start, or obstacle
        if event.type == MOUSEBUTTONDOWN:
            if hasRun == True:
                grid.reset()
                hasRun = False
            if event.button == 1:
                #Left Click
                mapMaker.setStart(grid.mouseToTile(event.pos))
            if event.button == 3:
                #Right Click
                mapMaker.setEnd(grid.mouseToTile(event.pos))
            if event.button == 2:
                #Middle Click
                mapMaker.toggleWall(grid.mouseToTile(event.pos))


        #press Enter to start the algorith, Delete to clear the grid, or
        #Escape to exit the program
        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                isRunning = True
                #start pathfinding
                pathFinder.pathAlgorithm(mapMaker.startTile, mapMaker.endTile)
                hasRun = True
            if event.key == K_DELETE:
                grid.reset()
                pass
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
                quit()
        #shutdown when you hit the X button
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            quit()
    #redraw or refresh the display
    pygame.display.update()
