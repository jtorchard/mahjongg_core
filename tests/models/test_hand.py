import pytest

from src.exceptions import InvalidObjectForHand
from models.hand import Hand
from models.tile import EastWind, GreenDragon, RedDragon


def test_hand_has_correct_defaults():
    hand = Hand()
    assert hand.one_chance_hand is False
    assert hand.can_go_out is False
    assert hand.wind_of_the_round is False
    assert hand.chows == 0
    assert hand.concealed_pungs == 0
    assert hand.concealed_kongs == 0
    assert hand.exposed_pungs == 0
    assert hand.exposed_kongs == 0
    assert hand.pairs == 0
    assert hand.seasons == 0
    assert hand.flowers == 0


def test_init_item_with_list_succeeds():
    hand = Hand([EastWind(), GreenDragon()])
    assert hand == [EastWind(), GreenDragon()]


def test_set_item_succeeds():
    hand = Hand([EastWind(), GreenDragon()])
    hand[0] = RedDragon()
    assert hand[0] == RedDragon()


def test_set_item_with_non_tile_raises_error():
    hand = Hand([EastWind(), GreenDragon()])
    with pytest.raises(InvalidObjectForHand):
        hand[0] = 1
