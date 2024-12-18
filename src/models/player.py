from faker import Faker
from pydantic import BaseModel, Field

from .wind import Wind


class Player(BaseModel):
    seat: Wind
    name: str = Field(default_factory=lambda: f"{Faker().word().title()} {Faker().word().title()}")
    number: int = Field(gt=0, lt=5)
    hand: list = Field(default_factory=list)
    score: int = 2000

#
# class Player:
#
#     def __init__(self):
#         self.seat = None
#         self.name = ""
#         self.number = 1
#         self.hand = []
#         self.score = 2000
