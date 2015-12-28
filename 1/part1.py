#http://adventofcode.com/day/1

floor = 0

with open('input.txt') as fp:
    data = fp.read()
    for symbol in data:
        if symbol == '(':
            floor += 1
        elif symbol == ')':
            floor -= 1

print(floor)