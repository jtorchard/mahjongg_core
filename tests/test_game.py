from core.game import Game


def test_in_progress_is_false_by_default(game=Game()):
    assert game.in_progress is False


def test_hand_is_1_by_default(game=Game()):
    assert game.hand == 1


def test_round_is_east_by_default(game=Game()):
    assert game.round == "east"


def test_turn_is_east_by_default(game=Game()):
    assert game.turn == "east"


def test_players_list_has_four_entries(game=Game()):
    assert len(game.players) == 4


def test_wall_is_initialised(game=Game()):
    assert len(game.wall.alive_tiles + game.wall.dead_tiles + game.wall.loose_tiles) == 144


def test_assign_seats_creates_seat_assignments(game=Game()):
    game.seats = []
    assert game.seats == []
    game.assign_seats()
    assert game.seats


def test_start_marks_game_as_in_progress(game=Game()):
    game.start()
    assert game.in_progress is True


def test_deal_gives_players_correct_tiles(game=Game()):
    game.deal()
    assert len(game.seats["east"].get_hand()) == 14
    assert len(game.seats["south"].get_hand()) == 13
    assert len(game.seats["west"].get_hand()) == 13
    assert len(game.seats["north"].get_hand()) == 13


def test_seats_are_correct_when_not_randomised(game=Game(randomise_seats=False)):
    assert str(game.seats["east"]) == "player_1"
    assert str(game.seats["south"]) == "player_2"
    assert str(game.seats["west"]) == "player_3"
    assert str(game.seats["north"]) == "player_4"


def test_change_seats_does_nothing_if_game_not_atarted(game=Game(randomise_seats=False)):
    game.change_seats()
    assert str(game.seats["east"]) == "player_1"
    assert str(game.seats["south"]) == "player_2"
    assert str(game.seats["west"]) == "player_3"
    assert str(game.seats["north"]) == "player_4"


def test_change_seats_moves_to_correct_seats(game=Game(randomise_seats=False)):
    game.start()
    game.change_seats()
    assert str(game.seats["east"]) == "player_4"
    assert str(game.seats["south"]) == "player_1"
    assert str(game.seats["west"]) == "player_2"
    assert str(game.seats["north"]) == "player_3"
    game.change_seats()
    assert str(game.seats["east"]) == "player_3"
    assert str(game.seats["south"]) == "player_4"
    assert str(game.seats["west"]) == "player_1"
    assert str(game.seats["north"]) == "player_2"
    game.change_seats()
    assert str(game.seats["east"]) == "player_2"
    assert str(game.seats["south"]) == "player_3"
    assert str(game.seats["west"]) == "player_4"
    assert str(game.seats["north"]) == "player_1"
    game.change_seats()
    assert str(game.seats["east"]) == "player_1"
    assert str(game.seats["south"]) == "player_2"
    assert str(game.seats["west"]) == "player_3"
    assert str(game.seats["north"]) == "player_4"
