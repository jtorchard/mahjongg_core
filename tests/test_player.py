import pytest

from core.player import Player
from core.tile import Tile
from core.data import east_wind


@pytest.mark.parametrize("number, name", [(1, "player_1"),
                                          (2, "player_2"),
                                          (3, "player_3"),
                                          (4, "player_4")])
def test_player_has_correct_defaults(number, name):
    player = Player(number)
    assert player.get_id() == number
    assert player.get_score() == 2000  # TODO Get valye from rules
    assert player.get_hand() == []
    assert str(player) == name


def test_hand_has_tile_after_adding(player=Player(1)):
    player.add_tile(Tile(east_wind))
    assert player.get_hand() == [Tile(east_wind)]


def test_hand_looses_tile_after_removing(player=Player(1)):
    player.add_tile(Tile(east_wind))
    assert player.get_hand() == [Tile(east_wind)]
    player.remove_tile(0)
    assert player.get_hand() == []


def test_player_with_invalid_id_raises_error():
    with pytest.raises(ValueError):
        Player(42)
