import time, pygame

class PathFinder2D:

    def __init__(self, PositionData):
        #references to position variables
        self.PositionData = PositionData
        self.startPos = self.PositionData.startPos
        self.goalPos = self.PositionData.goalPos
        self.obstaclesPos = self.PositionData.obstaclesPos
        self.currentGridPos = self.PositionData.currentGridPos
        #stores the coordinates of the shortest path from the start tile to the goal tile
        self.bestPath = []
    #finds the shortest path from the start tile to the goal tile
    def pathAlgorithm(self):
        #refresh position variables
        self.startPos = self.PositionData.startPos
        self.goalPos = self.PositionData.goalPos
        self.obstaclesPos = self.PositionData.obstaclesPos
        self.currentGridPos = self.startPos
        #reset best path
        self.bestPath = []

        #algorithm for when there are no obstacles
        if (self.obstaclesPos == []):
            #original difference between goal and start tiles
            deltaX = self.goalPos[0] - self.startPos[0]
            deltaY = self.goalPos[1] - self.startPos[1]
            #current difference between goal and start tiles
            deltaXInc = abs(deltaX)
            deltaYInc = abs(deltaY)
            #checks if current position is equal to goal position
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

        #algorithm for when there are obstacles
        else:
            pass
