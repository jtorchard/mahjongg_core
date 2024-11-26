import pytest

from core.tile import Tile
from core.data import (
    east_wind,
    south_wind,
    west_wind,
    north_wind,
    red_dragon,
    green_dragon,
    white_dragon,
    one_character,
    two_character,
    three_character,
    four_character,
    five_character,
    six_character,
    seven_character,
    eight_character,
    nine_character,
    one_bamboo,
    two_bamboo,
    three_bamboo,
    four_bamboo,
    five_bamboo,
    six_bamboo,
    seven_bamboo,
    eight_bamboo,
    nine_bamboo,
    one_circle,
    two_circle,
    three_circle,
    four_circle,
    five_circle,
    six_circle,
    seven_circle,
    eight_circle,
    nine_circle,
    plum_flower,
    orchid_flower,
    bamboo_flower,
    chrysanthemum_flower,
    spring_season,
    summer_season,
    autumn_season,
    winter_season,
)


def test_two_identical_tiles_compare_equal():
    assert Tile(east_wind) == Tile(east_wind)


def test_extract_name_from_unicode_dragon_is_correct(tile=Tile(red_dragon)):
    assert tile.name == "red_dragon"


def test_extract_name_from_unicode_wind_is_correct(tile=Tile(east_wind)):
    assert tile.name == "east_wind"


def test_extract_name_from_unicode_character_terminal_is_correct(
    tile=Tile(nine_character),
):
    assert tile.name == "nine_character"


def test_extract_name_from_unicode_character_simple_is_correct(
    tile=Tile(six_character),
):
    assert tile.name == "six_character"


def test_extract_name_from_unicode_bamboo_terminal_is_correct(tile=Tile(nine_bamboo)):
    assert tile.name == "nine_bamboo"


def test_extract_name_from_unicode_bamboo_simple_is_correct(tile=Tile(six_bamboo)):
    assert tile.name == "six_bamboo"


def test_extract_name_from_unicode_circle_terminal_is_correct(tile=Tile(nine_circle)):
    assert tile.name == "nine_circle"


def test_extract_name_from_unicode_circle_simple_is_correct(tile=Tile(six_circle)):
    assert tile.name == "six_circle"


def test_extract_name_from_unicode_plum_flower_is_correct(tile=Tile(plum_flower)):
    assert tile.name == "plum_flower"


def test_extract_name_from_unicode_autumn_season_is_correct(tile=Tile(autumn_season)):
    assert tile.name == "autumn_season"


def test_extract_name_from_unicode_letter_d_raises_value_error():
    with pytest.raises(ValueError):
        Tile("d")


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


def test_one_character_data_correct(tile=Tile(one_character)):
    assert tile.utf8 == "🀇"
    assert tile.name == "one_character"
    assert tile.rank == "one"
    assert tile.suit == "character"
    assert tile.is_dragon is False
    assert tile.is_wind is False
    assert tile.is_special is False
    assert tile.is_honour is False
    assert tile.is_suit is True
    assert tile.is_terminal is True


def test_two_character_data_correct(tile=Tile(two_character)):
    assert tile.utf8 == "🀈"
    assert tile.name == "two_character"
    assert tile.rank == "two"
    assert tile.suit == "character"
    assert tile.is_dragon is False
    assert tile.is_wind is False
    assert tile.is_special is False
    assert tile.is_honour is False
    assert tile.is_suit is True
    assert tile.is_terminal is False


def test_three_character_data_correct(tile=Tile(three_character)):
    assert tile.utf8 == "🀉"
    assert tile.name == "three_character"
    assert tile.rank == "three"
    assert tile.suit == "character"
    assert tile.is_dragon is False
    assert tile.is_wind is False
    assert tile.is_special is False
    assert tile.is_honour is False
    assert tile.is_suit is True
    assert tile.is_terminal is False


def test_four_character_data_correct(tile=Tile(four_character)):
    assert tile.utf8 == "🀊"
    assert tile.name == "four_character"
    assert tile.rank == "four"
    assert tile.suit == "character"
    assert tile.is_dragon is False
    assert tile.is_wind is False
    assert tile.is_special is False
    assert tile.is_honour is False
    assert tile.is_suit is True
    assert tile.is_terminal is False


