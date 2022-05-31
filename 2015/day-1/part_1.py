def santa_claus_floor(instructions: str) -> int:
    floor = 0
    for inst in instructions:
        match inst:
            case "(":
                floor += 1

            case _:
                floor -= 1

    return floor
