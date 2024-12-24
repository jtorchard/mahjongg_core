import pytest

from src.exceptions import InvalidObjectForHand
from src.models.hand import Hand
from src.models.tile import EastWind, GreenDragon, RedDragon, NorthWind, OneCharacter, WhiteDragon


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


def test_str_representation():
    hand = Hand([EastWind(), GreenDragon()])
    assert str(hand) == "🀀 🀅"


def test_init_with_list_succeeds():
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


def test_delete_item_removes_item():
    hand = Hand([EastWind(), GreenDragon()])
    del hand[1]
    assert len(hand) == 1


def test_append_item_with_non_tile_raises_error():
    hand = Hand([EastWind(), GreenDragon()])
    with pytest.raises(InvalidObjectForHand):
        hand.append(42)


def test_append_with_tile_succeeds():
    hand = Hand([EastWind(), GreenDragon()])
    hand.append(NorthWind())
    assert hand == Hand([EastWind(), GreenDragon(), NorthWind()])


def test_remove_item_removes_item():
    hand = Hand([EastWind(), OneCharacter(), GreenDragon()])
    hand.remove(OneCharacter())
    assert hand == Hand([EastWind(), GreenDragon()])


def test_remove_item_with_missing_item_raises_error():
    hand = Hand([EastWind(), OneCharacter(), GreenDragon()])
    with pytest.raises(ValueError):
        hand.remove(RedDragon())


def test_pop_item_removes_item():
    hand = Hand([EastWind(), OneCharacter(), GreenDragon()])
    hand.pop(1)
    assert hand == Hand([EastWind(), GreenDragon()])


def test_pop_item_with_missing_item_raises_error():
    hand = Hand([EastWind(), OneCharacter(), GreenDragon()])
    with pytest.raises(IndexError):
        hand.pop(3)


def test_pop_item_with_no_argument_removes_last_item():
    hand = Hand([EastWind(), OneCharacter(), GreenDragon()])
    hand.pop()
    assert hand == Hand([EastWind(), OneCharacter()])


def test_insert_item_succeeds():
    hand = Hand([EastWind(), OneCharacter(), GreenDragon()])
    hand.insert(1, WhiteDragon())
    assert hand == Hand([EastWind(), WhiteDragon(), OneCharacter(), GreenDragon()])


def test_insert_non_tile_raises_error():
    hand = Hand([EastWind(), OneCharacter(), GreenDragon()])
    with pytest.raises(InvalidObjectForHand):
        hand.insert(1, 42)


def test_extend_with_list_of_tiles_succeeds():
    hand = Hand([EastWind(), OneCharacter(), GreenDragon()])
    hand.extend([WhiteDragon()])
    assert hand == Hand([EastWind(), OneCharacter(), GreenDragon(), WhiteDragon()])


def test_extend_with_list_of_non_tiles_raises_error():
    hand = Hand([EastWind(), OneCharacter(), GreenDragon()])
    with pytest.raises(InvalidObjectForHand):
        hand.extend([1, 2])
