from classes.tile import *

class Grid:
    #This call will be called to draw the tiles
    def __init__(self, xLen = 10, yLen = 10, tileSize = 20):
        #array that holds tile objects
        self.tiles =[]
        #how many tiles in each coordinate directions and size of tiles
        self.xLen = xLen
        self.yLen = yLen
        self.tileSize = tileSize
        #initialize canvas
        self.DISPLAYSURF = pygame.display.set_mode((self.tileSize*self.xLen, self.tileSize*self.yLen), pygame.RESIZABLE)
        self.create(self.xLen, self.yLen, self.tileSize)

    #this creates all tile objects and draws them
    def create(self, xLen = 10, yLen = 10, tileSize = 20):
        self.tiles = []
        #draw a black screen to get rid of old tiles
        self.DISPLAYSURF.fill((0,0,0))
        #set variables
        self.xLen = xLen
        self.yLen = yLen
        self.tileSize = tileSize
        #nested for loop to create 2d array to old tile objects
        for x in range(xLen):
            self.tiles.append([])
            for y in range(yLen):
                #create tile object and draw it
                tile = Tile(self.DISPLAYSURF, tileSize-1,(x*tileSize, y*tileSize))
                #tile.draw()
                #add object pointer to array
                self.tiles[x].append(tile)
                self.tiles[x][y].draw()
        #return self.tiles

    def draw(self):
        for row in self.tiles:
            for tile in row:
                tile.draw()

    def reset(self):
        for row in self.tiles:
            for tile in row:
                tile.reset()

    def resetTile(self, pos):
        self.tiles[pos[0],pos[1]].reset()

    def changeColor(self, pos, *rgb):
        self.tiles[pos[0],pos[1]].newColor(rgb)

    #creates a random rgb color
    def randomColor(self):
        rgbColor = (((random.randrange(255)),(random.randrange(255)),(random.randrange(255))))
        return rgbColor

    #takes in grid coordinate and changed that tile to a random color
    def randomTileColor(self, pos):
        self.changeColor(randomColor())

    #gets mouse position and turns into a grid coordinate based on the tile size
    def mouseToTile(self):
        pos = pygame.mouse.get_pos()
        xCor = int(pos[0] / self.tileSize)
        yCor = int(pos[1] / self.tileSize)
        tile = (xCor, yCor)
        return tile
