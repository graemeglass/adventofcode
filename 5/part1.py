#http://adventofcode.com/day/5
from collections import Counter

vowels = 'aeiou'
evil_pairs = ('ab', 'cd', 'pq', 'xy')

nice_string = 0

with open('input.txt') as fp:
    for line in fp:
        line = line.strip()
        evil_found = False

        for evil_pair in evil_pairs:
            if evil_pair in line:
                evil_found = True
                break

        if evil_found:
            continue

        if not sum((1 for letter in line if letter in vowels)) >= 3:
            continue

        if len(set(line)) != len(line):
            c = Counter(line)

            for candidate_letter in (l for l,d in c.iteritems() if d >= 2):
                if line.count('{letter}{letter}'.format(**{'letter': candidate_letter})):
                    nice_string += 1
                    break

print(nice_string)