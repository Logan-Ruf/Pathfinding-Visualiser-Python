from classes.grid import *
from classes.pathfinder2d import *

class PositionData:

    def __init__(self, grid):
        #get access to grid
        self.grid = grid
        #variables for array based path finding - ie pathAlgorithm
        self.startPos = []
        self.goalPos = []
        self.obstaclesPos = []
        self.currentGridPos = []
        self.bestPath = []
        #variables for node based programing - ie pathAlgorithm2
        self.startTile = (-1, -1)
        self.endTile =   (-1, -1)

    #changes the position of the start tile
    def setStart(self, pos):
        #ARRAY FIRST
        #if there is a current tile reset it's color
        if self.startPos != []:
            self.clearTile(self.startPos)
        self.grid.tiles[pos[0]][pos[1]].newColor((0,255,0))
        self.startPos = list(pos)
        #NODE SECOND
        if self.startTile != (-1,-1):
            self.grid.resetTile(self.startTile)
        #use pos to set new tile as tart
        self.grid.tiles[pos[0]][pos[1]].setStart()
        self.startTile = pos

        '''
        if self.startPos == []:
            self.startPos.append(pos[0])
            self.startPos.append(pos[1])
        self.clearTile(self.startPos)
        self.grid.tiles[pos[0]][pos[1]].newColor((0,255,0))
        self.startPos = [pos[0], pos[1]]
        '''
    #changes the position of the goal tile
    def setEnd(self, pos):
        #Array first
        #if there is a current tile reset it's color
        if self.goalPos != []:
            self.clearTile(self.goalPos)
        self.grid.changeColor(pos, (0, 0, 255))
        self.goalPos = list(pos)
        #Node Second
        if self.endTile != (-1,-1):
            self.grid.resetTile(self.endTile)
        #use pos to set new tile as end
        self.grid.tiles[pos[0]][pos[1]].setEnd()
        self.endTile = pos


    #add/remove obstacle tiles
    def toggleWall(self, pos):
        #Array first
        if [pos[0], pos[1]] in self.obstaclesPos:
            self.obstaclesPos.remove([pos[0], pos[1]])
            self.grid.changeColor(pos, (200, 200, 200))
        else:
            self.obstaclesPos.append([pos[0], pos[1]])
            self.grid.changeColor(pos, (255, 0, 0))
            #Node SECOND
            oldWall = self.grid.tiles[pos[0]][pos[1]].toggleWall()
            #if toggleWall method on tile returns start or end reset those variables to default
            if(oldWall == 'start'):
                self.startTile = (-1, -1)
            elif(oldWall == 'end'):
                self.endTile = (-1, -1)

        #Check to make sure there is a start and end tile
        def okToStart(self):
            if self.startTile == (-1, -1) or self.endTile == (-1, -1):
                return False
            else:
                return True

    #sets a tile to the original color
    def clearTile(self, pos):
        self.grid.tiles[pos[0]][pos[1]].reset()

    #sets the entire grid to the original color and clears all tile positions
    def cleargrid(self):
        self.grid.reset()
        self.startPos = []
        self.goalPos = []
        self.obstaclesPos = []
        self.bestPath = []

    #uses pathfinder class to get a path
    def findPath(self, finder):
        finder = PathFinder2D(self)
        self.bestPath = finder.pathAlgorithm()

    #traverses path
    def traversePath(self):
        for pos in self.bestPath:
            self.grid.changeColor(pos, (0,0,0))
            time.sleep(.01)
            pygame.display.update()
