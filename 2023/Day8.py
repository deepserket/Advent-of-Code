data = """..."""

from itertools import cycle

instructions = data.split("\n")[0]
data = data[data.find("\n") + 2:]
data = data.replace(' = ', '": ')
data = data.replace('(', '("')
data = data.replace(', ', '", "')
data = data.replace(')', '")')
data = data.replace('\n', ', "')
data = '{"' + data + "}"

d = eval(data)

position = "AAA"

for i, c in enumerate(cycle(instructions)):
    position = d[position][c == "R"]
    if position == "ZZZ":
        print(i+1)
        break

#part 2
from math import lcm

position = [k for k in d.keys() if k.endswith("A")]

delta = [] # this problem is "easyfied" so the paths are perfect circles

for p in position:
    for i, c in enumerate(cycle(instructions)):
        p = d[p][c == "R"]
        if p.endswith("Z"):
            delta.append(i+1)
            break

print(lcm(*delta))