"""
    Handles the tiles in a player's hand.
    Ordering, sorting, determining special cases etc.
"""
from collections import Counter, UserList
from functools import wraps
from typing import Any, Callable, Dict, List, SupportsIndex

from loguru import logger

from .tile import Tile

logger.remove()  # Turn off default console logger
logger.add("mahjong.log", colorize=True, level="INFO")


def hand_mutated(func: Callable) -> Callable:
    @wraps(func)
    def inner(self: Hand, *args: Any, **kwargs: Dict[Any, Any]) -> None:
        func(self, *args, **kwargs)
        self.analyse_hand(*args, **kwargs)

    return inner


class Hand(UserList):
    def __init__(self, *args: Any, **kwargs: Dict[Any, Any]) -> None:
        super().__init__(*args, **kwargs)
        self.one_chance_hand: bool = False
        self.can_go_out: bool = False
        self.wind_of_the_round: bool = False
        self.chows: int = 0
        self.concealed_pungs:int = 0
        self.concealed_kongs:int = 0
        self.exposed_pungs: int = 0
        self.exposed_kongs:int = 0
        self.pairs:int = 0
        self.seasons:int = 0
        self.flowers:int = 0

    def __setitem__(self, i: SupportsIndex | slice, item: object) -> None:
        if not isinstance(item, Tile):
            raise NotImplementedError()
        self.data[i] = item

    def __delitem__(self, i: SupportsIndex | slice) -> None:
        del self.data[i]

    @hand_mutated
    def append(self, item: object) -> None:
        if not isinstance(item, Tile):
            raise NotImplementedError()
        self.data.append(item)

    @hand_mutated
    def remove(self, i: int) -> None:
        self.data.remove(i)

    @hand_mutated
    def pop(self, i: int = -1) -> None:
        self.data.pop(i)

    @hand_mutated
    def insert(self, i: int, item: object) -> None:
        if not isinstance(item, Tile):
            raise NotImplementedError()
        self.data.insert(i, item)

    @hand_mutated
    def extend(self, other: List[object]) -> None:
        if other and not isinstance(other[0], Tile):
            raise NotImplementedError()
        self.data.extend(other)

    def __str__(self) -> str:
        return " ".join([t.utf8 for t in self.data])

    def analyse_hand(self, *args: Any, **kwargs: Dict[Any, Any]) -> None:
        logger.info(f"Hand changed. args: {args} kwargs: {kwargs} - Analysing hand...")
        c: Counter = Counter(self.data)
        logger.info(f"Potential Pairs: {list(filter(lambda a: a[1] >= 2, c.items()))}")
        logger.info(f"Tiles: |{'| |'.join([f'{k.name}:{v}' for k, v in c.items()])}|")
