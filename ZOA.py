import pygame
import sys
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)
DARKBLUEBACK = (13, 13, 27)
CODEKEY = {"AA": (255, 255, 255), "AB": (0, 100, 255), "X": (13, 13, 27)}
#EMPTY SQUARES DENOTED BY "X"
#SWEEPERS ARE OBJECTS THAT ARE AT RISK OF TURNING TO X UNLESS ANOTHER OBJECT FILLS THEIR PLACE. ONCE ALL OBJECTS ARE MOVED ANY OUTSTANDING SWEEPERS ARE CONVERTED TO "X"
#CLASS OBJECTS FOR ZOA PYTHON LIBRARY
#SEED IS LOCATION OF ARM BUNDLE AND CORTICAL PROTEIN RESPECTIVELY  EXAMPLE: {[0, 1], [0, 2]}
#TYPES OF ACTION - - - - - MOVEMENT, EAT, ATTACK, REPOSITION, STORE/COLLECT,



class Session:
    def __init__(self, cosm, tick):
        self.tickSpeed = tick
        global SCREEN, CLOCK
        self.cosm = cosm
        pygame.init()
        SCREEN = pygame.display.set_mode((cosm.COSM_HEIGHT, cosm.COSM_WIDTH))
        pygame.display.set_caption("LifeEngine ||| VERSION 0.0.1 ||| Cosm 1 ")
        CLOCK = pygame.time.Clock()
    def runSession(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.cosm.updateCosm()
            for i in range(self.cosm.COSM_HEIGHT):
                for j in range(self.cosm.COSM_WIDTH):
                    rect = pygame.Rect(1 + self.cosm.increment * (j), 1 + self.cosm.increment * (i), self.cosm.increment - 2, self.cosm.increment - 2)
                    pygame.draw.rect(SCREEN, CODEKEY[self.cosm.COSM_CENTRAL_DATA[i][j]], rect)

            pygame.display.flip()
            CLOCK.tick(self.tickSpeed)
def drawParticle(xCoord, yCoord):
    ##will handle drawing single particle at single index
    print("FUNCTION - drawParticle() is currently under construction")
def deleteParticle(xCoord, yCoord):
    ##MAKES PARTICLE EMPTY SPACE AT SPECIFIC LOCATION
    print("FUNCTION - deleteParticle() is currently under construction")
def checkMoveQuery(currentX, currentY, queriedX, queriedY):
    ##check if proposed move is possible, or if there is collision, returns false if collisions detected
    moveApproved = False
    print("FUNCTION - checkMoveQuery() is currently under construction")
class Cosm:
    def __init__(self, ID, width, height, increment):
        self.increment = increment
        self.COSM_CENTRAL_DATA = [["X"] * width] * height
        self.COSM_ELEMENT_TABLE = 0
        self.COSM_ID = ID
        self.COSM_HEIGHT = height
        self.COSM_WIDTH = width
        self.SWEEP_INDEXES = []
    def changeIndex(self, x, y, change):
        self.COSM_CENTRAL_DATA[y][x] = change
    def data(self):
        print(self.COSM_CENTRAL_DATA)
        print(self.COSM_ELEMENT_TABLE)
        print(self.COSM_ID)
        print(self.COSM_HEIGHT)
        print(self.COSM_WIDTH)
    def moveElement(self, inputIndex, Direction):
        current = self.COSM_CENTRAL_DATA[inputIndex[0], inputIndex[1]]
        # check if queried space is empty
        if Direction == "LEFT":
            if(inputIndex[1] > 0 and (self.COSM_CENTRAL_DATA[inputIndex[1]-1])[-1] == "X"):
                self.COSM_CENTRAL_DATA[inputIndex[0], (inputIndex[1]-1)]
                self.COSM_CENTRAL_DATA[inputIndex[0], (inputIndex[1])] += "X"
                self.SWEEP_INDEXES.append([(inputIndex[0], (inputIndex[1]))])
        if Direction == "RIGHT":
            if (inputIndex[1] < self.COSM_WIDTH - 1 and (self.COSM_CENTRAL_DATA[inputIndex[1] + 1])[-1] == "X"):
                self.COSM_CENTRAL_DATA[inputIndex[0], (inputIndex[1] + 1)]
                self.COSM_CENTRAL_DATA[inputIndex[0], (inputIndex[1])] += "X"
                self.SWEEP_INDEXES.append([inputIndex[0], (inputIndex[1])])
        if Direction == "DOWN":
            if (inputIndex[0] > 0 and (self.COSM_CENTRAL_DATA[inputIndex[0] + 1])[-1] == "X"):
                self.COSM_CENTRAL_DATA[inputIndex[0] + 1, (inputIndex[1])]
                self.COSM_CENTRAL_DATA[inputIndex[0], (inputIndex[1])] += "X"
                self.SWEEP_INDEXES.append([inputIndex[0], (inputIndex[1])])
        if Direction == "UP":
            if (inputIndex[0] < self.COSM_HEIGHT-1 and (self.COSM_CENTRAL_DATA[inputIndex[0] - 1])[-1] == "X"):
                self.COSM_CENTRAL_DATA[inputIndex[0] - 1, (inputIndex[1])]
                self.COSM_CENTRAL_DATA[inputIndex[0], (inputIndex[1])] += "X"
                self.SWEEP_INDEXES.append([inputIndex[0], (inputIndex[1])])
    def moveOrganism(organismArray, Direction, Velocity):
        #velocity is determined by total negative mass of organism (-m) + its locomotive coefficient (LOCOCO)
        #It's a large spatula, and we all live on it, but when you climb through the divots to the other side and the spatula does not flip, you live backwards


        print("under construction")
    def updateSweepers(self):
        for index in self.SWEEP_INDEXES:
            if(self.COSM_CENTRAL_DATA[index][-1] == "X" and len(self.COSM_CENTRAL_DATA[index]) != 1):
                self.COSM_CENTRAL_DATA[index] = "X"
        self.SWEEP_INDEXES = []
    def updateCosm(self):
        print("updating cosm")
class Organism:
    def __init__(self, ARM, Seed):
        self.ARM = ARM
        self.Seed = Seed
        self.ElementArray = []
        #make sure to initialize element array with seed
    def addElement(self, Element, Location):
        if(Element.getConnection() == False):
            Element.toggleConnection()
    def completeAction(self):
        print("under construction")
class Ecosystem:
    def __init__(self, Organisms):
        self.organisms = Organisms
    def addOrganism(self, Organism):
        self.organisms.update(Organism)
class Element:
    def __init__(self, ID, Connected, INDEX):
        self.ID = ID
        self.connected = False
        self.elementIndex = INDEX
    def toggleConnection(self):
        if(self.connected == True):
            self.connected = False
        if(self.connected == False):
            self.connected = True
    def getConnection(self):
        return self.connected
    def getID(self):
        return self.ID
class Element_Table:
    def __init__(self, currentElements):
        #Pass in dictionary
        self.elementTable = currentElements
    def addElement(self, Element):
        #add to dictionary of elements
        self.elementTable.update(Element)




#GENERAL COSM STRUCTURE
#
#Cosm contains array of elements,
#once a part of an organism, elements are no longer controleld by the cosm but rather the organism
#organism calls action each tick to choose action. if organism moves, it passes a movement direction plus the array of its member elements to the cosm for the movement function to occur there.
#
#
#
#
#
#