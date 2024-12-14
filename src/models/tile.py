from pydantic import BaseModel, ConfigDict


class Tile(BaseModel):
    model_config = ConfigDict(str_to_lower=True, frozen=True)

    utf8: str = ""
    name: str = ""
    value: int = 0

    def __eq__(self, other):
        return self.utf8 == other.utf8

    def __gt__(self, other):
        return self.value > other.value

    def __str__(self):
        return f"{self.name} -- {self.utf8}"

    def __repr__(self):
        return self.__str__()


class EastWind(Tile):
    utf8: str = "🀀"
    name: str = "east_wind"
    suit: str = "wind"
    rank: str = "east"
    value: int = 1

    is_suit: bool = False
    is_simple: bool = False
    is_terminal: bool = False

    is_honour: bool = True
    is_dragon: bool = False
    is_wind: bool = True

    is_special: bool = False
    is_flower: bool = False
    is_season: bool = False


class SouthWind(Tile):
    utf8: str = "🀁"
    name: str = "south_wind"
    suit: str = "wind"
    rank: str = "south"
    value: int = 2

    is_suit: bool = False
    is_simple: bool = False
    is_terminal: bool = False

    is_honour: bool = True
    is_dragon: bool = False
    is_wind: bool = True

    is_special: bool = False
    is_flower: bool = False
    is_season: bool = False


class WestWind(Tile):
    utf8: str = "🀂"
    name: str = "west_wind"
    suit: str = "wind"
    rank: str = "west"
    value: int = 3

    is_suit: bool = False
    is_simple: bool = False
    is_terminal: bool = False

    is_honour: bool = True
    is_dragon: bool = False
    is_wind: bool = True

    is_special: bool = False
    is_flower: bool = False
    is_season: bool = False


class NorthWind(Tile):
    utf8: str = "🀃"
    name: str = "north_wind"
    suit: str = "wind"
    rank: str = "north"
    value: int = 4

    is_suit: bool = False
    is_simple: bool = False
    is_terminal: bool = False

    is_honour: bool = True
    is_dragon: bool = False
    is_wind: bool = True

    is_special: bool = False
    is_flower: bool = False
    is_season: bool = False


class RedDragon(Tile):
    utf8: str = "🀄"
    name: str = "red_dragon"
    suit: str = "dragon"
    rank: str = "red"
    value: int = 1

    is_suit: bool = False
    is_simple: bool = False
    is_terminal: bool = False

    is_honour: bool = True
    is_dragon: bool = True
    is_wind: bool = False

    is_special: bool = False
    is_flower: bool = False
    is_season: bool = False


class GreenDragon(Tile):
    utf8: str = "🀅"
    name: str = "green_dragon"
    suit: str = "dragon"
    rank: str = "green"
    value: int = 2

    is_suit: bool = False
    is_simple: bool = False
    is_terminal: bool = False

    is_honour: bool = True
    is_dragon: bool = True
    is_wind: bool = False

    is_special: bool = False
    is_flower: bool = False
    is_season: bool = False


class WhiteDragon(Tile):
    utf8: str = "🀆"
    name: str = "white_dragon"
    suit: str = "dragon"
    rank: str = "white"
    value: int = 3

    is_suit: bool = False
    is_simple: bool = False
    is_terminal: bool = False

    is_honour: bool = True
    is_dragon: bool = True
    is_wind: bool = False

    is_special: bool = False
    is_flower: bool = False
    is_season: bool = False


class PlumFlower(Tile):
    utf8: str = "🀢"
    name: str = "plum_flower"
    suit: str = "flower"
    rank: str = "plum"
    value: int = 1

    is_suit: bool = False
    is_simple: bool = False
    is_terminal: bool = False

    is_honour: bool = False
    is_dragon: bool = False
    is_wind: bool = False

    is_special: bool = True
    is_flower: bool = True
    is_season: bool = False


class OrchidFlower(Tile):
    utf8: str = "🀣"
    name: str = "orchid_flower"
    suit: str = "flower"
    rank: str = "orchid"
    value: int = 2

    is_suit: bool = False
    is_simple: bool = False
    is_terminal: bool = False

    is_honour: bool = False
    is_dragon: bool = False
    is_wind: bool = False

    is_special: bool = True
    is_flower: bool = True
    is_season: bool = False


