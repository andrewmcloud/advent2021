from collections import defaultdict, Counter

rules = defaultdict(str)
with open("resources/day14_input.txt") as f:
    polymer = f.readline().strip()
    f.readline()            # consume blank
    for line in f.readlines():
        p, i = line.strip().split(" -> ")
        rules[p] = i


def mutate(polymer):
    new_polymer = ""
    for i in range(len(polymer) - 1):
        pair = polymer[i]+polymer[i+1]
        new_polymer += polymer[i] + rules[pair]
    return new_polymer + polymer[-1]


for i in range(10):
    polymer = mutate(polymer)

counts = Counter(polymer)
high = max(counts, key=counts.get)
low = min(counts, key=counts.get)

print(counts[high] - counts[low])
