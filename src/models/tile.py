class Tile:
    def __init__(self):
        self.utf8 = None
        self.name = None
        self.value = None

    def __eq__(self, other):
        if not isinstance(other, Tile):
            raise ValueError()
        return self.utf8 == other.utf8

    def __gt__(self, other):
        if not isinstance(other, Tile):
            raise ValueError()
        return self.value > other.value

    def __lt__(self, other):
        if not isinstance(other, Tile):
            raise ValueError()
        return self.value < other.value

    def __str__(self):
        return f"{self.name} -- {self.utf8}"

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(self.utf8)


class EastWind(Tile):
    def __init__(self):
        super().__init__()
        self.utf8: str = "🀀"
        self.name: str = "east_wind"
        self.suit: str = "wind"
        self.rank: str = "east"
        self.value: int = 1

        self.is_suit: bool = False
        self.is_simple: bool = False
        self.is_terminal: bool = False

        self.is_honour: bool = True
        self.is_dragon: bool = False
        self.is_wind: bool = True

        self.is_special: bool = False
        self.is_flower: bool = False
        self.is_season: bool = False


class SouthWind(Tile):
    def __init__(self):
        super().__init__()
        self.utf8: str = "🀁"
        self.name: str = "south_wind"
        self.suit: str = "wind"
        self.rank: str = "south"
        self.value: int = 2

        self.is_suit: bool = False
        self.is_simple: bool = False
        self.is_terminal: bool = False

        self.is_honour: bool = True
        self.is_dragon: bool = False
        self.is_wind: bool = True

        self.is_special: bool = False
        self.is_flower: bool = False
        self.is_season: bool = False


class WestWind(Tile):
    def __init__(self):
        super().__init__()
        self.utf8: str = "🀂"
        self.name: str = "west_wind"
        self.suit: str = "wind"
        self.rank: str = "west"
        self.value: int = 3

        self.is_suit: bool = False
        self.is_simple: bool = False
        self.is_terminal: bool = False

        self.is_honour: bool = True
        self.is_dragon: bool = False
        self.is_wind: bool = True

        self.is_special: bool = False
        self.is_flower: bool = False
        self.is_season: bool = False


class NorthWind(Tile):
    def __init__(self):
        super().__init__()
        self.utf8: str = "🀃"
        self.name: str = "north_wind"
        self.suit: str = "wind"
        self.rank: str = "north"
        self.value: int = 4

        self.is_suit: bool = False
        self.is_simple: bool = False
        self.is_terminal: bool = False

        self.is_honour: bool = True
        self.is_dragon: bool = False
        self.is_wind: bool = True

        self.is_special: bool = False
        self.is_flower: bool = False
        self.is_season: bool = False


class RedDragon(Tile):
    def __init__(self):
        super().__init__()
        self.utf8: str = "🀄"
        self.name: str = "red_dragon"
        self.suit: str = "dragon"
        self.rank: str = "red"
        self.value: int = 1

        self.is_suit: bool = False
        self.is_simple: bool = False
        self.is_terminal: bool = False

        self.is_honour: bool = True
        self.is_dragon: bool = True
        self.is_wind: bool = False

        self.is_special: bool = False
        self.is_flower: bool = False
        self.is_season: bool = False


class GreenDragon(Tile):
    def __init__(self):
        super().__init__()
        self.utf8: str = "🀅"
        self.name: str = "green_dragon"
        self.suit: str = "dragon"
        self.rank: str = "green"
        self.value: int = 2

        self.is_suit: bool = False
        self.is_simple: bool = False
        self.is_terminal: bool = False

        self.is_honour: bool = True
        self.is_dragon: bool = True
        self.is_wind: bool = False

        self.is_special: bool = False
        self.is_flower: bool = False
        self.is_season: bool = False


class WhiteDragon(Tile):
    def __init__(self):
        super().__init__()
        self.utf8: str = "🀆"
        self.name: str = "white_dragon"
        self.suit: str = "dragon"
        self.rank: str = "white"
        self.value: int = 3

        self.is_suit: bool = False
        self.is_simple: bool = False
        self.is_terminal: bool = False

        self.is_honour: bool = True
        self.is_dragon: bool = True
        self.is_wind: bool = False

        self.is_special: bool = False
        self.is_flower: bool = False
        self.is_season: bool = False


class PlumFlower(Tile):
    def __init__(self):
        super().__init__()
        self.utf8: str = "🀢"
        self.name: str = "plum_flower"
        self.suit: str = "flower"
        self.rank: str = "plum"
        self.value: int = 1

        self.is_suit: bool = False
        self.is_simple: bool = False
        self.is_terminal: bool = False

        self.is_honour: bool = False
        self.is_dragon: bool = False
        self.is_wind: bool = False

        self.is_special: bool = True
        self.is_flower: bool = True
        self.is_season: bool = False


