import pytest

from src.core.player import Player
from src.core.tile import Tile
from src.core.data import east_wind


@pytest.mark.parametrize("number, name, score", [(1, "player_1", 2000),
                                          (2, "player_2", 2000),
                                          (3, "player_3", 2000),
                                          (4, "player_4", 2000)])
def test_player_has_correct_defaults(number, name, score):
    player = Player(number, starting_score=score)
    assert player.player_id == number
    assert player.score == score
    assert player.hand == []
    assert str(player) == name


def test_hand_has_tile_after_adding(player=Player(1)):
    player.add_tile(Tile(east_wind))
    assert player.hand == [Tile(east_wind)]


def test_hand_looses_tile_after_removing(player=Player(1)):
    player.add_tile(Tile(east_wind))
    assert player.hand == [Tile(east_wind)]
    player.remove_tile(0)
    assert player.hand == []


def test_player_with_invalid_id_raises_error():
    with pytest.raises(ValueError):
        Player(42)
