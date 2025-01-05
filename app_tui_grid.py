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
                    Placeholder(variant="size", id="col1"),
                    Placeholder(variant="text", id="col2"),
                    Placeholder(variant="size", id="col3"),
                    id="c1",
                ),
                Horizontal(
                    Placeholder(variant="size", id="col4"),
                    Placeholder(variant="text", id="col5"),
                    Placeholder(variant="size", id="col6"),
                    id="c2",
                ),
                Horizontal(
                    Placeholder(variant="size", id="col7"),
                    Placeholder(variant="text", id="col8"),
                    Placeholder(variant="size", id="col9"),
                    id="c3",
                ),
                id="top",
            ),
            Container(
                Placeholder(variant="text", id="tiles"),
                Placeholder(variant="text", id="log"),
                id="bot",
            ),
            id="content",
        )

        yield Footer(id="footer")


if __name__ == "__main__":
    app = PlaceholderApp()
    app.run()
