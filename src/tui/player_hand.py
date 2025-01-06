from textual.app import ComposeResult
from textual.reactive import reactive
from textual.widget import Widget
from textual.widgets import Label


class PlayerHand(Widget):
    CSS_PATH = "tcss/player_hand.tcss"

    tiles_utf8 = reactive("xxxxx")
    tiles = reactive("xxxxx")
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

    def watch_tiles_utf8(self):
        widget = self.query_one("#player_tiles_uft8")
        widget.update(self.tiles_utf8)

    def watch_tiles(self):
        widget = self.query_one("#player_tiles")
        widget.update(self.tiles)

    def update_hand(self, tiles):
        self.tiles_utf8 = " || ".join([t for t in tiles])
        self.tiles = " || ".join([self.UTF8_TO_TEXT[t] for t in tiles])

    def compose(self) -> ComposeResult:
        yield Label("XXXXX", id="player_tiles_uft8")
        yield Label("XXXXX", id="player_tiles")
