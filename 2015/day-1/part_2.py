def santa_claus_enters_basement(instructions: str) -> int:
    """
    Returns the position of the instruction that causes santa claus to
    enter the basement
    """
    floor = 0

    for i, inst in enumerate(instructions):
        match inst:
            case "(":
                floor += 1

            case _:
                floor -= 1

        if floor == -1:
            return i + 1
