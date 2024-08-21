import unicodedata


class Tile:
    def __init__(self, unicode_tile):
        self.utf8 = unicode_tile
        self.name = self._extract_name_from_unicode(self.utf8)
        self.rank, self.suit = self.name.split("_")
        self.is_dragon = "dragon" in self.suit
        self.is_wind = "wind" in self.suit
        self.is_special = self.suit in ("flower", "season")
        self.is_honour = self.suit in ("dragon", "wind")
        self.is_suit = self.suit in ("character", "circle", "bamboo")
        self.is_terminal = self.rank in ("one", "nine")

    @staticmethod
    def _extract_name_from_unicode(unicode_tile):
        split_name = unicodedata.name(unicode_tile).split()

        tile_type = split_name[-1]
        if tile_type in ("CIRCLES", "CHARACTERS", "BAMBOOS"):
            _, _, rank, _, suit = split_name
            suit = suit[:-1]
        elif tile_type in ("WIND", "DRAGON"):
            _, _, rank, suit = split_name
        elif tile_type in ("SPRING", "SUMMER", "AUTUMN", "WINTER"):
            rank = tile_type
            suit = "season"
        elif tile_type in ("PLUM", "ORCHID", "BAMBOO", "CHRYSANTHEMUM"):
            rank = tile_type
            suit = "flower"
        else:
            raise ValueError

        return f"{rank.lower()}_{suit.lower()}"

    def __str__(self):
        return f"{self.name} -- {self.utf8}"