def test_five_character_data_correct(tile=Tile(five_character)):
    assert tile.utf8 == "🀋"
    assert tile.name == "five_character"
    assert tile.rank == "five"
    assert tile.suit == "character"
    assert tile.is_dragon is False
    assert tile.is_wind is False
    assert tile.is_special is False
    assert tile.is_honour is False
    assert tile.is_suit is True
    assert tile.is_terminal is False


def test_six_character_data_correct(tile=Tile(six_character)):
    assert tile.utf8 == "🀌"
    assert tile.name == "six_character"
    assert tile.rank == "six"
    assert tile.suit == "character"
    assert tile.is_dragon is False
    assert tile.is_wind is False
    assert tile.is_special is False
    assert tile.is_honour is False
    assert tile.is_suit is True
    assert tile.is_terminal is False


def test_seven_character_data_correct(tile=Tile(seven_character)):
    assert tile.utf8 == "🀍"
    assert tile.name == "seven_character"
    assert tile.rank == "seven"
    assert tile.suit == "character"
    assert tile.is_dragon is False
    assert tile.is_wind is False
    assert tile.is_special is False
    assert tile.is_honour is False
    assert tile.is_suit is True
    assert tile.is_terminal is False


def test_eight_character_data_correct(tile=Tile(eight_character)):
    assert tile.utf8 == "🀎"
    assert tile.name == "eight_character"
    assert tile.rank == "eight"
    assert tile.suit == "character"
    assert tile.is_dragon is False
    assert tile.is_wind is False
    assert tile.is_special is False
    assert tile.is_honour is False
    assert tile.is_suit is True
    assert tile.is_terminal is False


def test_nine_character_data_correct(tile=Tile(nine_character)):
    assert tile.utf8 == "🀏"
    assert tile.name == "nine_character"
    assert tile.rank == "nine"
    assert tile.suit == "character"
    assert tile.is_dragon is False
    assert tile.is_wind is False
    assert tile.is_special is False
    assert tile.is_honour is False
    assert tile.is_suit is True
    assert tile.is_terminal is True


def test_one_bamboo_data_correct(tile=Tile(one_bamboo)):
    assert tile.utf8 == "🀐"
    assert tile.name == "one_bamboo"
    assert tile.rank == "one"
    assert tile.suit == "bamboo"
    assert tile.is_dragon is False
    assert tile.is_wind is False
    assert tile.is_special is False
    assert tile.is_honour is False
    assert tile.is_suit is True
    assert tile.is_terminal is True


def test_two_bamboo_data_correct(tile=Tile(two_bamboo)):
    assert tile.utf8 == "🀑"
    assert tile.name == "two_bamboo"
    assert tile.rank == "two"
    assert tile.suit == "bamboo"
    assert tile.is_dragon is False
    assert tile.is_wind is False
    assert tile.is_special is False
    assert tile.is_honour is False
    assert tile.is_suit is True
    assert tile.is_terminal is False


def test_three_bamboo_data_correct(tile=Tile(three_bamboo)):
    assert tile.utf8 == "🀒"
    assert tile.name == "three_bamboo"
    assert tile.rank == "three"
    assert tile.suit == "bamboo"
    assert tile.is_dragon is False
    assert tile.is_wind is False
    assert tile.is_special is False
    assert tile.is_honour is False
    assert tile.is_suit is True
    assert tile.is_terminal is False


def test_four_bamboo_data_correct(tile=Tile(four_bamboo)):
    assert tile.utf8 == "🀓"
    assert tile.name == "four_bamboo"
    assert tile.rank == "four"
    assert tile.suit == "bamboo"
    assert tile.is_dragon is False
    assert tile.is_wind is False
    assert tile.is_special is False
    assert tile.is_honour is False
    assert tile.is_suit is True
    assert tile.is_terminal is False


def test_five_bamboo_data_correct(tile=Tile(five_bamboo)):
    assert tile.utf8 == "🀔"
    assert tile.name == "five_bamboo"
    assert tile.rank == "five"
    assert tile.suit == "bamboo"
    assert tile.is_dragon is False
    assert tile.is_wind is False
    assert tile.is_special is False
    assert tile.is_honour is False
    assert tile.is_suit is True
    assert tile.is_terminal is False


def test_six_bamboo_data_correct(tile=Tile(six_bamboo)):
    assert tile.utf8 == "🀕"
    assert tile.name == "six_bamboo"
    assert tile.rank == "six"
    assert tile.suit == "bamboo"
    assert tile.is_dragon is False
    assert tile.is_wind is False
    assert tile.is_special is False
    assert tile.is_honour is False
    assert tile.is_suit is True
    assert tile.is_terminal is False


