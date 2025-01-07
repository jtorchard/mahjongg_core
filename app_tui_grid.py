from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.widgets import Placeholder, Footer

from src.game import Game
from src.tui.player_info import PlayerInfo
from src.tui.player_hand import PlayerHand
from src.tui.game_info import GameInfo


class PlaceholderApp(App):
    CSS_PATH = "src/tui/tcss/app_tui_grid.tcss"
    BINDINGS = [
        ("r", "randomise_seats", "Randomise Player Seats"),
        ("d", "deal", "Deal tiles"),
        ("t", "discard_tile", "Discard Tile"),
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.g = Game(seed=None)

    def action_randomise_seats(self):
        self.g.randomise_seats()
        self.update_players()

    def action_discard_tile(self):
        ph = self.query_one("#player_hand")
        self.g.current_state["players"][0]["hand"]["tiles"].pop()
        self.update_hand()

    def action_deal(self):
        self.g.deal()
        self.update_players()

    def update_hand(self):
        players = self.g.current_state["players"]
        tiles = players[0]["hand"]["tiles"]
        ph = self.query_one("#player_hand")
        ph.update_tiles([t.utf8 for t in tiles])

    def update_players(self):
        players = self.g.current_state["players"]
        for pi in self.query(PlayerInfo):
            pi.update_info({
                "name": players[pi.player_number-1]["name"],
                "score": str(players[pi.player_number-1]["score"]),
                "seat": str(players[pi.player_number-1]["seat"]),
            })

    def update_game_info(self):
        self.query_one(GameInfo).update({
            "hand": str(self.g.current_state["hand"]),
            "round": str(self.g.current_state["round"]),
            "round_progress": str(self.g.current_state["seating_counter"]),
            "wall_tiles": len(self.g.current_state["live_wall"]),
        })

    def on_ready(self):
        self.g.deal()
        self.update_players()
        self.update_hand()
        self.update_game_info()

    def compose(self) -> ComposeResult:
        yield Vertical(
            Container(
                Horizontal(
                    Placeholder(variant="size", id="blank_1", classes="blank"),
                    PlayerInfo(player_number=3, id="player_info_top", classes="player_info"),
                    Placeholder(variant="size", id="blank_2", classes="blank"),
                    id="c1",
                ),
                Horizontal(
                    PlayerInfo(player_number=4, id="player_info_left", classes="player_info"),
                    GameInfo(id="game_info"),
                    PlayerInfo(player_number=2, id="player_info_right", classes="player_info"),
                    id="c2",
                ),
                Horizontal(
                    Placeholder(variant="size", id="blank_3", classes="blank"),
                    PlayerInfo(player_number=1, id="player_info_bottom", classes="player_info"),
                    Placeholder(variant="size", id="blank_4", classes="blank"),
                    id="c3",
                ),
                id="player_info_and_wall",
            ),
            Container(
                Placeholder(id="left_tiles", classes="blank"),
                PlayerHand(id="player_hand"),
                Placeholder(id="right_tiles", classes="blank"),
                Placeholder(variant="text", id="log"),
                id="tiles_and_log",
            ),
            id="content",
        )

        yield Footer(id="footer")


if __name__ == "__main__":
    app = PlaceholderApp()
    app.run()
