from dataclasses import dataclass
from io import StringIO
from typing import List, Tuple


@dataclass
class Bingo:
    numbers_to_draw: List[int]
    cards: List[Tuple[int, bool]]

    def __init__(self, bingo_info: StringIO) -> None:
        numbers, cards = self.parse_info(bingo_info)
        self.numbers_to_draw = numbers
        self.cards = cards

    def parse_info(self, bingo_info: StringIO) -> Tuple[List[int], List[Tuple[int, bool]]]:
        raw_numbers = next(bingo_info).split(',')
        numbers = list(map(int, raw_numbers))
        next(bingo_info)  # it throws away first empty line

        cards = []
        curr_card = []
        
        for line in bingo_info:
            if line == '\n':
                cards.append(curr_card)
                curr_card = []
            
            curr_card += [(item, 0) for item in map(int, line.split())]
        cards.append(curr_card)

        return numbers, cards


def calculate_score(bingo_info: StringIO) -> int:
    bingo = Bingo(bingo_info)

    return bingo.numbers_to_draw, bingo.cards



# parser numbers_to_draw and bingo cards
# draw numbers and mark it on bingo cards ## [[(orig_num[int], marked[bool])]]
# check to find if there is a bingo!
# calculate score
