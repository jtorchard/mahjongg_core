"""
    Tests for player class.
"""

import pytest

from src.exceptions import InvalidPlayerNumber
from src.models.player import Player
from src.models.tile import EastWind
from src.models.wind import Wind


@pytest.mark.parametrize(
    "number, name, score",
    [
        (1, "player_1", 2000),
        (2, "player_2", 2000),
        (3, "player_3", 2000),
        (4, "player_4", 2000),
    ],
)
def test_player_has_correct_defaults(number, name, score):
    player = Player(seat=Wind.EAST, number=number)
    assert player.number == number
    assert player.score == score
    assert player.hand == []


def test_hand_has_tile_after_adding(player=Player(seat=Wind.EAST, number=1)):
    player.hand.append(EastWind())
    assert player.hand == [EastWind()]


def test_hand_looses_tile_after_removing(player=Player(seat=Wind.EAST, number=1)):
    player.hand.append(EastWind())
    assert player.hand == [EastWind()]
    player.hand.pop()
    assert player.hand == []


@pytest.mark.parametrize("number", [42, 5, 0, -1])
def test_player_with_invalid_numbers_raises_error(number):
    with pytest.raises(InvalidPlayerNumber):
        Player(seat=Wind.EAST, number=number)
