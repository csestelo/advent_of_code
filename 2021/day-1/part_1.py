from io import StringIO


def larger_measurement_count(measurements: StringIO) -> int:
    last_measurement = int(next(measurements))
    increased = 0

    for item in measurements:
        measurement = int(item)
        if measurement > last_measurement:
            increased += 1
        
        last_measurement = measurement
    
    return increased
