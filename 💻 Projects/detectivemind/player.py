class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.solved = False

    def add_score(self, points):
        self.score += points