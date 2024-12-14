# from __future__ import annotations
#
# import random
#
#
# class Game:
#     seat_change = {
#         "east": "south",
#         "south": "west",
#         "west": "north",
#         "north": "east",
#     }
#
#     def __init__(self):
#         self.hand = 1
#         self.round = "east"
#         self.seats = {}
#         self.turn = "east"
#         self.in_progress = False
#         self.seat_change_count = 0
#
#     @property
#     def last_hand_played(self):
#         return self.seat_change_count == len(self.players)
#
#     def ai_take_turn(self):
#         player = self.seats[self.turn]
#         player.add_tile(self.wall.take_live_wall())
#         tile = player.remove_tile(random.randint(0, 13))
#         self.wall.add_discard(tile)
#
#     def advance_turn(self):
#         if not self.in_progress:
#             return
#         self.seat_change_count += 1
#         self.turn = self.seat_change[self.turn]
#
#     def change_wind_of_round(self):
#         self.round = self.seat_change[self.round]
#         self.seat_change_count = 0
#
#     def end_hand_mahjong(self):
#         east_out = self.turn == "east"
#         self.score(east_out=east_out)
#         self.settle(east_out=east_out)
#
#         if not east_out:
#             self.advance_turn()
#
#         if self.last_hand_played:
#             self.change_wind_of_round()
#
#         self.new_hand()
#
#     def end_hand_draw(self):
#         self.new_hand()
#
#     def new_hand(self):
#         self.hand += 1
#         self.turn = "east"
#         self.wall = self.build_wall()
#         self.deal()
#
#     def start(self):
#         if self.in_progress:
#             return
#         self.in_progress = True
#         if self.seats["east"].is_ai:
#             self.ai_take_turn()
#
#     def change_seats(self):
#         if not self.in_progress:
#             return
#         self.seats = {
#             new_seat: self.seats[current_seat]
#             for current_seat, new_seat in self.seat_change.items()
#         }
#
#     def get_seats(self):
#         return self.seats
#
#     def draw_tile(self):
#         if not self.in_progress:
#             return
#
#         if not len(self.wall):
#             self.end_hand_draw()
#
#     def discard_tile(self):
#         if not self.in_progress:
#             return
#
#     def claim_discard(self, player):
#         if not self.in_progress or player.lower() == self.turn:
#             return
#
#     def claim_mahjong(self):
#         if not self.in_progress:
#             return
