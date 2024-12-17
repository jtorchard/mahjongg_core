from models.hand import Hand


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
