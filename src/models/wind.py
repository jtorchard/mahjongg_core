from enum import IntEnum


class Wind(IntEnum):
    EAST = 1
    SOUTH = 2
    WEST = 3
    NORTH = 4

    def __str__(self) -> str:
        return self.name

    def next(self):
        try:
            wind = Wind(self.value + 1)
        except ValueError:
            wind = Wind.EAST
        return wind

    def previous(self):
        try:
            wind = Wind(self.value - 1)
        except ValueError:
            wind = Wind.NORTH
        return wind
