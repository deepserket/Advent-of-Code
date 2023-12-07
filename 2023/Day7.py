from collections import Counter
from functools import cmp_to_key

data = """..."""

second_part = False # change this to change between parts

data = data.split("\n")

if second_part:
    labels = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
else:
    labels = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]


def compare(h1, h2): # compare 2 hands
    h1 = h1.split()[0]
    h2 = h2.split()[0]
    
    if h1 == h2:
        return 0
    
    c1 = Counter(h1)
    c2 = Counter(h2)
    
    if second_part:
        c1["J"] = 0
        c2["J"] = 0
        c1[c1.most_common()[0][0]] += h1.count("J")
        c2[c2.most_common()[0][0]] += h2.count("J")
    
    c1 = c1.values()
    c2 = c2.values()
    
    max1 = max(c1)
    max2 = max(c2)

    def second_ordering(h1, h2):
        for a, b in zip(h1, h2):
            if a == b:
                continue
            if labels.index(a) < labels.index(b):
                return 1
            else:
                return -1
        return 0
    
    # two pair
    twop1 = list(c1).count(2) == 2
    twop2 = list(c2).count(2) == 2
    if twop1 and twop2:
        return second_ordering(h1, h2)
    if twop1 and max2 < 3:
        return 1
    if twop2 and max1 < 3:
        return -1
    
    full1 = 3 in c1 and 2 in c1
    full2 = 3 in c2 and 2 in c2
    
    if full1 and full2:
        return second_ordering(h1, h2)
    
    # full house vs something else
    if full1 and max2 < 3:
        return 1
    if full1 and max2 > 3:
        return -1
    if full2 and max1 < 3:
        return -1
    if full2 and max1 > 3:
        return 1
    
    if full1 and len(c2) > 2:
        return 1
    if full2 and len(c1) > 2:
        return -1

    for n in 5, 4, 3, 2:
        if max1 == n and max2 < n:
            return 1
        if max2 == n and max1 < n:
            return -1
    
    return second_ordering(h1, h2)

data.sort(key=cmp_to_key(compare))

total = 0

for i, line in enumerate(data):
    value = int(line.split()[1])
    total += (i+1) * value

print(total)
