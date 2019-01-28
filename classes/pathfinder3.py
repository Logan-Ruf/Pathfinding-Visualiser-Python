'''
Requirements for this algorithm

Does not store any data other than start and end position after switching to new
node.

Stores data like distance from start on current path and other data in tile


each node needs to store its distance from start from path
its absolute distance from end
which sides have walls next to them
'''
class MapMaker:

    def __init__(self, grid):
        self.grid = grid
        self.startTile = (-1, -1)
        self.endTile =   (-1, -1)

    def setStart(self, pos):
        if self.startTile != (-1,-1):
<<<<<<< HEAD
            #reset current tile
            self.grid.resetTile(self.startTile)
        #use pos to set new tile as tart
        self.grid.tiles[pos[0]][pos[1]].setStart()
=======
            self.grid.resetTile(self.startTile)
        #use pos to set new tile as tart
        print(self.grid.tiles)
        self.grid.tiles[pos[0],pos[1]].setStart()
>>>>>>> 4307e1e55be4021c68fd9b3c2e4b02bab631ddd6
        self.startTile = pos

    def setEnd(self, pos):
        if self.endTile != (-1,-1):
            #reset current tile
            self.grid.resetTile(self.endTile)
        #use pos to set new tile as end
<<<<<<< HEAD
        self.grid.tiles[pos[0]][pos[1]].setEnd()
=======
        self.grid.tiles[pos[0],pos[1]].setEnd()
>>>>>>> 4307e1e55be4021c68fd9b3c2e4b02bab631ddd6
        self.endTile = pos

class PathFinder2D:

    def __init__ (self, gridArray):
        self.gridArray = gridArray

    def pathAlgorithm(self):
        pass
