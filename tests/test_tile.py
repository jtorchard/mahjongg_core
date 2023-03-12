from core.tile import Tile
from core.data import (
    east_wind,
    south_wind,
    west_wind,
    north_wind,
    red_dragon,
    green_dragon,
    white_dragon,
)


def test_east_wind_data_correct(tile=Tile(east_wind)):
    assert tile.utf8 == "🀀"
    assert tile.name == "east_wind"
    assert tile.rank == "east"
    assert tile.suit == "wind"
    assert tile.is_dragon is False
    assert tile.is_wind is True
    assert tile.is_special is False
    assert tile.is_honour is True
    assert tile.is_suit is False
    assert tile.is_terminal is False


def test_south_wind_data_correct(tile=Tile(south_wind)):
    assert tile.utf8 == "🀁"
    assert tile.name == "south_wind"
    assert tile.rank == "south"
    assert tile.suit == "wind"
    assert tile.is_dragon is False
    assert tile.is_wind is True
    assert tile.is_special is False
    assert tile.is_honour is True
    assert tile.is_suit is False
    assert tile.is_terminal is False


def test_west_wind_data_correct(tile=Tile(west_wind)):
    assert tile.utf8 == "🀂"
    assert tile.name == "west_wind"
    assert tile.rank == "west"
    assert tile.suit == "wind"
    assert tile.is_dragon is False
    assert tile.is_wind is True
    assert tile.is_special is False
    assert tile.is_honour is True
    assert tile.is_suit is False
    assert tile.is_terminal is False


def test_north_wind_data_correct(tile=Tile(north_wind)):
    assert tile.utf8 == "🀃"
    assert tile.name == "north_wind"
    assert tile.rank == "north"
    assert tile.suit == "wind"
    assert tile.is_dragon is False
    assert tile.is_wind is True
    assert tile.is_special is False
    assert tile.is_honour is True
    assert tile.is_suit is False
    assert tile.is_terminal is False


def test_red_dragon_data_correct(tile=Tile(red_dragon)):
    assert tile.utf8 == "🀄"
    assert tile.name == "red_dragon"
    assert tile.rank == "red"
    assert tile.suit == "dragon"
    assert tile.is_dragon is True
    assert tile.is_wind is False
    assert tile.is_special is False
    assert tile.is_honour is True
    assert tile.is_suit is False
    assert tile.is_terminal is False


def test_green_dragon_data_correct(tile=Tile(green_dragon)):
    assert tile.utf8 == "🀅"
    assert tile.name == "green_dragon"
    assert tile.rank == "green"
    assert tile.suit == "dragon"
    assert tile.is_dragon is True
    assert tile.is_wind is False
    assert tile.is_special is False
    assert tile.is_honour is True
    assert tile.is_suit is False
    assert tile.is_terminal is False


def test_white_dragon_data_correct(tile=Tile(white_dragon)):
    assert tile.utf8 == "🀆"
    assert tile.name == "white_dragon"
    assert tile.rank == "white"
    assert tile.suit == "dragon"
    assert tile.is_dragon is True
    assert tile.is_wind is False
    assert tile.is_special is False
    assert tile.is_honour is True
    assert tile.is_suit is False
    assert tile.is_terminal is False
