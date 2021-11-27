acc = 0
with open('input.txt') as fp:
    for l in fp.readlines():
        acc += int(l)
    print(acc)
