#http://adventofcode.com/day/2/input
from heapq import nsmallest

total = 0

with open('input.txt') as fp:
    data = fp.read()
    for dimensions in data.split('\n'):
        length, width, height = dimensions.split('x')
        length = int(length)
        width = int(width)
        height = int(height)

        a, b = nsmallest(2, (length, width, height))
        total += (a * 2) + (b * 2)
        total += (length * width * height)

print(total)