def test_seven_bamboo_data_correct(tile=Tile(seven_bamboo)):
    assert tile.utf8 == "🀖"
    assert tile.name == "seven_bamboo"
    assert tile.rank == "seven"
    assert tile.suit == "bamboo"
    assert tile.is_dragon is False
    assert tile.is_wind is False
    assert tile.is_special is False
    assert tile.is_honour is False
    assert tile.is_suit is True
    assert tile.is_terminal is False


def test_eight_bamboo_data_correct(tile=Tile(eight_bamboo)):
    assert tile.utf8 == "🀗"
    assert tile.name == "eight_bamboo"
    assert tile.rank == "eight"
    assert tile.suit == "bamboo"
    assert tile.is_dragon is False
    assert tile.is_wind is False
    assert tile.is_special is False
    assert tile.is_honour is False
    assert tile.is_suit is True
    assert tile.is_terminal is False


def test_nine_bamboo_data_correct(tile=Tile(nine_bamboo)):
    assert tile.utf8 == "🀘"
    assert tile.name == "nine_bamboo"
    assert tile.rank == "nine"
    assert tile.suit == "bamboo"
    assert tile.is_dragon is False
    assert tile.is_wind is False
    assert tile.is_special is False
    assert tile.is_honour is False
    assert tile.is_suit is True
    assert tile.is_terminal is True


def test_one_circle_data_correct(tile=Tile(one_circle)):
    assert tile.utf8 == "🀙"
    assert tile.name == "one_circle"
    assert tile.rank == "one"
    assert tile.suit == "circle"
    assert tile.is_dragon is False
    assert tile.is_wind is False
    assert tile.is_special is False
    assert tile.is_honour is False
    assert tile.is_suit is True
    assert tile.is_terminal is True


def test_two_circle_data_correct(tile=Tile(two_circle)):
    assert tile.utf8 == "🀚"
    assert tile.name == "two_circle"
    assert tile.rank == "two"
    assert tile.suit == "circle"
    assert tile.is_dragon is False
    assert tile.is_wind is False
    assert tile.is_special is False
    assert tile.is_honour is False
    assert tile.is_suit is True
    assert tile.is_terminal is False


def test_three_circle_data_correct(tile=Tile(three_circle)):
    assert tile.utf8 == "🀛"
    assert tile.name == "three_circle"
    assert tile.rank == "three"
    assert tile.suit == "circle"
    assert tile.is_dragon is False
    assert tile.is_wind is False
    assert tile.is_special is False
    assert tile.is_honour is False
    assert tile.is_suit is True
    assert tile.is_terminal is False


def test_four_circle_data_correct(tile=Tile(four_circle)):
    assert tile.utf8 == "🀜"
    assert tile.name == "four_circle"
    assert tile.rank == "four"
    assert tile.suit == "circle"
    assert tile.is_dragon is False
    assert tile.is_wind is False
    assert tile.is_special is False
    assert tile.is_honour is False
    assert tile.is_suit is True
    assert tile.is_terminal is False


def test_five_circle_data_correct(tile=Tile(five_circle)):
    assert tile.utf8 == "🀝"
    assert tile.name == "five_circle"
    assert tile.rank == "five"
    assert tile.suit == "circle"
    assert tile.is_dragon is False
    assert tile.is_wind is False
    assert tile.is_special is False
    assert tile.is_honour is False
    assert tile.is_suit is True
    assert tile.is_terminal is False


def test_six_circle_data_correct(tile=Tile(six_circle)):
    assert tile.utf8 == "🀞"
    assert tile.name == "six_circle"
    assert tile.rank == "six"
    assert tile.suit == "circle"
    assert tile.is_dragon is False
    assert tile.is_wind is False
    assert tile.is_special is False
    assert tile.is_honour is False
    assert tile.is_suit is True
    assert tile.is_terminal is False


def test_seven_circle_data_correct(tile=Tile(seven_circle)):
    assert tile.utf8 == "🀟"
    assert tile.name == "seven_circle"
    assert tile.rank == "seven"
    assert tile.suit == "circle"
    assert tile.is_dragon is False
    assert tile.is_wind is False
    assert tile.is_special is False
    assert tile.is_honour is False
    assert tile.is_suit is True
    assert tile.is_terminal is False


