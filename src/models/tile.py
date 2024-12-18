from dataclasses import dataclass


@dataclass(frozen=True)
class Tile:
    utf8: str = ""
    name: str = ""
    value: int = 0

    def __eq__(self, other):
        if not isinstance(other, Tile):
            raise NotImplementedError()
        return self.utf8 == other.utf8

    def __gt__(self, other):
        if not isinstance(other, Tile):
            raise NotImplementedError()
        return self.value > other.value

    def __lt__(self, other):
        if not isinstance(other, Tile):
            raise NotImplementedError()
        return self.value < other.value

    def __str__(self):
        return f"{self.name} -- {self.utf8}"


@dataclass(frozen=True)
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


@dataclass(frozen=True)
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


@dataclass(frozen=True)
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


@dataclass(frozen=True)
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


@dataclass(frozen=True)
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


@dataclass(frozen=True)
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


@dataclass(frozen=True)
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


@dataclass(frozen=True)
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


@dataclass(frozen=True)
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


@dataclass(frozen=True)
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


@dataclass(frozen=True)
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


@dataclass(frozen=True)
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


@dataclass(frozen=True)
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


@dataclass(frozen=True)
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


@dataclass(frozen=True)
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


@dataclass(frozen=True)
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


@dataclass(frozen=True)
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


@dataclass(frozen=True)
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


@dataclass(frozen=True)
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


@dataclass(frozen=True)
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


@dataclass(frozen=True)
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


@dataclass(frozen=True)
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


@dataclass(frozen=True)
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


@dataclass(frozen=True)
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


@dataclass(frozen=True)
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


@dataclass(frozen=True)
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


@dataclass(frozen=True)
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


@dataclass(frozen=True)
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


@dataclass(frozen=True)
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


@dataclass(frozen=True)
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


@dataclass(frozen=True)
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


@dataclass(frozen=True)
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


@dataclass(frozen=True)
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


@dataclass(frozen=True)
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


@dataclass(frozen=True)
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


@dataclass(frozen=True)
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


@dataclass(frozen=True)
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


@dataclass(frozen=True)
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


@dataclass(frozen=True)
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


@dataclass(frozen=True)
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


@dataclass(frozen=True)
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


@dataclass(frozen=True)
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
