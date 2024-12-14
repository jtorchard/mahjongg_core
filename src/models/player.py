from typing import List

from pydantic import BaseModel, Field

from .tile import Tile
from .wind import Wind


# noinspection PyDataclass
class Player(BaseModel):
    seat: Wind
    number: int = Field(gt=0, lt=5)
    hand: List[Tile] = Field(default_factory=list)
    score: int = 2000
