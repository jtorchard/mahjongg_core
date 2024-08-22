from core.wall import Wall


def test_wall_has_correct_number_of_tiles(wall=Wall()):
    assert len(wall) == 144


def test_wall_is_shuffled(wall=Wall()):
    assert wall.is_shuffled is True


def test_wall_is_not_shuffled(wall=Wall(shuffle_wall=False)):
    assert wall.is_shuffled is False


def test_dead_wall_is_16_tiles(wall=Wall()):
    assert len(wall.dead_tiles) == 14


def test_alive_wall_is_152_tiles_after_break(wall=Wall()):
    assert len(wall.alive_tiles) == (144 - 16)


def test_alive_wall_is_151_tiles_after_taking(wall=Wall()):
    wall.take_live_wall()
    assert len(wall.alive_tiles) == 127


def test_dead_wall_is_15_tiles_after_taking(wall=Wall()):
    wall.take_dead_wall()
    assert len(wall.dead_tiles) == 13


def test_2_loose_tiles(wall=Wall()):
    assert len(wall.loose_tiles) == 2
