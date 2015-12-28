#http://adventofcode.com/day/3

unique_location_count = 1
current_address = [0, 0]
seen_before = []

with open('input.txt') as fp:
    data = fp.read()
    for symbol in data:
        if symbol == '^':
            current_address[0] += 1
        elif symbol == 'v':
            current_address[0] -= 1
        elif symbol == '>':
            current_address[1] += 1
        elif symbol == '<':
            current_address[1] -= 1

        if tuple(current_address) not in seen_before:
            seen_before.append(tuple(current_address))
            unique_location_count += 1

    print(unique_location_count)