class OrchidFlower(Tile):
    def __init__(self):
        super().__init__()
        self.utf8: str = "🀣"
        self.name: str = "orchid_flower"
        self.suit: str = "flower"
        self.rank: str = "orchid"
        self.value: int = 2

        self.is_suit: bool = False
        self.is_simple: bool = False
        self.is_terminal: bool = False

        self.is_honour: bool = False
        self.is_dragon: bool = False
        self.is_wind: bool = False

        self.is_special: bool = True
        self.is_flower: bool = True
        self.is_season: bool = False


class BambooFlower(Tile):
    def __init__(self):
        super().__init__()

        self.utf8: str = "🀤"
        self.name: str = "bamboo_flower"
        self.suit: str = "flower"
        self.rank: str = "bamboo"
        self.value: int = 3

        self.is_suit: bool = False
        self.is_simple: bool = False
        self.is_terminal: bool = False

        self.is_honour: bool = False
        self.is_dragon: bool = False
        self.is_wind: bool = False

        self.is_special: bool = True
        self.is_flower: bool = True
        self.is_season: bool = False


class ChrysanthemumFlower(Tile):
    def __init__(self):
        super().__init__()

        self.utf8: str = "🀥"
        self.name: str = "chrysanthemum_flower"
        self.suit: str = "flower"
        self.rank: str = "chrysanthemum"
        self.value: int = 4

        self.is_suit: bool = False
        self.is_simple: bool = False
        self.is_terminal: bool = False

        self.is_honour: bool = False
        self.is_dragon: bool = False
        self.is_wind: bool = False

        self.is_special: bool = True
        self.is_flower: bool = True
        self.is_season: bool = False


class SpringSeason(Tile):
    def __init__(self):
        super().__init__()

        self.utf8: str = "🀦"
        self.name: str = "spring_season"
        self.suit: str = "season"
        self.rank: str = "spring"
        self.value: int = 1

        self.is_suit: bool = False
        self.is_simple: bool = False
        self.is_terminal: bool = False

        self.is_honour: bool = False
        self.is_dragon: bool = False
        self.is_wind: bool = False

        self.is_special: bool = True
        self.is_flower: bool = False
        self.is_season: bool = True


class SummerSeason(Tile):
    def __init__(self):
        super().__init__()

        self.utf8: str = "🀧"
        self.name: str = "summer_season"
        self.suit: str = "season"
        self.rank: str = "summer"
        self.value: int = 2

        self.is_suit: bool = False
        self.is_simple: bool = False
        self.is_terminal: bool = False

        self.is_honour: bool = False
        self.is_dragon: bool = False
        self.is_wind: bool = False

        self.is_special: bool = True
        self.is_flower: bool = False
        self.is_season: bool = True


class AutumnSeason(Tile):
    def __init__(self):
        super().__init__()

        self.utf8: str = "🀨"
        self.name: str = "autumn_season"
        self.suit: str = "season"
        self.rank: str = "autumn"
        self.value: int = 3

        self.is_suit: bool = False
        self.is_simple: bool = False
        self.is_terminal: bool = False

        self.is_honour: bool = False
        self.is_dragon: bool = False
        self.is_wind: bool = False

        self.is_special: bool = True
        self.is_flower: bool = False
        self.is_season: bool = True


class WinterSeason(Tile):
    def __init__(self):
        super().__init__()

        self.utf8: str = "🀩"
        self.name: str = "winter_season"
        self.suit: str = "season"
        self.rank: str = "winter"
        self.value: int = 4

        self.is_suit: bool = False
        self.is_simple: bool = False
        self.is_terminal: bool = False

        self.is_honour: bool = False
        self.is_dragon: bool = False
        self.is_wind: bool = False

        self.is_special: bool = True
        self.is_flower: bool = False
        self.is_season: bool = True


class OneCharacter(Tile):
    def __init__(self):
        super().__init__()

        self.utf8: str = "🀇"
        self.name: str = "one_character"
        self.suit: str = "character"
        self.rank: str = "one"
        self.value: int = 1

        self.is_suit: bool = True
        self.is_simple: bool = False
        self.is_terminal: bool = True

        self.is_honour: bool = False
        self.is_dragon: bool = False
        self.is_wind: bool = False

        self.is_special: bool = False
        self.is_flower: bool = False
        self.is_season: bool = False


