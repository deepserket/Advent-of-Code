from math import log
from itertools import count

# some parsing and then some prime numbers magic to get the results

data = """...""" #input problem

colors = "red", "green", "blue"

for color in colors:
    data = data.replace(color, "**" + color)

data = data.replace(",", "*")

data = data.split("\n")

# removing the "game n:" part
# reversing the lines, reversing the numbers (because we use a positional system)
for n, line in enumerate(data, start=1):
    new = line[8+int(log(n, 10)):]
    new = new[::-1].split(" ")
    for i, token in enumerate(new):
        try:
            int(token)
        except ValueError:
            pass
        else:
            new[i] = token[::-1]
    data[n-1] = " ".join(new)
    
primes = 3, 5, 7

red, der = 3, 3
green, neerg = 5, 5
blue, eulb = 7, 7

nred = 12
ngreen = 13
nblue = 14

# in my case magic is 439984799875421641845703125
magic = red ** nred * green ** ngreen * blue ** nblue


total = 0
for n, line in enumerate(data, start=1):
    line = "((" + line.replace(";", "), (") + "))"
    for value in eval(line, globals()):
        if magic % value != 0:
            break
    else:
        total += n
print("First Solution:", total)


total = 0
for line in data:
    line = "((" + line.replace(";", "), (") + "))"
    temp = {3: 1, 5: 1, 7: 1}
    for value in eval(line, globals()):
        for prime in primes:
            for i in count():
                if value % prime ** i != 0:
                    temp[prime] = max(temp[prime], i-1)
                    break
    else:
        total += temp[3] * temp[5] * temp[7]
        
print("Second solution:", total)
