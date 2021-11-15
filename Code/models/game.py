class Game():
    def __init__(self, player1, player2, score=[0, 0], completed=False, id=None):
        self.player1 = player1
        self.player2 = player2
        self.score = score
        self.completed = completed
        self.id = id
    
    def input_score(self, score1, score2):
        self.score = [score1, score2]
    
    def reconcile_game(self):
        # set game to completed
        self.completed = True
        # identify which player won 
        if self.score[0] > self.score[1]:
        # give the player that won a win
            self.player1.winner()
        # give the player that lost a loss 
            self.player2.loser()
        elif self.score[0] < self.score[1]:
            self.player1.loser()
            self.player2.winner()
        # assign the pts for and againsy for each player
        self.player1.pts_for = self.score[0]
        self.player2.pts_against = self.score[0]
        self.player1.pts_against = self.score[1]
        self.player2.pts_for = self.score[1]
            