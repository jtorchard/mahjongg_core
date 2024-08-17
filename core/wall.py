from itertools import chain

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
        self.tiles = [
            Tile(tile) for tile in chain(
                characters, bamboos, circles, dragons, winds, flowers, seasons)
        ] * 4

    def __str__(self):
        return "".join([tile.utf8 for tile in self.tiles])
