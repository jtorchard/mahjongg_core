from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.widgets import Placeholder, Header, Footer

from src.game import Game
from src.tui.player_info import PlayerInfo


class PlaceholderApp(App):
    CSS_PATH = "src/tui/tcss/app_tui_grid.tcss"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.g = Game(seed=69)

    def action_update_players(self):
        players = self.g.current_state["players"]
        for pi in self.query(PlayerInfo):
            pi.update_info({
                "name": players[pi.player_number-1]["name"],
                "score": str(players[pi.player_number-1]["score"]),
                "seat": str(players[pi.player_number-1]["seat"]),
            })

    def on_ready(self):
        self.action_update_players()

    def compose(self) -> ComposeResult:
        yield Header(id="header")

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
                    Placeholder(variant="text", id="game_info"),
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
                Placeholder(variant="text", id="tiles"),
                Placeholder(variant="text", id="log"),
                id="tiles_and_log",
            ),
            id="content",
        )

        yield Footer(id="footer")


if __name__ == "__main__":
    app = PlaceholderApp()
    app.run()
