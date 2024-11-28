import random
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
    def __init__(self, seed=None, use_flowers=True, use_seasons=True):
        self.seed = seed
        self.use_flowers = use_flowers
        self.use_seasons = use_seasons
        self.alive_tiles = []
        self.dead_tiles = []
        self.discards = []
        self.loose_tiles = []
        self.shuffled = False
        self.initialise_wall()
        self.shuffle_wall()
        self.break_wall()

    @property
    def is_shuffled(self):
        return self.shuffled

    def _set_seed(self):
        random.seed(self.seed)

    def initialise_wall(self):
        self.alive_tiles = [
            Tile(tile)
            for tile in chain(
                characters * 4,
                bamboos * 4,
                circles * 4,
                dragons * 4,
                winds * 4,
                flowers if self.use_flowers else [],
                seasons if self.use_seasons else [],
            )
        ]
        self.dead_tiles = []
        self.shuffled = False

    def shuffle_wall(self):
        self._set_seed()
        shuffle(self.alive_tiles)
        self.shuffled = True if self.seed is None else False

    def take_live_wall(self):
        return self.alive_tiles.pop()

    def take_dead_wall(self):
        return self.dead_tiles.pop()

    def add_discard(self, tile):
        self.discards.append(tile)

    def break_wall(self):
        self.dead_tiles = self.alive_tiles[:16]
        self.alive_tiles = self.alive_tiles[16:]
        self.loose_tiles = [self.dead_tiles.pop(), self.dead_tiles.pop()]

    def __str__(self):
        return " ".join([tile.utf8 for tile in chain(self.alive_tiles)])

    def __len__(self):
        return len(self.alive_tiles)
