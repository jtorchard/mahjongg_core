from core.wall import Wall


def test_wall_has_correct_number_of_tiles(wall=Wall()):
    assert len(wall) == 168
