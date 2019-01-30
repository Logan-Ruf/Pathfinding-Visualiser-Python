import numpy, pygame, time
'''
Requirements for this algorithm

Does not store any data other than start and end position after switching to new
node.

Stores data like distance from start on current path and other data in tile

each node needs to store its distance from start from path
its absolute distance from end
which sides have walls next to them

class MapMaker:

    def __init__(self, grid):
        self.grid = grid
        self.startTile = (-1, -1)
        self.endTile =   (-1, -1)

    def setStart(self, pos):
        #if there is currently a start tile, reset it
        if self.startTile != (-1,-1):
            self.grid.resetTile(self.startTile)
        #use pos to set new tile as tart
        self.grid.tiles[pos[0]][pos[1]].setStart()
        self.startTile = pos

    def setEnd(self, pos):
        #if there is currently a end tile, reset it
        if self.endTile != (-1,-1):
            self.grid.resetTile(self.endTile)
        #use pos to set new tile as end
        self.grid.tiles[pos[0]][pos[1]].setEnd()
        self.endTile = pos

    #toggle the wall attribute and track if the user just replaced a start or end block
    def toggleWall(self, pos):
        oldWall = self.grid.tiles[pos[0]][pos[1]].toggleWall()
        #if toggleWall method on tile returns start or end reset those variables to default
        if(oldWall == 'start'):
            self.startTile = (-1, -1)
        elif(oldWall == 'end'):
            self.endTile = (-1, -1)

    def okToStart(self):
        if self.startTile == (-1, -1) or self.endTile == (-1, -1):
            return False
        else:
            return True

class PathFinder2D:

    def __init__ (self, gridArray):
        self.gridArray = gridArray

    def pathAlgorithm2(self, startPos, endPos, gridArray):
        currentPos = startPos
        while currentPos != endPos:
            #find the difference of currentPos and endPos
            movement = (endPos[0] - currentPos[0], endPos[1] - currentPos[1])
            #normailze the difference to a max of 1
            maxInt = max(abs(movement[0]), abs(movement[1]))
            movement = (round(movement[0]/maxInt), round(movement[1]/maxInt))
            #add movement to find current tile
            currentPos = (currentPos[0]+movement[0],currentPos[1]+movement[1])
            #Change color of current tile and update screen
            gridArray[currentPos[0]][currentPos[1]].newColor((100,100,100))
            pygame.display.update()
            #Wait a tenth of a second for the humans
            time.sleep(.1)
'''