class BambooFlower(Tile):
    utf8: str = "🀤"
    name: str = "bamboo_flower"
    suit: str = "flower"
    rank: str = "bamboo"
    value: int = 3

    is_suit: bool = False
    is_simple: bool = False
    is_terminal: bool = False

    is_honour: bool = False
    is_dragon: bool = False
    is_wind: bool = False

    is_special: bool = True
    is_flower: bool = True
    is_season: bool = False


class ChrysanthemumFlower(Tile):
    utf8: str = "🀥"
    name: str = "chrysanthemum_flower"
    suit: str = "flower"
    rank: str = "chrysanthemum"
    value: int = 4

    is_suit: bool = False
    is_simple: bool = False
    is_terminal: bool = False

    is_honour: bool = False
    is_dragon: bool = False
    is_wind: bool = False

    is_special: bool = True
    is_flower: bool = True
    is_season: bool = False


class SpringSeason(Tile):
    utf8: str = "🀦"
    name: str = "spring_season"
    suit: str = "season"
    rank: str = "spring"
    value: int = 1

    is_suit: bool = False
    is_simple: bool = False
    is_terminal: bool = False

    is_honour: bool = False
    is_dragon: bool = False
    is_wind: bool = False

    is_special: bool = True
    is_flower: bool = False
    is_season: bool = True


class SummerSeason(Tile):
    utf8: str = "🀧"
    name: str = "summer_season"
    suit: str = "season"
    rank: str = "summer"
    value: int = 2

    is_suit: bool = False
    is_simple: bool = False
    is_terminal: bool = False

    is_honour: bool = False
    is_dragon: bool = False
    is_wind: bool = False

    is_special: bool = True
    is_flower: bool = False
    is_season: bool = True


class AutumnSeason(Tile):
    utf8: str = "🀨"
    name: str = "autumn_season"
    suit: str = "season"
    rank: str = "autumn"
    value: int = 3

    is_suit: bool = False
    is_simple: bool = False
    is_terminal: bool = False

    is_honour: bool = False
    is_dragon: bool = False
    is_wind: bool = False

    is_special: bool = True
    is_flower: bool = False
    is_season: bool = True


class WinterSeason(Tile):
    utf8: str = "🀩"
    name: str = "winter_season"
    suit: str = "season"
    rank: str = "winter"
    value: int = 4

    is_suit: bool = False
    is_simple: bool = False
    is_terminal: bool = False

    is_honour: bool = False
    is_dragon: bool = False
    is_wind: bool = False

    is_special: bool = True
    is_flower: bool = False
    is_season: bool = True


class OneCharacter(Tile):
    utf8: str = "🀇"
    name: str = "one_character"
    suit: str = "character"
    rank: str = "one"
    value: int = 1

    is_suit: bool = True
    is_simple: bool = False
    is_terminal: bool = True

    is_honour: bool = False
    is_dragon: bool = False
    is_wind: bool = False

    is_special: bool = False
    is_flower: bool = False
    is_season: bool = False


class TwoCharacter(Tile):
    utf8: str = "🀈"
    name: str = "two_character"
    suit: str = "character"
    rank: str = "two"
    value: int = 2

    is_suit: bool = True
    is_simple: bool = True
    is_terminal: bool = False

    is_honour: bool = False
    is_dragon: bool = False
    is_wind: bool = False

    is_special: bool = False
    is_flower: bool = False
    is_season: bool = False


class ThreeCharacter(Tile):
    utf8: str = "🀉"
    name: str = "three_character"
    suit: str = "character"
    rank: str = "three"
    value: int = 3

    is_suit: bool = True
    is_simple: bool = True
    is_terminal: bool = False

    is_honour: bool = False
    is_dragon: bool = False
    is_wind: bool = False

    is_special: bool = False
    is_flower: bool = False
    is_season: bool = False


class FourCharacter(Tile):
    utf8: str = "🀊"
    name: str = "four_character"
    suit: str = "character"
    rank: str = "four"
    value: int = 4

    is_suit: bool = True
    is_simple: bool = True
    is_terminal: bool = False

    is_honour: bool = False
    is_dragon: bool = False
    is_wind: bool = False

    is_special: bool = False
    is_flower: bool = False
    is_season: bool = False


