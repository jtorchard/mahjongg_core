from random import shuffle

from core.player import Player
from core.wall import Wall


class Game:
    seat_change = {
        "east": "south",
        "south": "west",
        "west": "north",
        "north": "east",
    }

    def __init__(self, shuffle_wall=True, randomise_seats=True):
        self.players = [Player(number) for number in range(1, 5)]
        self.hand = 1
        self.round = "east"
        self.seats = {}
        self.turn = "east"
        self.wall = Wall(shuffle_wall=shuffle_wall)
        self.in_progress = False
        self.assign_seats(randomise_seats=randomise_seats)

    def assign_seats(self, randomise_seats=True):
        seats = ["east", "south", "west", "north"]
        if randomise_seats:
            shuffle(seats)
        self.seats = {
            seat: player for seat, player in zip(seats, self.players)
        }

    def start(self):
        self.in_progress = True

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
        self.seats = {new_seat: self.seats[current_seat]
                      for current_seat, new_seat in self.seat_change.items()}

    def get_seats(self):
        return self.seats

    def draw_tile(self):
        pass

    def discard_tile(self):
        pass

    def claim_discard(self, player):
        if player.lower() == self.turn:
            raise ValueError

    def claim_mahjong(self):
        pass
