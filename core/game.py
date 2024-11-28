import random

from core.player import Player
from core.wall import Wall
from config import config as default_config


class Game:
    seat_change = {
        "east": "south",
        "south": "west",
        "west": "north",
        "north": "east",
    }

    def __init__(self, config=default_config):
        self.ruleset = config["ruleset"]
        self.random_seed = config["random_seed"]
        self.shuffle_wall = config["shuffle_wall"]
        self.randomise_seats = config["randomise_seats"]
        self.number_of_players = config["players"]
        self.starting_score = 2000  # TODO Pull from rules config
        self.hand = 1
        self.round = "east"
        self.seats = {}
        self.turn = "east"
        self.in_progress = False
        self.seat_change_count = 0
        self.players = self.create_players()
        self.wall = self.build_wall()
        self.seats = self.assign_seats()

    def build_wall(self):
        return Wall(seed=self.random_seed, use_flowers=True, use_seasons=True)

    def create_players(self):
        return [
            Player(number, starting_score=self.starting_score)
            for number in range(1, self.number_of_players + 1)
        ]

    @property
    def last_hand_played(self):
        return self.seat_change_count == len(self.players)

    def assign_seats(self):
        seats = ["east", "south", "west", "north"]
        if self.randomise_seats:
            random.shuffle(seats)
        return {seat: player for seat, player in zip(seats, self.players)}

    def ai_take_turn(self):
        player = self.seats[self.turn]
        player.add_tile(self.wall.take_live_wall())
        tile = player.remove_tile(random.randint(0, 13))
        self.wall.add_discard(tile)

    def ai_assess_discards(self):
        pass

    def score(self, east_out):
        pass

    def settle(self, east_out):
        pass

    def advance_turn(self):
        if not self.in_progress:
            return
        self.seat_change_count += 1
        self.turn = self.seat_change[self.turn]

    def change_wind_of_round(self):
        self.round = self.seat_change[self.round]
        self.seat_change_count = 0

    def end_hand_mahjong(self):
        east_out = self.turn == "east"
        self.score(east_out=east_out)
        self.settle(east_out=east_out)

        if not east_out:
            self.advance_turn()

        if self.last_hand_played:
            self.change_wind_of_round()

        self.new_hand()

    def end_hand_draw(self):
        self.new_hand()

    def new_hand(self):
        self.hand += 1
        self.turn = "east"
        self.wall = self.build_wall()
        self.deal()

    def start(self):
        if self.in_progress:
            return
        self.in_progress = True
        if self.seats["east"].is_ai:
            self.ai_take_turn()

    def deal(self):
        # Take twelve tiles each
        for _ in range(3):
            for wind in self.seat_change.keys():
                player = self.seats[wind]
                for _ in range(4):
                    player.add_tile(self.wall.take_live_wall())

        # Each player takes a thirteenth tile
        for wind in self.seat_change.keys():
            player = self.seats[wind]
            player.add_tile(self.wall.take_live_wall())

        # East takes a fourteenth tile
        self.seats["east"].add_tile(self.wall.take_live_wall())

    def change_seats(self):
        if not self.in_progress:
            return
        self.seats = {
            new_seat: self.seats[current_seat]
            for current_seat, new_seat in self.seat_change.items()
        }

    def get_seats(self):
        return self.seats

    def draw_tile(self):
        if not self.in_progress:
            return

        if not len(self.wall):
            self.end_hand_draw()

    def discard_tile(self):
        if not self.in_progress:
            return

    def claim_discard(self, player):
        if not self.in_progress or player.lower() == self.turn:
            return

    def claim_mahjong(self):
        if not self.in_progress:
            return
