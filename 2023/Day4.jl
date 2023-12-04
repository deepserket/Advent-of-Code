data = """..."""

data = split(data, "\n")

total = 0

for line in data
	wins = 0
	_, line = split(line, ": ")
	winning, have = split(line, " | ")
	for i in range(start=1, stop=29, step=3)
		for j in range(start=1, stop=74, step=3)
			if winning[i:i+1] == have[j: j+1]
				wins += 1
			end
		end
	end
	if wins > 0
		global total += 2^(wins-1)
	end
end

println(total)

#=============================================================================#
# Part 2

repetitions = ones(length(data))

for (i, line) in enumerate(data)
	_, line = split(line, ": ")
	winning, have = split(line, " | ")
	wins = 0
	for i in range(start=1, stop=29, step=3)
		for j in range(start=1, stop=74, step=3)
			if winning[i:i+1] == have[j: j+1]
				wins += 1
			end
		end
	end
	while wins > 0
		repetitions[i + wins] += 1 * repetitions[i]
		wins -= 1
	end
end

println(floor(Int64(sum(repetitions))))
