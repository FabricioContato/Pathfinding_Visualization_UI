import pygame

class Node:
    def __init__(self,cell,name = "",value = 0):
        self.cell = cell
       # self.coordinates = coordinates
        self.value = value
        self.cost = 0
        self.name = ""
        self.parent = None

   # def getCoordinates(self):
       # return self.coordinates

    def getCell(self):
        return self.cell

    def getValue(self):
        return self.getValue

    def getName(self):
        return self.name

    def getCost(self):
        return self.cost

    def setCost(self,cost):
        self.cost = cost

    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent = parent

    def setAsExpanded(self):
        self.cell.setStateAsExpanded()

    def setAsInlist(self):
        self.cell.setStateAsInlist()

    def setAsPath(self):
        self.cell.setStateAsPath()

    def isExpanded(self):
        return self.cell.isStateExpanded()

    def isInlist(self):
        return self.cell.isStateInlist()

    def isNew(self):
        return not (self.isExpanded() or self.isInlist())

    def isParent_of(self, node):
        return node.getParent() != None and node.getParent().getCell() == self.cell

    def isEqual(self,node):
        return self.cell == node.getCell()
