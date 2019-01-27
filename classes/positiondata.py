from classes.grid import *
from classes.pathfinder2d import *
from classes.pathrender import *

class PositionData:

    def __init__(self, Grid):
        self.Grid = Grid
        self.startPos = []
        self.goalPos = []
        self.obstaclesPos = []
        self.currentGridPos = []

    #changes the position of the start tile
    def changeStartTile(self, pos):
        if self.startPos == []:
            self.startPos.append(pos[0])
            self.startPos.append(pos[1])
        self.clearTile(self.startPos)
        self.Grid.tiles[pos[0]][pos[1]].newColor((0,255,0))
        self.startPos = [pos[0], pos[1]]

    #changes the position of the goal tile
    def changeGoalTile(self, pos):
        if self.goalPos == []:
            self.goalPos.append(pos[0])
            self.goalPos.append(pos[1])
        self.clearTile(self.goalPos)
        self.Grid.changeColor(pos, (0, 0, 255))
        self.goalPos = [pos[0], pos[1]]

    #add/remove obstacle tiles
    def changeObstacleTile(self, pos):
        if [pos[0], pos[1]] in self.obstaclesPos:
            self.obstaclesPos.remove([pos[0], pos[1]])
            self.Grid.changeColor(pos, (200, 200, 200))
        else:
            self.obstaclesPos.append([pos[0], pos[1]])
            self.Grid.changeColor(pos, (255, 0, 0))

    #sets a tile to the original color
    def clearTile(self, pos):
        self.Grid.tiles[pos[0]][pos[1]].reset()

    #sets the entire grid to the original color and clears all tile positions
    def clearGrid(self):
        self.Grid.reset()
        self.startPos = []
        self.goalPos = []
        self.obstaclesPos = []
