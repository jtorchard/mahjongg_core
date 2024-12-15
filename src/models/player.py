from faker import Faker
from pydantic import BaseModel, Field

from .wind import Wind


class Player(BaseModel):
    seat: Wind
    name: str = Field(default_factory=lambda: f"{Faker().word()} {Faker().word()}")
    number: int = Field(gt=0, lt=5)
    hand: list = Field(default_factory=list)
    score: int = 2000
