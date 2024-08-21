from core.player import Player
from core.wall import Wall


class Game:

    def __init__(self, shuffle_wall=True):
        self.players = [Player(number) for number in range(1, 5)]
        self.wind = "East"
        self.round = None
        self.seats = None
        self.turn = None
        self.wall = Wall(shuffle_wall=shuffle_wall)

    def start(self):
        pass

    def deal(self):
        pass
