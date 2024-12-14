"""
Contains data for each hand played.
"""

from typing import List

from models.tile import Tile


class Hand:
    def __init__(self):
        self.tiles: List[Tile] = []

    def from_unicode_string(self, string: str) -> None:
        self.tiles = [Tile(s) for s in string]

    def __getitem__(self, index: int) -> Tile:
        return self.tiles[index]

    def __len__(self) -> int:
        return len(self.tiles)

    def __str__(self) -> str:
        return " ".join([t.utf8 for t in self.tiles])
