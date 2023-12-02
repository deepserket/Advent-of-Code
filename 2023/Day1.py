from string import digits

data """...""" #input problem

data = (data.replace("one", "one1one")
            .replace("two", "two2two")
            .replace("three", "three3three")
            .replace("four", "four4four")
            .replace("five", "five5five")
            .replace("six", "six6six")
            .replace("seven", "seven7seven")
            .replace("eight", "eight8eight")
            .replace("nine", "nine9nine")
   )

counter = 0

for line in data.split("\n"):
    first = None
    last = None
    for c in line:
        if c in digits:
            if first is None:
                first = int(c)
            last = int(c)
    counter += first * 10 + last

print(counter)