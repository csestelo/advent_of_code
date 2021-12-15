from dataclasses import dataclass, field
from functools import reduce
from io import StringIO
from itertools import filterfalse, islice
from typing import List, Tuple

# It needs full refactor with part 1 :grimacing
@dataclass
class Bingo:
    numbers_to_draw: List[int]
    boards: List[List[int]]
    curr_idx: int = 0
    losing_board: List[int] = field(default_factory=list)
    has_loser_board: bool = False

    @classmethod
    def from_info(cls, bingo_info: StringIO) -> 'Bingo':
        numbers, boards = cls.parse_info(bingo_info)
        return cls(numbers_to_draw=numbers, boards=boards)

    @property
    def drawn_number(self):
        return self.numbers_to_draw[self.curr_idx]

    @classmethod
    def parse_info(cls, bingo_info: StringIO) -> Tuple[List[int], List[List[int]]]:
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
        if self.found_loser_board():
            self.bingo_drawn_number = self.drawn_number
            return

        self.curr_idx += 1

    def mark_numbers(self, drawn_number: int) -> None:
        for board in self.boards:
            for number in board:
                if number[0] == drawn_number:
                    number[1] = True
                    break
        
    def found_loser_board(self) -> bool:
        loser_boards = []
        for board in self.boards:
            horiz_win = self.has_bingo_row(board)
            vert_win = self.has_bingo_column(board)
            if not horiz_win and not vert_win:
                loser_boards.append(board)

        if len(loser_boards) == 0:
            self.losing_board = board
            self.has_loser_board = True
            return True

        else:
            self.boards = loser_boards
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

                    
def calculate_loser_score(bingo_info: StringIO) -> int:
    bingo = Bingo.from_info(bingo_info)

    while not bingo.has_loser_board:
        bingo.new_round()

    sum_unmarked = reduce(return_unmarked, bingo.losing_board, 0)

    return sum_unmarked * bingo.drawn_number


def return_unmarked(acc, board_item: List[int]) -> int:
    if not board_item[1]:
        return board_item[0] + acc

    return acc
