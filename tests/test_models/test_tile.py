import pytest

from src.models.tile import (
    AutumnSeason,
    BambooFlower,
    ChrysanthemumFlower,
    EastWind,
    EightBamboo,
    EightCharacter,
    EightCircle,
    FiveBamboo,
    FiveCharacter,
    FiveCircle,
    FourBamboo,
    FourCharacter,
    FourCircle,
    GreenDragon,
    NineBamboo,
    NineCharacter,
    NineCircle,
    NorthWind,
    OneBamboo,
    OneCharacter,
    OneCircle,
    OrchidFlower,
    PlumFlower,
    RedDragon,
    SevenBamboo,
    SevenCharacter,
    SevenCircle,
    SixBamboo,
    SixCharacter,
    SixCircle,
    SouthWind,
    SpringSeason,
    SummerSeason,
    ThreeBamboo,
    ThreeCharacter,
    ThreeCircle,
    Tile,
    TwoBamboo,
    TwoCharacter,
    TwoCircle,
    WestWind,
    WhiteDragon,
    WinterSeason,
    tiles,
)


@pytest.mark.parametrize("tile", tiles)
def test_tiles_compared_to_non_tiles_are_not_equal(tile):
    with pytest.raises(ValueError):
        assert tile() != 3


@pytest.mark.parametrize("tile", tiles)
def test_tiles_are_instance_of_tile(tile):
    assert isinstance(tile(), Tile)


@pytest.mark.parametrize("tile", tiles)
def test_two_identical_tiles_compare_equal(tile):
    assert tile() == tile()


