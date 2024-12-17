from src.models.wind import Wind


def test_creating_east_wind():
    assert Wind.EAST.value == 1


def test_creating_south_wind():
    assert Wind.SOUTH.value == 2


def test_creating_west_wind():
    assert Wind.WEST.value == 3


def test_creating_north_wind():
    assert Wind.NORTH.value == 4


def test_east_next_wind_returns_south():
    assert Wind.EAST.next() == Wind.SOUTH


def test_south_next_wind_returns_west():
    assert Wind.SOUTH.next() == Wind.WEST


def test_west_next_wind_returns_north():
    assert Wind.WEST.next() == Wind.NORTH


def test_north_next_wind_returns_east():
    assert Wind.NORTH.next() == Wind.EAST


def test_east_previous_wind_returns_north():
    assert Wind.EAST.previous() == Wind.NORTH


def test_south_previous_wind_returns_east():
    assert Wind.SOUTH.previous() == Wind.EAST


def test_west_previous_wind_returns_south():
    assert Wind.WEST.previous() == Wind.SOUTH


def test_north_previous_wind_returns_west():
    assert Wind.NORTH.previous() == Wind.WEST