class FiveCharacter(Tile):
    utf8: str = "🀋"
    name: str = "five_character"
    suit: str = "character"
    rank: str = "five"
    value: int = 5

    is_suit: bool = True
    is_simple: bool = True
    is_terminal: bool = False

    is_honour: bool = False
    is_dragon: bool = False
    is_wind: bool = False

    is_special: bool = False
    is_flower: bool = False
    is_season: bool = False


class SixCharacter(Tile):
    utf8: str = "🀌"
    name: str = "six_character"
    suit: str = "character"
    rank: str = "six"
    value: int = 6

    is_suit: bool = True
    is_simple: bool = True
    is_terminal: bool = False

    is_honour: bool = False
    is_dragon: bool = False
    is_wind: bool = False

    is_special: bool = False
    is_flower: bool = False
    is_season: bool = False


class SevenCharacter(Tile):
    utf8: str = "🀍"
    name: str = "seven_character"
    suit: str = "character"
    rank: str = "seven"
    value: int = 7

    is_suit: bool = True
    is_simple: bool = True
    is_terminal: bool = False

    is_honour: bool = False
    is_dragon: bool = False
    is_wind: bool = False

    is_special: bool = False
    is_flower: bool = False
    is_season: bool = False


class EightCharacter(Tile):
    utf8: str = "🀎"
    name: str = "eight_character"
    suit: str = "character"
    rank: str = "eight"
    value: int = 8

    is_suit: bool = True
    is_simple: bool = True
    is_terminal: bool = False

    is_honour: bool = False
    is_dragon: bool = False
    is_wind: bool = False

    is_special: bool = False
    is_flower: bool = False
    is_season: bool = False


class NineCharacter(Tile):
    utf8: str = "🀏"
    name: str = "nine_character"
    suit: str = "character"
    rank: str = "nine"
    value: int = 9

    is_suit: bool = True
    is_simple: bool = False
    is_terminal: bool = True

    is_honour: bool = False
    is_dragon: bool = False
    is_wind: bool = False

    is_special: bool = False
    is_flower: bool = False
    is_season: bool = False


class OneBamboo(Tile):
    utf8: str = "🀐"
    name: str = "one_bamboo"
    suit: str = "bamboo"
    rank: str = "one"
    value: int = 1

    is_suit: bool = True
    is_simple: bool = False
    is_terminal: bool = True

    is_honour: bool = False
    is_dragon: bool = False
    is_wind: bool = False

    is_special: bool = False
    is_flower: bool = False
    is_season: bool = False


class TwoBamboo(Tile):
    utf8: str = "🀑"
    name: str = "two_bamboo"
    suit: str = "bamboo"
    rank: str = "two"
    value: int = 2

    is_suit: bool = True
    is_simple: bool = True
    is_terminal: bool = False

    is_honour: bool = False
    is_dragon: bool = False
    is_wind: bool = False

    is_special: bool = False
    is_flower: bool = False
    is_season: bool = False


class ThreeBamboo(Tile):
    utf8: str = "🀒"
    name: str = "three_bamboo"
    suit: str = "bamboo"
    rank: str = "three"
    value: int = 3

    is_suit: bool = True
    is_simple: bool = True
    is_terminal: bool = False

    is_honour: bool = False
    is_dragon: bool = False
    is_wind: bool = False

    is_special: bool = False
    is_flower: bool = False
    is_season: bool = False


class FourBamboo(Tile):
    utf8: str = "🀓"
    name: str = "four_bamboo"
    suit: str = "bamboo"
    rank: str = "four"
    value: int = 4

    is_suit: bool = True
    is_simple: bool = True
    is_terminal: bool = False

    is_honour: bool = False
    is_dragon: bool = False
    is_wind: bool = False

    is_special: bool = False
    is_flower: bool = False
    is_season: bool = False


class FiveBamboo(Tile):
    utf8: str = "🀔"
    name: str = "five_bamboo"
    suit: str = "bamboo"
    rank: str = "five"
    value: int = 5

    is_suit: bool = True
    is_simple: bool = True
    is_terminal: bool = False

    is_honour: bool = False
    is_dragon: bool = False
    is_wind: bool = False

    is_special: bool = False
    is_flower: bool = False
    is_season: bool = False


