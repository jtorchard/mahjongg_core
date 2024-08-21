class Player:

    def __init__(self, player_id):
        if player_id not in range(1, 5):
            raise ValueError
        self.player_id = player_id
        self.score = 2000
        self.hand = []
        self.wind = None

    def __str__(self):
        return f"player_{self.player_id}"
