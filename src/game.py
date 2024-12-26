"""
    Game class holds all current_state for a game.
"""

import random
from collections import defaultdict
from functools import wraps
from itertools import chain
from random import shuffle

from deepdiff import DeepDiff, Delta
from faker import Faker
from loguru import logger

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


def state_mutated(func):
    @wraps(func)
    def inner(self, *args, **kwargs):
        func(self, *args, **kwargs)
        self.create_delta(
            self.deltas[self.current_state["hand"]],
            self.deltas[self.current_state["hand"]][-1],
            self.current_state,
        )

    return inner


class Game:
    def __init__(self, seed=None):
        self.deltas = defaultdict(list)
        self.current_state = {
            "seed": seed,
            "hand": 1,
            "seating_counter": 1,
            "east_out_counter": 0,
            "round": Wind.EAST,
            "turn": Wind.EAST,
            "players": [
                {
                    "seat": Wind.EAST,
                    "name": f"{Faker().word().title()} {Faker().word().title()}",
                    "number": 1,
                    "hand": [],
                    "score": 2000,
                },
                {
                    "seat": Wind.SOUTH,
                    "name": f"{Faker().word().title()} {Faker().word().title()}",
                    "number": 2,
                    "hand": [],
                    "score": 2000,
                },
                {
                    "seat": Wind.WEST,
                    "name": f"{Faker().word().title()} {Faker().word().title()}",
                    "number": 3,
                    "hand": [],
                    "score": 2000,
                },
                {
                    "seat": Wind.NORTH,
                    "name": f"{Faker().word().title()} {Faker().word().title()}",
                    "number": 4,
                    "hand": [],
                    "score": 2000,
                },
            ],
            "live_wall": [],
            "dead_wall": [],
            "discards": [],
            "loose_tiles": [],
        }
        logger.info("Saving initial state delta...")
        self.create_delta(
            self.deltas[self.current_state["hand"]],
            {}, self.current_state,
        )

        logger.info(f"Initialising game with seed: {seed}")
        random.seed(self.current_state["seed"])
        self.build_wall()
        self.shuffle_wall()
        self.break_wall()
        self.shuffle_seats()

    @staticmethod
    def create_delta(delta_list, old_state, new_state):
        delta_list.append(Delta(DeepDiff(old_state, new_state)))

    @staticmethod
    def recreate_current_state(deltas):
        state = {}
        for delta in deltas:
            state += delta
        return state

    def player_by_wind(self, wind):
        return {p.get("seat"): p for p in self.current_state["players"]}[wind]

    @state_mutated
    def shuffle_wall(self):
        shuffle(self.current_state["live_wall"])

    @state_mutated
    def build_wall(self):
        logger.info("Building wall...")
        self.current_state["live_wall"] = [
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
        logger.info(f"Wall built with {len(self.current_state["live_wall"])} tiles")

    @state_mutated
    def break_wall(self):
        logger.info("Breaking wall...")
        self.current_state["dead_wall"] = self.current_state["live_wall"][:SIZE_OF_DEAD_WALL]
        self.current_state["live_wall"] = self.current_state["live_wall"][SIZE_OF_DEAD_WALL:]
        self.current_state["loose_tiles"] = [
            self.current_state["dead_wall"].pop(),
            self.current_state["dead_wall"].pop(),
        ]

        logger.info("Wall broken")

    @state_mutated
    def shuffle_seats(self):
        logger.info("Shuffling seats...")
        _winds = list(Wind)
        shuffle(_winds)
        (
            self.current_state["players"][0]["seat"],
            self.current_state["players"][1]["seat"],
            self.current_state["players"][2]["seat"],
            self.current_state["players"][3]["seat"],
        ) = _winds
        logger.info("Seats shuffled")

    @state_mutated
    def change_seats(self):
        player_seats = {p.get("number"): p.get("seat") for p in self.current_state["players"]}
        logger.info("Changing seats...")

        for player in self.current_state["players"]:
            player["seat"] = player.get("seat").next()

        for p in self.current_state["players"]:
            logger.info(
                f"Seat changed for Player {p.get("number")}: {player_seats[p.get("number")]} -> {p.get("seat")}"
            )

    @state_mutated
    def deal(self):
        logger.info("Dealing tiles...")
        # Take twelve tiles each
        players_by_wind = sorted(self.current_state["players"], key=lambda p: p.get("seat"))
        for _ in range(3):
            for player in players_by_wind:
                for _ in range(4):
                    player.get("hand").append(self.current_state["live_wall"].pop())

        # Each player takes a thirteenth tile
        for player in players_by_wind:
            player.get("hand").append(self.current_state["live_wall"].pop())

        # East takes a fourteenth tile
        self.player_by_wind(Wind.EAST).get("hand").append(self.current_state["live_wall"].pop())

        logger.info("Tiles dealt")