class TwoCharacter(Tile):
    def __init__(self):
        super().__init__()

        self.utf8: str = "🀈"
        self.name: str = "two_character"
        self.suit: str = "character"
        self.rank: str = "two"
        self.value: int = 2

        self.is_suit: bool = True
        self.is_simple: bool = True
        self.is_terminal: bool = False

        self.is_honour: bool = False
        self.is_dragon: bool = False
        self.is_wind: bool = False

        self.is_special: bool = False
        self.is_flower: bool = False
        self.is_season: bool = False


class ThreeCharacter(Tile):
    def __init__(self):
        super().__init__()
        self.utf8: str = "🀉"
        self.name: str = "three_character"
        self.suit: str = "character"
        self.rank: str = "three"
        self.value: int = 3

        self.is_suit: bool = True
        self.is_simple: bool = True
        self.is_terminal: bool = False

        self.is_honour: bool = False
        self.is_dragon: bool = False
        self.is_wind: bool = False

        self.is_special: bool = False
        self.is_flower: bool = False
        self.is_season: bool = False


class FourCharacter(Tile):
    def __init__(self):
        super().__init__()
        self.utf8: str = "🀊"
        self.name: str = "four_character"
        self.suit: str = "character"
        self.rank: str = "four"
        self.value: int = 4

        self.is_suit: bool = True
        self.is_simple: bool = True
        self.is_terminal: bool = False

        self.is_honour: bool = False
        self.is_dragon: bool = False
        self.is_wind: bool = False

        self.is_special: bool = False
        self.is_flower: bool = False
        self.is_season: bool = False


class FiveCharacter(Tile):
    def __init__(self):
        super().__init__()
        self.utf8: str = "🀋"
        self.name: str = "five_character"
        self.suit: str = "character"
        self.rank: str = "five"
        self.value: int = 5

        self.is_suit: bool = True
        self.is_simple: bool = True
        self.is_terminal: bool = False

        self.is_honour: bool = False
        self.is_dragon: bool = False
        self.is_wind: bool = False

        self.is_special: bool = False
        self.is_flower: bool = False
        self.is_season: bool = False


class SixCharacter(Tile):
    def __init__(self):
        super().__init__()
        self.utf8: str = "🀌"
        self.name: str = "six_character"
        self.suit: str = "character"
        self.rank: str = "six"
        self.value: int = 6

        self.is_suit: bool = True
        self.is_simple: bool = True
        self.is_terminal: bool = False

        self.is_honour: bool = False
        self.is_dragon: bool = False
        self.is_wind: bool = False

        self.is_special: bool = False
        self.is_flower: bool = False
        self.is_season: bool = False


class SevenCharacter(Tile):
    def __init__(self):
        super().__init__()
        self.utf8: str = "🀍"
        self.name: str = "seven_character"
        self.suit: str = "character"
        self.rank: str = "seven"
        self.value: int = 7

        self.is_suit: bool = True
        self.is_simple: bool = True
        self.is_terminal: bool = False

        self.is_honour: bool = False
        self.is_dragon: bool = False
        self.is_wind: bool = False

        self.is_special: bool = False
        self.is_flower: bool = False
        self.is_season: bool = False


class EightCharacter(Tile):
    def __init__(self):
        super().__init__()
        self.utf8: str = "🀎"
        self.name: str = "eight_character"
        self.suit: str = "character"
        self.rank: str = "eight"
        self.value: int = 8

        self.is_suit: bool = True
        self.is_simple: bool = True
        self.is_terminal: bool = False

        self.is_honour: bool = False
        self.is_dragon: bool = False
        self.is_wind: bool = False

        self.is_special: bool = False
        self.is_flower: bool = False
        self.is_season: bool = False


class NineCharacter(Tile):
    def __init__(self):
        super().__init__()
        self.utf8: str = "🀏"
        self.name: str = "nine_character"
        self.suit: str = "character"
        self.rank: str = "nine"
        self.value: int = 9

        self.is_suit: bool = True
        self.is_simple: bool = False
        self.is_terminal: bool = True

        self.is_honour: bool = False
        self.is_dragon: bool = False
        self.is_wind: bool = False

        self.is_special: bool = False
        self.is_flower: bool = False
        self.is_season: bool = False


class OneBamboo(Tile):
    def __init__(self):
        super().__init__()
        self.utf8: str = "🀐"
        self.name: str = "one_bamboo"
        self.suit: str = "bamboo"
        self.rank: str = "one"
        self.value: int = 1

        self.is_suit: bool = True
        self.is_simple: bool = False
        self.is_terminal: bool = True

        self.is_honour: bool = False
        self.is_dragon: bool = False
        self.is_wind: bool = False

        self.is_special: bool = False
        self.is_flower: bool = False
        self.is_season: bool = False


