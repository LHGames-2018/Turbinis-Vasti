from helper import *


class Bot:
    def __init__(self):
        self.turn = 0
        pass


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
        #directions = [Go.Right, Go.Right, Go.Right, Go.Right, Go.Right]

        # Write your bot here. Use functions from aiHelper to instantiate your actions.
        return create_move_action(Go.Right.value)

    def after_turn(self):
        self.turn += 1
        """
        Gets called after executeTurn
        """
        pass
