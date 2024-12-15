from __future__ import annotations

from enum import IntEnum


class Wind(IntEnum):
    EAST: int = 1
    SOUTH: int = 2
    WEST: int = 3
    NORTH: int = 4

    def __str__(self) -> str:
        return self.name

    def next(self) -> Wind:
        try:
            wind = Wind(self.value + 1)
        except ValueError:
            wind = Wind.EAST
        return wind

    def previous(self) -> Wind:
        try:
            wind = Wind(self.value - 1)
        except ValueError:
            wind = Wind.NORTH
        return wind
