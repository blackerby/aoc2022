with open("input.txt", "r") as f:
    input = f.read().split("\n\n")

data = list(map(lambda s: s.splitlines(), input))

total_per_elf = sorted([sum([int(s) for s in lst]) for lst in data], reverse=True)

# Part 1
print(f"Elf with most: {total_per_elf[0]}")

# Part 2
print(f"Top 3 elves: {sum(total_per_elf[:3])}")
