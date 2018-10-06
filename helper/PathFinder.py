from queue import PriorityQueue
from helper.structs import *
from helper.tile import *
from enum import Enum

class Moves(Enum):
    North = Point(0, -1)
    East = Point(1, 0)
    South = Point(0, 1)
    West = Point(-1, 0)

class State(object):
    def __init__(self, value, parent, start = 0, goal = 0):
        self.children = []
        self.parent = parent
        self.value = value
        self.distance = 0
        if parent:
            self.path = parent.path[:]
            self.path.append(value)
            self.start = parent.start
            self.goal = parent.goal
        else:
            self.path = [value]
            self.start = start
            self.goal = goal

    def GetDistance(self):
        pass
    def CreateChildren(self):
        pass

class PositionState(State):
    def __init__(self, value, parent, start = 0, goal = 0):
        super().__init__(value, parent, start, goal)
        self.distance = self.GetDistance()

    def __lt__(self, other):
        return self.distance < other.distance

    def GetDistance(self):
        if (self.value == self.goal):
            return 0
        else:
            return Point.Distance(self.value, self.goal)

    def CreateChildren(self):
        if not self.children:
            for direction in Moves:
                val = self.value + direction.value
                child = PositionState(val, self, self.start, self.goal)
                self.children.append(child)


class PathFinder(object):
    def __init__(self, start, goal, gameMap):
        self.path = []
        self.start = start
        self.goal = goal
        self.openQueue = PriorityQueue()
        self.visitedQueue = []
        self.gameMap = gameMap

    def childStateIsObstacle(self, position):
        objectId = self.gameMap.getTileAt(position.value)
        return objectId != TileContent.Empty or objectId != TileContent.Wall

    def computeMoves(self, path):
        moves = []
        for i in range(len(path)-1):
            moves.append(path[i+1]-path[i])
        return moves


    def Solve(self):
        startState = PositionState(self.start, 0, self.start, self.goal )
        self.openQueue.put(startState)
        while not self.path and self.openQueue.qsize():
            closestChild = self.openQueue.get()
            closestChild.CreateChildren()

            self.visitedQueue.append(closestChild.value)
            counter = 0
            for child in closestChild.children:
                counter +=1
                print(counter)
                if counter > 10:
                    break
                if child.value not in self.visitedQueue:
                    if child.distance == 0.0:
                        self.path = self.computeMoves(child.path)
                        break
                    if self.childStateIsObstacle(child):
                        self.visitedQueue.append(child)

                    self.openQueue.put(child)

        if not self.path:
            print("Goal of " + str(self.goal) + "is not possible")
            return
        else:
            return self.path
