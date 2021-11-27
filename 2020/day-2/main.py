from dataclasses import dataclass
from typing import TextIO, Callable


@dataclass
class Policy:
    first_constraint: int
    second_constraint: int
    char: str
    passwd: str

    def __init__(self, raw_policy: str):
        parsed_items = raw_policy.split()
        self.char = parsed_items[1][0]
        self.passwd = parsed_items[2]
        self.first_constraint, self.second_constraint = [
            int(item) for item in parsed_items[0].split('-')
        ]


def has_ok_policy_qtd(db: TextIO, validator: Callable[[Policy], bool]) -> int:
    good_passwords = 0

    for item in db:
        good_passwords += validator(Policy(item))

    return good_passwords
