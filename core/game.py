from random import shuffle

from core.player import Player
from core.wall import Wall


class Game:
    seat_change = {
        "East": "South",
        "South": "West",
        "West": "North",
        "North": "East",
    }

    def __init__(self, shuffle_wall=True):
        self.players = [Player(number) for number in range(1, 5)]
        self.hand = 1
        self.round = "East"
        self.seats = {}
        self.turn = "East"
        self.wall = Wall(shuffle_wall=shuffle_wall)
        self.in_progress = False
        self.assign_seats()

    def assign_seats(self, shuffle_seats=True):
        seats = ["East", "South", "West", "North"]
        if shuffle_seats:
            shuffle(seats)
        self.seats = {
            seat: player for seat, player in zip(seats, self.players)
        }

    def start(self):
        self.in_progress = True

    def deal(self):
        pass

    def change_seats(self):
        self.seats = {new_seat: self.seats[current_seat]
                      for current_seat, new_seat in self.seat_change.items()}

    def print_seats(self):
        for k, v in self.seats.items():
            print(f"{k} - {v}")
