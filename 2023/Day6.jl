data = """..."""

time, distance = split(data, "\n")
_, time = split(time, ":")
time = split(time)
_, distance = split(distance, ":")
distance = split(distance)

total = 1 # neutral value in a multiplication

for (t, d) in zip(time, distance)
    t, d = parse(Int64, t), parse(Int64, d)
    total *= sum([((t - p) * p) > d for p in 0:t])
end

println("part 1: ", total)

# part 2

total = 0
t = parse(Int64, join(time))
d = parse(Int64, join(distance))

for p in 0:t
    if (t-p) * p > d
        total += 1
    end
end

println("part 2: ", total)