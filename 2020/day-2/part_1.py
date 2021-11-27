from collections import Counter
from dataclasses import dataclass
from typing import TextIO, List


@dataclass
class PolicyRule:
    policy: List
    char: str
    passwd: str

    def min(self) -> int:
        return int(self.policy[0])

    def max(self) -> int:
        return int(self.policy[1])


def is_allowed_passwd(rule: PolicyRule) -> bool:
    occurrences = Counter(rule.passwd)[rule.char]
    return rule.min() <= occurrences <= rule.max()


def parse_policy(line: str) -> PolicyRule:
    """
    :line 1-3 b: cdefg
    :return ('1', '3'), b, cdefg
    """
    parsed_items = line.split()
    return PolicyRule(
        policy=parsed_items[0].split('-'),
        char=parsed_items[1][0],
        passwd=parsed_items[2]
    )


def has_ok_policy_qtd(passwords: TextIO) -> int:
    good_passwords = 0

    for line in passwords:
        policy_rule = parse_policy(line)
        good_passwords += is_allowed_passwd(policy_rule)

    return good_passwords
