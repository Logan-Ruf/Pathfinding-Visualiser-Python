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


        return self.bestPath

    #Path algorith2 is self-suffcient. Just pass in required variables
    #and it will find the path while updating tiles
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

    def dikjstra(self, startPos, endPos, gridArray, width, height):
        '''
        Welp, it's time to see if I can implement the famous Dijkstra's algorthm

        How this should work:
        Dijkstra's algorith works by always checking the closest path.
        As soon as the end of the found it will always be the closest path.

        how the code should work.

        have an array that stores grid coordinates

        start the algorith
        check all neighboring positions
        if
        '''
        gridArray[startPos[0]][startPos[1]].distance = 0

        currentPos = startPos
        unvisitedNodes = []

        while True:

            x, y = currentPos
            currentDistance = gridArray[x][y].distance + 1

            #Check to see if you have found the end. If you have draw the line and break
            if gridArray[x][y].isEnd == True:
                onPath = currentPos
                while onPath != None:
                    gridArray[onPath[0]][onPath[1]].newColor((100,100,100))
                    onPath = gridArray[onPath[0]][onPath[1]].parent
                    pygame.display.update()
                    time.sleep(.1)
                break

            #make sure neighboring tiles are in bounds
            #then if at shortest distance add it to unvisitedNodes
            if x - 1 >= 0:
                print("RUN 1")
                if gridArray[x - 1][y].isWall != True:
                    print("RUN 2")
                    isShorter = False
                    isShorter = gridArray[x - 1][y].isClosest(currentDistance, (x,y))
                    if isShorter:
                        print("RUN 3")
                        unvisitedNodes.append((x-1,y))
            if x + 1 < width:
                if gridArray[x + 1][y].isWall != True:
                    isShorter = False
                    isShorter = gridArray[x + 1][y].isClosest(currentDistance, (x,y))
                    if isShorter:
                        unvisitedNodes.append((x+1,y))
            if y - 1 >= 0:
                if gridArray[x][y - 1].isWall != True:
                    isShorter = False
                    isShorter = gridArray[x][y - 1].isClosest(currentDistance, (x,y))
                    if isShorter:
                        unvisitedNodes.append((x,y-1))
            if y + 1 < height:
                if gridArray[x][y + 1].isWall != True:
                    isShorter = False
                    isShorter = gridArray[x][y + 1].isClosest(currentDistance, (x,y))
                    if isShorter:
                        unvisitedNodes.append((x,y+1))

            pygame.display.update()
            time.sleep(.05)



            currentPos = unvisitedNodes.pop(0)
