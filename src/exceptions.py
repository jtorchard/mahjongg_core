class MahjongException(Exception):
    pass


class InvalidObjectForHand(MahjongException, ValueError):
    message = "Mahjong hand can only contain Tiles."
