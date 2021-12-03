from io import StringIO


def calculate_position_as_in_manual(instructions: StringIO) -> int:
    horizontal_position = 0
    depth = 0
    aim = 0

    for step in instructions:
        direction, qty = step.strip().split(' ')
        qty = int(qty)

        if direction == 'forward':
            horizontal_position += qty
            depth += aim * qty

        elif direction == 'up':
            aim -= qty
        
        else:
            aim += qty
    
    return horizontal_position * depth
