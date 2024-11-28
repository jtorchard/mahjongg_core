class Player:
    def __init__(self, player_id, ai=False, starting_score=1000):
        if player_id not in range(1, 5):
            raise ValueError
        self.ai = ai
        self._player_id = player_id
        self._score = starting_score
        self._hand = []

    def __str__(self):
        return f"player_{self._player_id}"

    @property
    def is_ai(self):
        return self.ai

    @property
    def hand(self):
        return self._hand

    @property
    def score(self):
        return self._score

    @property
    def player_id(self):
        return self._player_id

    def add_tile(self, tile):
        self.hand.append(tile)

    def remove_tile(self, tile):
        self.hand.pop(tile)
