import pytest

from core.tile import Tile


@pytest.fixture
def east_wind():
    return Tile("🀀")
