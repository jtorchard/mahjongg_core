"""
    Tests general play-through scenarios.
"""

import pytest

from src.core.big_state import Game


@pytest.fixture
def game_random_seed():
    return Game(seed=None)


@pytest.fixture
def game_fixed_seed():
    return Game(seed=69)


def test_game_scenario(game_fixed_seed):
    game_fixed_seed.deal()
