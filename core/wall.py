from itertools import chain
from random import shuffle

from .tile import Tile
from .data import (
    characters,
    bamboos,
    circles,
    dragons,
    winds,
    flowers,
    seasons,
)


class Wall:
    def __init__(self):
        self.alive_tiles = []
        self.dead_tiles = []
        self.initialise_wall()

    def initialise_wall(self):
        self.alive_tiles = [
            Tile(tile) for tile in chain(
                characters, bamboos, circles, dragons, winds, flowers, seasons)
        ] * 4
        self._shuffle_wall()

    def _shuffle_wall(self):
        shuffle(self.alive_tiles)

    def __str__(self):
        return "".join([tile.utf8 for tile in self.tiles])
