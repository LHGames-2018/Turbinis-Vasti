from helper import *


class Bot:
    def __init__(self):
        pass

    def before_turn(self, playerInfo):
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
               # print(str(x) + " " + str(y))
                temp.append(gameMap.getTileAt(Point(x, y)))
            local.append(temp)
        return local

    def scanResources(self, surr):
        nearbyRes = []
        for y in range(0, len(surr)):
            for x in range(0, len(surr[y])):
                if surr[y][x] is TileContent.Resource:
                    nearbyRes.append([x, y])
        return nearbyRes

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
