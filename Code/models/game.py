class Game():
    def __init__(self, player1, player2, score=[0, 0], completed=False, id=None):
        self.player1 = player1
        self.player2 = player2
        self.score = score
        self.completed = completed
        self.id = id
    
    def input_score(self, score1, score2):
        self.score = [score1, score2]
    
    def reconcile_game():
        pass