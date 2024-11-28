import pytest

from src.core.data import east_wind
from src.core.tile import Tile
from src.core.wall import Wall


@pytest.fixture
def shuffled_wall():
    return Wall(seed=None)


@pytest.fixture
def deterministic_wall():
    return Wall(seed=0)


def test_wall_has_correct_number_of_tiles(shuffled_wall):
    assert len(shuffled_wall.alive_tiles + shuffled_wall.dead_tiles + shuffled_wall.loose_tiles) == 144


def test_wall_is_shuffled(shuffled_wall):
    assert shuffled_wall.is_shuffled is True


def test_wall_is_not_shuffled(deterministic_wall):
    assert deterministic_wall.is_shuffled is False


def test_dead_wall_is_16_tiles(shuffled_wall):
    assert len(shuffled_wall.dead_tiles) == 14


def test_alive_wall_is_152_tiles_after_break(shuffled_wall):
    assert len(shuffled_wall.alive_tiles) == (144 - 16)


def test_alive_wall_is_151_tiles_after_taking(shuffled_wall):
    shuffled_wall.take_live_wall()
    assert len(shuffled_wall.alive_tiles) == 127


def test_dead_wall_is_15_tiles_after_taking(shuffled_wall):
    shuffled_wall.take_dead_wall()
    assert len(shuffled_wall.dead_tiles) == 13


def test_2_loose_tiles(shuffled_wall):
    assert len(shuffled_wall.loose_tiles) == 2


def test_wall_has_tile_after_adding_discard(shuffled_wall):
    shuffled_wall.add_discard(Tile(east_wind))
    assert shuffled_wall.discards == [Tile(east_wind)]