class SixBamboo(Tile):
    utf8: str = "🀕"
    name: str = "six_bamboo"
    suit: str = "bamboo"
    rank: str = "six"
    value: int = 6

    is_suit: bool = True
    is_simple: bool = True
    is_terminal: bool = False

    is_honour: bool = False
    is_dragon: bool = False
    is_wind: bool = False

    is_special: bool = False
    is_flower: bool = False
    is_season: bool = False


class SevenBamboo(Tile):
    utf8: str = "🀖"
    name: str = "seven_bamboo"
    suit: str = "bamboo"
    rank: str = "seven"
    value: int = 7

    is_suit: bool = True
    is_simple: bool = True
    is_terminal: bool = False

    is_honour: bool = False
    is_dragon: bool = False
    is_wind: bool = False

    is_special: bool = False
    is_flower: bool = False
    is_season: bool = False


class EightBamboo(Tile):
    utf8: str = "🀗"
    name: str = "eight_bamboo"
    suit: str = "bamboo"
    rank: str = "eight"
    value: int = 8

    is_suit: bool = True
    is_simple: bool = True
    is_terminal: bool = False

    is_honour: bool = False
    is_dragon: bool = False
    is_wind: bool = False

    is_special: bool = False
    is_flower: bool = False
    is_season: bool = False


class NineBamboo(Tile):
    utf8: str = "🀘"
    name: str = "nine_bamboo"
    suit: str = "bamboo"
    rank: str = "nine"
    value: int = 9

    is_suit: bool = True
    is_simple: bool = False
    is_terminal: bool = True

    is_honour: bool = False
    is_dragon: bool = False
    is_wind: bool = False

    is_special: bool = False
    is_flower: bool = False
    is_season: bool = False


class OneCircle(Tile):
    utf8: str = "🀙"
    name: str = "one_circle"
    suit: str = "circle"
    rank: str = "one"
    value: int = 1

    is_suit: bool = True
    is_simple: bool = False
    is_terminal: bool = True

    is_honour: bool = False
    is_dragon: bool = False
    is_wind: bool = False

    is_special: bool = False
    is_flower: bool = False
    is_season: bool = False


class TwoCircle(Tile):
    utf8: str = "🀚"
    name: str = "two_circle"
    suit: str = "circle"
    rank: str = "two"
    value: int = 2

    is_suit: bool = True
    is_simple: bool = True
    is_terminal: bool = False

    is_honour: bool = False
    is_dragon: bool = False
    is_wind: bool = False

    is_special: bool = False
    is_flower: bool = False
    is_season: bool = False


class ThreeCircle(Tile):
    utf8: str = "🀛"
    name: str = "three_circle"
    suit: str = "circle"
    rank: str = "three"
    value: int = 3

    is_suit: bool = True
    is_simple: bool = True
    is_terminal: bool = False

    is_honour: bool = False
    is_dragon: bool = False
    is_wind: bool = False

    is_special: bool = False
    is_flower: bool = False
    is_season: bool = False


class FourCircle(Tile):
    utf8: str = "🀜"
    name: str = "four_circle"
    suit: str = "circle"
    rank: str = "four"
    value: int = 4

    is_suit: bool = True
    is_simple: bool = True
    is_terminal: bool = False

    is_honour: bool = False
    is_dragon: bool = False
    is_wind: bool = False

    is_special: bool = False
    is_flower: bool = False
    is_season: bool = False


class FiveCircle(Tile):
    utf8: str = "🀝"
    name: str = "five_circle"
    suit: str = "circle"
    rank: str = "five"
    value: int = 5

    is_suit: bool = True
    is_simple: bool = True
    is_terminal: bool = False

    is_honour: bool = False
    is_dragon: bool = False
    is_wind: bool = False

    is_special: bool = False
    is_flower: bool = False
    is_season: bool = False


class SixCircle(Tile):
    utf8: str = "🀞"
    name: str = "six_circle"
    suit: str = "circle"
    rank: str = "six"
    value: int = 6

    is_suit: bool = True
    is_simple: bool = True
    is_terminal: bool = False

    is_honour: bool = False
    is_dragon: bool = False
    is_wind: bool = False

    is_special: bool = False
    is_flower: bool = False
    is_season: bool = False


