from collections import defaultdict, Counter
from functools import cache

rules = {}
with open("resources/day14_input.txt") as f:
    polymer = f.readline().strip()
    f.readline()           
    for line in f.readlines():
        p, i = line.strip().split(" -> ")
        rules[p] = i

@cache
def mutate(a, b, depth):
    if depth == 0:
        return Counter('')
    x = rules[a+b]
    return Counter(x) + mutate(a, x, depth-1) + mutate(x, b, depth-1)


# part 1
counter = Counter(polymer)
for i in range(len(polymer) - 1):
    counter.update(mutate(polymer[i], polymer[i+1], 10))
print(max(counter.values()) - min(counter.values()))

# part 2
counter = Counter(polymer)
for i in range(len(polymer) - 1):
    counter.update(mutate(polymer[i], polymer[i+1], 40))
print(max(counter.values()) - min(counter.values()))
