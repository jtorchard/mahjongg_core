import random
from itertools import chain
from random import shuffle
from typing import List, Optional

from models.player import Player
from models.tile import (
    Tile,
    bamboos,
    characters,
    circles,
    dragons,
    flowers,
    seasons,
    winds,
)
from models.wind import Wind


class Game:
    def __init__(self, seed: Optional[int] = None):
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
        self.players = (self.player_1, self.player_2, self.player_3, self.player_4)

        random.seed(self.seed)
        self.build_wall()
        shuffle(self.live_wall)
        self.break_wall()
        self.shuffle_seats()

    def build_wall(self) -> None:
        self.live_wall = [
            tile()
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

    def break_wall(self) -> None:
        self.dead_wall: List[Tile] = self.live_wall[:16]
        self.live_wall: List[Tile] = self.live_wall[16:]
        self.loose_tiles: List[Tile] = [self.dead_wall.pop(), self.dead_wall.pop()]

    def shuffle_seats(self):
        _winds = list(Wind)
        shuffle(_winds)
        (
            self.player_1.seat,
            self.player_2.seat,
            self.player_3.seat,
            self.player_4.seat,
        ) = _winds

    def change_seats(self):
        for player in self.players:
            player.seat = player.seat.next()

    def deal(self):
        # Take twelve tiles each
        players_by_wind = sorted(self.players, key=lambda p: p.seat)
        for _ in range(3):
            for player in players_by_wind:
                for _ in range(4):
                    player.hand.append(self.live_wall.pop())

        # Each player takes a thirteenth tile
        for player in players_by_wind:
            player.hand.append(self.live_wall.pop())

        # East takes a fourteenth tile
        players_by_wind[0].hand.append(self.live_wall.pop())


def main():
    game = Game(seed=None)
    random.seed(game.seed)
    game.build_wall()
    shuffle(game.live_wall)
    game.break_wall()
    game.shuffle_seats()

    print(f"Game: {game}")
    print(f"live wall: {game.live_wall}")
    print(f"dead wall: {game.dead_wall}")
    print(f"loose tiles: {game.loose_tiles}")
    players = sorted(
        [game.player_1, game.player_2, game.player_3, game.player_4],
        key=lambda p: p.seat,
    )
    print(f"Players: {players}")


if __name__ == "__main__":
    main()
