from textual.app import ComposeResult
from textual.containers import Vertical, Horizontal
from textual.widget import Widget
from textual.widgets import Placeholder


class GameInfo(Widget):

    def compose(self) -> ComposeResult:
        yield Horizontal(
            Vertical(
                Placeholder(variant="size", classes="p", id="total_hands"),
                Placeholder(variant="size", classes="p", id="wind"),
                Placeholder(variant="size", classes="p", id="round_progress"),
                id="hand_round",
            ),
            Vertical(
                Placeholder(variant="size", classes="p", id="wall_tiles"),
                Placeholder(variant="size", classes="p", id="discards"),
                id="wall_discards",
            )
        )
