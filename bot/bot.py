from helper import *


class Bot:
    def __init__(self):
        pass
        self.turn = 0

    def before_turn(self, playerInfo):
        """
        Gets called before ExecuteTurn. This is where you get your bot's state.
            :param playerInfo: Your bot's current state.
        """
        self.PlayerInfo = playerInfo

    def execute_turn(self, gameMap, visiblePlayers):
        """
        This is where you decide what action to take.
            :param gameMap: The gamemap.
            :param visiblePlayers:  The list of visible players.
        """
        directions = [Point(0,-1), Point(0, -1), Point(0, -1), Point(0, 1), Point(-1, 0), Point(-1, 0), Point(1, 0), Point(1, 0)]
        # Write your bot here. Use functions from aiHelper to instantiate your actions.
        return create_move_action(Point(directions[self.turn]))

    def after_turn(self):
        """
        Gets called after executeTurn
        """
        self.turn += 1
        pass
