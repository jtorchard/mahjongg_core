"""
    Custom exception classes specific to Mahjong.
"""


class MahjongException(Exception):
    pass


class InvalidObjectForHand(MahjongException, ValueError):
    message = "Mahjong hand can only contain Tiles."


class InvalidPlayerNumber(MahjongException):
    pass
