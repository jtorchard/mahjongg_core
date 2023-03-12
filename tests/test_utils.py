from core.tile import Tile
from core.data import east_wind, south_wind, west_wind, north_wind


def test_east_wind_data_correct(tile=Tile(east_wind)):
    assert tile.utf8 == '🀀'
    assert tile.name == 'east_wind'
    assert tile.rank == 'east'
    assert tile.suit == 'wind'
    assert tile.is_dragon is False
    assert tile.is_wind is True
    assert tile.is_special is False
    assert tile.is_honour is True
    assert tile.is_suit is False
    assert tile.is_terminal is False


def test_south_wind_data_correct(tile=Tile(south_wind)):
    assert tile.utf8 == '🀁'
    assert tile.name == 'south_wind'
    assert tile.rank == 'south'
    assert tile.suit == 'wind'
    assert tile.is_dragon is False
    assert tile.is_wind is True
    assert tile.is_special is False
    assert tile.is_honour is True
    assert tile.is_suit is False
    assert tile.is_terminal is False


def test_west_wind_data_correct(tile=Tile(west_wind)):
    assert tile.utf8 == '🀂'
    assert tile.name == 'west_wind'
    assert tile.rank == 'west'
    assert tile.suit == 'wind'
    assert tile.is_dragon is False
    assert tile.is_wind is True
    assert tile.is_special is False
    assert tile.is_honour is True
    assert tile.is_suit is False
    assert tile.is_terminal is False


def test_north_wind_data_correct(tile=Tile(north_wind)):
    assert tile.utf8 == '🀃'
    assert tile.name == 'north_wind'
    assert tile.rank == 'north'
    assert tile.suit == 'wind'
    assert tile.is_dragon is False
    assert tile.is_wind is True
    assert tile.is_special is False
    assert tile.is_honour is True
    assert tile.is_suit is False
    assert tile.is_terminal is False
