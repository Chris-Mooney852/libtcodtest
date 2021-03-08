import numpy as np
from tcod.console import Console

import tile_types

class GameMap:
    def __init__(self, width: int, height: int):
        self.width, self.height = width, height
        self.tiles = np.full((width, height), fill_value=tile_types.wall, order="F")

        self.visible = np.full((width, height), fill_value=False, order="F") # Tiles the player can see
        self.explored = np.full((width, height), fill_value=False, order="F") # Tiles the player has seen already

    def in_bounds(self, x: int, y: int) -> bool:
        """ Return true if x and y are inside the bounds of the map """
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self, console: Console) -> None:
        """
        Renders the map

        If a tile is in the visible array, draw it with the light color
        If it isnt, but is in the expolored array, then draw it with dark
        Else its the default SHROUD
        """
        console.tiles_rgb[0:self.width, 0:self.height] = np.select(
            condlist=[self.visible, self.explored],
            choicelist=[self.tiles["light"], self.tiles["dark"]],
            default=tile_types.SHROUD
        )