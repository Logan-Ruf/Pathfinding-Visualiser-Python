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

class Tile():
    #This Class handles tile position and color
    #each indiviual tile is an object of this class
    def __init__(self, size = 20, pos = (0, 0), color = (200,200,200)):
        self.size = size
        self.color = color
        self.pos = pos
        self.posx = pos[0]
        self.posy = pos[1]

    #call pygame draw rectangle function
    def draw(self):
        pygame.draw.rect(DISPLAYSURF, self.color, (self.posx,self.posy,self.size,self.size))

    #set new color
    def newColor(self, color):
        self.color = color
        self.draw()

    def reset(self):
        self.newColor((200,200,200))
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
        self.create(self.xLen, self.yLen, self.tileSize)

    #this creates all tile objects and draws them
    def create(self, xLen = 10, yLen = 10, tileSize = 20):
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
                #tile.draw()
                #add object pointer to array
                self.classesArray[x].append(tile)
                self.classesArray[x][y].draw()
        #return self.classesArray

    def draw(self):
        for row in self.classesArray:
            for tile in row:
                tile.draw()

    def reset(self):
        for row in self.classesArray:
            for tile in row:
                tile.reset()


#deff beg and end coordinate
# divide x and y diff by max(x , y)
# 2,2 / 2 = 1,1
# 32, 2 / 32 = 1 , 0.005
# 6 , 2 / 6 = 1 , .333
    #4, 2 = 1 , .5
class PositionData:

    def __init__(self):
        self.startPos = []
        self.goalPos = []
        self.obstaclesPos = []
        self.gridPos = []

    #changes the position of the start tile
    def changeStartTile(self, pos):
        if self.startPos == []:
            self.startPos.append(pos[0])
            self.startPos.append(pos[1])
        self.clearTile(self.startPos)
        grid.classesArray[pos[0]][pos[1]].newColor((0,255,0))
        self.startPos = [pos[0], pos[1]]

    #changes the position of the goal tile
    def changeGoalTile(self, pos):
        if self.goalPos == []:
            self.goalPos.append(pos[0])
            self.goalPos.append(pos[1])
        self.clearTile(self.goalPos)
        grid.classesArray[pos[0]][pos[1]].newColor((0,0,255))
        self.goalPos = [pos[0], pos[1]]

    #add/remove obstacle tiles
    def changeObstacleTile(self, pos):
        if [pos[0], pos[1]] in self.obstaclesPos:
            self.obstaclesPos.remove([pos[0], pos[1]])
            grid.classesArray[pos[0]][pos[1]].newColor((200,200,200))
        else:
            self.obstaclesPos.append([pos[0], pos[1]])
            grid.classesArray[pos[0]][pos[1]].newColor((255,0,0))

    #sets a tile to the original color
    def clearTile(self, pos):
        grid.classesArray[pos[0]][pos[1]].reset()

    #sets the entire grid to the original color and clears all tile positions
    def clearGrid(self,grid):
        grid.reset()
        self.startPos = []
        self.goalPos = []
        self.obstaclesPos = []

class PathFinder2D:

    def __init__(self, PositionData):
        self.PositionData = PositionData
    #finds the shortest path from the start tile to the goal tile
    def pathAlgorithm(self):
        if self.PositionData.obstaclesPos == []:
            self.deltaX = self.PositionData.goalPos[0] - self.PositionData.startPos[0]
            self.deltaY = self.PositionData.goalPos[1] - self.PositionData.startPos[1]
            self.PositionData.gridPos = self.PositionData.startPos

            if abs(self.deltaX) > 0:
                while self.PositionData.gridPos[0] != self.PositionData.goalPos[0]:
                    self.PositionData.gridPos[0] += self.deltaX // abs(self.deltaX)
                    grid.classesArray[self.PositionData.gridPos[0]][self.PositionData.gridPos[1]].newColor((0,0,0))
                    time.sleep(.1)
                    pygame.display.update()

            if abs(self.deltaY) > 0:
                while self.PositionData.gridPos[1] != self.PositionData.goalPos[1]:
                    self.PositionData.gridPos[1] += self.deltaY // abs(self.deltaY)
                    grid.classesArray[self.PositionData.gridPos[0]][self.PositionData.gridPos[1]].newColor((0,0,0))
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
pathPosition1 = PositionData()
pathFinder1 = PathFinder2D(pathPosition1)
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
                pathPosition1.clearGrid(grid)
                hasRun = False
            if event.button == 1:
                pathPosition1.changeStartTile(mouseToTile())
                print("\nStart Position:", pathPosition1.startPos, "\n")
            if event.button == 3:
                pathPosition1.changeGoalTile(mouseToTile())
                print("\nGoal Position:", pathPosition1.goalPos, "\n")
            if event.button == 2:
                pathPosition1.changeObstacleTile(mouseToTile())
                print("\nObstacle Positions:", pathPosition1.obstaclesPos, "\n")
        #press Enter to start the algorith, Delete to clear the grid, or
        #Escape to exit the program
        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                pathFinder1.pathAlgorithm()
                hasRun = True
            if event.key == K_DELETE:
                pathPosition1.clearGrid(grid)
                print("\nGrid Cleared\n")
                print("Start Position:", pathPosition1.startPos)
                print("Goal Position:", pathPosition1.goalPos)
                print("Obstacle Positions:", pathPosition1.obstaclesPos, "\n")
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
