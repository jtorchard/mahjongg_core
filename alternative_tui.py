from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical, Center
from textual.widgets import Footer, Header, Static


class GameApp(App):

    CSS_PATH = "src/tui/tcss/alternative_tui.tcss"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        yield Header()

        with Vertical():

            with Horizontal():
                with Center():
                    yield Static("player_info_top", id="pi_top", classes="player_info")

            with Horizontal():
                yield Static("player_info_middle_left", id="pi_middle_left", classes="player_info")
                with Center():
                    yield Static("wall and discards", id="wall_and_discards", classes="")
                yield Static("player_info_middle_right", id="pi_middle_right", classes="player_info")

            with Center():
                yield Static("tiles", id="tiles")

            with Center():
                yield Static("player_info_bottom", id="pi_bottom", classes="player_info")

            yield Static("logger", id="logger")

        yield Footer()

    def action_toggle_dark(self) -> None:
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )


if __name__ == "__main__":
    app = GameApp()
    app.run()
