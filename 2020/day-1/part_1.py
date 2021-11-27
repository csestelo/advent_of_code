def report_repair_find_2(entries):
    # if changing the input were a problem, this would be a 'for' with 'enumerate' in order to use the index
    while entries:
        entry = entries.pop()
        for curr_entry in entries:
            if entry + curr_entry == 2020:
                return entry * curr_entry
