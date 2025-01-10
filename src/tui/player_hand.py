from textual import events
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
        for gui_tile in self.query("Tile"):
            gui_tile.remove_class("selected")

        event.button.add_class("selected")

    def _on_enter(self, event: events.Enter) -> None:
        event.node.add_class("tile_hover")

    def _on_leave(self, event: events.Enter) -> None:
        event.node.remove_class("tile_hover")

    def update_tiles(self, tiles):
        for gui_tile in self.query("Tile"):
            gui_tile.remove()
        tiles.sort()

        for game_tile in tiles:
            self.query_one("#tile_container").mount(Tile(game_tile=game_tile))

        for gui_tile in self.query("Tile"):
            utf8 = gui_tile.game_tile.utf8
            gui_tile.label = f"{self.UTF8_TO_TEXT[utf8]}  {utf8}"

    def compose(self) -> ComposeResult:
        yield Horizontal(id="tile_container")
