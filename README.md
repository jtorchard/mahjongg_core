Create all game actions as Commands.
Keep full history of commands to allow undoing and also replaying games. Can also be used for saving and loading.
Can also be used for testing, and generating random games, etc.

Add logging
Add docstrings
Add type annotations

Four phases: setup, play, scoring, settling.

mahjong write down all rules, organise.
maybe add all mutable state to one object and just have many small methods to modify it?
lebowski tiles!

Flowers: Plum (East), Orchid (South), Chrysanthemum (West) and Bamboo (North).
Seasons: Spring (East), Summer (South), Autumn (West) and Winter (North).

implement extra draws if drawing a bonus tile

List out all primitive commands or opcodes:
start_game
build_wall
shuffle_wall
deal_tiles
end_game
start_round
end_round
start_hand
end_hand
draw_tile
discard_tile
claim_pung
clam_kong
claim_mahjong
declare_mahjong
declare_kong
assign_seats
change_seats
change_round
change_wind
east_goes_out
draw_bonus_tile
drawn_game

List of special conditions:
out on last tile
out on self-drawn tile
east goes out
drawn game
own wind
wind of the round
all seasons
all flowers

special hands:
