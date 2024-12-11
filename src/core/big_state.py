from dataclasses import dataclass, field
from enum import IntEnum
from itertools import chain
from typing import List

from core.tile import Tile
from data import (
    bamboos,
    characters,
    circles,
    dragons,
    flowers,
    seasons,
    winds,
)


class Wind(IntEnum):
    East = 1
    South = 2
    West = 3
    North = 4

    def __str__(self):
        return self.name

    @property
    def next(self):
        try:
            wind = Wind(self.value + 1)
        except ValueError:
            wind = Wind.East
        return wind

    @property
    def previous(self):
        try:
            wind = Wind(self.value - 1)
        except ValueError:
            wind = Wind.North
        return wind


@dataclass
class Player:
    hand: List[Tile] = field(default_factory=list)
    score: int = 2000


def build_wall():
    return [
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


@dataclass
class Wall:
    tiles: List[Tile] = field(default_factory=lambda: build_wall())

    def __str__(self):
        return "".join([t.utf8 for t in self.tiles])

    def __len__(self):
        return len(self.tiles)


class Game:

    def __init__(self):
        self.starting_score = 2000
        self.hand = 1
        self.round = Wind.East
        self.turn = Wind.East
        self.wind_to_player = {}
        self.player_to_wind = {}
        self.seating_counter = 1
        self.player_1 = Player()
        self.player_2 = Player()
        self.player_3 = Player()
        self.player_4 = Player()
        self.wall = Wall()
