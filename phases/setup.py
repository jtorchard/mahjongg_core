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
