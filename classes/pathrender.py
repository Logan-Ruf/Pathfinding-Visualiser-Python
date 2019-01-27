import time
from classes.grid import*

class PathRender:

    def __init__(self, Grid):
        self.Grid = Grid

    def pathRender(self, bestPath):
        for pos in bestPath:
            self.Grid.changeColor(pos, (0, 0, 0))
            time.sleep(.01)
            pygame.display.update()
