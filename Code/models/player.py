class Player():
    def __init__(self, name, army, wins=0, losses=0, pts_for=0, pts_against=0, id=None):
        self.name = name
        self.army = army
        self.wins = 0
        self.losses = 0
        self.pts_for = 0
        self.pts_against = 0
        self.id = id

    def winner(self):
        self.wins += 1

    def loser(self):
        self.losses += 1

    def increase_pts_for(self, pts):
        self.pts_for += pts
    
    def increase_pts_against(self, pts):
        self.pts_against += pts