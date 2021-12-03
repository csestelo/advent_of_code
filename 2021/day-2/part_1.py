from io import StringIO


def calculate_position(instructions: StringIO) -> int:
    horizontal_position = 0
    depth = 0

    for step in instructions:
        direction, qty = step.strip().split(' ')
        qty = int(qty)

        if direction == 'forward':
            horizontal_position += qty

        elif direction == 'up':
            depth -= qty
        
        else:
            depth += qty
    
    return horizontal_position * depth
