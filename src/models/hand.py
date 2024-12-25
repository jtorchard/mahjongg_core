"""
    Handles the tiles in a player's hand.
    Ordering, sorting, determining special cases etc.
"""

from collections import Counter, UserList
from functools import wraps

from loguru import logger

from src.exceptions import InvalidObjectForHand
from src.models.tile import Tile

logger.remove()  # Turn off default console logger
logger.add("mahjong.log", colorize=True, level="INFO")


def hand_mutated(func):
    @wraps(func)
    def inner(self, *args, **kwargs):
        func(self, *args, **kwargs)
        self.analyse_hand(*args, **kwargs)

    return inner


class Hand(UserList):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.one_chance_hand = False
        self.can_go_out = False
        self.wind_of_the_round = False
        self.chows = 0
        self.concealed_pungs = 0
        self.concealed_kongs = 0
        self.exposed_pungs = 0
        self.exposed_kongs = 0
        self.pairs = 0
        self.seasons = 0
        self.flowers = 0

    @hand_mutated
    def __setitem__(self, i, item):
        if not isinstance(item, Tile):
            raise InvalidObjectForHand()
        self.data[i] = item

    @hand_mutated
    def __delitem__(self, i):
        del self.data[i]

    @hand_mutated
    def append(self, item):
        if not isinstance(item, Tile):
            raise InvalidObjectForHand()
        self.data.append(item)

    @hand_mutated
    def remove(self, i):
        self.data.remove(i)

    @hand_mutated
    def pop(self, i=-1):
        self.data.pop(i)

    @hand_mutated
    def insert(self, i, item):
        if not isinstance(item, Tile):
            raise InvalidObjectForHand()
        self.data.insert(i, item)

    @hand_mutated
    def extend(self, other):
        if isinstance(other, list):
            if other and not isinstance(other[0], Tile):
                raise InvalidObjectForHand()
        self.data.extend(other)

    def __str__(self):
        return " ".join([t.utf8 for t in self.data])

    def analyse_hand(self, *args, **kwargs):
        logger.info(f"Hand changed. args: {args} kwargs: {kwargs} - Analysing hand...")
        c: Counter = Counter(self.data)
        logger.info(f"Potential Pairs: {list(filter(lambda a: a[1] >= 2, c.items()))}")
        logger.info(f"Tiles: |{'| |'.join([f'{k.name}:{v}' for k, v in c.items()])}|")