def test_eight_circle_data_correct(tile=Tile(eight_circle)):
    assert tile.utf8 == "🀠"
    assert tile.name == "eight_circle"
    assert tile.rank == "eight"
    assert tile.suit == "circle"
    assert tile.is_dragon is False
    assert tile.is_wind is False
    assert tile.is_special is False
    assert tile.is_honour is False
    assert tile.is_suit is True
    assert tile.is_terminal is False


def test_nine_circle_data_correct(tile=Tile(nine_circle)):
    assert tile.utf8 == "🀡"
    assert tile.name == "nine_circle"
    assert tile.rank == "nine"
    assert tile.suit == "circle"
    assert tile.is_dragon is False
    assert tile.is_wind is False
    assert tile.is_special is False
    assert tile.is_honour is False
    assert tile.is_suit is True
    assert tile.is_terminal is True


def test_plum_flower_data_correct(tile=Tile(plum_flower)):
    assert tile.utf8 == "🀢"
    assert tile.name == "plum_flower"
    assert tile.rank == "plum"
    assert tile.suit == "flower"
    assert tile.is_dragon is False
    assert tile.is_wind is False
    assert tile.is_special is True
    assert tile.is_honour is False
    assert tile.is_suit is False
    assert tile.is_terminal is False


def test_orchid_flower_data_correct(tile=Tile(orchid_flower)):
    assert tile.utf8 == "🀣"
    assert tile.name == "orchid_flower"
    assert tile.rank == "orchid"
    assert tile.suit == "flower"
    assert tile.is_dragon is False
    assert tile.is_wind is False
    assert tile.is_special is True
    assert tile.is_honour is False
    assert tile.is_suit is False
    assert tile.is_terminal is False


def test_bamboo_flower_data_correct(tile=Tile(bamboo_flower)):
    assert tile.utf8 == "🀤"
    assert tile.name == "bamboo_flower"
    assert tile.rank == "bamboo"
    assert tile.suit == "flower"
    assert tile.is_dragon is False
    assert tile.is_wind is False
    assert tile.is_special is True
    assert tile.is_honour is False
    assert tile.is_suit is False
    assert tile.is_terminal is False


def test_chrysanthemum_flower_data_correct(tile=Tile(chrysanthemum_flower)):
    assert tile.utf8 == "🀥"
    assert tile.name == "chrysanthemum_flower"
    assert tile.rank == "chrysanthemum"
    assert tile.suit == "flower"
    assert tile.is_dragon is False
    assert tile.is_wind is False
    assert tile.is_special is True
    assert tile.is_honour is False
    assert tile.is_suit is False
    assert tile.is_terminal is False


def test_spring_season_data_correct(tile=Tile(spring_season)):
    assert tile.utf8 == "🀦"
    assert tile.name == "spring_season"
    assert tile.rank == "spring"
    assert tile.suit == "season"
    assert tile.is_dragon is False
    assert tile.is_wind is False
    assert tile.is_special is True
    assert tile.is_honour is False
    assert tile.is_suit is False
    assert tile.is_terminal is False


def test_summer_season_data_correct(tile=Tile(summer_season)):
    assert tile.utf8 == "🀧"
    assert tile.name == "summer_season"
    assert tile.rank == "summer"
    assert tile.suit == "season"
    assert tile.is_dragon is False
    assert tile.is_wind is False
    assert tile.is_special is True
    assert tile.is_honour is False
    assert tile.is_suit is False
    assert tile.is_terminal is False


def test_autumn_season_data_correct(tile=Tile(autumn_season)):
    assert tile.utf8 == "🀨"
    assert tile.name == "autumn_season"
    assert tile.rank == "autumn"
    assert tile.suit == "season"
    assert tile.is_dragon is False
    assert tile.is_wind is False
    assert tile.is_special is True
    assert tile.is_honour is False
    assert tile.is_suit is False
    assert tile.is_terminal is False


def test_winter_season_data_correct(tile=Tile(winter_season)):
    assert tile.utf8 == "🀩"
    assert tile.name == "winter_season"
    assert tile.rank == "winter"
    assert tile.suit == "season"
    assert tile.is_dragon is False
    assert tile.is_wind is False
    assert tile.is_special is True
    assert tile.is_honour is False
    assert tile.is_suit is False
    assert tile.is_terminal is False
