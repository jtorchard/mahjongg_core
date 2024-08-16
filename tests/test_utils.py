from core.utils import extract_name_from_unicode
from core.data import (
    red_dragon,
    east_wind,
    nine_character,
    six_character,
    nine_bamboo,
    six_bamboo,
    nine_circle,
    six_circle,
    plum_flower,
    autumn_season,
)


def test_extract_name_from_unicode_dragon_is_correct(utf8_symbol=red_dragon):
    name = extract_name_from_unicode(utf8_symbol)
    assert name == "red_dragon"


def test_extract_name_from_unicode_wind_is_correct(utf8_symbol=east_wind):
    name = extract_name_from_unicode(utf8_symbol)
    assert name == "east_wind"


def test_extract_name_from_unicode_character_terminal_is_correct(utf8_symbol=nine_character):
    name = extract_name_from_unicode(utf8_symbol)
    assert name == "nine_character"


def test_extract_name_from_unicode_character_simple_is_correct(utf8_symbol=six_character):
    name = extract_name_from_unicode(utf8_symbol)
    assert name == "six_character"


def test_extract_name_from_unicode_bamboo_terminal_is_correct(utf8_symbol=nine_bamboo):
    name = extract_name_from_unicode(utf8_symbol)
    assert name == "nine_bamboo"


def test_extract_name_from_unicode_bamboo_simple_is_correct(utf8_symbol=six_bamboo):
    name = extract_name_from_unicode(utf8_symbol)
    assert name == "six_bamboo"


def test_extract_name_from_unicode_circle_terminal_is_correct(utf8_symbol=nine_circle):
    name = extract_name_from_unicode(utf8_symbol)
    assert name == "nine_circle"


def test_extract_name_from_unicode_circle_simple_is_correct(utf8_symbol=six_circle):
    name = extract_name_from_unicode(utf8_symbol)
    assert name == "six_circle"


def test_extract_name_from_unicode_plum_flower_is_correct(utf8_symbol=plum_flower):
    name = extract_name_from_unicode(utf8_symbol)
    assert name == "plum_flower"


def test_extract_name_from_unicode_autumn_season_is_correct(utf8_symbol=autumn_season):
    name = extract_name_from_unicode(utf8_symbol)
    assert name == "autumn_season"
