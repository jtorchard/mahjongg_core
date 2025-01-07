from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.reactive import reactive
from textual.widget import Widget
from textual.widgets import Button

from .tile import Tile


class PlayerHand(Widget):
    CSS_PATH = "tcss/player_hand.tcss"

    tiles_utf8 = reactive("xxxxx")
    tiles = reactive("xxxxx")
    tile_list = []
    UTF8_TO_TEXT = {
        '🀀': 'e',
        '🀁': 's',
        '🀂': 'w',
        '🀃': 'n',
        '🀄': 'rd',
        '🀅': 'gd',
        '🀆': 'wd',
        '🀢': 'pf',
        '🀣': 'of',
        '🀤': 'bf',
        '🀥': 'cf',
        '🀦': 'sus',
        '🀧': 'sps',
        '🀨': 'as',
        '🀩': 'ws',
        '🀐': '1b',
        '🀑': '2b',
        '🀒': '3b',
        '🀓': '4b',
        '🀔': '5b',
        '🀕': '6b',
        '🀖': '7b',
        '🀗': '8b',
        '🀘': '9b',
        '🀙': '1d',
        '🀚': '2d',
        '🀛': '3d',
        '🀜': '4d',
        '🀝': '5d',
        '🀞': '6d',
        '🀟': '7d',
        '🀠': '8d',
        '🀡': '9d',
        '🀇': '1c',
        '🀈': '2c',
        '🀉': '3c',
        '🀊': '4c',
        '🀋': '5c',
        '🀌': '6c',
        '🀍': '7c',
        '🀎': '8c',
        '🀏': '9c',
    }

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Event handler called when a button is pressed."""
        event.button.add_class("clicked")

    def update_tiles(self, tiles):
        tiles.sort()
        while len(self.query("Tile")) < len(tiles):
            self.query_one("#tile_container").mount(Tile())

        button_count = len(self.query("Tile"))
        tile_count = len(tiles)
        if button_count != tile_count:
            for _ in range(button_count - tile_count):
                self.query("Tile").last().remove()

        for button, tile in zip(self.query("Tile"), tiles):
            button.label = f"{self.UTF8_TO_TEXT[tile]}  {tile}"

    def compose(self) -> ComposeResult:
        yield Horizontal(id="tile_container")
