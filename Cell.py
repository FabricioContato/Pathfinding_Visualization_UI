import pygame

ACCESSIBLE = 1
UNACCESSIBLE = 0
EXPANDED = 2
PATH = 3
END = 4
START = 5
IN_LIST = 6
SELECTED = 7

GRAY = (125,125,125)
BLUE = (0,0,125)
LIGHT_BLUE = (0,0,255)
YELLOW = (255,255,0)
BLACK = (0,0,0)
OUTLINE_GRAY = (65,65,65)
RED = (255,0,0)
GREEN = (0,255,0)
PINK = (255,0,255)
WHITE =(255,255,255)

THICKNESS = 2

class Cell:
    def __init__(self, cell_point_place, cell_dimension, matrix, state = ACCESSIBLE):
        self.cell_point_place = cell_point_place
        self.cell_dimension = cell_dimension
        self.surface = pygame.Surface(cell_dimension)
        self.rect = pygame.Rect(cell_point_place,cell_dimension)
        self.state = state
        self.cost = 1
        self.expanded_counter = 0
        self.inList_counter = 0
        #self.pastState = None
        #self.visual_state = state
        #self.visual_state_priority = []
        #self.end_or_start = False
        self.matrix = matrix
        self.initSprite()

    def getState(self):
        return self.state

    def getCost(self):
        return self.cost

    def setCost(self, cost):
        self.cost = cost
        self.updateSprite()
        self.updateMatrix()

    def expanded_counter_up(self):
        self.expanded_counter = self.expanded_counter + 1

    def inList_counter_up(self):
        self.inList_counter = self.inList_counter + 1

    def reset_couters(self):
        self.expanded_counter = 0
        self.inList_counter = 0

    def getExpanded_counter(self):
        return self.expanded_counter

    def getInList_counter(self):
        return self.inList_counter

    #def getVisual_state(self):
    #    return self.visual_state

    def getRect(self):
        return self.rect

    def getCell_point_place(self):
        return self.cell_point_place

    #def setEnd_or_start_as_true(self):
    #    self.end_or_start = True

    #def setEnd_or_start_as_false(self):
    #    self.end_or_start = False

    #def IsEnd_or_start(self):
    #    return self.pastState == END or self.pastState == START

    def getStateColor(self):
        state = self.state
        if(state == ACCESSIBLE):
            return GRAY
        elif(state == UNACCESSIBLE):
            return BLACK
        elif(state == EXPANDED):
            return BLUE
        elif(state == PATH):
            return YELLOW
        elif(state == END):
            return RED
        elif(state == START):
            return GREEN
        elif(state == IN_LIST):
            return LIGHT_BLUE
        elif(state == SELECTED):
            return PINK

    def initSprite(self):
        self.updateSprite()

    def updateSprite(self):
        self.surface.fill(self.getStateColor())
        if self.isStateExpanded() and self.getExpanded_counter() > 1:
            self.number_blit(self.getExpanded_counter())
        elif self.isStateInlist() and self.getInList_counter() > 1:
            self.number_blit(self.getInList_counter())
        elif self.isStateAccessible() and self.getCost() != 1:
            self.number_blit(self.getCost(),color = WHITE)

        self.line_square()

    def updateState(self, state):
        if not (self.isStateEnd() or self.isStateStart()):
            self.state = state
            self.updateSprite()
            self.updateMatrix()
        else:
            if state == ACCESSIBLE or state == EXPANDED:
                self.state = state



    #def updateState(self, state):
        #if self.isStateAccessible():
        #    self.state = state
        #    self.updateSprite()
        #    self.updateMatrix()
        #elif self.isStateUnaccessible():
        #    self.state = state
        #    self.updateSprite()
        #    self.updateMatrix()
        #elif self.isStateSelected():
        #    self.state = state
        #    self.updateSprite()
        #    self.updateMatrix()
        #elif self.isStatePath():
        #    self.state = state
        #    self.updateMatrix()
        #elif self.isStateInlist():
        #    self.state = state
        #    self.updateSprite()
        #    self.updateMatrix()
        #elif self.isStateExpanded():
        #    self.state = state
        #    if state == ACCESSIBLE or state == PATH:
        #        self.updateSprite()
        #        self.updateMatrix()
        #elif self.isStateEnd():
        #    if not (state == UNACCESSIBLE or state == SELECTED or state == IN_LIST):
        #        self.state = state
        #    if state == ACCESSIBLE :
        #        self.updateSprite()
        #        self.updateMatrix()
        #elif self.isStateStart():
        #    if not (state == UNACCESSIBLE or state == SELECTED or state == IN_LIST):
        #        self.state = state
        #    if state == ACCESSIBLE :
        #        self.updateSprite()
        #        self.updateMatrix()

        #if self.state == START or self.state == END:
        #    self.setEnd_or_start_as_true()

    def updateMatrix(self):
        self.matrix.updateSprite(self)

    def setStateAsAccessible(self):
        self.reset_couters()
        self.updateState(ACCESSIBLE)


    def setStateAsUnaccessible(self):
        self.updateState(UNACCESSIBLE)



    def setStateAsExpanded(self):
        self.expanded_counter_up()
        self.updateState(EXPANDED)


    def setStateAsPath(self):
        self.updateState(PATH)


    def setStateAsEnd(self):
        self.updateState(END)


    def setStateAsStart(self):
        self.updateState(START)


    def setStateAsInlist(self): #o que me encomoda é que como a cell start não ganha o status de IN_LIST ele será objeto de n nodes. Tudo bem quando isso ocorra para a cell end. Na verdade isso só me é um problema para buscas que procuram não adicionar na sua estrutura nodes cuja coordenada já foi expandida
        self.inList_counter_up()
        self.updateState(IN_LIST)


    def setStateAsSelected(self):
        self.updateState(SELECTED)


    def isStateAccessible(self):
        return self.state == ACCESSIBLE

    def isStateUnaccessible(self):
        return self.state == UNACCESSIBLE

    def isStateExpanded(self):
        return self.state == EXPANDED

    def isStatePath(self):
        return self.state == PATH

    def isStateStart(self):
        return self.state == START

    def isStateEnd(self):
        return self.state == END

    def isStateInlist(self):
        return self.state == IN_LIST

    def isStateSelected(self):
        return self.state == SELECTED

    def number_blit(self, number, color = PINK):
        font_size = min(self.cell_dimension[0],self.cell_dimension[1])
        font = pygame.font.Font(None, font_size)
        text = font.render("{}".format(number), 1, color)
        self.surface.blit(text, (5, 3))

    def line_square(self, color=OUTLINE_GRAY):
        surface = self.surface
        rect = pygame.Rect((0,0),self.cell_dimension)
        thickness = THICKNESS

        start_point = rect.topleft
        end_point = rect.bottomleft
        pygame.draw.line(surface, color, start_point, end_point, thickness)

        start_point = end_point
        end_point = rect.bottomright
        pygame.draw.line(surface, color, start_point, end_point, thickness)

        start_point = end_point
        end_point = rect.topright
        pygame.draw.line(surface, color, start_point, end_point, thickness)

        start_point = end_point
        end_point = rect.topleft
        pygame.draw.line(surface, color, start_point, end_point, thickness)

    def getSprite(self):
        return self.surface

    #def click_check(self):
        #return self.rect.collidepoint(pygame.mouse.get_pos())
