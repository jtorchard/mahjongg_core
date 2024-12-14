import random
from itertools import chain
from random import shuffle
from typing import List, Optional, Sequence

from loguru import logger

from src.models.player import Player
from src.models.tile import (
    Tile,
    bamboos,
    characters,
    circles,
    dragons,
    flowers,
    seasons,
    winds,
)
from src.models.wind import Wind

logger.add("mahjong.log")

NUM_OF_TILES_SUIT: int = 4
NUM_OF_TILES_HONOUR: int = 4
SIZE_OF_DEAD_WALL: int = 16


class Game:
    def __init__(self, seed: Optional[int] = None):
        logger.debug(f"Initialising game with seed: {seed}")
        self.seed: Optional[int] = seed
        self.hand: int = 1
        self.seating_counter: int = 1
        self.east_out_counter: int = 0
        self.round: Wind = Wind.EAST
        self.turn: Wind = Wind.EAST
        self.player_1: Player = Player(seat=Wind.EAST, number=1)
        self.player_2: Player = Player(seat=Wind.SOUTH, number=2)
        self.player_3: Player = Player(seat=Wind.WEST, number=3)
        self.player_4: Player = Player(seat=Wind.NORTH, number=4)
        self.live_wall: List[Tile] = []
        self.dead_wall: List[Tile] = []
        self.discards: List[Tile] = []
        self.loose_tiles: List[Tile] = []
        self.players: Sequence[Player] = (self.player_1, self.player_2, self.player_3, self.player_4)

        random.seed(self.seed)
        self.build_wall()
        shuffle(self.live_wall)
        self.break_wall()
        self.shuffle_seats()

    def player_by_wind(self, wind: Wind) -> Player:
        return {p.seat: p for p in self.players}[wind]

    def build_wall(self) -> None:
        logger.debug("Building wall...")
        self.live_wall = [
            tile()
            for tile in chain(
                characters * NUM_OF_TILES_SUIT,
                bamboos * NUM_OF_TILES_SUIT,
                circles * NUM_OF_TILES_SUIT,
                dragons * NUM_OF_TILES_HONOUR,
                winds * NUM_OF_TILES_HONOUR,
                flowers,
                seasons,
            )
        ]
        logger.debug(f"Wall built with {len(self.live_wall)} tiles")

    def break_wall(self) -> None:
        self.dead_wall = self.live_wall[:SIZE_OF_DEAD_WALL]
        self.live_wall = self.live_wall[SIZE_OF_DEAD_WALL:]
        self.loose_tiles = [self.dead_wall.pop(), self.dead_wall.pop()]

    def shuffle_seats(self) -> None:
        _winds = list(Wind)
        shuffle(_winds)
        self.player_1.seat, self.player_2.seat, self.player_3.seat, self.player_4.seat, = _winds

    def change_seats(self) -> None:
        for player in self.players:
            player.seat = player.seat.next()

    def deal(self) -> None:
        # Take twelve tiles each
        players_by_wind: List[Player] = sorted(self.players, key=lambda p: p.seat)
        for _ in range(3):
            for player in players_by_wind:
                for _ in range(4):
                    player.hand.append(self.live_wall.pop())

        # Each player takes a thirteenth tile
        for player in players_by_wind:
            player.hand.append(self.live_wall.pop())

        # East takes a fourteenth tile
        self.player_by_wind(Wind.EAST).hand.append(self.live_wall.pop())
