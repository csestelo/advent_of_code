from collections import Counter, defaultdict


def find_duplicated1():
    with open('input.txt') as fp:
        duplicated_letters_counter = {'2': 0, '3': 0}
        for word in fp.readlines():
            found_letters_counter = defaultdict(int)
            for letter in word:
                found_letters_counter[letter] += 1

            duplicated_letters = found_letters_counter.values()

            if 2 in duplicated_letters:
                duplicated_letters_counter['2'] += 1
            if 3 in duplicated_letters:
                duplicated_letters_counter['3'] += 1

        return duplicated_letters_counter


def checksum1():
    counter = find_duplicated1()
    return counter.get('2') * counter.get('3')


# Elias refactors
def find_duplicated2():
    with open('input.txt') as fp:
        duplicated_letters_counter = {2: 0, 3: 0}
        for word in fp.readlines():
            found_letters_counter = Counter(word)
            duplicated_letters = found_letters_counter.values()

            if 2 in duplicated_letters:
                duplicated_letters_counter[2] += 1

            if 3 in duplicated_letters:
                duplicated_letters_counter[3] += 1

        return duplicated_letters_counter


def checksum2():
    counter = find_duplicated2()
    return counter.get(2) * counter.get(3)


def find_duplicated3():
    fname = '/home/cintiasestelo/.PyCharm2018.3/config/scratches/scratch_1.txt'

    twos = 0
    threes = 0
    for word in open(fname):
        found_letters_counter = Counter(word)
        duplicated_letters = found_letters_counter.values()

        if 2 in duplicated_letters:
            twos += 1

        if 3 in duplicated_letters:
            threes += 1

    return twos, threes


def checksum3():
    twos, threes = find_duplicated3()
    return twos * threes


print(checksum1())
print(checksum2())
print(checksum3())
