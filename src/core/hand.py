"""
    Handles the tiles in a player's hand.
    Ordering, sorting, determining special cases etc.
"""
from typing import List

from src.models.tile import Tile


class Hand:
    def __init__(self) -> None:
        self._tiles: List[Tile] = []

    def __getitem__(self, index: int) -> Tile:
        return self._tiles[index]

    def __len__(self) -> int:
        return len(self._tiles)

    def __str__(self) -> str:
        return " ".join([t.utf8 for t in self._tiles])

    def tiles(self):
        return self._tiles
