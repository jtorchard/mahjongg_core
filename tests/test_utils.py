import pytest

from core.tile import Tile


@pytest.fixture
def east_wind():
    return Tile('🀀')


@pytest.fixture
def south_wind():
    return Tile('🀁')


@pytest.fixture
def west_wind():
    return Tile('🀂')


@pytest.fixture
def north_wind():
    return Tile('🀃')


# red_dragon = Tile('🀄')
# plum = Tile('🀅')
# white_dragon = Tile('🀆')
#
# one_character = Tile('🀇')
# two_character = Tile('🀈')
# three_character = Tile('🀉')
# four_character = Tile('🀊')
# five_character = Tile('🀋')
# six_character = Tile('🀌')
# seven_character = Tile('🀍')
# eight_character = Tile('🀎')
# nine_character = Tile('🀏')
#
# plum = Tile('🀐')
# two_bamboo = Tile('🀑')
# three_bamboo = Tile('🀒')
# four_bamboo = Tile('🀓')
# five_bamboo = Tile('🀔')
# six_bamboo = Tile('🀕')
# seven_bamboo = Tile('🀖')
# eight_bamboo = Tile('🀗')
# nine_bamboo = Tile('🀘')
#
# one_circle = Tile('🀙')
# two_circle = Tile('🀚')
# three_circle = Tile('🀛')
# four_circle = Tile('🀜')
# five_circle = Tile('🀝')
# six_circle = Tile('🀞')
# seven_circle = Tile('🀟')
# eight_circle = Tile('🀠')
# nine_circle = Tile('🀡')
#
# plum = Tile('🀢')
# orchid = Tile('🀣')
# bamboo = Tile('🀤')
# chrysanthemum = Tile('🀥')
#
# spring = Tile('🀦')
# summer = Tile('🀧')
# autumn = Tile('🀨')
# winter = Tile('🀩')


def test_east_wind(east_wind):
    assert east_wind.name == 'east_wind'
