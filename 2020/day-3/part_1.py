from typing import TextIO
from common import multiply_trees, Strategy


def count_slope_trees(toboggan_map: TextIO):
    return multiply_trees(toboggan_map, [Strategy(3, 1)])
