def assign_seats(players, seats):
    return {seat: player for seat, player in zip(seats, players)}


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


def build_wall():
    Wall(shuffle_wall=config["shuffle_wall"])


def set_seed():
    random.seed(self.random_seed)


def create_players():
    self.players = [Player(number) for number in range(1, config["players"] + 1)]


def setup_new_game():
    create_players()
    assign_seats()
    setup_new_hand()


def setup_new_hand(game):
    set_seed()
    build_wall()
    deal()
    game.increment_hand_counter()
    game.reset_turn_to_east()
