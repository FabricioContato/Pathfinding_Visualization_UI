from Cell import Cell
from Node import Node
from random import randint
import pygame

class Matrix:
    def __init__(self,surface_dimension,matrix_rows,matrix_columns):
        self.surface = pygame.Surface(surface_dimension)
        self.surface_dimension = surface_dimension
        self.matrix_rows = matrix_rows
        self.matrix_columns = matrix_columns
        self.initCell_dimension()
        self.initMatrix()
        self.initSprite()
        self.end_cell = None
        self.start_cell = None
        self.selected_cell = None

        #self.to_be_bleated = []
        #self.change = True

    def initCell_dimension(self):
        self.cell_width = self.surface_dimension[0] // self.matrix_columns
        self.cell_height = self.surface_dimension[1] // self.matrix_rows

    def initMatrix(self):
        self.matrix = []
        row = []
        cell_dimension = (self.cell_width,self.cell_height)
        matrix = self
        for i in range(self.matrix_rows):
            row = []
            for j in range(self.matrix_columns):
                cell_y = i * self.cell_height
                cell_x = j * self.cell_width
                cell_point_place = (cell_x,cell_y)
                row.append(Cell(cell_point_place,cell_dimension, matrix))
            self.matrix.append(row)

    def inboundaries(self,i,j):
        return  0 <= i < self.matrix_rows and 0 <= j < self.matrix_columns

    def i_of_cell(self, cell):
        return cell.getCell_point_place()[1] // self.cell_height

    def j_of_cell(self, cell):
        return cell.getCell_point_place()[0] // self.cell_width

    def initSprite(self):
        #cell = None;
        for i in range(self.matrix_rows):
            for j in range(self.matrix_columns):
                cell = self.matrix[i][j]
                self.surface.blit(cell.getSprite(),cell.getRect())

        return self.surface

    def getSprite(self):
        #self.blitCells(self.to_be_bleated)
        return self.surface

    def blitCell(self,cell):
        #self.change = True
        self.surface.blit(cell.getSprite(),cell.getRect())

    #def blitCells(self,cell_list):
        #for cell in cell_list:
            #self.blitCell(cell)

    #def spriteChange(self):
        #result = (len(self.to_be_bleated) > 0 or self.change)
        #self.change = False
        #return result
    def updateSprite(self,cell):
        self.blitCell(cell)

    def cell_click_check_for_end(self):
        point = pygame.mouse.get_pos()
        j = point[0] // self.cell_width
        i = point[1] // self.cell_height
        cell = self.matrix[i][j]
        cell.setStateAsEnd()
        self.end_cell = cell
        #self.blitCell(cell)

    def cell_click_check_for_start(self):
        point = pygame.mouse.get_pos()
        j = point[0] // self.cell_width
        i = point[1] // self.cell_height
        cell = self.matrix[i][j]
        cell.setStateAsStart()
        self.start_cell = cell
        #self.blitCell(cell)

    def cell_click_check_for_unaccessible(self):
        point = pygame.mouse.get_pos()
        j = point[0] // self.cell_width
        i = point[1] // self.cell_height
        cell = self.matrix[i][j]
        cell.setStateAsUnaccessible()

        #self.blitCell(cell)

    def cell_click_check_for_unaccessible_or_acessible(self):
        point = pygame.mouse.get_pos()
        j = point[0] // self.cell_width
        i = point[1] // self.cell_height
        cell = self.matrix[i][j]
        #print(self.heuristic_euclidean_distance2(cell))
        if cell.isStateAccessible():
            cell.setStateAsUnaccessible()
        elif cell.isStateUnaccessible():
            cell.setStateAsAccessible()

    def line_draw(self):
        if self.selected_cell == None :
            point = pygame.mouse.get_pos()
            j = point[0] // self.cell_width
            i = point[1] // self.cell_height
            self.selected_cell = self.matrix[i][j]
            self.selected_cell.setStateAsSelected()
        else:
            point = pygame.mouse.get_pos()
            j = point[0] // self.cell_width
            i = point[1] // self.cell_height
            selected_cell2 = self.matrix[i][j]

            c1i = self.i_of_cell(self.selected_cell)
            c1j = self.j_of_cell(self.selected_cell)
            c2i = self.i_of_cell(selected_cell2)
            c2j = self.j_of_cell(selected_cell2)

            if c1i != c2i :
                imx = max(c1i,c2i)
                imn = min(c1i,c2i)
                for i in range(imn,imx + 1):
                    self.matrix[i][c1j].setStateAsUnaccessible()
                for i in range(imn,imx + 1):
                    self.matrix[i][c2j].setStateAsUnaccessible()

                #jmx = max(c1j,c2j)
                #jmn = min(c1j,c2j)
                #for i in range(jmn,jmx + 1):
                    #self.matrix[imx][c1j].setStateAsUnaccessible()

            if c1j != c2j :
                jmx = max(c1j,c2j)
                jmn = min(c1j,c2j)
                for j in range(jmn,jmx + 1):
                    self.matrix[c1i][j].setStateAsUnaccessible()
                for j in range(jmn,jmx + 1):
                    self.matrix[c2i][j].setStateAsUnaccessible()

                #imx = max(c1i,c2i)
                #imn = min(c1i,c2i)
                #for i in range(imn,imx + 1):
                    #self.matrix[i][jmx].setStateAsUnaccessible()

            self.selected_cell = None


    def getStart_node(self):
        return Node(self.start_cell)

    def getEnd_node(self):
        return Node(self.end_cell)

    def set_cost(self,n):
        point = pygame.mouse.get_pos()
        j = point[0] // self.cell_width
        i = point[1] // self.cell_height
        cell = self.matrix[i][j]
        cell.setCost(n)

    def heuristic_euclidean_distance(self, node):
        end_j = self.end_cell.getCell_point_place()[0] // self.cell_width
        end_i = self.end_cell.getCell_point_place()[1] // self.cell_height
        j = node.getCell().getCell_point_place()[0] // self.cell_width
        i = node.getCell().getCell_point_place()[1] // self.cell_height

        h = (abs(end_i - i)**2 + abs(end_j - j)**2)**0.5
        return h

    #def heuristic_euclidean_distance2(self, node):
    #    end_j = self.end_cell.getCell_point_place()[0] // self.cell_width
    #    end_i = self.end_cell.getCell_point_place()[1] // self.cell_height
    #    j = node.getCell_point_place()[0] // self.cell_width
    #    i = node.getCell_point_place()[1] // self.cell_height

    #    h = (abs(end_i - i)**2 + abs(end_j - j)**2)**0.5
    #    return h

    def get_neighbors(self,node):
        j = node.getCell().getCell_point_place()[0] // self.cell_width
        i = node.getCell().getCell_point_place()[1] // self.cell_height

        neighbors = []

        if self.inboundaries(i+1,j):
            up_neighbor = self.matrix[i+1][j]
            if not up_neighbor.isStateUnaccessible():
                #up_neighbor.setStateAsExpanded()
                #self.blitCell(up_neighbor
                #self.to_be_bleated.append(up_neighbor)
                neighbors.append(Node(up_neighbor))

        if self.inboundaries(i-1,j):
            down_neighbor = self.matrix[i-1][j]
            if not down_neighbor.isStateUnaccessible():
                #down_neighbor.setStateAsExpanded()
                #self.blitCell(down_neighbor)
                #self.to_be_bleated.append(down_neighbor)
                neighbors.append(Node(down_neighbor))

        if self.inboundaries(i,j-1):
            left_neighbor = self.matrix[i][j-1]
            if not left_neighbor.isStateUnaccessible():
                #left_neighbor.setStateAsExpanded()
                #self.blitCell(left_neighbor)
                #self.to_be_bleated.append(left_neighbor)
                neighbors.append(Node(left_neighbor))

        if self.inboundaries(i,j+1):
            right_neighbor = self.matrix[i][j+1]
            if not right_neighbor.isStateUnaccessible():
                #right_neighbor.setStateAsExpanded()
                #self.blitCell(right_neighbor)
                #self.to_be_bleated.append(right_neighbor)
                neighbors.append(Node(right_neighbor))

        return neighbors

    def n_of_new_Neighbors(self,node):
        j = node.getCell().getCell_point_place()[0] // self.cell_width
        i = node.getCell().getCell_point_place()[1] // self.cell_height

        number = 0

        if self.inboundaries(i+1,j):
            up_neighbor = self.matrix[i+1][j]
            if up_neighbor.isStateAccessible():
                #up_neighbor.setStateAsExpanded()
                #self.blitCell(up_neighbor
                #self.to_be_bleated.append(up_neighbor)
                number = number + 1


        if self.inboundaries(i-1,j):
            down_neighbor = self.matrix[i-1][j]
            if down_neighbor.isStateAccessible():
                #down_neighbor.setStateAsExpanded()
                #self.blitCell(down_neighbor)
                #self.to_be_bleated.append(down_neighbor)
                number = number + 1

        if self.inboundaries(i,j-1):
            left_neighbor = self.matrix[i][j-1]
            if left_neighbor.isStateAccessible():
                #left_neighbor.setStateAsExpanded()
                #self.blitCell(left_neighbor)
                #self.to_be_bleated.append(left_neighbor)
                number = number + 1

        if self.inboundaries(i,j+1):
            right_neighbor = self.matrix[i][j+1]
            if right_neighbor.isStateAccessible():
                #right_neighbor.setStateAsExpanded()
                #self.blitCell(right_neighbor)
                #self.to_be_bleated.append(right_neighbor)
                number = number + 1

        return number

    def reset(self):
        for i in range(self.matrix_rows):
            for j in range(self.matrix_columns):
                cell = self.matrix[i][j]
                cell.setStateAsAccessible()
                cell.setCost(1)

        self.start_node = None
        self.end_node = None

    def random_unaccessible_cells(self):
        for i in range(self.matrix_rows):
            for j in range(self.matrix_columns):
                if randint(1,10) <= 1:
                    cell = self.matrix[i][j]
                    cell.setStateAsUnaccessible()
                    #self.surface.blit(cell.getSprite(),cell.getRect())
