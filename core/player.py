class Player:

    def __init__(self, player_id, ai=False):
        if player_id not in range(1, 5):
            raise ValueError
        self.ai = ai
        self.player_id = player_id
        self.score = 2000
        self.hand = []

    def __str__(self):
        return f"player_{self.player_id}"

    @property
    def is_ai(self):
        return self.ai

    def add_tile(self, tile):
        self.hand.append(tile)

    def remove_tile(self, tile):
        self.hand.pop(tile)

    def get_hand(self):
        return self.hand

    def get_score(self):
        return self.score

    def get_id(self):
        return self.player_id
