from helper import *


class Bot:
    def __init__(self):
        self.priority = ""
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

    # returns a list containing [x, y] of the coordinates of nearby players
    def scanPlayers(self, surr):
        nearbyPlayers = []
        for y in range(0, len(surr)):
            for x in range(0, len(surr[y])):
                if surr[y][x] is TileContent.Player:
                    nearbyPlayers.append([x, y])
        if self.priority is "ply":
            print("insert pathfinder algorithm to find resources")
        return nearbyPlayers

    def execute_turn(self, gameMap, visiblePlayers):
        """
        This is where you decide what action to take.
            :param gameMap: The gamemap.
            :param visiblePlayers:  The list of visible players.
        """
        surr = self.surroundings(gameMap)

        # Write your bot here. Use functions from aiHelper to instantiate your actions.
        return create_move_action(Point(-1, 0))

    def after_turn(self):
        """
        Gets called after executeTurn
        """
        pass
