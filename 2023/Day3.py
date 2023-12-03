# problem 1

from string import digits

data = """..."""

old_data = data

data = data.split("\n")

good_coords = set()

for i, line in enumerate(data):
    for j, char in enumerate(line):
        if char not in digits and char != '.':
            for x in [i-1, i, i+1]:
                for y in [j-1, j, j+1]:
                    good_coords.add((x, y))

data = "".join([c if (c in digits or c == "\n") else " " for c in old_data])
data = data.split("\n")

flag = False
temp = ""
total = 0

for i, line in enumerate(data):
    for j, c in enumerate(line):
        if c in digits:
            temp += c
            if (i, j) in good_coords:
                flag = True
        if c == " ":
            if flag:
                print(temp)
                total += int(temp)
            temp = ""
            flag = False
                
    if flag:
        total += int(temp)
    temp = ""
    flag = False

print(total)
                

#=============================================================================#


# problem 2

from string import digits
from itertools import chain

data = """..."""

old_data = data

data = data.split("\n")

good_coords = dict()

for i, line in enumerate(data):
    for j, char in enumerate(line):
        if char == "*":
            temp = set()
            for x in [i-1, i, i+1]:
                for y in [j-1, j, j+1]:
                    temp.add((x, y))
            good_coords[tuple(temp)] = list()
            
flattened_keys = list(chain.from_iterable(good_coords.keys()))

data = "".join([c if (c in digits or c == "\n") else " " for c in old_data])
data = data.split("\n")

flag = False
temp = ""
key = None

for i, line in enumerate(data):
    for j, c in enumerate(line):
        if c in digits:
            temp += c
            if (i, j) in flattened_keys:
                flag = True
                key = (i, j)
        if c == " ":
            if flag:
                for k, v in good_coords.items():
                    if key in k:
                        v.append(int(temp))
            temp = ""
            flag = False
            key = None
            
    if flag:
        for k, v in good_coords.items():
            if key in k:
                v.append(int(temp))
    temp = ""
    flag = False
    key = None

total = 0

for v in good_coords.values():
    if len(v) == 2:
        total += v[0] * v[1]

print(total)
                























































# problem 1

from string import digits

old_data = data

data = data.split("\n")

good_coords = set()

for i, line in enumerate(data):
    for j, char in enumerate(line):
        if char not in digits and char != '.':
            for x in [i-1, i, i+1]:
                for y in [j-1, j, j+1]:
                    good_coords.add((x, y))

data = "".join([c if (c in digits or c == "\n") else " " for c in old_data])
data = data.split("\n")

flag = False
temp = ""
total = 0

for i, line in enumerate(data):
    for j, c in enumerate(line):
        if c in digits:
            temp += c
            if (i, j) in good_coords:
                flag = True
        if c == " ":
            if flag:
                print(temp)
                total += int(temp)
            temp = ""
            flag = False
                
    if flag:
        total += int(temp)
    temp = ""
    flag = False

print(total)
                















































