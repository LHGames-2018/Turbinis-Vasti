from helper import *
from helper import PathFinder
import math

class Bot:
    def __init__(self):

        self.turn = 0
        self.priority = ""
        self.start = True
        self.inMotion = False
        self.nextMove = 0
        self.path = []
        pass


    def before_turn(self, playerInfo):
        # decide priority for turn here
        #self.priority = "res"
        """
        Gets called before ExecuteTurn. This is where you get your bot's state.
            :param playerInfo: Your bot's current state.
        """
        self.PlayerInfo = playerInfo

    def surroundings(self, gameMap):
        local = []
        for y in range(gameMap.yMin, gameMap.yMax):
            temp = []
            for x in range(gameMap.xMin, gameMap.xMax):
                #print(str(x) + " " + str(y))
                temp.append(gameMap.getTileAt(Point(x, y)))
            local.append(temp)
        return local

    # returns a list containing lists [x, y] of the coordinates of nearby resources
    def scanResources(self, surr):
        nearbyRes = []
        for y in range(-10, 21):
            for x in range(-10, 21):
                if surr.getTileAt(self.PlayerInfo.Position + Point(x, y)) is TileContent.Resource:
                    #print(self.PlayerInfo.Position)
                    #print(self.PlayerInfo.Position + Point(x, y))
                    nearbyRes.append(self.PlayerInfo.Position + Point(x, y))
        if self.priority is "res":
            print("insert pathfinder algorithm to find resources")
        return nearbyRes

    # takes an array of Point objects and returns the one which is closest to the player
    def findClosest(self, list):
        pos = self.PlayerInfo.Position
        closest = Point(0, 0)
        print(pos)
        for entry in list:
            if (abs((pos.x - entry.x)) + abs((pos.y - entry.y))) < (abs((pos.x - closest.x)) + abs((pos.y - closest.y))):
                closest = entry
        return closest

    def scanClose(self, gameMap, tile):
        pos = self.PlayerInfo.Position
        if gameMap.getTileAt(pos + Point(0, -1)) is tile:
            return pos + Point(0, -1)
        if gameMap.getTileAt(pos + Point(0, 1)) is tile:
            return pos + Point(0, 1)
        if gameMap.getTileAt(pos + Point(1, 0)) is tile:
            return pos + Point(1, 0)
        if gameMap.getTileAt(pos + Point(-1, 0)) is tile:
            return pos + Point(-1, 0)
        return pos

    def execute_turn(self, gameMap, visiblePlayers):
        """
        This is where you decide what action to take.
            :param gameMap: The gamemap.
            :param visiblePlayers:  The list of visible players.
        """
        #print(self.scanClose(gameMap, TileContent.Resource))
        nearbyRes = self.scanResources(gameMap)
        print(nearbyRes)
        print(self.findClosest(nearbyRes))
        print("==========================================================")
        if self.start:
            self.start = True
            self.inMotion = True
            '''print(self.PlayerInfo.Position)
            print(Point(-6, 0))
            print(self.PlayerInfo.Position + Point(-6, 0))'''
            pathFinder = PathFinder.PathFinder(self.PlayerInfo.Position, self.PlayerInfo.Position + Point(2, 0))
            '''print(gameMap)'''
            self.path = pathFinder.Solve(gameMap)
            for point in self.path:
                print(point)


        if self.inMotion:
            if self.nextMove == len(self.path):
                self.nextMove = 0
                self.path = []
                self.inMotion = False
            else:
                currentMove = self.nextMove
                self.nextMove +=1
                return create_move_action(self.path[currentMove])

        #directions = [Go.Right, Go.Right, Go.Right, Go.Right, Go.Right]
        #surr = self.surroundings(gameMap)
        # Write your bot here. Use functions from aiHelper to instantiate your actions.
        return create_move_action(Go.Left.value)

    def after_turn(self):
        self.turn += 1
        """
        Gets called after executeTurn
        """
        pass
