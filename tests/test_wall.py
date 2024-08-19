from core.wall import Wall

def test_east_wind_data_correct(tile=Tile(east_wind)):
    assert tile.utf8 == "🀀"
    assert tile.name == "east_wind"
    assert tile.rank == "east"
    assert tile.suit == "wind"
    assert tile.is_dragon is False
    assert tile.is_wind is True
    assert tile.is_special is False
    assert tile.is_honour is True
    assert tile.is_suit is False
    assert tile.is_terminal is False
