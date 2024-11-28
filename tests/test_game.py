from copy import deepcopy

import pytest

from core.game import Game
from config import config as default_config


@pytest.fixture
def game_default():
    return Game(config=default_config)


@pytest.fixture
def game_fixed_seats():
    config = deepcopy(default_config)
    config["randomise_seats"] = False
    return Game(config=config)


def test_in_progress_is_false_by_default(game_default):
    assert game_default.in_progress is False


def test_hand_is_1_by_default(game_default):
    assert game_default.hand == 1


def test_round_is_east_by_default(game_default):
    assert game_default.round == "east"


def test_turn_is_east_by_default(game_default):
    assert game_default.turn == "east"


def test_players_list_has_four_entries(game_default):
    assert len(game_default.players) == 4


def test_wall_is_initialised(game_default):
    tile_count = len(game_default.wall.alive_tiles + game_default.wall.dead_tiles + game_default.wall.loose_tiles)
    assert tile_count == game_default.total_tiles


def test_assign_seats_creates_seat_assignments(game_default):
    game_default.seats = []
    assert game_default.seats == []
    game_default.seats = game_default.assign_seats()
    assert game_default.seats


def test_start_marks_game_as_in_progress(game_default):
    game_default.start()
    assert game_default.in_progress is True


def test_deal_gives_players_correct_tiles(game_default):
    game_default.deal()
    assert len(game_default.seats["east"].hand) == 14
    assert len(game_default.seats["south"].hand) == 13
    assert len(game_default.seats["west"].hand) == 13
    assert len(game_default.seats["north"].hand) == 13


def test_seats_are_correct_when_not_randomised(game_fixed_seats):
    assert str(game_fixed_seats.seats["east"]) == "player_1"
    assert str(game_fixed_seats.seats["south"]) == "player_2"
    assert str(game_fixed_seats.seats["west"]) == "player_3"
    assert str(game_fixed_seats.seats["north"]) == "player_4"


# noinspection DuplicatedCode
def test_change_seats_does_nothing_if_game_not_started(game_fixed_seats):
    game_fixed_seats.change_seats()
    assert str(game_fixed_seats.seats["east"]) == "player_1"
    assert str(game_fixed_seats.seats["south"]) == "player_2"
    assert str(game_fixed_seats.seats["west"]) == "player_3"
    assert str(game_fixed_seats.seats["north"]) == "player_4"


# noinspection DuplicatedCode
def test_change_seats_moves_to_correct_seats(game_fixed_seats):
    game_fixed_seats.start()
    game_fixed_seats.change_seats()
    assert str(game_fixed_seats.seats["east"]) == "player_4"
    assert str(game_fixed_seats.seats["south"]) == "player_1"
    assert str(game_fixed_seats.seats["west"]) == "player_2"
    assert str(game_fixed_seats.seats["north"]) == "player_3"
    game_fixed_seats.change_seats()
    assert str(game_fixed_seats.seats["east"]) == "player_3"
    assert str(game_fixed_seats.seats["south"]) == "player_4"
    assert str(game_fixed_seats.seats["west"]) == "player_1"
    assert str(game_fixed_seats.seats["north"]) == "player_2"
    game_fixed_seats.change_seats()
    assert str(game_fixed_seats.seats["east"]) == "player_2"
    assert str(game_fixed_seats.seats["south"]) == "player_3"
    assert str(game_fixed_seats.seats["west"]) == "player_4"
    assert str(game_fixed_seats.seats["north"]) == "player_1"
    game_fixed_seats.change_seats()
    assert str(game_fixed_seats.seats["east"]) == "player_1"
    assert str(game_fixed_seats.seats["south"]) == "player_2"
    assert str(game_fixed_seats.seats["west"]) == "player_3"
    assert str(game_fixed_seats.seats["north"]) == "player_4"


def test_loading_ruleset(game_default):
    game_default._load_ruleset()
    assert game_default.ruleset


@pytest.mark.parametrize("number", (n for n in range(0, 4)))
def test_loading_ruleset_uses_correct_starting_score(game_default, number):
    assert game_default.ruleset["setup"]["players"]["starting_score"] == game_default.players[number].score
