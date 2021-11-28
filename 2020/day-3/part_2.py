from typing import TextIO
from common import multiply_trees, Strategy


def multiply_all_slopes_trees(toboggan_map: TextIO):
    strategies = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    return multiply_trees(toboggan_map, [Strategy(*s) for s in strategies])
