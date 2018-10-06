from helper import *
from helper import PathFinder

class Bot:
    def __init__(self):

        self.turn = 0
        self.priority = ""
        self.start = True
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
                temp.append(gameMap.getTileAt(Point(x, y)))
            local.append(temp)
        return local

    # returns a list containing lists [x, y] of the coordinates of nearby resources
    def scanResources(self, surr):
        nearbyRes = []
        for y in range(0, len(surr)):
            for x in range(0, len(surr[y])):
                if surr[y][x] is TileContent.Resource:
                    nearbyRes.append([x, y])
        if self.priority is "res":
            print("insert pathfinder algorithm to find resources")
        return nearbyRes

        # a tear drops for val RIP your valuable time

    def choosePathAction(self, gameMap,nextMove):
        nextBlock = self.PlayerInfo.position + nextMove
        blockId =  gameMap.getTileAt(nextBlock).value
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

    def execute_turn(self, gameMap, visiblePlayers):
        """
        This is where you decide what action to take.
            :param gameMap: The gamemap.
            :param visiblePlayers:  The list of visible players.
        """

        if not self.inMotion:
            mineralPositions = self.scanArea(gameMap)
            if len(mineralPositions) == 0:
                #defaultMove = self.computeDefaultNextMove()
                defaultMove = Point(1,0)
                return create_move_action(defaultMove)
            else:
                closestMineral = self.findClosest(mmineralPositions)
                pathFinder = PathFinder.PathFinder(self.PlayerInfo.Position, closestMineral, gameMap)
                self.path = pathFinder.Solve()
                self.inMotion = True
                self.destinationAction = "collect"


        if self.inMotion:
            nextMove = self.path[self.nextMoveIndex]
            decision = self.choosePathAction(gameMap, nextMove)
            if self.nextMoveIndex == len(self.path):
                destinationAction = self.execDestinationAction(self.path[self.nextMoveIndex-1])
                self.nextMoveIndex = 0
                self.path = []
                self.inMotion = False
                return destinationAction

            elif decision == "attack":
                return create_attack_action(nextMove)
            elif decision == "move":
                self.nextMoveIndex += 1
                create_move_action(nextMove)

        if self.goHome:
            pathFinder = PathFinder.PathFinder(self.PlayerInfo.Position, closestMineral, gameMap)
            self.path = pathFinder.Solve()
            self.inMotion = True
            self.destinationAction = "home"
            self.goHome = False




        #print(visiblePlayers)
        '''print(visiblePlayers)
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
        surr = self.surroundings(gameMap)
        # Write your bot here. Use functions from aiHelper to instantiate your actions.
        return create_move_action(Go.Up.value)'''
        return create_move_action(Point(0, 0))
    def after_turn(self):
        self.turn += 1
        """
        Gets called after executeTurn
        """
        pass
