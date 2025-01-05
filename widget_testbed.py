from textual.app import App, ComposeResult

from src.game import Game
from src.tui.player_info import PlayerInfo


class MyApp(App):
    CSS_PATH = "src/tui/tcss/widget_testbed.tcss"
    BINDINGS = [("u", "update_players", "Update Player")]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.g = Game(seed=69)

    def action_update_players(self):
        players = self.g.current_state["players"]
        for i, pi in enumerate(self.query(PlayerInfo)):
            pi.update_info({
                "name": players[i]["name"],
                "score": str(players[i]["score"]),
                "seat": str(players[i]["seat"]),
            })

    def on_ready(self):
        self.action_update_players()

    def compose(self) -> ComposeResult:
        yield PlayerInfo(player_number=1, id="player_1")
        yield PlayerInfo(player_number=2, id="player_2")
        yield PlayerInfo(player_number=3, id="player_3")
        yield PlayerInfo(player_number=4, id="player_4")


if __name__ == "__main__":
    app = MyApp()
    app.run()
