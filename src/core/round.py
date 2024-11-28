"""
    Contains data for each round played.
    Each round has its own wind and consists of at least four hands.
"""


class Round:

    def __init__(self, wind):
        self.wind = wind
        self.hands = []
        self.seats = {}
        self.seat_change_count = 0

    @property
    def hand_count(self):
        return len(self.hands)
