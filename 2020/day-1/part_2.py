from itertools import islice


def report_repair_find_3(entries):
    # if changing the input were a problem, this would be a 'for' with 'enumerate' in order to use the index
    while entries:
        entry = entries.pop()
        for curr_entry in entries:
            for next_entry in islice(entries, 1, None):  # it doesnt copy the list as 'entries[1:]' would
                if entry + curr_entry + next_entry == 2020:
                    return entry * curr_entry * next_entry
