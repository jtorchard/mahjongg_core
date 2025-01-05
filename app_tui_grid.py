from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.widgets import Placeholder, Header, Footer


class PlaceholderApp(App):
    CSS_PATH = "src/tui/tcss/app_tui_grid.tcss"

    def on_ready(self) -> None:
        pass

    def compose(self) -> ComposeResult:
        yield Header(id="header")

        yield Vertical(
            Container(
                Horizontal(
                    Placeholder(variant="size", id="blank_1", classes="blank"),
                    Placeholder(variant="text", id="player_info_top", classes="player_info"),
                    Placeholder(variant="size", id="blank_2", classes="blank"),
                    id="c1",
                ),
                Horizontal(
                    Placeholder(variant="size", id="player_info_left", classes="player_info"),
                    Placeholder(variant="text", id="game_info"),
                    Placeholder(variant="size", id="player_info_right", classes="player_info"),
                    id="c2",
                ),
                Horizontal(
                    Placeholder(variant="size", id="blank_3", classes="blank"),
                    Placeholder(variant="text", id="player_info_bottom", classes="player_info"),
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
