from collections import Counter
from main import Policy


def is_valid_passwd(rule: Policy) -> bool:
    occurrences = Counter(rule.passwd)[rule.char]
    return rule.first_constraint <= occurrences <= rule.second_constraint
