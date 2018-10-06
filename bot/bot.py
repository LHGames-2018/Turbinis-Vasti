from helper import *
from helper import PathFinder

class Bot:
    def __init__(self):
        self.start = True
        self.inMotion = False
        self.nextMove = 0
        self.path = []

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

        # Write your bot here. Use functions from aiHelper to instantiate your actions.
        return create_move_action(Point(0, 0))

    def after_turn(self):
        """
        Gets called after executeTurn
        """
        pass
