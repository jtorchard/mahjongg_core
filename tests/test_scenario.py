"""
    Tests general play-through scenarios.
    Simulated play-through of a full game, etc.
"""

import pytest

from src.game import Game


@pytest.fixture
def game_fixed_seed():
    return Game(seed=69)


def test_game_scenario(game_fixed_seed):
    game_fixed_seed.deal()
