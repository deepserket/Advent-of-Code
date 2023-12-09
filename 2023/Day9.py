data = """..."""

from itertools import pairwise

data = [[int(n) for n in line.split()] for line in data.split("\n")]

def calculate(l):
    last_elems = []
    while any(l):
        last_elems.append(l[-1])
        l = [b - a for a, b in pairwise(l)]
    return sum(last_elems)

total = 0
for line in data:
    total += calculate(line)

print(total)

# part 2
from functools import reduce

def calculate_part2(l):
    first_elems = []
    while any(l):
        first_elems.append(l[0])
        l = [b - a for a, b in pairwise(l)]
    first_elems.append(0)
    return reduce(lambda a, b: b - a, reversed(first_elems))

total = 0
for line in data:
    total += calculate_part2(line)

print(total)
