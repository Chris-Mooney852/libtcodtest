from typing import Tuple

import numpy as np

# graphics structure
graphic_dt = np.dtype(
    [
        ("ch", np.int32), # Unicode codepoint
        ("fg", "3B"), # 3 unsigned bytes for RGB colors
        ("bg", "3B")
    ]
)

# tile structure used for statically defined tile data
tile_dt = np.dtype(
    [
        ("walkable", np.bool), # true if tile can be walked over
        ("transparent", np.bool), # trie if tile doesnt block fov
        ("dark", graphic_dt), # graphics for fog of war tiles
        ("light", graphic_dt), # graphics for when the tile is in FOV
    ]
)

def new_tile(
    *, # enforce keywords so order doesnt matter
    walkable: int,
    transparent: int,
    dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
    light: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:
    """ Helper function for defining individual tiles """
    return np.array((walkable, transparent, dark, light), dtype=tile_dt)

SHROUD = np.array((ord(" "), (255, 255, 255), (0, 0, 0)), dtype=graphic_dt)

floor = new_tile(
    walkable=True, 
    transparent=True, 
    dark=(ord("."), (105, 105, 105), (0, 0, 0)),
    light=(ord("."), (255, 255, 255), (0, 0, 0)),
)

wall = new_tile(
    walkable=False, 
    transparent=False, 
    dark=(ord("#"), (105, 105, 105), (0, 0, 0)),
    light=(ord("#"), (255, 255, 255), (0, 0, 0)),
)