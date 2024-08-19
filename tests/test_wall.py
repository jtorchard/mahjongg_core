from core.wall import Wall


def test_wall_has_correct_number_of_tiles(wall=Wall()):
    assert len(wall) == 168


def test_wall_is_shuffled(wall=Wall()):
    assert wall.is_shuffled is True


def test_wall_is_not_shuffled(wall=Wall(shuffle_wall=False)):
    assert wall.is_shuffled is False
