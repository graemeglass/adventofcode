#http://adventofcode.com/day/4
from hashlib import md5

puzzle_input = 'bgvyzdsv'

not_found = True

number_value = 254575
while not_found:
    if md5('{}{}'.format('bgvyzdsv', str(number_value))).hexdigest()[:6] == '000000':
        print number_value
        not_found = False

    number_value += 1