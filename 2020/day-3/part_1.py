from io import StringIO
from typing import List


def parse_map(_map: StringIO) -> List[List[str]]:
    return [list(line.strip()) for line in _map]


def count_trees(toboggan_map: StringIO) -> int:
    # pace right 3 and down 1
    found_trees = 0
    index_x = 0

    parsed_map = parse_map(toboggan_map)
    max_y = len(parsed_map) - 1

    for index_y in range(max_y):  # down walk
        # side walk
        index_x += 3

        if parsed_map[index_y][index_x] == '#':
            found_trees += 1

    return found_trees
