from textual.app import ComposeResult
from textual.reactive import reactive
from textual.widget import Widget
from textual.widgets import Label, Static, Rule


class PlayerInfo(Widget):
    CSS_PATH = "tcss/player_info.tcss"
    WIND_UTF8 = {
        "EAST": "🀀",
        "SOUTH": "🀁",
        "WEST": "🀂",
        "NORTH": "🀃",
    }

    player_name = reactive("xxxxx")
    score = reactive("xxxxx")
    seat = reactive("xxxxx")

    def __init__(self, player_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.player_number = player_number

    def watch_player_name(self):
        widget = self.query_one("#player_name")
        widget.update(self.player_name)

    def watch_score(self):
        widget = self.query_one("#score")
        widget.update(self.score)

    def watch_seat(self):
        wind = self.WIND_UTF8.get(self.seat, "")
        widget = self.query_one("#seat")
        widget.update(f"{self.seat} -> {wind}")

    def update_info(self, data):
        self.player_name = data["name"]
        self.score = data["score"]
        self.seat = data["seat"]

    def compose(self) -> ComposeResult:
        yield Static(f"Player {self.player_number}", id="player_number")
        yield Label("XXXXX", id="player_name")
        yield Rule(line_style="ascii", id="decoration")
        yield Label("XXXXX", id="score")
        yield Label("XXXXX -> 🀀", id="seat")
