from dataclasses import dataclass, field
from functools import reduce
from io import StringIO
from itertools import filterfalse, islice
from typing import List, Tuple

# It needs full refactor :grimacing
@dataclass
class Bingo:
    numbers_to_draw: List[int]
    boards: List[List[int]]
    curr_idx: int = 0
    winner_board: List[int] = field(default_factory=list)
    has_winner: bool = False

    def __init__(self, bingo_info: StringIO) -> None:
        numbers, boards = self.parse_info(bingo_info)
        self.numbers_to_draw = numbers
        self.boards = boards

    @property
    def drawn_number(self):
        return self.numbers_to_draw[self.curr_idx]

    def parse_info(self, bingo_info: StringIO) -> Tuple[List[int], List[List[int]]]:
        raw_numbers = next(bingo_info).split(',')
        numbers = list(map(int, raw_numbers))
        next(bingo_info)  # it throws away first empty line

        boards = []
        curr_board = []
        
        for line in bingo_info:
            if line == '\n':
                boards.append(curr_board)
                curr_board = []
            
            curr_board += [[item, 0] for item in map(int, line.split())]
        boards.append(curr_board)

        return numbers, boards

    def new_round(self) -> None:
        self.mark_numbers(self.drawn_number)
        if self.has_winner_board():
            self.bingo_drawn_number = self.drawn_number
            return

        self.curr_idx += 1

    def mark_numbers(self, drawn_number: int) -> None:
        for board in self.boards:
            for number in board:
                if number[0] == drawn_number:
                    number[1] = True
                    break
        
    def has_winner_board(self) -> bool:
        for board in self.boards:
            cond1 = self.has_bingo_row(board)
            cond2 = self.has_bingo_column(board)
            if cond1 or cond2:
                self.winner_board = board
                self.has_winner = True
                return True
        return False

    @staticmethod
    def is_checked(number: List[int]) -> bool:
        return number[1]

    def has_bingo_row(self, board: List[int]) -> False:
        for idx in range(0, 21, 5):
            row = list(islice(board, idx, idx + 5))
            if self.is_winner(row):
                return True
        return False

    def has_bingo_column(self, board: List[List[int]]) -> False:
        for idx in range(5):
            idxs = list(range(idx, 25, 5))
            row = [board[i] for i in idxs]
            if self.is_winner(row):
                return True
        return False

    def is_winner(self, line: List[List[int]]) -> bool:
        unmarked_numbers = list(filterfalse(self.is_checked, line))
        return len(unmarked_numbers) == 0

                    
def calculate_score(bingo_info: StringIO) -> int:
    bingo = Bingo(bingo_info)

    while not bingo.has_winner:
        bingo.new_round()

    sum_unmarked = reduce(return_unmarked, bingo.winner_board, 0)

    return sum_unmarked * bingo.drawn_number


def return_unmarked(acc, board_item: List[int]) -> int:
    if not board_item[1]:
        return board_item[0] + acc

    return acc
