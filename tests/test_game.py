from core.game import Game


def test_in_progress_is_false_by_default(game=Game()):
    assert game.in_progress is False


def test_hand_is_1_by_default(game=Game()):
    assert game.hand == 1


def test_round_is_east_by_default(game=Game()):
    assert game.round == "East"


def test_turn_is_east_by_default(game=Game()):
    assert game.turn == "East"


def test_players_list_has_four_entries(game=Game()):
    assert len(game.players) == 4


def test_wall_is_initialised(game=Game()):
    assert len(game.wall) == 144


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
    assert len(game.seats["East"].get_hand()) == 14
    assert len(game.seats["South"].get_hand()) == 13
    assert len(game.seats["West"].get_hand()) == 13
    assert len(game.seats["North"].get_hand()) == 13


def test_seats_are_correct_when_not_randomised(game=Game(randomise_seats=False)):
    assert str(game.seats["East"]) == "player_1"
    assert str(game.seats["South"]) == "player_2"
    assert str(game.seats["West"]) == "player_3"
    assert str(game.seats["North"]) == "player_4"


def test_change_seats_moves_to_correct_seats(game=Game(randomise_seats=False)):
    game.change_seats()
    assert str(game.seats["East"]) == "player_4"
    assert str(game.seats["South"]) == "player_1"
    assert str(game.seats["West"]) == "player_2"
    assert str(game.seats["North"]) == "player_3"
    game.change_seats()
    assert str(game.seats["East"]) == "player_3"
    assert str(game.seats["South"]) == "player_4"
    assert str(game.seats["West"]) == "player_1"
    assert str(game.seats["North"]) == "player_2"
    game.change_seats()
    assert str(game.seats["East"]) == "player_2"
    assert str(game.seats["South"]) == "player_3"
    assert str(game.seats["West"]) == "player_4"
    assert str(game.seats["North"]) == "player_1"
    game.change_seats()
    assert str(game.seats["East"]) == "player_1"
    assert str(game.seats["South"]) == "player_2"
    assert str(game.seats["West"]) == "player_3"
    assert str(game.seats["North"]) == "player_4"
