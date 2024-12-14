from typing import List

from faker import Faker
from pydantic import BaseModel, Field

from .tile import Tile
from .wind import Wind


# noinspection PyDataclass
class Player(BaseModel):
    seat: Wind
    name: str = Field(default_factory=lambda: f"{Faker().word()} {Faker().word()}")
    number: int = Field(gt=0, lt=5)
    hand: List[Tile] = Field(default_factory=list)
    score: int = 2000
