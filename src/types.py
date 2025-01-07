from typing import Tuple, List, NamedTuple

# Type definitions
ColorRGB = Tuple[int, int, int]
ColorOptions = List[ColorRGB]

class GameState(NamedTuple):
    target_color: ColorRGB
    options: ColorOptions
    score: int
    needs_new_round: bool