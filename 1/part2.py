#http://adventofcode.com/day/1

floor = 0

with open('input.txt') as fp:
    data = fp.read()
    for count, symbol in enumerate(data, 1):
        if symbol == '(':
            floor += 1
        elif symbol == ')':
            floor -= 1

        if floor == -1:
            print(count)
            break