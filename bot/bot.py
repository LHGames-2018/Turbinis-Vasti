from helper import *
from helper import PathFinder
import math

class Bot:
    def __init__(self):

        self.turn = 0
        self.priority = ""
        #self.start = True
        self.inMotion = False
        self.nextMoveIndex = 0
        self.path = []
        self.goHome = False
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
    def scanResources(self, gameMap):
        nearbyRes = []
        for y in range(-10, 11):
            for x in range(-10, 11):
                if gameMap.getTileAt(self.PlayerInfo.Position + Point(x, y)) is TileContent.Resource:
                    #print(self.PlayerInfo.Position)
                    #print(self.PlayerInfo.Position + Point(x, y))
                    nearbyRes.append(self.PlayerInfo.Position + Point(x, y))
        if self.priority is "res":
            print("insert pathfinder algorithm to find resources")
        return nearbyRes


        # a tear drops for val RIP your valuable time

    def choosePathAction(self, gameMap,nextMove):
        nextBlock = self.PlayerInfo.Position + nextMove
        blockId =  gameMap.getTileAt(nextBlock)
        print(blockId)
        if blockId == TileContent.Wall:
            return "attack"
        elif blockId == TileContent.Empty:
            return "move"

    def execDestinationAction(self, direction):
        if self.destinationAction == "collect":
            self.goHome = True
            return create_collect_action(direction)
        elif self.destinationAction == "home":
            return create_move_action(Point(0,0))

    # takes an array of Point objects and returns the one which is closest to the player
    def findClosest(self, list):
        pos = self.PlayerInfo.Position
        closest = Point(0, 0)
        print(pos)
        for entry in list:
            if (abs((pos.x - entry.x)) + abs((pos.y - entry.y))) < (abs((pos.x - closest.x)) + abs((pos.y - closest.y))):
                closest = entry
        return closest


    def execute_turn(self, gameMap, visiblePlayers):
        """
        This is where you decide what action to take.
            :param gameMap: The gamemap.
            :param visiblePlayers:  The list of visible players.
        """

        if not self.inMotion:
            mineralPositions = self.scanResources(gameMap)
            if len(mineralPositions) == 0:
                #defaultMove = self.computeDefaultNextMove()
                defaultMove = Point(1,0)
                print("This is number 1")
                return create_move_action(defaultMove)
            else:
                closestMineral = self.findClosest(mineralPositions)
                pathFinder = PathFinder.PathFinder(self.PlayerInfo.Position, closestMineral, gameMap)
                self.path = pathFinder.Solve()
                self.inMotion = True
                self.destinationAction = "collect"


        if self.inMotion:
            print("inMotion")
            #print(self.path)
            nextMove = self.path[self.nextMoveIndex]
            print (nextMove)
            print(self.nextMoveIndex)
            decision = self.choosePathAction(gameMap, nextMove)
            print(decision)

            if self.nextMoveIndex == len(self.path) - 1:
                ressourceDirection = scanClose
                destinationAction = self.execDestinationAction(self.path[self.nextMoveIndex-1])
                self.nextMoveIndex = 0
                self.path = []
                self.inMotion = False
                return destinationAction

            elif decision == "attack":
                print("attack")
                return create_attack_action(nextMove)
            elif decision == "move":
                self.nextMoveIndex += 1
                return create_move_action(nextMove)

        if self.goHome:
            pathFinder = PathFinder.PathFinder(self.PlayerInfo.Position, self.PlayerInfo.HouseLocation, gameMap)
            self.path = pathFinder.Solve()
            self.inMotion = True
            self.destinationAction = "home"
            self.goHome = False




        #print(visiblePlayers)
        '''print(visiblePlayers)
        nearbyRes = self.scanResources(gameMap)
        print(nearbyRes)
        print(self.findClosest(nearbyRes))

        print("==========================================================")
        if self.start:
            self.start = True
            self.inMotion = True

            pathFinder = PathFinder.PathFinder(self.PlayerInfo.Position, self.PlayerInfo.Position + Point(2, 0))
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
            '''
        return create_move_action(Point(0, 0))

    def after_turn(self):
        self.turn += 1
        """
        Gets called after executeTurn
        """
        pass
