from classes.positiondata import *

#global parameters
TILESIZE = 20
MAPWIDTH = 20
MAPHEIGHT = 20

#initialize pygame
pygame.init()

#create grid for the first time with variables at the top of the file
grid = Grid(MAPWIDTH, MAPHEIGHT, TILESIZE)
pathPosition1 = PositionData(grid)
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
                pathPosition1.clearGrid()
                hasRun = False
            if event.button == 1:
                pathPosition1.changeStartTile(grid.mouseToTile())
                print("\nStart Position:", pathPosition1.startPos, "\n")
            if event.button == 3:
                pathPosition1.changeGoalTile(grid.mouseToTile())
                print("\nGoal Position:", pathPosition1.goalPos, "\n")
            if event.button == 2:
                pathPosition1.changeObstacleTile(grid.mouseToTile())
                print("\nObstacle Positions:", pathPosition1.obstaclesPos, "\n")
        #press Enter to start the algorith, Delete to clear the grid, or
        #Escape to exit the program
        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                pathPosition1.findPath()
                pathPosition1.traversePath()
                hasRun = True
            if event.key == K_DELETE:
                pathPosition1.clearGrid()
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
