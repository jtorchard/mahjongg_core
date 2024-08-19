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
    def __init__(self, shuffle_wall=True):
        self.alive_tiles = []
        self.dead_tiles = []
        self.is_shuffled = False
        self.initialise_wall()
        if shuffle_wall:
            self.shuffle_wall()

    def initialise_wall(self):
        self.alive_tiles = [
            Tile(tile) for tile in chain(
                characters, bamboos, circles, dragons, winds, flowers, seasons)
        ] * 4
        self.dead_tiles = []
        self.is_shuffled = False

    def shuffle_wall(self):
        shuffle(self.alive_tiles)
        self.is_shuffled = True

    def take_live_wall(self):
        return self.alive_tiles.pop()

    def take_dead_wall(self):
        return self.dead_tiles.pop()

    def break_wall(self):
        pass

    def __str__(self):
        return "".join([tile.utf8 for tile in chain(self.alive_tiles, self.dead_tiles)])

    def __len__(self):
        return len(self.alive_tiles + self.dead_tiles)
