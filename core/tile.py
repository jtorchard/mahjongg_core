from .utils import extract_name_from_unicode


class Tile:
    def __init__(self, unicode_tile):
        self.utf8 = unicode_tile
        self.name = extract_name_from_unicode(self.utf8)
        self.rank, self.suit = self.name.split("_")
        self.is_dragon = "dragon" in self.suit
        self.is_wind = "wind" in self.suit
        self.is_special = self.suit in ("flower", "season")
        self.is_honour = self.suit in ("dragon", "wind")
        self.is_suit = self.suit in ("character", "circle", "bamboo")
        self.is_terminal = self.rank in ("one", "nine")

    def __str__(self):
        return f"{self.name} -- {self.utf8}"
