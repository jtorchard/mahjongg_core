import pytest
from pydantic import ValidationError

from models.player import Player
from models.tile import EastWind
from models.wind import Wind


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


def test_player_with_invalid_id_raises_error():
    with pytest.raises(ValidationError):
        Player(seat=Wind.EAST, number=42)
