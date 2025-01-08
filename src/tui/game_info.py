from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widget import Widget
from textual.widgets import Label


class GameInfo(Widget):
    def update(self, data):
        self.query_one("#total_hands").update(data["hand"])
        self.query_one("#round").update(data["round"])
        self.query_one("#round_progress").update(f"{data["round_progress"]}/4")
        self.query_one("#wall_tiles").update("🀆" * data["wall_tiles"])
        self.query_one("#wall_tiles_count").update(str(data["wall_tiles"]))
        self.query_one("#discards").update(data["discards"])

    def compose(self) -> ComposeResult:
        yield Horizontal(
            Vertical(
                Label("XXXXX", classes="game_info", id="total_hands"),
                Label("XXXXX", classes="game_info", id="round"),
                Label("XXXXX", classes="game_info", id="round_progress"),
                id="hand_round",
            ),
            Vertical(
                Label("XXXXX", classes="game_info", id="wall_tiles"),
                Label("XXXXX", classes="game_info", id="wall_tiles_count"),
                Label("XXXXX", classes="game_info", id="discards"),
                id="wall_discards",
            ),
        )
