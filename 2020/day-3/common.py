from dataclasses import dataclass
from typing import TextIO, List


@dataclass
class Strategy:
    side_walk: int
    down_walk: int


def count_trees(toboggan_map: List[List[str]], strategy: Strategy) -> int:
    found_trees = 0
    index_x = 0

    max_y = len(toboggan_map)
    max_x = len(toboggan_map[0])

    for index_y in range(strategy.down_walk, max_y, strategy.down_walk):
        index_x = (index_x + strategy.side_walk) % max_x

        if toboggan_map[index_y][index_x] == '#':
            found_trees += 1

    return found_trees


def multiply_trees(toboggan_map: TextIO, strategies: List[Strategy]) -> int:
    found_trees = 1
    parsed_map = [list(line.strip()) for line in toboggan_map]

    for strategy in strategies:
        trees_qtd = count_trees(parsed_map, strategy)
        found_trees *= trees_qtd

    return found_trees