@pytest.mark.parametrize(
    "tile_a, tile_b", ((tiles.pop(), tiles.pop()) for _ in range(len(tiles) // 2))
)
def test_two_different_tiles_compare_unequal_all(tile_a, tile_b):
    assert tile_a != tile_b


def test_two_character_gt_one_character():
    assert TwoCharacter() > OneCharacter()


def test_eight_character_lt_nine_character():
    assert EightCharacter() < NineCharacter()


def test_string_representation():
    assert str(SixBamboo()) == "six_bamboo -- 🀕"


def test_repr_representation():
    assert repr(SixBamboo()) == "six_bamboo -- 🀕"


def test_extract_name_from_unicode_dragon_is_correct(tile=RedDragon()):
    assert tile.name == "red_dragon"


def test_extract_name_from_unicode_wind_is_correct(tile=EastWind()):
    assert tile.name == "east_wind"


def test_extract_name_from_unicode_character_terminal_is_correct(tile=NineCharacter()):
    assert tile.name == "nine_character"


def test_extract_name_from_unicode_character_simple_is_correct(tile=SixCharacter()):
    assert tile.name == "six_character"


def test_extract_name_from_unicode_bamboo_terminal_is_correct(tile=NineBamboo()):
    assert tile.name == "nine_bamboo"


def test_extract_name_from_unicode_bamboo_simple_is_correct(tile=SixBamboo()):
    assert tile.name == "six_bamboo"


def test_extract_name_from_unicode_circle_terminal_is_correct(tile=NineCircle()):
    assert tile.name == "nine_circle"


def test_extract_name_from_unicode_circle_simple_is_correct(tile=SixCircle()):
    assert tile.name == "six_circle"


def test_extract_name_from_unicode_plum_flower_is_correct(tile=PlumFlower()):
    assert tile.name == "plum_flower"


def test_extract_name_from_unicode_autumn_season_is_correct(tile=AutumnSeason()):
    assert tile.name == "autumn_season"


def test_east_wind_data_correct(tile=EastWind()):
    assert tile.utf8 == "🀀"
    assert tile.name == "east_wind"
    assert tile.rank == "east"
    assert tile.suit == "wind"
    assert tile.value == 1

    assert tile.is_suit is False
    assert tile.is_simple is False
    assert tile.is_terminal is False

    assert tile.is_honour is True
    assert tile.is_dragon is False
    assert tile.is_wind is True

    assert tile.is_special is False
    assert tile.is_flower is False
    assert tile.is_season is False


def test_south_wind_data_correct(tile=SouthWind()):
    assert tile.utf8 == "🀁"
    assert tile.name == "south_wind"
    assert tile.rank == "south"
    assert tile.suit == "wind"
    assert tile.value == 2

    assert tile.is_suit is False
    assert tile.is_simple is False
    assert tile.is_terminal is False

    assert tile.is_honour is True
    assert tile.is_dragon is False
    assert tile.is_wind is True

    assert tile.is_special is False
    assert tile.is_flower is False
    assert tile.is_season is False


def test_west_wind_data_correct(tile=WestWind()):
    assert tile.utf8 == "🀂"
    assert tile.name == "west_wind"
    assert tile.rank == "west"
    assert tile.suit == "wind"
    assert tile.value == 3

    assert tile.is_simple is False
    assert tile.is_suit is False
    assert tile.is_terminal is False

    assert tile.is_honour is True
    assert tile.is_dragon is False
    assert tile.is_wind is True

    assert tile.is_special is False
    assert tile.is_flower is False
    assert tile.is_season is False


def test_north_wind_data_correct(tile=NorthWind()):
    assert tile.utf8 == "🀃"
    assert tile.name == "north_wind"
    assert tile.rank == "north"
    assert tile.suit == "wind"
    assert tile.value == 4

    assert tile.is_suit is False
    assert tile.is_simple is False
    assert tile.is_terminal is False

    assert tile.is_honour is True
    assert tile.is_dragon is False
    assert tile.is_wind is True

    assert tile.is_special is False
    assert tile.is_flower is False
    assert tile.is_season is False


def test_red_dragon_data_correct(tile=RedDragon()):
    assert tile.utf8 == "🀄"
    assert tile.name == "red_dragon"
    assert tile.rank == "red"
    assert tile.suit == "dragon"
    assert tile.value == 1

    assert tile.is_suit is False
    assert tile.is_simple is False
    assert tile.is_terminal is False

    assert tile.is_honour is True
    assert tile.is_dragon is True
    assert tile.is_wind is False

    assert tile.is_special is False
    assert tile.is_flower is False
    assert tile.is_season is False


def test_green_dragon_data_correct(tile=GreenDragon()):
    assert tile.utf8 == "🀅"
    assert tile.name == "green_dragon"
    assert tile.rank == "green"
    assert tile.suit == "dragon"
    assert tile.value == 2

    assert tile.is_suit is False
    assert tile.is_simple is False
    assert tile.is_terminal is False

    assert tile.is_honour is True
    assert tile.is_dragon is True
    assert tile.is_wind is False

    assert tile.is_special is False
    assert tile.is_flower is False
    assert tile.is_season is False


def test_white_dragon_data_correct(tile=WhiteDragon()):
    assert tile.utf8 == "🀆"
    assert tile.name == "white_dragon"
    assert tile.rank == "white"
    assert tile.suit == "dragon"
    assert tile.value == 3

    assert tile.is_suit is False
    assert tile.is_simple is False
    assert tile.is_terminal is False

    assert tile.is_honour is True
    assert tile.is_dragon is True
    assert tile.is_wind is False

    assert tile.is_special is False
    assert tile.is_flower is False
    assert tile.is_season is False


def test_one_character_data_correct(tile=OneCharacter()):
    assert tile.utf8 == "🀇"
    assert tile.name == "one_character"
    assert tile.rank == "one"
    assert tile.suit == "character"
    assert tile.value == 1

    assert tile.is_suit is True
    assert tile.is_simple is False
    assert tile.is_terminal is True

    assert tile.is_honour is False
    assert tile.is_dragon is False
    assert tile.is_wind is False

    assert tile.is_special is False
    assert tile.is_flower is False
    assert tile.is_season is False


def test_two_character_data_correct(tile=TwoCharacter()):
    assert tile.utf8 == "🀈"
    assert tile.name == "two_character"
    assert tile.rank == "two"
    assert tile.suit == "character"
    assert tile.value == 2

    assert tile.is_suit is True
    assert tile.is_simple is True
    assert tile.is_terminal is False

    assert tile.is_honour is False
    assert tile.is_dragon is False
    assert tile.is_wind is False

    assert tile.is_special is False
    assert tile.is_flower is False
    assert tile.is_season is False


def test_three_character_data_correct(tile=ThreeCharacter()):
    assert tile.utf8 == "🀉"
    assert tile.name == "three_character"
    assert tile.rank == "three"
    assert tile.suit == "character"
    assert tile.value == 3

    assert tile.is_suit is True
    assert tile.is_simple is True
    assert tile.is_terminal is False

    assert tile.is_honour is False
    assert tile.is_dragon is False
    assert tile.is_wind is False

    assert tile.is_special is False
    assert tile.is_flower is False
    assert tile.is_season is False


def test_four_character_data_correct(tile=FourCharacter()):
    assert tile.utf8 == "🀊"
    assert tile.name == "four_character"
    assert tile.rank == "four"
    assert tile.suit == "character"
    assert tile.value == 4

    assert tile.is_suit is True
    assert tile.is_simple is True
    assert tile.is_terminal is False

    assert tile.is_honour is False
    assert tile.is_dragon is False
    assert tile.is_wind is False

    assert tile.is_special is False
    assert tile.is_flower is False
    assert tile.is_season is False


def test_five_character_data_correct(tile=FiveCharacter()):
    assert tile.utf8 == "🀋"
    assert tile.name == "five_character"
    assert tile.rank == "five"
    assert tile.suit == "character"
    assert tile.value == 5

    assert tile.is_suit is True
    assert tile.is_simple is True
    assert tile.is_terminal is False

    assert tile.is_honour is False
    assert tile.is_dragon is False
    assert tile.is_wind is False

    assert tile.is_special is False
    assert tile.is_flower is False
    assert tile.is_season is False


def test_six_character_data_correct(tile=SixCharacter()):
    assert tile.utf8 == "🀌"
    assert tile.name == "six_character"
    assert tile.rank == "six"
    assert tile.suit == "character"
    assert tile.value == 6

    assert tile.is_suit is True
    assert tile.is_simple is True
    assert tile.is_terminal is False

    assert tile.is_honour is False
    assert tile.is_dragon is False
    assert tile.is_wind is False

    assert tile.is_special is False
    assert tile.is_flower is False
    assert tile.is_season is False


def test_seven_character_data_correct(tile=SevenCharacter()):
    assert tile.utf8 == "🀍"
    assert tile.name == "seven_character"
    assert tile.rank == "seven"
    assert tile.suit == "character"
    assert tile.value == 7

    assert tile.is_suit is True
    assert tile.is_simple is True
    assert tile.is_terminal is False

    assert tile.is_honour is False
    assert tile.is_dragon is False
    assert tile.is_wind is False

    assert tile.is_special is False
    assert tile.is_flower is False
    assert tile.is_season is False


def test_eight_character_data_correct(tile=EightCharacter()):
    assert tile.utf8 == "🀎"
    assert tile.name == "eight_character"
    assert tile.rank == "eight"
    assert tile.suit == "character"
    assert tile.value == 8

    assert tile.is_suit is True
    assert tile.is_simple is True
    assert tile.is_terminal is False

    assert tile.is_honour is False
    assert tile.is_dragon is False
    assert tile.is_wind is False

    assert tile.is_special is False
    assert tile.is_flower is False
    assert tile.is_season is False


def test_nine_character_data_correct(tile=NineCharacter()):
    assert tile.utf8 == "🀏"
    assert tile.name == "nine_character"
    assert tile.rank == "nine"
    assert tile.suit == "character"
    assert tile.value == 9

    assert tile.is_suit is True
    assert tile.is_simple is False
    assert tile.is_terminal is True

    assert tile.is_honour is False
    assert tile.is_dragon is False
    assert tile.is_wind is False

    assert tile.is_special is False
    assert tile.is_flower is False
    assert tile.is_season is False


def test_one_bamboo_data_correct(tile=OneBamboo()):
    assert tile.utf8 == "🀐"
    assert tile.name == "one_bamboo"
    assert tile.rank == "one"
    assert tile.suit == "bamboo"
    assert tile.value == 1

    assert tile.is_suit is True
    assert tile.is_simple is False
    assert tile.is_terminal is True

    assert tile.is_honour is False
    assert tile.is_dragon is False
    assert tile.is_wind is False

    assert tile.is_special is False
    assert tile.is_flower is False
    assert tile.is_season is False


def test_two_bamboo_data_correct(tile=TwoBamboo()):
    assert tile.utf8 == "🀑"
    assert tile.name == "two_bamboo"
    assert tile.rank == "two"
    assert tile.suit == "bamboo"
    assert tile.value == 2

    assert tile.is_suit is True
    assert tile.is_simple is True
    assert tile.is_terminal is False

    assert tile.is_honour is False
    assert tile.is_dragon is False
    assert tile.is_wind is False

    assert tile.is_special is False
    assert tile.is_flower is False
    assert tile.is_season is False


def test_three_bamboo_data_correct(tile=ThreeBamboo()):
    assert tile.utf8 == "🀒"
    assert tile.name == "three_bamboo"
    assert tile.rank == "three"
    assert tile.suit == "bamboo"
    assert tile.value == 3

    assert tile.is_suit is True
    assert tile.is_simple is True
    assert tile.is_terminal is False

    assert tile.is_honour is False
    assert tile.is_dragon is False
    assert tile.is_wind is False

    assert tile.is_special is False
    assert tile.is_flower is False
    assert tile.is_season is False


def test_four_bamboo_data_correct(tile=FourBamboo()):
    assert tile.utf8 == "🀓"
    assert tile.name == "four_bamboo"
    assert tile.rank == "four"
    assert tile.suit == "bamboo"
    assert tile.value == 4

    assert tile.is_suit is True
    assert tile.is_simple is True
    assert tile.is_terminal is False

    assert tile.is_honour is False
    assert tile.is_dragon is False
    assert tile.is_wind is False

    assert tile.is_special is False
    assert tile.is_flower is False
    assert tile.is_season is False


def test_five_bamboo_data_correct(tile=FiveBamboo()):
    assert tile.utf8 == "🀔"
    assert tile.name == "five_bamboo"
    assert tile.rank == "five"
    assert tile.suit == "bamboo"
    assert tile.value == 5

    assert tile.is_suit is True
    assert tile.is_simple is True
    assert tile.is_terminal is False

    assert tile.is_honour is False
    assert tile.is_dragon is False
    assert tile.is_wind is False

    assert tile.is_special is False
    assert tile.is_flower is False
    assert tile.is_season is False


def test_six_bamboo_data_correct(tile=SixBamboo()):
    assert tile.utf8 == "🀕"
    assert tile.name == "six_bamboo"
    assert tile.rank == "six"
    assert tile.suit == "bamboo"
    assert tile.value == 6

    assert tile.is_suit is True
    assert tile.is_simple is True
    assert tile.is_terminal is False

    assert tile.is_honour is False
    assert tile.is_dragon is False
    assert tile.is_wind is False

    assert tile.is_special is False
    assert tile.is_flower is False
    assert tile.is_season is False


def test_seven_bamboo_data_correct(tile=SevenBamboo()):
    assert tile.utf8 == "🀖"
    assert tile.name == "seven_bamboo"
    assert tile.rank == "seven"
    assert tile.suit == "bamboo"
    assert tile.value == 7

    assert tile.is_suit is True
    assert tile.is_simple is True
    assert tile.is_terminal is False

    assert tile.is_honour is False
    assert tile.is_dragon is False
    assert tile.is_wind is False

    assert tile.is_special is False
    assert tile.is_flower is False
    assert tile.is_season is False


def test_eight_bamboo_data_correct(tile=EightBamboo()):
    assert tile.utf8 == "🀗"
    assert tile.name == "eight_bamboo"
    assert tile.rank == "eight"
    assert tile.suit == "bamboo"
    assert tile.value == 8

    assert tile.is_suit is True
    assert tile.is_simple is True
    assert tile.is_terminal is False

    assert tile.is_honour is False
    assert tile.is_dragon is False
    assert tile.is_wind is False

    assert tile.is_special is False
    assert tile.is_flower is False
    assert tile.is_season is False


def test_nine_bamboo_data_correct(tile=NineBamboo()):
    assert tile.utf8 == "🀘"
    assert tile.name == "nine_bamboo"
    assert tile.rank == "nine"
    assert tile.suit == "bamboo"
    assert tile.value == 9

    assert tile.is_suit is True
    assert tile.is_simple is False
    assert tile.is_terminal is True

    assert tile.is_honour is False
    assert tile.is_dragon is False
    assert tile.is_wind is False

    assert tile.is_special is False
    assert tile.is_flower is False
    assert tile.is_season is False


def test_one_circle_data_correct(tile=OneCircle()):
    assert tile.utf8 == "🀙"
    assert tile.name == "one_circle"
    assert tile.rank == "one"
    assert tile.suit == "circle"
    assert tile.value == 1

    assert tile.is_suit is True
    assert tile.is_simple is False
    assert tile.is_terminal is True

    assert tile.is_honour is False
    assert tile.is_dragon is False
    assert tile.is_wind is False

    assert tile.is_special is False
    assert tile.is_flower is False
    assert tile.is_season is False


def test_two_circle_data_correct(tile=TwoCircle()):
    assert tile.utf8 == "🀚"
    assert tile.name == "two_circle"
    assert tile.rank == "two"
    assert tile.suit == "circle"
    assert tile.value == 2

    assert tile.is_suit is True
    assert tile.is_simple is True
    assert tile.is_terminal is False

    assert tile.is_honour is False
    assert tile.is_dragon is False
    assert tile.is_wind is False

    assert tile.is_special is False
    assert tile.is_flower is False
    assert tile.is_season is False


def test_three_circle_data_correct(tile=ThreeCircle()):
    assert tile.utf8 == "🀛"
    assert tile.name == "three_circle"
    assert tile.rank == "three"
    assert tile.suit == "circle"
    assert tile.value == 3

    assert tile.is_suit is True
    assert tile.is_simple is True
    assert tile.is_terminal is False

    assert tile.is_honour is False
    assert tile.is_dragon is False
    assert tile.is_wind is False

    assert tile.is_special is False
    assert tile.is_flower is False
    assert tile.is_season is False


def test_four_circle_data_correct(tile=FourCircle()):
    assert tile.utf8 == "🀜"
    assert tile.name == "four_circle"
    assert tile.rank == "four"
    assert tile.suit == "circle"
    assert tile.value == 4

    assert tile.is_suit is True
    assert tile.is_simple is True
    assert tile.is_terminal is False

    assert tile.is_honour is False
    assert tile.is_dragon is False
    assert tile.is_wind is False

    assert tile.is_special is False
    assert tile.is_flower is False
    assert tile.is_season is False


def test_five_circle_data_correct(tile=FiveCircle()):
    assert tile.utf8 == "🀝"
    assert tile.name == "five_circle"
    assert tile.rank == "five"
    assert tile.suit == "circle"
    assert tile.value == 5

    assert tile.is_suit is True
    assert tile.is_simple is True
    assert tile.is_terminal is False

    assert tile.is_honour is False
    assert tile.is_dragon is False
    assert tile.is_wind is False

    assert tile.is_special is False
    assert tile.is_flower is False
    assert tile.is_season is False


def test_six_circle_data_correct(tile=SixCircle()):
    assert tile.utf8 == "🀞"
    assert tile.name == "six_circle"
    assert tile.rank == "six"
    assert tile.suit == "circle"
    assert tile.value == 6

    assert tile.is_suit is True
    assert tile.is_simple is True
    assert tile.is_terminal is False

    assert tile.is_honour is False
    assert tile.is_dragon is False
    assert tile.is_wind is False

    assert tile.is_special is False
    assert tile.is_flower is False
    assert tile.is_season is False


def test_seven_circle_data_correct(tile=SevenCircle()):
    assert tile.utf8 == "🀟"
    assert tile.name == "seven_circle"
    assert tile.rank == "seven"
    assert tile.suit == "circle"
    assert tile.value == 7

    assert tile.is_suit is True
    assert tile.is_simple is True
    assert tile.is_terminal is False

    assert tile.is_honour is False
    assert tile.is_dragon is False
    assert tile.is_wind is False

    assert tile.is_special is False
    assert tile.is_flower is False
    assert tile.is_season is False


def test_eight_circle_data_correct(tile=EightCircle()):
    assert tile.utf8 == "🀠"
    assert tile.name == "eight_circle"
    assert tile.rank == "eight"
    assert tile.suit == "circle"
    assert tile.value == 8

    assert tile.is_suit is True
    assert tile.is_simple is True
    assert tile.is_terminal is False

    assert tile.is_honour is False
    assert tile.is_dragon is False
    assert tile.is_wind is False

    assert tile.is_special is False
    assert tile.is_flower is False
    assert tile.is_season is False


def test_nine_circle_data_correct(tile=NineCircle()):
    assert tile.utf8 == "🀡"
    assert tile.name == "nine_circle"
    assert tile.rank == "nine"
    assert tile.suit == "circle"
    assert tile.value == 9

    assert tile.is_suit is True
    assert tile.is_simple is False
    assert tile.is_terminal is True

    assert tile.is_honour is False
    assert tile.is_dragon is False
    assert tile.is_wind is False

    assert tile.is_special is False
    assert tile.is_flower is False
    assert tile.is_season is False


def test_plum_flower_data_correct(tile=PlumFlower()):
    assert tile.utf8 == "🀢"
    assert tile.name == "plum_flower"
    assert tile.rank == "plum"
    assert tile.suit == "flower"
    assert tile.value == 1

    assert tile.is_suit is False
    assert tile.is_simple is False
    assert tile.is_terminal is False

    assert tile.is_honour is False
    assert tile.is_dragon is False
    assert tile.is_wind is False

    assert tile.is_special is True
    assert tile.is_flower is True
    assert tile.is_season is False


def test_orchid_flower_data_correct(tile=OrchidFlower()):
    assert tile.utf8 == "🀣"
    assert tile.name == "orchid_flower"
    assert tile.rank == "orchid"
    assert tile.suit == "flower"
    assert tile.value == 2

    assert tile.is_suit is False
    assert tile.is_simple is False
    assert tile.is_terminal is False

    assert tile.is_honour is False
    assert tile.is_dragon is False
    assert tile.is_wind is False

    assert tile.is_special is True
    assert tile.is_flower is True
    assert tile.is_season is False


def test_bamboo_flower_data_correct(tile=BambooFlower()):
    assert tile.utf8 == "🀤"
    assert tile.name == "bamboo_flower"
    assert tile.rank == "bamboo"
    assert tile.suit == "flower"
    assert tile.value == 3

    assert tile.is_suit is False
    assert tile.is_simple is False
    assert tile.is_terminal is False

    assert tile.is_honour is False
    assert tile.is_dragon is False
    assert tile.is_wind is False

    assert tile.is_special is True
    assert tile.is_flower is True
    assert tile.is_season is False


def test_chrysanthemum_flower_data_correct(tile=ChrysanthemumFlower()):
    assert tile.utf8 == "🀥"
    assert tile.name == "chrysanthemum_flower"
    assert tile.rank == "chrysanthemum"
    assert tile.suit == "flower"
    assert tile.value == 4

    assert tile.is_suit is False
    assert tile.is_simple is False
    assert tile.is_terminal is False

    assert tile.is_honour is False
    assert tile.is_dragon is False
    assert tile.is_wind is False

    assert tile.is_special is True
    assert tile.is_flower is True
    assert tile.is_season is False


def test_spring_season_data_correct(tile=SpringSeason()):
    assert tile.utf8 == "🀦"
    assert tile.name == "spring_season"
    assert tile.rank == "spring"
    assert tile.suit == "season"
    assert tile.value == 1

    assert tile.is_suit is False
    assert tile.is_simple is False
    assert tile.is_terminal is False

    assert tile.is_honour is False
    assert tile.is_dragon is False
    assert tile.is_wind is False

    assert tile.is_special is True
    assert tile.is_flower is False
    assert tile.is_season is True


def test_summer_season_data_correct(tile=SummerSeason()):
    assert tile.utf8 == "🀧"
    assert tile.name == "summer_season"
    assert tile.rank == "summer"
    assert tile.suit == "season"
    assert tile.value == 2

    assert tile.is_suit is False
    assert tile.is_simple is False
    assert tile.is_terminal is False

    assert tile.is_honour is False
    assert tile.is_dragon is False
    assert tile.is_wind is False

    assert tile.is_special is True
    assert tile.is_flower is False
    assert tile.is_season is True


def test_autumn_season_data_correct(tile=AutumnSeason()):
    assert tile.utf8 == "🀨"
    assert tile.name == "autumn_season"
    assert tile.rank == "autumn"
    assert tile.suit == "season"
    assert tile.value == 3

    assert tile.is_suit is False
    assert tile.is_simple is False
    assert tile.is_terminal is False

    assert tile.is_honour is False
    assert tile.is_dragon is False
    assert tile.is_wind is False

    assert tile.is_special is True
    assert tile.is_flower is False
    assert tile.is_season is True


def test_winter_season_data_correct(tile=WinterSeason()):
    assert tile.utf8 == "🀩"
    assert tile.name == "winter_season"
    assert tile.rank == "winter"
    assert tile.suit == "season"
    assert tile.value == 4

    assert tile.is_suit is False
    assert tile.is_simple is False
    assert tile.is_terminal is False

    assert tile.is_honour is False
    assert tile.is_dragon is False
    assert tile.is_wind is False

    assert tile.is_special is True
    assert tile.is_flower is False
    assert tile.is_season is True