class TwoBamboo(Tile):
    def __init__(self):
        super().__init__()
        self.utf8: str = "🀑"
        self.name: str = "two_bamboo"
        self.suit: str = "bamboo"
        self.rank: str = "two"
        self.value: int = 2

        self.is_suit: bool = True
        self.is_simple: bool = True
        self.is_terminal: bool = False

        self.is_honour: bool = False
        self.is_dragon: bool = False
        self.is_wind: bool = False

        self.is_special: bool = False
        self.is_flower: bool = False
        self.is_season: bool = False


class ThreeBamboo(Tile):
    def __init__(self):
        super().__init__()
        self.utf8: str = "🀒"
        self.name: str = "three_bamboo"
        self.suit: str = "bamboo"
        self.rank: str = "three"
        self.value: int = 3

        self.is_suit: bool = True
        self.is_simple: bool = True
        self.is_terminal: bool = False

        self.is_honour: bool = False
        self.is_dragon: bool = False
        self.is_wind: bool = False

        self.is_special: bool = False
        self.is_flower: bool = False
        self.is_season: bool = False


class FourBamboo(Tile):
    def __init__(self):
        super().__init__()
        self.utf8: str = "🀓"
        self.name: str = "four_bamboo"
        self.suit: str = "bamboo"
        self.rank: str = "four"
        self.value: int = 4

        self.is_suit: bool = True
        self.is_simple: bool = True
        self.is_terminal: bool = False

        self.is_honour: bool = False
        self.is_dragon: bool = False
        self.is_wind: bool = False

        self.is_special: bool = False
        self.is_flower: bool = False
        self.is_season: bool = False


class FiveBamboo(Tile):
    def __init__(self):
        super().__init__()
        self.utf8: str = "🀔"
        self.name: str = "five_bamboo"
        self.suit: str = "bamboo"
        self.rank: str = "five"
        self.value: int = 5

        self.is_suit: bool = True
        self.is_simple: bool = True
        self.is_terminal: bool = False

        self.is_honour: bool = False
        self.is_dragon: bool = False
        self.is_wind: bool = False

        self.is_special: bool = False
        self.is_flower: bool = False
        self.is_season: bool = False


class SixBamboo(Tile):
    def __init__(self):
        super().__init__()
        self.utf8: str = "🀕"
        self.name: str = "six_bamboo"
        self.suit: str = "bamboo"
        self.rank: str = "six"
        self.value: int = 6

        self.is_suit: bool = True
        self.is_simple: bool = True
        self.is_terminal: bool = False

        self.is_honour: bool = False
        self.is_dragon: bool = False
        self.is_wind: bool = False

        self.is_special: bool = False
        self.is_flower: bool = False
        self.is_season: bool = False


class SevenBamboo(Tile):
    def __init__(self):
        super().__init__()
        self.utf8: str = "🀖"
        self.name: str = "seven_bamboo"
        self.suit: str = "bamboo"
        self.rank: str = "seven"
        self.value: int = 7

        self.is_suit: bool = True
        self.is_simple: bool = True
        self.is_terminal: bool = False

        self.is_honour: bool = False
        self.is_dragon: bool = False
        self.is_wind: bool = False

        self.is_special: bool = False
        self.is_flower: bool = False
        self.is_season: bool = False


class EightBamboo(Tile):
    def __init__(self):
        super().__init__()
        self.utf8: str = "🀗"
        self.name: str = "eight_bamboo"
        self.suit: str = "bamboo"
        self.rank: str = "eight"
        self.value: int = 8

        self.is_suit: bool = True
        self.is_simple: bool = True
        self.is_terminal: bool = False

        self.is_honour: bool = False
        self.is_dragon: bool = False
        self.is_wind: bool = False

        self.is_special: bool = False
        self.is_flower: bool = False
        self.is_season: bool = False


class NineBamboo(Tile):
    def __init__(self):
        super().__init__()
        self.utf8: str = "🀘"
        self.name: str = "nine_bamboo"
        self.suit: str = "bamboo"
        self.rank: str = "nine"
        self.value: int = 9

        self.is_suit: bool = True
        self.is_simple: bool = False
        self.is_terminal: bool = True

        self.is_honour: bool = False
        self.is_dragon: bool = False
        self.is_wind: bool = False

        self.is_special: bool = False
        self.is_flower: bool = False
        self.is_season: bool = False


