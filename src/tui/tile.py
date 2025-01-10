from textual import events
from textual.widgets import Button


class Tile(Button):

    def __init__(self, game_tile):
        super().__init__()
        self.game_tile = game_tile
