'''
virtualenv

activate your virtual env

pip install gamepy


install atom package "script"

install atom package platformio-ide-terminal
'''

#import dependencies
import pygame, sys, time, numpy, random

from pygame.locals import *




#global parameters
TILESIZE = 20
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

class Algorithm:

    startPos = []
    goalPos = []
    obstaclesPos = []
    #changes the position of the start tile
    def changeStartTile(pos):
        if Algorithm.startPos == []:
            Algorithm.startPos.append(pos[0])
            Algorithm.startPos.append(pos[1])
        Algorithm.clearTile(Algorithm.startPos)
        grid.classesArray[pos[0]][pos[1]].newColor((0,255,0))
        Algorithm.startPos = [pos[0], pos[1]]

    #changes the position of the goal tile
    def changeGoalTile(pos):
        if Algorithm.goalPos == []:
            Algorithm.goalPos.append(pos[0])
            Algorithm.goalPos.append(pos[1])
        Algorithm.clearTile(Algorithm.goalPos)
        grid.classesArray[pos[0]][pos[1]].newColor((0,0,255))
        Algorithm.goalPos = [pos[0], pos[1]]

    #add/remove obstacle tiles
    def changeObstacleTile(pos):
        if [pos[0], pos[1]] in Algorithm.obstaclesPos:
            Algorithm.obstaclesPos.remove([pos[0], pos[1]])
            grid.classesArray[pos[0]][pos[1]].newColor((200,200,200))
        else:
            Algorithm.obstaclesPos.append([pos[0], pos[1]])
            grid.classesArray[pos[0]][pos[1]].newColor((255,0,0))

    #sets a tile to the original color
    def clearTile(pos):
        grid.classesArray[pos[0]][pos[1]].newColor((200,200,200))

    #sets the entire grid to the original color and clears all tile positions
    def clearGrid():
        for x in range(MAPWIDTH):
            for y in range(MAPHEIGHT):
                grid.classesArray[x][y].newColor((200,200,200))
        Algorithm.startPos = []
        Algorithm.goalPos = []
        Algorithm.obstaclesPos = []

    #finds the shortest path from the start tile to the goal tile
    def pathAlgorithm():
        Algorithm.gridPos = Algorithm.startPos
        if Algorithm.obstaclesPos == []:
            deltaX = Algorithm.startPos[0] - Algorithm.goalPos[0]
            deltaY = Algorithm.startPos[1] - Algorithm.goalPos[1]

            if deltaX < 0:
                while Algorithm.gridPos[0] != Algorithm.goalPos[0]:
                    Algorithm.gridPos[0] += 1
                    grid.classesArray[Algorithm.gridPos[0]][Algorithm.gridPos[1]].newColor((0,0,0))
                    time.sleep(.1)
                    pygame.display.update()
            elif deltaX > 0:
                while Algorithm.gridPos[0] != Algorithm.goalPos[0]:
                    Algorithm.gridPos[0] -= 1
                    grid.classesArray[Algorithm.gridPos[0]][Algorithm.gridPos[1]].newColor((0,0,0))
                    time.sleep(.1)
                    pygame.display.update()
            if deltaY < 0:
                while Algorithm.gridPos[1] != Algorithm.goalPos[1]:
                    Algorithm.gridPos[1] += 1
                    grid.classesArray[Algorithm.gridPos[0]][Algorithm.gridPos[1]].newColor((0,0,0))
                    time.sleep(.1)
                    pygame.display.update()
            if deltaY > 0:
                while Algorithm.gridPos[1] != Algorithm.goalPos[1]:
                    Algorithm.gridPos[1] -= 1
                    grid.classesArray[Algorithm.gridPos[0]][Algorithm.gridPos[1]].newColor((0,0,0))
                    time.sleep(.1)
                    pygame.display.update()
        else:
            pass


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
        #underneath it to goal, start, or obstacle
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                Algorithm.changeStartTile(mouseToTile())
                print("\nStart Position:", Algorithm.startPos, "\n")
            if event.button == 3:
                Algorithm.changeGoalTile(mouseToTile())
                print("\nGoal Position:", Algorithm.goalPos, "\n")
            if event.button == 2:
                Algorithm.changeObstacleTile(mouseToTile())
                print("\nObstacle Positions:", Algorithm.obstaclesPos, "\n")
        #press Enter to start the algorith, Delete to clear the grid, or
        #Escape to exit the program
        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                Algorithm.pathAlgorithm()
            if event.key == K_DELETE:
                Algorithm.clearGrid()
                print("\nGrid Cleared\n")
                print("Start Position:", Algorithm.startPos)
                print("Goal Position:", Algorithm.goalPos)
                print("Obstacle Positions:", Algorithm.obstaclesPos, "\n")
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
