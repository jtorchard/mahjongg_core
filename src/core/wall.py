import random
from abc import abstractmethod
from itertools import chain
from random import shuffle

from .data import (
    bamboos,
    characters,
    circles,
    dragons,
    flowers,
    seasons,
    winds,
)
from .tile import Tile


class Wall:
    def __init__(self, seed=None):
        self.seed = seed
        self.alive_tiles = []
        self.dead_tiles = []
        self.discards = []
        self.loose_tiles = []
        self.shuffled = False
        self.initialise_wall()
        self.shuffle_wall()
        self.break_wall()

    def _set_seed(self):
        random.seed(self.seed)

    @property
    def is_shuffled(self):
        return self.shuffled

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

    def __str__(self):
        return " ".join([tile.utf8 for tile in chain(self.alive_tiles)])

    def __len__(self):
        return len(self.alive_tiles)

    @abstractmethod
    def initialise_wall(self):
        raise NotImplementedError()

    @abstractmethod
    def break_wall(self):
        raise NotImplementedError()


class ChineseClassicalWall(Wall):
    def __init__(self, seed: int | None = None):
        super().__init__(seed=seed)

    def initialise_wall(self):
        self.alive_tiles = [
            Tile(tile)
            for tile in chain(
                characters * 4,
                bamboos * 4,
                circles * 4,
                dragons * 4,
                winds * 4,
                flowers,
                seasons,
            )
        ]
        self.dead_tiles = []
        self.shuffled = False

    def break_wall(self):
        self.dead_tiles = self.alive_tiles[:16]
        self.alive_tiles = self.alive_tiles[16:]
        self.loose_tiles = [self.dead_tiles.pop(), self.dead_tiles.pop()]
