data = """..."""

data = data.split("\n\n")

seeds = data[0]
seeds = seeds.split(": ")[1]
seeds = [int(s) for s in seeds.split()]

data = data[1:]

for i, m in enumerate(data):
    temp = m.split(":\n")[1]
    temp = temp.split("\n")
    temp = [[int(n) for n in line.split()] for line in temp]
    data[i] = temp


#part 1
def follow_the_rabbit(s):
    for path in data:
        for dest, source, step in path:
            if source <= s < source + step:
                s = s - source + dest
                break
    return s

print(min([follow_the_rabbit(s) for s in seeds]))


# part 2 bruteforced
from itertools import islice, count

def batched(iterable, n):
    # batched('ABCDEFG', 3) --> ABC DEF G
    if n < 1:
        raise ValueError('n must be at least one')
    it = iter(iterable)
    while batch := tuple(islice(it, n)):
        yield batch

def is_a_seed(s):
    for start, delta in batched(seeds, 2):
        if start <= s < start + delta:
            return True
    return False

def exit_the_hole():
    for i in count():
        temp = i
        for path in data[::-1]:
            for dest, source, step in path:
                if dest <= temp < dest + step:
                    temp = temp - dest + source
                    break
        if is_a_seed(temp):
            return i
    
print(exit_the_hole())
