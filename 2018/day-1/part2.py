frequencies = set()
acc = 0
found = False
while not found:
    with open('input.txt') as fp:
        for l in fp.readlines():
            acc += int(l)
            if acc in frequencies:
                found = True
                break
            frequencies.add(acc)
print({"frequency_found_twice": acc})
