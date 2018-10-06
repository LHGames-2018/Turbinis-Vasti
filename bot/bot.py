from helper import *
from helper import PathFinder

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

    def execute_turn(self, gameMap, visiblePlayers):
        """
        This is where you decide what action to take.
            :param gameMap: The gamemap.
            :param visiblePlayers:  The list of visible players.
        """

        directions = [Go.Up, Go.Up, Go.Up, Go.Left, Go.Up]
        #directions = [Point(-1, 0), Point(0, -1)]
        # Write your bot here. Use functions from aiHelper to instantiate your actions.
        #print("move")
        #if (directions.__len__ == (self.turn -1)):
        #    return create_move_action(Go.Up)
        return create_move_action(directions[self.turn].value)
        
        #gameMap.getTileAt(Point())
        #if (self.PlayerInfo.Position
        #return create_move_action(Go.Right.value)

        print(self.scanResources(gameMap))

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
        #return create_move_action(Go.Up.value)



    def after_turn(self):
        self.turn += 1
        """
        Gets called after executeTurn
        """
        pass


    lastDirection = [Go.Up.value]

    def findNextDirection(self, lastDirection):
        if (lastDirection.len == 0):
            lastDirection[0] = Go.Up.value
            return lastDirection[0]
        else:
            lastDirection.append(Go[lastDirection.len].value)
            return lastDirection[lastDirection.len - 1]