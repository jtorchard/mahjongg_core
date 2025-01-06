from textual.app import App, ComposeResult

from src.game import Game
from src.tui.player_hand import PlayerHand


class MyApp(App):
    CSS_PATH = "src/tui/tcss/widget_testbed.tcss"
    BINDINGS = [("u", "update_players", "Update Player")]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.g = Game(seed=69)
        self.g.deal()

    def action_update_players(self):
        self.g = Game(seed=None)
        self.g.deal()
        player_1 = self.g.current_state["players"][0]
        pi = self.query_one("#player_hand")
        pi.update_hand(self.g.hand_as_str(player_1["hand"]["tiles"]))
        # for pi in self.query(PlayerInfo):
        #     pi.update_info({
        #         "name": players[pi.player_number-1]["name"],
        #         "score": str(players[pi.player_number-1]["score"]),
        #         "seat": str(players[pi.player_number-1]["seat"]),
        #     })

    def on_ready(self):
        self.action_update_players()

    def compose(self) -> ComposeResult:
        yield PlayerHand(id="player_hand")


if __name__ == "__main__":
    app = MyApp()
    app.run()
