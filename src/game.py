import random
from itertools import chain
from random import shuffle

from loguru import logger

from src.models.player import Player
from src.models.tile import (
    bamboos,
    characters,
    circles,
    dragons,
    flowers,
    seasons,
    winds,
)
from src.models.wind import Wind

logger.remove()  # Turn off default console logger
logger.add("mahjong.log", colorize=True, level="INFO")

NUM_OF_TILES_SUIT = 4
NUM_OF_TILES_HONOUR = 4
SIZE_OF_DEAD_WALL = 16


class Game:
    def __init__(self, seed=None):
        logger.info(f"Initialising game with seed: {seed}")
        self.seed = seed
        self.hand = 1
        self.seating_counter = 1
        self.east_out_counter = 0
        self.round = Wind.EAST
        self.turn = Wind.EAST
        self.player_1 = Player(seat=Wind.EAST, number=1)
        self.player_2 = Player(seat=Wind.SOUTH, number=2)
        self.player_3 = Player(seat=Wind.WEST, number=3)
        self.player_4 = Player(seat=Wind.NORTH, number=4)
        self.live_wall = []
        self.dead_wall = []
        self.discards = []
        self.loose_tiles = []
        self.players = (self.player_1, self.player_2, self.player_3, self.player_4)

        random.seed(self.seed)
        self.build_wall()
        shuffle(self.live_wall)
        self.break_wall()
        self.shuffle_seats()

    def player_by_wind(self, wind):
        return {p.seat: p for p in self.players}[wind]

    def build_wall(self):
        logger.info("Building wall...")
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
        logger.info(f"Wall built with {len(self.live_wall)} tiles")

    def break_wall(self):
        logger.info("Breaking wall...")
        self.dead_wall = self.live_wall[:SIZE_OF_DEAD_WALL]
        self.live_wall = self.live_wall[SIZE_OF_DEAD_WALL:]
        self.loose_tiles = [self.dead_wall.pop(), self.dead_wall.pop()]
        logger.info("Wall broken")

    def shuffle_seats(self):
        logger.info("Shuffling seats...")
        _winds = list(Wind)
        shuffle(_winds)
        self.player_1.seat, self.player_2.seat, self.player_3.seat, self.player_4.seat, = _winds
        logger.info("Seats shuffled")

    def change_seats(self):
        player_seats = {p.number: p.seat for p in self.players}
        logger.info("Changing seats...")

        for player in self.players:
            player.seat = player.seat.next()

        for p in self.players:
            logger.info(f"Seat changed for Player {p.number}: {player_seats[p.number]} -> {p.seat}")

    def deal(self):
        logger.info("Dealing tiles...")
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
        self.player_by_wind(Wind.EAST).hand.append(self.live_wall.pop())
        logger.info("Tiles dealt")
