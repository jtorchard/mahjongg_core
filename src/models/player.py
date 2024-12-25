"""
    Player class represents individual player in the game.
"""

from faker import Faker

from src.exceptions import InvalidPlayerNumber


class Player:
    def __init__(self, *, seat, number, score=2000):
        if number not in range(1, 5):
            raise InvalidPlayerNumber()

        self.seat = seat
        self.name = f"{Faker().word().title()} {Faker().word().title()}"
        self.number = number
        self.hand = []
        self.score = score
