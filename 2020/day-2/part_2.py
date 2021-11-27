from main import Policy


def check_rule(passwd: str, index: int, char: str) -> bool:
    # This check is necessary only due my personal test scenario
    try:
        return passwd[index - 1] == char
    except IndexError:
        return False


def is_valid_passwd(rule: Policy) -> bool:
    first_check = check_rule(rule.passwd, rule.first_constraint, rule.char)
    second_check = check_rule(rule.passwd, rule.second_constraint, rule.char)

    return first_check != second_check
