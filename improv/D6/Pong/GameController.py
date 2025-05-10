from numpy import array

class GameController:
    def __init__(self):
        self.scores = array([0, 0])

    def __new__(self):
        if not hasattr(self, "instance"):
            self.instance = super(GameController, self).__new__(self)
        return self.instance

    def score(self, player:int):
        self.scores[player] += 1

    def get_score(self, player:int|None = None):
        if player is None:
            return self.scores
        return self.scores[player]