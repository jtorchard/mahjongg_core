"""
    Tests Game class.
"""

import pytest

from src.game import Game
from src.models.tile import EastWind
from src.models.wind import Wind


@pytest.fixture
def game_random_seed():
    return Game(seed=None)


@pytest.fixture
def game_fixed_seed():
    return Game(seed=69)


def test_adding_discard(game_random_seed):
    game_random_seed.discards.append(EastWind())
    assert game_random_seed.discards == [EastWind()]


def test_hand_is_1_by_default(game_random_seed):
    assert game_random_seed.hand == 1


def test_round_is_east_by_default(game_random_seed):
    assert game_random_seed.round == Wind.EAST


def test_turn_is_east_by_default(game_random_seed):
    assert game_random_seed.turn == Wind.EAST


def test_players_list_has_four_entries(game_random_seed):
    assert len(game_random_seed.players) == 4


def test_wall_is_initialised(game_random_seed):
    tile_count = len(
        game_random_seed.live_wall
        + game_random_seed.dead_wall
        + game_random_seed.loose_tiles
    )
    assert tile_count == 144


def test_correct_seats_with_fixed_seed(game_fixed_seed):
    game_fixed_seed.player_1.seat = Wind.EAST
    game_fixed_seed.player_2.seat = Wind.SOUTH
    game_fixed_seed.player_3.seat = Wind.WEST
    game_fixed_seed.player_4.seat = Wind.NORTH

    assert game_fixed_seed.player_1.seat == Wind.EAST
    assert game_fixed_seed.player_2.seat == Wind.SOUTH
    assert game_fixed_seed.player_3.seat == Wind.WEST
    assert game_fixed_seed.player_4.seat == Wind.NORTH

    game_fixed_seed.shuffle_seats()

    assert game_fixed_seed.player_1.seat == Wind.SOUTH
    assert game_fixed_seed.player_2.seat == Wind.WEST
    assert game_fixed_seed.player_3.seat == Wind.EAST
    assert game_fixed_seed.player_4.seat == Wind.NORTH


def test_deal_gives_players_correct_tiles(game_random_seed):
    game_random_seed.deal()
    for player in game_random_seed.players:
        number_of_tiles = len(player.hand)
        if player.seat == Wind.EAST:
            assert number_of_tiles == 14
        else:
            assert number_of_tiles == 13


# noinspection DuplicatedCode
def test_change_seats_moves_to_correct_seats(game_fixed_seed):
    game_fixed_seed.change_seats()
    assert game_fixed_seed.player_4.seat == Wind.EAST
    assert game_fixed_seed.player_1.seat == Wind.SOUTH
    assert game_fixed_seed.player_2.seat == Wind.WEST
    assert game_fixed_seed.player_3.seat == Wind.NORTH
    game_fixed_seed.change_seats()
    assert game_fixed_seed.player_3.seat == Wind.EAST
    assert game_fixed_seed.player_4.seat == Wind.SOUTH
    assert game_fixed_seed.player_1.seat == Wind.WEST
    assert game_fixed_seed.player_2.seat == Wind.NORTH
    game_fixed_seed.change_seats()
    assert game_fixed_seed.player_2.seat == Wind.EAST
    assert game_fixed_seed.player_3.seat == Wind.SOUTH
    assert game_fixed_seed.player_4.seat == Wind.WEST
    assert game_fixed_seed.player_1.seat == Wind.NORTH
    game_fixed_seed.change_seats()
    assert game_fixed_seed.player_1.seat == Wind.EAST
    assert game_fixed_seed.player_2.seat == Wind.SOUTH
    assert game_fixed_seed.player_3.seat == Wind.WEST
    assert game_fixed_seed.player_4.seat == Wind.NORTH


def test_wall_has_correct_number_of_tiles(game_fixed_seed):
    assert len(game_fixed_seed.live_wall) == 128


def test_dead_wall_is_16_tiles(game_fixed_seed):
    assert len(game_fixed_seed.dead_wall) == 14


def test_alive_wall_is_152_tiles_after_break(game_fixed_seed):
    assert len(game_fixed_seed.live_wall) == (144 - 16)


def test_alive_wall_is_151_tiles_after_taking(game_fixed_seed):
    game_fixed_seed.live_wall.pop()
    assert len(game_fixed_seed.live_wall) == 127


def test_dead_wall_is_15_tiles_after_taking(game_fixed_seed):
    game_fixed_seed.dead_wall.pop()
    assert len(game_fixed_seed.dead_wall) == 13


def test_2_loose_tiles(game_fixed_seed):
    assert len(game_fixed_seed.loose_tiles) == 2