class SevenCircle(Tile):
    utf8: str = "🀟"
    name: str = "seven_circle"
    suit: str = "circle"
    rank: str = "seven"
    value: int = 7

    is_suit: bool = True
    is_simple: bool = True
    is_terminal: bool = False

    is_honour: bool = False
    is_dragon: bool = False
    is_wind: bool = False

    is_special: bool = False
    is_flower: bool = False
    is_season: bool = False


class EightCircle(Tile):
    utf8: str = "🀠"
    name: str = "eight_circle"
    suit: str = "circle"
    rank: str = "eight"
    value: int = 8

    is_suit: bool = True
    is_simple: bool = True
    is_terminal: bool = False

    is_honour: bool = False
    is_dragon: bool = False
    is_wind: bool = False

    is_special: bool = False
    is_flower: bool = False
    is_season: bool = False


class NineCircle(Tile):
    utf8: str = "🀡"
    name: str = "nine_circle"
    suit: str = "circle"
    rank: str = "nine"
    value: int = 9

    is_suit: bool = True
    is_simple: bool = False
    is_terminal: bool = True

    is_honour: bool = False
    is_dragon: bool = False
    is_wind: bool = False

    is_special: bool = False
    is_flower: bool = False
    is_season: bool = False


winds = [EastWind, SouthWind, WestWind, NorthWind]
dragons = [RedDragon, GreenDragon, WhiteDragon]
honours = winds + dragons
flowers = [PlumFlower, OrchidFlower, BambooFlower, ChrysanthemumFlower]
seasons = [SpringSeason, SummerSeason, AutumnSeason, WinterSeason]
bamboos = [
    OneBamboo,
    TwoBamboo,
    ThreeBamboo,
    FourBamboo,
    FiveBamboo,
    SixBamboo,
    SevenBamboo,
    EightBamboo,
    NineBamboo,
]
circles = [
    OneCircle,
    TwoCircle,
    ThreeCircle,
    FourCircle,
    FiveCircle,
    SixCircle,
    SevenCircle,
    EightCircle,
    NineCircle,
]
characters = [
    OneCharacter,
    TwoCharacter,
    ThreeCharacter,
    FourCharacter,
    FiveCharacter,
    SixCharacter,
    SevenCharacter,
    EightCharacter,
    NineCharacter,
]
suits = bamboos + circles + characters
tiles = honours + flowers + seasons + suits

# class Tile():
#     def __init__(self, unicode_tile):
#         super().__init__()
#         self.utf8 = unicode_tile
#         self.name: str = ""
#         self.suit: str = ""
#         self.rank: str = ""
#         self._set_data_from_unicode(self.utf8)
#
#         self.is_dragon = "dragon" in self.suit
#         self.is_wind = "wind" in self.suit
#         self.is_special = self.suit in ("flower", "season")
#         self.is_honour = self.suit in ("dragon", "wind")
#         self.is_suit = self.suit in ("character", "circle", "bamboo")
#         self.is_terminal = self.rank in ("one", "nine")
#         self.is_simple = self.rank in ("two", "three", "four", "five", "six", "seven", "eight")
#
#     def _set_data_from_unicode(self, unicode_tile):
#         split_name = unicodedata.name(unicode_tile).lower().split()
#
#         tile_type = split_name[-1]
#         if tile_type in ("circles", "characters", "bamboos"):
#             _, _, self.rank, _, suit = split_name
#             self.suit = suit[:-1]
#         elif tile_type in ("wind", "dragon"):
#             _, _, self.rank, self.suit = split_name
#         elif tile_type in ("spring", "summer", "autumn", "winter"):
#             self.rank = tile_type
#             self.suit = "season"
#         elif tile_type in ("plum", "orchid", "bamboo", "chrysanthemum"):
#             self.rank = tile_type
#             self.suit = "flower"
#         else:
#             raise ValueError
#
#         self.name = f"{self.rank.lower()}_{self.suit.lower()}"
#
#     def __eq__(self, other):
#         return self.utf8 == other.utf8
#
#     def __gt__(self, other):
#         return self.rank > other.rank
#
#     def __str__(self):
#         return f"{self.name} -- {self.utf8}"
#
#     def __repr__(self):
#         return self.__str__()
