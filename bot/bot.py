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

    def after_turn(self):
        """
        Gets called after executeTurn
        """
        self.turn += 1
        pass
