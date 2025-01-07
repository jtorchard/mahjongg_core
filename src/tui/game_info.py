from textual.app import ComposeResult
from textual.containers import Vertical, Horizontal
from textual.widget import Widget
from textual.widgets import Placeholder, Label

from .tile import Tile


class GameInfo(Widget):

    def update(self, data):
        self.query_one("#total_hands").update(data["hand"])
        self.query_one("#round").label = (data["round"])
        self.query_one("#round_progress").update(f"{data["round_progress"]}/4")
        self.query_one("#wall_tiles").update("🀆" * data["wall_tiles"] + '+++')


    def compose(self) -> ComposeResult:
        yield Horizontal(
            Vertical(
                Label("1", classes="game_info", id="total_hands"),
                Tile("E", classes="game_info", id="round"),
                Label("XXXXX", classes="game_info", id="round_progress"),
                id="hand_round",
            ),
            Vertical(
                Label("XXXXX", classes="game_info", id="wall_tiles"),
                Placeholder(variant="size", classes="game_info", id="discards"),
                id="wall_discards",
            )
        )
