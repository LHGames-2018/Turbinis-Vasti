from queue import PriorityQueue
from struct.py import Point

class Moves:
    North = Point(0,-1)
    East = Point(1,0)
    South = Point(0,1)
    West = Point(-1,0)

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
        self.distance = self.getDistance()

    def __tl__(self, other):
        return self.distance < other.distance

    def GetDistance(self):
        if (self.value == self.goal):
            return 0
        else:
            return self.value.Distance(self.goal)

    def CreateChildren(self):
        if not self.children:
            for direction in Moves:
                val = self.value.add(direction)
                child = PositionState(val, self, self.start, self.goal)
                self.children.append(child)


class PathFinder(object):
    def __init__(self, start, goal):
        self.path = []
        self.start = start
        self.goal = goal
        self.openQueue = PriorityQueue()
        self.visitedQueue = []

    def childStateIsObstacle(self, position, gameMap):
        objectId = gameMap.getTileAt(position)
        return objectId != 0

    def Solve(self, gameMap):
        startState = PositionState(self.start, 0, self.start, self.goal )
        self.openQueue.put(startState)
        while not self.path and self.openQueue.qsize():
            closestChild = self.openQueue.get()
            closestChild.CreateChildren()

            self.visitedQueue.append(closestChild.value)
            for child in closestChild.children:
                if child.value not in self.visitedQueue:
                    if child.dist == 0:
                        path = self.computeMoves(child.path)
                        self.path = path
                        break
                    if childStateIsObstacle():
                        self.visitedQueue.append(child)
                        continue

                    self.openQueue.put(child)



        if not self.path:
            print("Goal of " + self.goal + "is not possible")
        return self.path