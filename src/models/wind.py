"""
    Wind class represents the four winds.
    Maintains the correct ordering which is used to determine
    seating, seat changes, wind of round changes, and play order.
    Wind order and numeric assignments with corresponding flowers
    and seasons:

         1        2        3       4
        East -> South -> West -> North

        Plum -> Orchid -> Chrysanthemum -> Bamboo

        Spring -> Summer -> Autumn -> Winter
"""
from enum import IntEnum


class Wind(IntEnum):
    EAST = 1
    SOUTH = 2
    WEST = 3
    NORTH = 4

    def __str__(self):
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
