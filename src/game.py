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

from .models.tile import (
    bamboos,
    characters,
    circles,
    dragons,
    flowers,
    seasons,
    winds,
)
from .models.wind import Wind

logger.remove()  # Turn off default console logger
logger.add("mahjong.log", colorize=True, level="INFO")

NUM_OF_TILES_SUIT = 4
NUM_OF_TILES_HONOUR = 4
SIZE_OF_DEAD_WALL = 16


def state_mutated(func):
    @wraps(func)
    def inner(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        hand = self.current_state["hand"]
        self.create_delta(
            self.deltas[hand],
            self.deltas[hand][-1],
            self.current_state,
        )
        return result

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
                    "hand": {
                        "tiles": [],
                        "one_chance_hand": False,
                        "can_go_out": False,
                        "wind_of_the_round": False,
                        "chows": 0,
                        "concealed_pungs": 0,
                        "concealed_kongs": 0,
                        "exposed_pungs": 0,
                        "exposed_kongs": 0,
                        "pairs": 0,
                        "seasons": 0,
                        "flowers": 0,
                    },
                    "score": 2000,
                },
                {
                    "seat": Wind.SOUTH,
                    "name": f"{Faker().word().title()} {Faker().word().title()}",
                    "number": 2,
                    "hand": {
                        "tiles": [],
                        "one_chance_hand": False,
                        "can_go_out": False,
                        "wind_of_the_round": False,
                        "chows": 0,
                        "concealed_pungs": 0,
                        "concealed_kongs": 0,
                        "exposed_pungs": 0,
                        "exposed_kongs": 0,
                        "pairs": 0,
                        "seasons": 0,
                        "flowers": 0,
                    },
                    "score": 2000,
                },
                {
                    "seat": Wind.WEST,
                    "name": f"{Faker().word().title()} {Faker().word().title()}",
                    "number": 3,
                    "hand": {
                        "tiles": [],
                        "one_chance_hand": False,
                        "can_go_out": False,
                        "wind_of_the_round": False,
                        "chows": 0,
                        "concealed_pungs": 0,
                        "concealed_kongs": 0,
                        "exposed_pungs": 0,
                        "exposed_kongs": 0,
                        "pairs": 0,
                        "seasons": 0,
                        "flowers": 0,
                    },
                    "score": 2000,
                },
                {
                    "seat": Wind.NORTH,
                    "name": f"{Faker().word().title()} {Faker().word().title()}",
                    "number": 4,
                    "hand": {
                        "tiles": [],
                        "one_chance_hand": False,
                        "can_go_out": False,
                        "wind_of_the_round": False,
                        "chows": 0,
                        "concealed_pungs": 0,
                        "concealed_kongs": 0,
                        "exposed_pungs": 0,
                        "exposed_kongs": 0,
                        "pairs": 0,
                        "seasons": 0,
                        "flowers": 0,
                    },
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
        delta_list.append(Delta(DeepDiff(old_state, new_state),
                                mutate=True))

    def recreate_game_state(self, deltas):
        state = {}
        for delta in deltas:
            state += delta
        self.current_state = state

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
            self.draw_tile_from_wall(self.current_state["dead_wall"])
            for _ in range(2)
        ]

        logger.info("Wall broken")

    @state_mutated
    def shuffle_seats(self):
        logger.info("Shuffling seats...")
        players = self.current_state["players"]
        _winds = list(Wind)
        shuffle(_winds)
        (
            players[0]["seat"],
            players[1]["seat"],
            players[2]["seat"],
            players[3]["seat"],
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
    def add_tile_to_hand(self, player, tile):
        player.get("hand").get("tiles").append(tile)

    @state_mutated
    def remove_tile_from_hand(self, player, tile):
        player.get("hand").get("tiles").remove(tile)

    @state_mutated
    def add_tile_to_wall(self, wall, tile):
        wall.append(tile)

    @state_mutated
    def draw_tile_from_wall(self, wall):
        return wall.pop()

    @staticmethod
    def hand_as_str(hand):
        return " ".join([t.utf8 for t in hand])

    @state_mutated
    def deal(self):
        logger.info("Dealing tiles...")
        live_wall = self.current_state["live_wall"]
        # Take twelve tiles each
        players_by_wind = sorted(self.current_state["players"], key=lambda p: p.get("seat"))
        for _ in range(3):
            for player in players_by_wind:
                for _ in range(4):
                    tile = self.draw_tile_from_wall(live_wall)
                    self.add_tile_to_hand(player, tile)

        # Each player takes a thirteenth tile
        for player in players_by_wind:
            tile = self.draw_tile_from_wall(live_wall)
            self.add_tile_to_hand(player, tile)

        # East takes a fourteenth tile
        tile = self.draw_tile_from_wall(live_wall)
        self.add_tile_to_hand(self.player_by_wind(Wind.EAST), tile)

        logger.info("Tiles dealt")