class OneCircle(Tile):
    def __init__(self):
        super().__init__()
        self.utf8: str = "🀙"
        self.name: str = "one_circle"
        self.suit: str = "circle"
        self.rank: str = "one"
        self.value: int = 1

        self.is_suit: bool = True
        self.is_simple: bool = False
        self.is_terminal: bool = True

        self.is_honour: bool = False
        self.is_dragon: bool = False
        self.is_wind: bool = False

        self.is_special: bool = False
        self.is_flower: bool = False
        self.is_season: bool = False


class TwoCircle(Tile):
    def __init__(self):
        super().__init__()
        self.utf8: str = "🀚"
        self.name: str = "two_circle"
        self.suit: str = "circle"
        self.rank: str = "two"
        self.value: int = 2

        self.is_suit: bool = True
        self.is_simple: bool = True
        self.is_terminal: bool = False

        self.is_honour: bool = False
        self.is_dragon: bool = False
        self.is_wind: bool = False

        self.is_special: bool = False
        self.is_flower: bool = False
        self.is_season: bool = False


class ThreeCircle(Tile):
    def __init__(self):
        super().__init__()
        self.utf8: str = "🀛"
        self.name: str = "three_circle"
        self.suit: str = "circle"
        self.rank: str = "three"
        self.value: int = 3

        self.is_suit: bool = True
        self.is_simple: bool = True
        self.is_terminal: bool = False

        self.is_honour: bool = False
        self.is_dragon: bool = False
        self.is_wind: bool = False

        self.is_special: bool = False
        self.is_flower: bool = False
        self.is_season: bool = False


class FourCircle(Tile):
    def __init__(self):
        super().__init__()
        self.utf8: str = "🀜"
        self.name: str = "four_circle"
        self.suit: str = "circle"
        self.rank: str = "four"
        self.value: int = 4

        self.is_suit: bool = True
        self.is_simple: bool = True
        self.is_terminal: bool = False

        self.is_honour: bool = False
        self.is_dragon: bool = False
        self.is_wind: bool = False

        self.is_special: bool = False
        self.is_flower: bool = False
        self.is_season: bool = False


class FiveCircle(Tile):
    def __init__(self):
        super().__init__()
        self.utf8: str = "🀝"
        self.name: str = "five_circle"
        self.suit: str = "circle"
        self.rank: str = "five"
        self.value: int = 5

        self.is_suit: bool = True
        self.is_simple: bool = True
        self.is_terminal: bool = False

        self.is_honour: bool = False
        self.is_dragon: bool = False
        self.is_wind: bool = False

        self.is_special: bool = False
        self.is_flower: bool = False
        self.is_season: bool = False


class SixCircle(Tile):
    def __init__(self):
        super().__init__()
        self.utf8: str = "🀞"
        self.name: str = "six_circle"
        self.suit: str = "circle"
        self.rank: str = "six"
        self.value: int = 6

        self.is_suit: bool = True
        self.is_simple: bool = True
        self.is_terminal: bool = False

        self.is_honour: bool = False
        self.is_dragon: bool = False
        self.is_wind: bool = False

        self.is_special: bool = False
        self.is_flower: bool = False
        self.is_season: bool = False


class SevenCircle(Tile):
    def __init__(self):
        super().__init__()
        self.utf8: str = "🀟"
        self.name: str = "seven_circle"
        self.suit: str = "circle"
        self.rank: str = "seven"
        self.value: int = 7

        self.is_suit: bool = True
        self.is_simple: bool = True
        self.is_terminal: bool = False

        self.is_honour: bool = False
        self.is_dragon: bool = False
        self.is_wind: bool = False

        self.is_special: bool = False
        self.is_flower: bool = False
        self.is_season: bool = False


class EightCircle(Tile):
    def __init__(self):
        super().__init__()
        self.utf8: str = "🀠"
        self.name: str = "eight_circle"
        self.suit: str = "circle"
        self.rank: str = "eight"
        self.value: int = 8

        self.is_suit: bool = True
        self.is_simple: bool = True
        self.is_terminal: bool = False

        self.is_honour: bool = False
        self.is_dragon: bool = False
        self.is_wind: bool = False

        self.is_special: bool = False
        self.is_flower: bool = False
        self.is_season: bool = False


class NineCircle(Tile):
    def __init__(self):
        super().__init__()
        self.utf8: str = "🀡"
        self.name: str = "nine_circle"
        self.suit: str = "circle"
        self.rank: str = "nine"
        self.value: int = 9

        self.is_suit: bool = True
        self.is_simple: bool = False
        self.is_terminal: bool = True

        self.is_honour: bool = False
        self.is_dragon: bool = False
        self.is_wind: bool = False

        self.is_special: bool = False
        self.is_flower: bool = False
        self.is_season: bool = False


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
