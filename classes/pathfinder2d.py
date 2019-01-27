import time, pygame

class PathFinder2D:

    def __init__(self, PositionData):
        self.PositionData = PositionData
        self.startPos = self.PositionData.startPos
        self.goalPos = self.PositionData.goalPos
        self.obstaclesPos = self.PositionData.obstaclesPos
        self.currentGridPos = self.PositionData.currentGridPos
        self.bestPath = []
    #finds the shortest path from the start tile to the goal tile
    def pathAlgorithm(self):

        self.startPos = self.PositionData.startPos
        self.goalPos = self.PositionData.goalPos
        self.obstaclesPos = self.PositionData.obstaclesPos
        self.currentGridPos = self.startPos
        self.bestPath = []

        if (self.obstaclesPos == [] and self.startPos != [] and self.goalPos != []):
            deltaX = self.goalPos[0] - self.startPos[0]
            deltaY = self.goalPos[1] - self.startPos[1]
            deltaXInc = abs(deltaX)
            deltaYInc = abs(deltaY)
            while self.currentGridPos != self.goalPos:
                if abs(deltaX) >= abs(deltaY):
                    if deltaXInc > deltaYInc * abs(deltaX) / (abs(deltaY) + 1):
                        self.currentGridPos[0] += deltaX // abs(deltaX)
                        self.bestPath.append([self.currentGridPos[0], self.currentGridPos[1]])
                        deltaXInc -= 1
                    elif deltaXInc <= deltaYInc * abs(deltaX) / (abs(deltaY) + 1):
                        self.currentGridPos[1] += deltaY // abs(deltaY)
                        self.bestPath.append([self.currentGridPos[0], self.currentGridPos[1]])
                        deltaYInc -= 1
                elif abs(deltaX) < abs(deltaY):
                    if deltaYInc > deltaXInc * abs(deltaY) / (abs(deltaX) + 1):
                        self.currentGridPos[1] += deltaY // abs(deltaY)
                        self.bestPath.append([self.currentGridPos[0], self.currentGridPos[1]])
                        deltaYInc -= 1
                    elif deltaYInc <= deltaXInc * abs(deltaY) / (abs(deltaX) + 1):
                        self.currentGridPos[0] += deltaX // abs(deltaX)
                        self.bestPath.append([self.currentGridPos[0], self.currentGridPos[1]])
                        deltaXInc -= 1

        else:
            pass

    def safeDivZero(self, n, d):
        if d == 0:
            return 0
        return n // d
#deff beg and end coordinate
# divide x and y diff by max(x , y)
# 2,2 / 2 = 1,1
# 32, 2 / 32 = 1 , 0.005
# 6 , 2 / 6 = 1 , .333
    #4, 2 = 1 , .5
